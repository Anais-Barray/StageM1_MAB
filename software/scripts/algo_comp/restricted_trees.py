#!usr/bin/python3
import subprocess, os, sys, subprocess
from Bio import SeqIO

subprocess.call("clear")

if __name__ == "__main__":

	allseqfile = sys.argv[1]
	refseqfile = sys.argv[2]
	allseqtree = sys.argv[3]
	placedseqtree = sys.argv[4]
	outputname = sys.argv[5]
	
	#~ Listes des noms de taxons necessaires pour realiser les arbres 
	#~ restreints avec nw_prune.
	list_alltaxa = []
	alltaxa = ""
	list_refseqtaxa = []
	refseqtaxa = ""
	list_readtaxa = []
	
	for sequence in SeqIO.parse(open(allseqfile), "fasta"):
		list_alltaxa.append(sequence.id)
	alltaxa = ' '.join(list_alltaxa)
	
	for sequence in SeqIO.parse(open(refseqfile), "fasta"):
		list_refseqtaxa.append(sequence.id)
	refseqtaxa = ' '.join(list_refseqtaxa)
	 
	for taxon in list_alltaxa:
		if not taxon in list_refseqtaxa:
			list_readtaxa.append(taxon)
	
	#~ => Faire les arbres restreints avec nw_prune pour realiser :  
	#~    les arbres avec placements vrais (simules) "true" des reads + 
	#~    les arbres avec placement des reads "placed" par le logiciel 
	#~    (epa/pplacer/sepp).
	#~ => Passe par un script bash car probleme avec nw_prune appele en 
	#~    subprocess (noms de taxons passent pas en string)
	#~ => 10 versions du read placed pour une 
	#~    sequence true. Par la suite (TreeDist), on compare chaque 
	#~    arbre "placed" avec l'arbre "true", on doit faire autant 
	#~    d'arbre dans les deux cas car ils seront compares par paire 
	#~ 	  (arbre_placed1 avec arbre_true1, arbre_placed2 avec 
	#~    arbre_true2, etc). Ils doivent donc etre dans le meme ordre 
	#~    d'apparition dans leur fichier respectif.
	for read in list_readtaxa:
		for i in range (0,10):
			bashcmd_true = "/home/anaisb/software/newick-utils-1.6/src/nw_prune -v " + allseqtree + " " + refseqtaxa + " " + read + " >> " + outputname + "_output_restrictedTrees_true"
			bashcmd_placed = "/home/anaisb/software/newick-utils-1.6/src/nw_prune -v " + placedseqtree + " " + refseqtaxa + " " + read + "_" + str(i) + " >> " + outputname + "_output_restrictedTrees_placed"
			f = open("run_restrict.sh", "w")
			f.write("#!/bin/bash\n")
			f.write(bashcmd_true+"\n")
			f.write(bashcmd_placed+"\n")
			f.write("exit 0")
			f.close()
			subprocess.call(["chmod","755","run_restrict.sh"])
			subprocess.call(["sh", "run_restrict.sh"])
	
