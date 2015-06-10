#!/usr/bin/python3
import subprocess, os, sys, string, shutil
from copy import deepcopy

if __name__ == "__main__":
	ifile = sys.argv[1]
	iformat = sys.argv[2]
	oformat = sys.argv[3]
	ofile = sys.argv[4]

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
		
	#unix : convbioseq -i iformat oformat ifile
	#itemp = ifile
	#ireal = shutil.move(itemp,os.path.splitext(ifile)[0]+iext)
	#subprocess.call(["convbioseq", oformat, ireal])

	itemp1 = os.path.splitext(ifile)[0]+iext
	itemp2 = deepcopy(ifile)
	ireal = shutil.move(itemp2,itemp1)
	subprocess.call(["convbioseq", oformat, ireal])
	shutil.move(ireal.replace(iext,oext),ofile)
