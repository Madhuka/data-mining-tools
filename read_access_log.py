"""
1st step to run
readdding access_log with skiping line and formatting access_log
author   :madhuka udantha
email    : madhukaudantha@gmail.com
date     : 2015-02-01
"""
import re
import timeit
from collections import Counter
import json
import csv
import os
import sys


#regex to filter on nic.lk site data
regex = '([a-zA-Z,.]*)(nic.lk )(.*?)'
path = os.path.dirname(os.path.realpath(__file__))
#buidlding string

count = 0
PageNo = 0
SEPS = ','

print 'starting to read accesslog file....'
log_list = ""
#filelist = ['access_log-20150125','access_log-20150208','access_log-20150222','access_log-20150301','access_log-20150302']
filelist = ['access_log-20150125']
for filename in filelist:
    print 'Starting pre processing on '+ filename
    with open(path+"/data/"+filename,"r") as f:

	for line in f :
	       
		#print line;
		match = re.match(regex, line)
		
		if match:
		    
		 # print "0 "+match.group(0)  
		 # print "1 "+match.group(1) 
		 # print "1 "+match.group(2) 
		 # print re.split(match.group(1), line)[1]
		  count +=1  
		  out = re.split(match.group(2), line)[1]
		  #print out+"iii"
		  log_list += str(out)
		  sys.stdout.write('|')
		  #print count
    #print 'Completed on '+ filename
    #with open(path+"/log", "a") as myfile:
     #   myfile.write(log_list)
print "Total log count: " + str(count)
#print log_list

#writting to file  called log
fd = open(path+"/log1", "w+") 
fd.write(log_list)
fd.close()
