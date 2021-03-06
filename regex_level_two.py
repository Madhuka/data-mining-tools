from __future__ import division
import os
import numpy as np
import operator
import string
from nltk.tokenize import RegexpTokenizer

path = os.path.dirname(os.path.realpath(__file__))

print '===starting reading skip_pages ==='

regex=[];
 

def grouping_sessions(session):
    out_line = ''
    count = 1
    array = []
    count_array = []
    page_ids = []
    print session
    for index, page in enumerate(session):
        
        if(index < len(session)-1):
            next  = session[index+1]
        if(page == next):
            count +=1
        else:
            #print count
            array.append(page+'['+str(count)+']')
            page_ids.append(page)
            count_array.append(count)
            count = 1
        if(index == len(session)-1):
            #print count-1
            array.append(page+'['+str(count-1)+']')
            page_ids.append(page)
            count_array.append(count-1)
            
    print array
    print page_ids
    print count_array
    out_line = str(page_ids)+','+str(count_array)+'\n'
    out_line = out_line.replace("[", '"').replace(']', '"')
    regex.append(out_line)
    
def page_sequences(file_name):
    global session_count, count
    with open(path+'/page_sequences/'+file_name+'.csv','r') as f:
        irofile = iter(f)   
        prevoius_session=[]
        x = 0    
   	for line in irofile:
   	    x +=1
   	    print x
   	    current_line = line
            trans = string.maketrans("\"' \n","    ")
            line = line.split('","')[0].translate(trans)               
   	    current_session = line.replace(" ", "").split(',')
   	    #print current_session
   	    #print prevoius_session
   	    print current_session == prevoius_session
   	    next_line = next(irofile)  #BEWARE, This could raise StopIteration!
   	    next_line = next_line.split('","')[0].translate(trans)           
   	    next_session = next_line.replace(" ", "").split(',')
            print current_session == next_session
            #print next_session
            prevoius_session = next_session
            #grouping_sessions(current_session);
            
                    
def getKey(item):
   print item.split('"')[1]
   return item.split('"')[1]        

def write_file(data_to_file,file_name):
    data_to_file = sorted(data_to_file, key=getKey)
    str1 = ''.join(data_to_file)
    directory = path+"/page_sequences"
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory+"/"+file_name+".csv", "w")    
    f.write(str1)      # str() converts to string
    f.close()
    
def make_regex_level1(file_name,file_out):
    page_sequences(file_name)
    #write_file(regex,file_out)

#main processing calling
make_regex_level1('skip_pages_regex_level_1','x');
#make_regex_level1('without_skip_pages','without_skip_pages_regex_level_1');

print "===END==="
