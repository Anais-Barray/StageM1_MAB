#!usr/bin/python3
import shutil, sys

if __name__ == "__main__":

	infofile = sys.argv[1]
	infofile_modif = sys.argv[2]
	
	#nouveau nom de fichier
	itemp = infofile+"checked"
	
	#ouverture des fichiers
	f1 = open(infofile)
	f2 = open(itemp, 'w')
	
	#copie du contenu de l'input infofile reconnaissable par pplacer dans itemp
	for line in f1:
		if ("Partition: 0 with name: No Name Provided" not in line):
			f2.write(line)
	
	#fermeture des fichiers	
	f1.close()
	f2.close()
	
	#itemp renomme en output infofile_modif pour que galaxy le recupere
	shutil.move(itemp,infofile_modif)

		
	
