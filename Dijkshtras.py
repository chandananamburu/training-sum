'''g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)],3:[(5,1),(6,3)]}
def fun(x):
    d={5:999,1:9999,3:9999,6:9999,2:9999}
    d[x]=0
    vi=[]
    q=[0,x]
    while(q):
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                x=i
        for i in g[x]:
            if(i[0] not in vi):
                q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        vi.append(x)
        q.remove(x)
    return d
print (fun(6))'''

'''g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)],3:[(5,1),(6,3)],6:[],2:[]}
def fun(x):
    d={5:999,1:9999,3:9999,6:9999,2:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        x=q.pop(0)
        for i in g[x]:
            if(i[0] not in vi):
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
                if i[0] not in q:
                    q.append(i[0])
        vi.append(x)
    return d
print (fun(5))'''

def fun(g,x):
    #d={5:9999,1:9999,3:9999,6:9999,2:9999,8:9999,7:9999,9:9999,4:9999}
    d={5:9999,3:9999,2:9999,8:9999,7:9999,4:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                x=i
        for i in g[x]:
            if(i[0] not in vi):
                if i[0] not in q:
                    q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x] 
        vi.append(x)
        q.remove(x)
    
    print(vi)
    print(d)
#g={5:[(2,2),(3,2),(8,2)],2:[(5,2),(3,1)],3:[(5,2),(2,1),(7,3),(8,3)],8:[(5,2),(6,4),(3,3)],6:[(8,4),(9,2)],7:[(3,3),(9,1)]
 #    ,9:[(6,2),(7,1,),(4,2)],4:[(9,2)]}

g={5:[(7,1),(3,3)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,6),(2,3)],8:[(3,5),(4,6),(2,2)],3:[(5,3),(7,2),(8,5)],2:[(4,3),(8,2)]}



fun(g,next(iter(g)))