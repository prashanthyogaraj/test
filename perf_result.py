import re
from collections import OrderedDict 
import sys

def readInp(path):
    try:
        d=OrderedDict()
        l=[]
        l1=[]
        write_pat="Wrote.*\((.*) MB/sec\)"
        read_pat="Read.*\((.*) MB/sec\)"
        #fp=open("inp2.txt",'r')
        fp=open(path,'r')
        out=fp.readlines()
        fp.close()
        print(type(out))
        for i in out:
            itr_pat="#*Running\s*(Iteration \d)\s*#*$"
            output_itr=re.search(itr_pat,i)
            if(output_itr):
                iteration=output_itr.group(1)
                l=[]
                d[iteration]={}                
            write_output=re.search(write_pat,i)
            read_output=re.search(read_pat,i)
            if(write_output):
                l.append(float(write_output.group(1)))
                d[iteration]['write']=l
            if(read_output):
                l1.append(float(read_output.group(1)))
                d[iteration]['Read']=l1
    except Exception as e:
        print("Exception: ",e)
        
#print(d)
    return d

def writeResult(d):
    try:
        fp1=open("res.txt",'w+')
        for k ,v in d.items():
            print("========",k,"==============")
            fp1.write("======================="+k+"============================\n")
            for k1,v1 in v.items():
                print("=========",k1,"=======")
                fp1.write("==================="+k1+"===========================\n")
                print(str(v1)+"\n")
                #print("=========",sum(v1),"========len is",len(v1))
                Avg=0
                Avg=(sum(v1))
                print("Sum is : "+str(Avg)+"\n")
                #v1=",".join(map(str,v1))
                fp1.write(str(v1)+"\n\n")
                fp1.write("Sum is : "+str(Avg)+"\n\n")
    except Exception as e:
        print("Exception: ",e)
    finally:		
        fp1.close()
		
		
if __name__ == '__main__':

    if(len(sys.argv)>1):
        path = sys.argv[1]	
        print("path is ",path)
        res=readInp(path)
        writeResult(res)
    else:
        print("Please Provide the input File Path")	