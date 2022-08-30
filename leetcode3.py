# def peopleAwareOfSecret(n, delay, forget):
#     start=[delay] # day+delay
#     end = [forget] # day+forget
#     count=1
#     j=0
#     mod=1e9+7
#     for i in range(1,n):
#         flag=0
#         active=0
#         jStart=j
#         while (jStart<len(start)) and (start[jStart]<i):
#             jStart+=1
#             active+=1
#         someoneForget =0
#         print("----------day",i+1)
#         print("checkß")
#         while end[j]<=i:
#             print(end[j],i)
#             j+=1
#             someoneForget+=1
#             active-=1
#             if j>=len(end):
#                 flag=1
#                 break
#         print("check2")
#         if flag:
#             break
#         print("check3")
#         if start[j]>i:
#             continue
#         # active = len(end)-j
        
#         # count+=active-someoneForget
#         count+=active
#         for k in range(active):
#             print("active on ith ",active,"on",i,j)
#             start.append(i+delay)
#             end.append(i+forget)
#         # count = count%mod    
        
#         print(end)

#     return int(count)




def peopleAwareOfSecret(n, delay, forget):
    start=[delay] # day+delay
    end = [forget] # day+forget
    activeMap = {(delay,forget):1}
    def calc(i,active):
        if n==i:
            return active
        if end[0]<=i:
            for _ in range(activeMap[(start[0],end[0])]):
                start.pop(0)
                end.pop(0)
                active-=1
        k=0    
        while start[k]<=i and i<end[k]:
            print("For k -> ",k,start,end)
            print(start[k],end[k])       
            print("before",i,active)    
            active+=activeMap[(start[0],end[0])]
            print("after",i,active,activeMap[(start[0],end[0])])    
            k+=1
        
        if active>0:
            for _ in range(active):
                start.append(i+delay+1)
                end.append(i+forget+1)
            activeMap[(i+delay+1,i+forget+1)] = active
        
        return calc(i+1,active)

    return calc(1,1)

print(peopleAwareOfSecret(6,2,4))