#!/bin/sh
#SBATCH -N 10 -c 1
##SBATCH -p debug
#SBATCH -t 00:12:00
#SBATCH -C haswell 
#SBATCH -J OmSiNs
#SBATCH -q premium
rm *.tfin
cd /global/cscratch1/sd/djbard/MUSIC_pyCola/github/cosmoflow-sims/pycola/taskfarmer/
export PATH=$PATH:/usr/common/tig/taskfarmer/1.5/bin:$(pwd)
export THREADS=1
runcommands.sh tasklist.txt
