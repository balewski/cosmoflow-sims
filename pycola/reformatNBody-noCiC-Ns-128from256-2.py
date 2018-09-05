import numpy as np
import os, shutil
import math

import sys


start = int(sys.argv[1])
stop = 1005

counter = -1
######## Loop over the files!
for afile in os.listdir("OmSiNs/onethousand-2/"):
    if "npz" not in afile or "pycola" not in afile:
        continue
    infile = "OmSiNs/onethousand-2/"+afile

    counter+=1
    if counter<start or counter>stop:
        continue

    print counter, infile

    outdir = infile[:-4]+"-noCiC-128from256"
    if os.path.exists(outdir):
        if len(os.listdir(outdir))==8:
            print "done this one!"
            continue
        else:
            print len(os.listdir(outdir))
            ### this is a half-empty folder. delete it!
            shutil.rmtree(outdir)

    os.mkdir(outdir)
    
    ### First, read in the px/py/pz
    data = np.load(infile)

    px = data['px']
    py = data['py']
    pz = data['pz']

    print px[0][0][0], py[0][0][0], pz[0][0][0]
   


    #### Try using this hp.histogramdd function...
    ### For this I need to turn the particl elists into coord lists, 
    ### so (  (px[i][j][k], py[i][j][k], pz[i][j][k]), ....)
    pxf = np.ndarray.flatten(px)
    pyf = np.ndarray.flatten(py)
    pzf = np.ndarray.flatten(pz)

    print pxf.shape
    print pxf[0], pyf[0], pzf[0]
    ### so the flattening is working. Now make this into a 3d array...
    ps = np.vstack( (pxf, pyf, pzf) ).T
    
    del(pxf); del(pyf); del(pzf)

    print "one big array!", ps.shape, ps[0,:]

    
    ## OK! Then this is indeed a big old array. Now I want to histogram it. 
    nbins = 256
    H, bins = np.histogramdd(ps, nbins, range=((0,512),(0,512),(0,512)) )

    print "histo dshape!", H.shape,  H[0][0][0]

    ### this appears to be a 512^3 histogram! Gosh, I hope it's doing the right thing. 




    ### now I have my density estimate, I split it up and write it out
    count = -1
    for i in range(0, 256, 128):
        for j in range(0, 256, 128):
            for k in range(0, 256, 128):
                
                count+=1
                d = H[i:(i+128),j:(j+128),k:(k+128)]
                #print d.shape
                #filename = outdir+"/"+str(i)+"_"+str(j)+"_"+str(k)+".npy"
                filename = outdir+"/"+str(count)+".npy"
                np.save(filename, d)
    print "got:", count

    print "**************************"
