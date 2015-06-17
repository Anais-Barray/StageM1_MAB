#!usr/bin/python3
import sys, subprocess, shutil, os

if __name__ == "__main__":
	
	itree = sys.argv[1]
	istat = sys.argv[2]
	imsa = sys.argv[3]
	iread = sys.argv[4]
	model = sys.argv[5]
	ofile = sys.argv[6]
	
	#nom de l'output
	oname = "output_placement.json"
	
	# unix : python run_sepp.py -t tree -a MSA -f read -m model(dna/rna/amino) -r raxml_info
	subprocess.call(["python", "/home/anaisb/software/sepp/run_sepp.py", "-t", itree, "-a", imsa, "-f", iread, "-m", model, "-r", istat]) 
	
	#fichiers crees renommes en fichier de sortie pour que galaxy le recupere
	shutil.move(oname, ofile) 	

	#supprime les fichiers inutilises
	subprocess.call(["rm", "output_alignment_masked.fasta", "output_alignment.fasta"]) 

