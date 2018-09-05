module load python
source activate cola2
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/common/software/fftw/3.3.4/hsw/gnu/lib/
cd /global/cscratch1/sd/djbard/MUSIC_pyCola/github/cosmoflow-sims/pycola/
python pycola-OmSiNs-template.py $1
