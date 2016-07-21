import csv, os, numpy
open_file = open("CTD_chem_gene_ixns.csv") #create a file holder for reading the csv file
iread = open_file.readlines()
max_molecules = 70000 #the number of molecules to be written in each file
file_ind = 1
imol = " "
count = 1
for i in range(0,len(iread)):
	imol += iread[i]
	count = count +1;
	if count == max_molecules:
		o = open("chem_gene"+str(file_ind)+".csv","w")
		o.write(imol)
		o.close()
		file_ind += 1
		count = 1
		imol = " "
	elif (i==len(iread)-1):
		o = open("chem_gene"+str(file_ind)+".csv","w")
		o.write(imol)
		o.close()

