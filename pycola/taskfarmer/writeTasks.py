outfile = open("tasklist.txt", "w")

for i in range(0,2005):
    print >> outfile, "taskwrapper.sh  "+str(i)
