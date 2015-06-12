#!usr/bin/python3
import subprocess, os, sys

if __name__ == "__main__":
	
	itree = sys.argv[1]
	istat = sys.argv[2]
	icombo = sys.argv[3]
	output = sys.argv[4]
	
	#fichier temporaire avec l'extension correcte pour etre reconnu par pplacer
	icombotemp = ""+os.path.splitext(icombo)[0]+".sth" 

	#copie pour pas modifier le fichier d'origine
	subprocess.call(["cp", icombo, icombotemp]) 
	
	#unix : /home/anaisb/software/pplacer/pplacer/pplacer -t $inputtree -s $inputstat $inputcombo -o $output
	subprocess.call(["/home/anaisb/software/pplacer/pplacer/pplacer", "-t", itree, "-s", istat, icombotemp, "-o", output]) 
	
	#supprime le fichier temporaire devenu obsolete
	subprocess.call(["rm", icombotemp]) 
