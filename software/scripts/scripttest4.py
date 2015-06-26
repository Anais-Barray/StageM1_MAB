#!/usr/bin/python3
import subprocess, os

subprocess.call("clear")

#~ # -------------------------- CONVERSION PHYLIP > STOCKHOLM -------------------------- 
#~ 
#~ def conv_Phy2Sth():
	#~ # unix : convbioseq stockholm test1msa.phy
	#~ print "\n*** Conversion PHYLIP > STOCKHOLM ***"
	#~ subprocess.call(["convbioseq", "stockholm", "/home/anaisb/datasets/PROTHOG000250281/test1msa.phy"])
	#~ print "*** Conversion done ***"
	#~ 
	
# -------------------------- HMMER -------------------------- 

def hmm():
	# unix : hmmbuild refseqaln.hmm refseqaln.sth
	print "\n*** Running HMMBUILD command ***"
	hmmbuild = subprocess.Popen(["/home/anaisb/software/hmmer/hmmer/src/hmmbuild", "/home/anaisb/datasets/PROTHOG000250281/test2hmm.hmm", "/home/anaisb/datasets/PROTHOG000250281/test1msa.phy"], stdout=subprocess.PIPE)
	output, err = hmmbuild.communicate()
	print "*** HMMBUILD success ***"
	
	
	# unix : hmmalign -o combo.sth --mapali refseqaln.sth refseqaln.hmm read.fasta
	print "\n*** Running HMMALIGN command ***"
	hmmalign = subprocess.Popen(["/home/anaisb/software/hmmer/hmmer/src/hmmalign", "-o", "/home/anaisb/datasets/PROTHOG000250281/test2combo.sth", "--mapali",  "/home/anaisb/datasets/PROTHOG000250281/test1msa.phy", "/home/anaisb/datasets/PROTHOG000250281/test2hmm.hmm", "/home/anaisb/datasets/PROTHOG000250281/test1read.fasta"], stdout=subprocess.PIPE) 
	output, err = hmmalign.communicate()
	print "*** HMMALIGN success ***"


# -------------------------- CONVERSION STOCKHOLM > PHYLIP (EPA) -------------------------- 

def conv_Sth2Phy():
	# unix : convbioseq phylip test1combo.sth
	print "\n*** Conversion STOCKHOLM > PHYLIP ***"
	subprocess.call(["convbioseq", "phylip", "/home/anaisb/datasets/PROTHOG000250281/test2combo.sth"])
	print "*** Conversion done ***"
	
	

# -------------------------- CHOSE PLACEMENT ALGORITHM -------------------------- 

def main():	
	print "\n*** Start of the HMM steps ***\n"
	#conv_Phy2Sth()
	hmm()
	conv_Sth2Phy()

if __name__ == "__main__":
	main()
