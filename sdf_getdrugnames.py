# This python script extracts a specific field from an sdf file. This script is an example to extract the drugnames.

import sys, os
inputf = open("structures.sdf","r")

prevline = ""
o = open("drugnames","w") #drugnames is the output file 
for currline in inputf:
	
	if "<GENERIC_NAME>" in prevline:
		o.write(currline)
	prevline = currline
		
o.close()	
