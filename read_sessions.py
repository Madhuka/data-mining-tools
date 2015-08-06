import re
import timeit
from collections import Counter
import json
import csv,os

path = os.path.dirname(os.path.realpath(__file__))
regex = '(.*?)"(.*?)"'


#buidlding string

count = 0
PageNo = 0
SEPS = ','

print 'starting....'
input = []
with open(path+"/sessions_file","r") as f:

	for line in f:
	       
		#print line;
		match = re.match(regex, line)
		if match and int(count) < 10000:
		  #print match.group(2)
		  r = match.group(2).split(SEPS)
		  v = Counter(r)
		  input +=[v]
                  print str(match.group(1)) + str(v)
                 # print len(r)
                  count +=1
                  '''
                  for rl in r:
                        
                        if PageNo == int(rl):
                            print 'x'
		  '''
print "Total session count: " + str(count)
totalCount = sum(
    (Counter(dict(x)) for x in input), Counter())
totalCount = totalCount.most_common(100)

#keylist = totalCount.values() #keys, values
#keylist.sort()
print len(totalCount)
data = [("pageID","requestCount")]
countNo = 1

with open(path+'/most_common.csv', 'wb') as f1:
        writer = csv.writer(f1)
        for row in totalCount:
            print row
           # row += count
            count += 1
            print row
        writer.writerows(data)
        writer.writerows(totalCount)