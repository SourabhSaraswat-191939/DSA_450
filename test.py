from queue import Queue

arr = ['T','T','P','P','T','P']
arr = ['P','T','T','P','T']
k=1
theifQ = Queue(maxsize=len(arr))
policeQ = Queue(maxsize=len(arr))
result = 0
for i in range(len(arr)):
    if (not theifQ.empty()) and i-theifQ.queue[0]>k:
        theifQ.get()
    if (not policeQ.empty()) and i-policeQ.queue[0]>k:
        policeQ.get()

    if arr[i]=='T':
        if not policeQ.empty():
            result+=1
            policeQ.get()
            continue
        theifQ.put(i)
    else:
        if not theifQ.empty():
            theifQ.get()
            result+=1
        else:
            policeQ.put(i)

print("Result =>",result)