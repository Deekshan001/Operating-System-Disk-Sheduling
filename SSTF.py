def SSTF(a,head,size):
    cur=head
    tot=0
    seq=[]
    while len(a)>0:
        mindif=abs(cur-a[0])
        imin=0
        for i in range(1,len(a)):
            dif=abs(cur-a[i])
            if dif<mindif:
                mindif=dif
                imin=i
        tot+=mindif
        cur=a[imin]
        seq.append(a[imin])
        a.pop(imin)
    print("Total number of seek operations =",tot)
    print("Average seek operation =",tot/size)
    print("Seek Sequence is :",head,end="")
    for i in range(size): 
        print(' ->',seq[i],end='')
    print()        

if __name__ == '__main__':
    size = 8
    arr = [98,183,37,122,14,124,65,67]
    head = 53
    SSTF(arr, head, size)
