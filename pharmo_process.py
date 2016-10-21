#The MOE feature extraction software yields pharmacophore descriptors which have to 
#be processed to create a binary matrix. This script takes in a csv file that tries 
#to convert a pharamacophore feature [eg: '305 677 890 234'] into a binary matrix 
#[eg: The binary matrix will have four fetures namely 305, 677, 890, 234].

import pandas as pd
import numpy as np
import os

os.system("clear")
protein_fam = ["DRD","H","HT","opioid"]
protein_num = [1,2,3]
unique_pharm = []
for fam in range(0,len(protein_fam)): # the following two for loops are used to call each file that i want to process
	for pnum in range(0,len(protein_num)):
		fname = protein_fam[fam]+str(protein_num[pnum])+"_feat.csv" #name of the file
		raw_dat = pd.read_csv(fname)  #read the csv file
		for ii in range(0,raw_dat.shape[0]):
			irecord = np.array(raw_dat.loc[ii]) # read each record in the csv
			rec_column = irecord[2] #The third column in my file contains the pharmacophore features in the form of a string
			rec_temp = rec_column.split(" ");
			rec_temp = map(int, rec_temp)
			unique_pharm_temp = list(set(rec_temp))
			unique_pharm = unique_pharm + unique_pharm_temp  #Keep adding the unique features to the set.

#		print 'done with one intra'
#		del raw_dat
#		del ii
#	print 'done with one fam'

unique_pharm = np.array(set(unique_pharm)) #The final set of pharma features




	
	
	

