import os, shutil

### making the list of cosmological params, which will be used by the CosmoFlow IO code to make the tensorflow files

list = open("list.txt", "w")
print >> list, "## seed, om, si"
counter = 999

start = 0
stop = 2000

ct = 0
for afile in os.listdir("./"):
    if  "pycola" not in afile or "npz" in afile:
        continue
    else:
        print afile
        counter+=1
        
        if counter>3000:
            continue
            
        om = afile.split("_")[1]
        si = afile.split("_")[2]
        ns = afile.split("_")[3]
        print counter, om, si, ns
        
        print >> list,  str(counter)+","+str(om)+","+str(si)+","+str(ns)
        
