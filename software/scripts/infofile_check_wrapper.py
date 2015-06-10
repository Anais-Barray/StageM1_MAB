#!usr/bin/python3
import shutil 

	infofile = sys.argv[1]
	infofile_modif = sys.argv[2]
	
	itemp = infofile+"checked"
	print (itemp)
	
	f1 = open(infofile)
	f2 = open(itemp, 'w')

	for line in f1:
		if ("Partition: 0 with name: No Name Provided" not in line):
			f2.write(line)
			
	f1.close()
	f2.close()
	
	shutil.move(itemp,infofile_modif)
	
		
	
