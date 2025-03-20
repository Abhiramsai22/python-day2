# def searching(l,w):
#     for num in l:
#         if w==num:
#             return True
#     return False
# def findindex(l,w):
#     for i in range(len(l)):
#         if l[i]==w:
#             return i
#     return -1
# list1=list(map(int,input().split()))
# want=int(input())
# print(searching(list1,want))
# print(findindex(list1,want))


#list duplicates

# list1=list(map(int,input().split()))
# dup=[]
# l=[]
# for num in list1:
#     if num in l and num not in dup:
#         dup.append(num)
#         print(num,"is duplicate")
#     l.append(num)
# print(dup)




def repeat(list1):
    final=[]
    for num in list1:
        rem=0
        l=[]
        dup=[]
        while(num>0):
            rem=num%10
            if rem in l and rem not in dup:
                dup.append(rem)
            l.append(rem)
            num=num//10
        if(dup):
            final.append(True)
        else:
            final.append(False)
    return final
list1=list(map(int,input().split()))
print(repeat(list1))




