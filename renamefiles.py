import os
import glob
fn = glob.glob("/media/lordlabakdas/Nivi/latest_drugbank/*.sdf")
for i in range(0,len(fn)):
	newfn = "output"+str(i+1)+".sdf"
        print newfn
	os.rename(fn[i],newfn)
