def afficher(p):
    res=""
    i=len(p)-1
    while i>=0:
        if i==0:
            res+="{}".format(p[i])
        if i==1:
            res+="{}*x".format(p[i])
        if i>1:
            res+="{}*x^{}".format(p[i],i)
        if i!=0:
            if p[i-1]>=0:
                res+=" + "
            else:
                res+=" "
        i-=1
    return res


def get_valeur(p,x):
    res=0
    i=0
    for coeff in p:
        res+=coeff*(x**i)
        i+=1
    return res

def deriver(p):
    res=[]
    if len(p)==1:
        res=[0]
        return res
    for i in range(1,len(p)):
        res.append(i*p[i])
    return res

def principal(p,x) :
	print(f"le polynome est= {afficher(p)}")
	print(f"la valeur au point {x} est= {get_valeur(p,x)}")
	print(f"la derivee est= {afficher(deriver(p))}")
	print(f"la derivee au point {x} est= {get_valeur(deriver(p),x)}")


polynome=[2,4,3,1]
x1=2
result=principal(polynome,x1)