import os, shutil

## need to rename all the files in the numbering scheme required by the CosmoFlow IO sceme. 
## Previously, the dir had a useful name containing the comso params used in the sim
## Now, this dir needs to be re-named so that it has a number, which corresponds to the position in the list of cosmo params
## I know, this is not very sensible. But then the CosmoFlow IO code picks random sets of sims + sub-volumes to make the TFRecord files, and it's easier to do that when the file names are the numbers. 

### In case you don't want to run this over all the files you have
start = 1000
stop = 1010

for line in open("list.txt"):
    if "#" in line:
        continue
    cols = line.split(",")
    num = cols[0]
    om = cols[1]
    si = cols[2]
    ns = cols[3][:-1]
    print line, num, om, si, ns

    if int(num)<start or int(num)>stop:
        print"skipping!"
        continue

    outdir = "./"+num
    if os.path.exists(outdir):
        if len(os.listdir(outdir))==8:
            print "done this one!"
            continue
        else:
            shutil.rmtree(outdir)

    ## now move the files 
    indir = "pycola_"+om+"_"+si+"_"+ns
    shutil.copytree(indir, outdir)
    
