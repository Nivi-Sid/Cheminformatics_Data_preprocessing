import sys, os
max_molecules_per_file = 1 #write 1 molecule per file
input_sdf = open("structures.sdf", "r") #structures.sdf is the file name
counter = 0
ind =1
mol = " "
o = open( "output_" + str(counter) + ".sdf", "w") #output file to write the molecule
for line in input_sdf:
    mol += line
    if "$$$$" in line: #delimiter that separated two molecules
	
        o.write( mol )
	
        if counter > 0 and counter % max_molecules_per_file == 0:
            o.close()
            o = open( "output_" + str(counter) + ".sdf", "w")
        mol = ""
        counter += 1
o.close()
