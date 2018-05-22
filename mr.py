from random import randint

def MR(n):
    t=2
    
    def get_vars(N):
        S=r=0
        for s in range(128,0,-1):
            if ((n-1)%(2**s)==0):
                k=(n-1)//(2**s)
                if(2**s*k+1==n and k%2==1):
                    S=s
                    r=k
        return S,r
    S=r=0
    SR=get_vars(n)

    if SR:
        S,r=SR[0],SR[1]
        #print("S",S,"r",r)
    else:
        return([n,"Bad number"])

    b=[]
    for i in range(t):
        a=randint(2,n-1)#last not included
        #print("a: "+str(a))
        b.append( pow(a,r,n) )
        for j in range(1,S+1):
            b.append( (pow(b[-1],2,n)))
        #print ("b: "+str(b))
        if  b[-1]!=1:
            return[n," - составное»"]
        elif b[b.index(1)-1]!=n-1:
            return[n," - составное»"]  
        b=[]
    return [n,"простое"]
            

    
    
def mr():
    BOUNDS=[2**127+1,(2**128)-1]
    x=0
    s=0
    while True:
        n=randint(BOUNDS[0],BOUNDS[1])
        while(n&1==0):
            n=randint(BOUNDS[0],BOUNDS[1])
        num=MR(n)
        if  "простое" in num[1]:
            return (num[0])