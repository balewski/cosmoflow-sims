import numpy as np
from ROOT import *
import time

data = np.load('OmSi/pycola_0.325_0.928.npz')
print np.shape(data['px'])

px = data['px']
py = data['py']
pz = data['pz']

print px[1][1][1], py[1][1][1], pz[1][1][1]
ncells = 128 # np.shape(px)[0]
hi = 256
lo = 0
nbins = 128
h = TH3F("","",nbins, lo, hi, nbins, lo, hi, nbins, lo, hi) ##xbinx, xlo, xhi...
for i in range(ncells):
    for j in range(ncells):
        for k in range(ncells):
            #h.SetBinContent(i, j, k, px[i][j][k]
            h.Fill(px[i][j][k], py[i][j][k], pz[i][j][k])

h.Draw()

time.sleep(300)
