"""
This is sample class

"""
#import pdb
import math
import sys
import time

class CustomError(Exception):
    def __init__(self,msg):
        self.msg=msg

class Test:
    
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c
		
    def __str__(self):
        return ("Test")
    
    def fact(self,n):
        #pdb.set_trace()
        try:
            if(n<1):
                raise CustomError("Value is LessThan 0")
		
            if(n==1):
                return 1
            else:
                return n*self.fact(n-1)		
        except CustomError as e:
            print(e)

class second(Test):
    print("third called")
    def __init__(self,a):
        self.a=a
		

    def __str__(self):
        print("Second"+self.a)
		
    def __add__(self,another):
        return self.a+another.a	

    def man(self):
        print("man")
		
    def __test(self):
        print("Hello")
		
class third(second):
    def __init__(self):
        pass
		

t=Test(1,2,3)
print("protected is ",t._b)
print("private is ",t._Test__a)
print(t)
out=t.fact(0)
print(out)
s=second(1)
s1=second(2)
print(s+s1)
s._second__test()
t=third()
out=t.fact(5)
print(out)


def fact(n):
    count=1
    out=1
    while(count<=n):
        out=out*count
        count+=1

    return out

res=fact(6)
print(res)

def fibo(n):
    a,b=0,1
    print(a)
    print(b)
    for i in  range(3,n+1):
        c=a+b
        a=b
        b=c
        print(b)
    return b if (a>1) else a

print("====",fibo(5))
    
	
def fibo(n,d={1:0,2:1}):
    if n in d:
        return d[n]
    else:
        d[n]= fibo(n-1,d)+fibo(n-2,d)
        print(d[n])
        return d[n]
		
d= fibo(5)
print(d)
"""
def add10(f):
    #pdb.set_trace()
    def inner(*args):
        print("Hey print "+f.__name__)
        out = f(*args)
        return out+10
    return inner		

@add10
def add(a,b):
    print(a+b)
    return(a+b)
	
def test(*arg,**k):
    for i in arg:
        print(i)
    print(k)
out=add(20,300)
print(out)
print(add.__name__)

test(1,2,3,a=2,b=20,c=30)

"""


s=900
e=1000
import re
st=time.time()

for i in range(s,e+1):
    if (i>1):
        for j in range(2,i):
            #print(i)
            if(i%j==0):	
                break
        else:
            print("i is ",i)	
et=time.time()
print("Total is ",et-st)

s=900
e=1000
print("==========")
#import pdb;pdb.set_trace()
st=time.time()
for i in range(s,e+1):
    if(i>1):
        if(i==2):
            print(i)
        if(i>2 and i%2==0):            
            continue
        num=math.floor(math.sqrt(i))
        for j in range(3,num+1,2):
            if(i%j==0):
                
                break
        else:
            print("i is ===",i)		
et=time.time()

total=et-st
print("Total is ",total)

#print((sys.argv[1]))


with open("sample.txt",'r+') as fp:
    b=2
    a=1
    out = fp.readlines()
    fp1=open("sample.txt","w+")
    for i in range(len(out)):
        line=out[i].strip()
        res=re.search("still",line,re.I)
        if(res):
            print(line)
            res1=re.sub("Still","will",line,re.I)
            print(res1)
            before=i-b
            After=i+a+1
            print("After before",out[before:After])
            fp1.write(res1+"\n")
        else:
            fp1.write(line+"\n")
			
			

class check:
    b=10
    def __init__(self,a):
        self.a=a	

    def test(self):
        print(self.a)
    
    @classmethod	
    def cls_m(cls,a):
        print("class method")
        cls.b=100		
        print(cls.b)
        return cls(b)
    @staticmethod
    def st_m(a):
        out=a
        print("static is ",a)
        return out
		
c=check(1)
out=c.st_m(2)
print("hey",out)
check.cls_m(1)
print(c.b)
c.test()





def tst(l):
    n=[None,None,None]
    for i in l:
        get_tst(n,i)
    return n

def get_tst(n,i):
    if(n[2] is None) or i >n[2]:
         shift_n(i,2,n)
   		 
    elif(n[1] is None) or i >n[1]:
         shift_n(i,1,n)
    elif(n[0] is None) or i >n[0]:
         shift_n(i,0,n)
		 
def shift_n(val,idx,n):
    for i in range(idx+1):
        if(i==idx):
            n[idx]=val	
        else:
            n[i]=n[i+1]
    		

l=[2,4,1,10,5,6]
out=tst(l)
print(out)	



class test:
    def __init__(self,p):
        self.p=p

    def add(self):
        print("a is ",self.p)
        return self.p


class child(test):
    def __init__(self,q):
        self.q=q
        super().__init__(q)
		
    def print1(self):
        outs=super().add()	
        print("outis",outs)

c=child(100)
c.add()	
c.print1()



def gen(max):
    n=0
    while(n<max):
        n+=2
        yield n


out=gen(10)
for i in gen(10):
    print(i)
    if(i>2):
        break
	