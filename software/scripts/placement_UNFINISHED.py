#!/usr/bin/python3
import subprocess, os, sys, getopt

subprocess.call("clear")


# -------------------------- CONVERSION PHYLIP > STOCKHOLM -------------------------- 

def conv_Phy2Sth():
	# unix : convbioseq stockholm test1msa.phy
	print "\n*** Conversion PHYLIP > STOCKHOLM ***"
	subprocess.call(["convbioseq", "stockholm", inputMSA])
	print "*** Conversion done ***"


# -------------------------- HMMER -------------------------- 

def hmm():
	# unix : hmmbuild refseqaln.hmm refseqaln.sth
	print "\n*** Running HMMBUILD command ***"
	hmmbuild = subprocess.Popen(["/home/anaisb/software/hmmer/hmmer/src/hmmbuild", "/home/anaisb/datasets/PROTHOG000250281/test1hmm.hmm", "/home/anaisb/datasets/PROTHOG000250281/test1msa.sth"], stdout=subprocess.PIPE)
	output, err = hmmbuild.communicate()
	print "*** HMMBUILD success ***"
	
	
	# unix : hmmalign -o combo.sth --mapali refseqaln.sth refseqaln.hmm read.fasta
	print "\n*** Running HMMALIGN command ***"
	hmmalign = subprocess.Popen(["/home/anaisb/software/hmmer/hmmer/src/hmmalign", "-o", "/home/anaisb/datasets/PROTHOG000250281/test1combo.sth", "--mapali",  "/home/anaisb/datasets/PROTHOG000250281/test1msa.sth", "/home/anaisb/datasets/PROTHOG000250281/test1hmm.hmm", "/home/anaisb/datasets/PROTHOG000250281/fam_HOG000250281-read"], stdout=subprocess.PIPE) 
	output, err = hmmalign.communicate()
	print "*** HMMALIGN success ***"


# -------------------------- CONVERSION STOCKHOLM > PHYLIP (EPA) -------------------------- 

def conv_Sth2Phy():
	# unix : convbioseq phylip test1combo.sth
	print "\n*** Conversion STOCKHOLM > PHYLIP ***"
	subprocess.call(["convbioseq", "phylip", "/home/anaisb/datasets/PROTHOG000250281/test1combo.sth"])
	print "*** Conversion done ***"
	

	
# -------------------------- INFO FILE CHECK (pplacer) -------------------------- 

# latest version of RAxML_info statistic file is not recognized by pplacer
# need to delete the line : "Partition: 0 with name: No Name Provided"
# => parse the info file f1 and write all the lines except this one into a new file f2

def infoCheck():
	print "\n*** Checking the RAxML_info file ***"
	f1 = open("/home/anaisb/datasets/PROTHOG000250281/TREES/raxml/test1RAxML_info.ARBRETEST1.1")
	f2 = open("/home/anaisb/datasets/PROTHOG000250281/TREES/raxml/test1_modifiedRAxML_info.ARBRETEST1.1", 'w')

	for line in f1:
		if ("Partition: 0 with name: No Name Provided" not in line):
			f2.write(line)
		else:
			print "line removed"
	f1.close()
	f2.close()
	print "*** Checking done ***"
	
	
# -------------------------- EPA -------------------------- 

def epa():
	conv_Phy2Sth()
	hmm()
	conv_Sth2Phy()
	
	print "\n*** Placement with EPA ***"
	# evolution model : user has to specify one for placement with EPA.
	input_var = None
	while True :
		try:
			input_var = raw_input("Specify the evolution model you want use for the placement with EPA:\n[OPTIONS : for DNA use GTRCAT or GTRGAMMA ; for AA use PROTCATWAG, PROTGAMMAWAG, PROTCATLG or PROTGAMMALG]\n")
		except ValueError :
			print "Incorrect value"
		if input_var in ("GTRCAT","GTRGAMMA","PROTCATWAG","PROTGAMMAWAG","PROTCATLG","PROTGAMMALG") :
			break
		else :
			print ">>>Incorrect model, try again\n"
	
	# unix : raxml -f v -s test1combo.phy -t test1RAxML_bestTree.ARBRETEST1.1 -m PROTGAMMAWAG -n test1Epa -w path/to/output/directory/
	print "Starting EPA algorithm with", input_var, "model"
	epa = subprocess.Popen(["/home/anaisb/software/epa/standard-RAxML-master/raxmlHPC-SSE3", "-f", "v", "-s", "/home/anaisb/datasets/PROTHOG000250281/test1combo.phy", "-t", "/home/anaisb/datasets/PROTHOG000250281/TREES/raxml/test1RAxML_bestTree.ARBRETEST1.1", "-m", input_var, "-n", "test1Epa", "-w", "/home/anaisb/datasets/PROTHOG000250281/EPA_results/test1"], stdout=subprocess.PIPE)
	output, err = epa.communicate()
	print "*** EPA success ***"


# -------------------------- pplacer -------------------------- 

def pplacer() :
	conv_Phy2Sth()
	hmm()
	infoCheck()
	
	print "\n*** Placement with PPLACER ***"
	# unix : pplacer -t reftree.nwk -s tree_stat -o test1Pplacer --out-dir path/to/output/directory/ combo.sto
	pplacer = subprocess.Popen(["/home/anaisb/software/pplacer/pplacer/pplacer", "/home/anaisb/datasets/PROTHOG000250281/test1combo.sth", "-t", "/home/anaisb/datasets/PROTHOG000250281/TREES/raxml/test1RAxML_bestTree.ARBRETEST1.1", "-s", "/home/anaisb/datasets/PROTHOG000250281/TREES/raxml/test1_modifiedRAxML_info.ARBRETEST1.1", "--out-dir", "/home/anaisb/datasets/PROTHOG000250281/pplacer-results/test1"], stdout=subprocess.PIPE)
	output, err = pplacer.communicate()
	print "*** PPLACER success ***"
	
	

# -------------------------- CHOSE PLACEMENT ALGORITHM -------------------------- 

def usage():
	print 'USAGE : placement.py -a <inputMSA> -r <inputREAD> -t <inputTREE> -s <inputSTAT> -p <placement_algorithm : epa or pplacer>\n'

# launches EPA or pplacer algorithm
def main():	
	
	inputMSA = ''
	inputREAD = ''
	inputTREE = ''
	inputSTAT = ''
	placement_algorithm = ''
	
	try:
		opts, args = getopt.getopt(sys.argv[1:], "ha:r:t:s:p:", ["help"])
	except getopt.GetoptError as err :
		print str(err)
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
			sys.exit()
		elif opt == "-a":
			inputMSA = arg
		elif opt == "-r":
			inputREAD = arg
		elif opt == "-t":
			inputTREE = arg
		elif opt == "-s":
			inputSTAT = arg
		elif opt == "-p":
			placement_algorithm = arg


	print "\n*** Start of the placements of the reads on reference tree ***\n"

	if placement_algorithm == "epa" :
		print placement_algorithm
		#epa()
		#break
	elif placement_algorithm == "pplacer"  :
		print placement_algorithm	
		#pplacer()
		#break
	else :
		usage()
	print inputMSA

if __name__ == "__main__":
	main()
