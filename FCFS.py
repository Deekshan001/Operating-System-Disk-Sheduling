def FCFS(arr,head,size): 
    tot=0
    cur=head
    for i in range(size):
        dis=abs(arr[i]-cur)
        tot+=dis
        cur=arr[i]  
    print("Total number of seek operations = ",tot)
    print("Average seek operation =",tot/size)
    print("Seek Sequence is :",head,end="")
    for i in range(size): 
        print(' ->',arr[i],end='')
    print()

if __name__ == '__main__':
    size = 8
    arr = [98,183,37,122,14,124,65,67]
    head = 53
    FCFS(arr, head, size)
