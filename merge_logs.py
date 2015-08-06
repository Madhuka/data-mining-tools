import os

filenames = ['log1','log2','log3','log4', 'log5']
path = os.path.dirname(os.path.realpath(__file__))
with open('D:/Research/Data/run05/log', 'w') as outfile:
    for fname in filenames:
        print 'Merging file '+fname
        with open(path+'/'+fname) as infile:
            for line in infile:
                outfile.write(line)