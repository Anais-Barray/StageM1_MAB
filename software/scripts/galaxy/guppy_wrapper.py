#!usr/bin/python3
import subprocess, os, sys

if __name__ == "__main__":
	
	ijson = sys.argv[1]
	output = sys.argv[2]
	outputxml = sys.argv[3]
	
	#fichier temporaire avec l'extension correcte pour etre reconnu par pplacer
	ijsontemp = ""+os.path.splitext(ijson)[0]+".json" 

	#copie pour pas modifier le fichier d'origine
	subprocess.call(["cp", ijson, ijsontemp]) 
	
	#unix : /home/anaisb/software/pplacer/pplacer/pplacer -t $inputtree -s $inputstat $inputcombo -o $output
	subprocess.call(["/home/anaisb/software/pplacer/pplacer/guppy", "tog", "-o", output, ijsontemp])
	subprocess.call(["/home/anaisb/software/pplacer/pplacer/guppy", "tog", "--xml", "-o", outputxml, ijsontemp])

	#supprime le fichier temporaire devenu obsolete
	subprocess.call(["rm", ijsontemp]) 
