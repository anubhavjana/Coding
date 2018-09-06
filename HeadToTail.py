T=int(input())
N=int(input())
l=[]
s=input()
l.append(s)
l1=[[l[i],l[j]] for i in range(0,len(l)) for j in range(0,len(l)) if (l[i][-1].lower()==l[j][0].lower()) & (i!=j)]
l2=[ j for i in l1 for j in i ]	
l2=set(l2)
l2=list(l2)
if(len(l2)==len(l)):
	print('Head to tail ordering is possible.')
else:
    print('Head to tail ordering is not possible.')




