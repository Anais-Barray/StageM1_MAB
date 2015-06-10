#!/usr/bin/python3
import subprocess, os, sys, string, shutil

if __name__ == "__main__":
	
	#fichiers d'entree (galaxy)
	ifile = sys.argv[1]
	iformat = sys.argv[2]
	oformat = sys.argv[3]
	ofile = sys.argv[4]

	#besoin des extensions pour le renommage de fichier
	iext=""
	oext=""
	
	if iformat == "phylip":
		iext = ".phy"
	elif iformat == "fasta":
		iext = ".fasta"
	elif iformat == "stockholm":
		iext = ".sth"
	
	if oformat == "phylip":
		oext = ".phy"
	elif oformat == "fasta":
		oext = ".fasta"
	elif oformat == "stockholm":
		oext = ".sth"
		
		
	#unix cmd : convbioseq -i iformat oformat ifile

	#nom que doit avoir le fichier pour etre reconnu par convbioseq
	itemp = ""+os.path.splitext(ifile)[0]+iext 
	
	#copie pour pas modifier le fichier d'origine
	subprocess.call(["cp", ifile, itemp]) 
	
	#nom qu'aura le fichier converti
	oconv = ""+itemp.replace(iext,oext) 
	
	#appel de convbioseq pour convertir l'input itemp1 (format iformat) en format oformat
	subprocess.call(["convbioseq", "-i", iformat, oformat, itemp]) 
	
	#fichier converti renomme en fichier de sorti pour que galaxy le recupere
	shutil.move(oconv,ofile) 

