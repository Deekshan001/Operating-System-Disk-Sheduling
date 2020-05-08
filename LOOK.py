def LOOK(arr,head,size):
    a=list(arr)
    cur=head
    tot=0
    a.append(head)
    a.sort()
    for i in range(len(a)):
        if a[i]==head:
            k=i
            break
    seq=[]
    if k<size//2:
        for i in range(k,len(a)):
            seq.append(a[i])
        for i in range(k-1,-1,-1):
            seq.append(a[i])
    else:
        for i in range(k,-1,-1):
            seq.append(a[i])
        for i in range(k+1,len(a)):
            seq.append(a[i])
    print("Seek Sequence is :",head,end="")
    for i in range(1,len(seq)): 
        print(' ->',seq[i],end='')
        tot+=abs(cur-seq[i])
        cur=seq[i]
    print()
    print("Total number of seek operations =",tot)
    print("Average seek operation =",tot/size)
    
if __name__ == '__main__':
    size = 8
    arr = [98,183,37,122,14,124,65,67]
    head = 53
    LOOK(arr,head,size)
