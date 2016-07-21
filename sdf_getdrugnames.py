import sys, os
inputf = open("structures.sdf","r")

prevline = ""
o = open("drugnames","w")
for currline in inputf:
	
	if "<GENERIC_NAME>" in prevline:
		o.write(currline)
	prevline = currline
		
o.close()	
