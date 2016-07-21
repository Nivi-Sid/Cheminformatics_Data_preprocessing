import csv, os, numpy
open_file = open("CTD_genes_diseases.csv")
iread = open_file.readlines()
max_molecules = 70000
file_ind = 1
imol = " "
count = 1
for i in range(0,len(iread)):
	imol += iread[i]
	count = count +1;
	if count == max_molecules:
		o = open("gene_dis"+str(file_ind)+".csv","w")
		o.write(imol)
		o.close()
		file_ind += 1
		count = 1
