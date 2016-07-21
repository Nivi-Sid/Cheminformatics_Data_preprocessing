import sys, os
max_molecules_per_file = 1
input_sdf = open("structures.sdf", "r")
counter = 0
ind =1
mol = " "
o = open( "output_" + str(counter) + ".sdf", "w")
for line in input_sdf:
    mol += line
    if "$$$$" in line:
	
        o.write( mol )
	
        if counter > 0 and counter % max_molecules_per_file == 0:
            o.close()
            o = open( "output_" + str(counter) + ".sdf", "w")
        mol = ""
        counter += 1
o.close()
