#!usr/bin/python3
import sys, os, subprocess, shutil

if __name__ == "__main__":
	
	icombo = sys.argv[1]
	itree = sys.argv[2]
	imodel = sys.argv[3]
	ojplace = sys.argv[4]
	oclassif = sys.argv[5]
	oclassifLW = sys.argv[6]

	#nom des output
	oname = "" + os.path.splitext(icombo)[0] + "_" + imodel + "_EPA_result"
	
	#fichier temporaire avec l'extension correcte pour etre reconnu par EPA
	icombotemp = ""+os.path.splitext(icombo)[0]+".phy" 
	
	#copie pour pas modifier le fichier d'origine
	subprocess.call(["cp", icombo, icombotemp]) 

	# unix : raxml -f v -s test1combo.phy -t test1RAxML_bestTree.ARBRETEST1.1 -m PROTGAMMAWAG -n test1Epa
	subprocess.call(["/home/anaisb/software/epa/standard-RAxML-master/raxmlHPC-SSE3", "-f", "v", "-s", icombotemp, "-t", itree, "-m", imodel, "-n", oname]) 
	
	#supprime le fichier temporaire devenu obsolete
	subprocess.call(["rm", icombotemp]) 
	
	#fichiers crees renommes en fichier de sortie pour que galaxy le recupere
	shutil.move("RAxML_portableTree." + oname + ".jplace", ojplace) 	
	shutil.move("RAxML_classification." + oname, oclassif)
	shutil.move("RAxML_classificationLikelihoodWeights." + oname, oclassifLW) 	

	#supprime les fichiers inutilises
	subprocess.call(["rm", "RAxML_entropy."+oname, "RAxML_info."+oname, "RAxML_labelledTree."+oname, "RAxML_originalLabelledTree."+oname]) 
