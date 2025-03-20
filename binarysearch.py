Numofinnerlist = int(input("Enter number of inner list: "))
list1 = [list(map(int, input().split())) for _ in range(Numofinnerlist)]
print(list1)

for i in range(len(list1)-1):
    flag=True
    for j in range(len(list1)-1-i):
        if list1[j][0] > list1[j+1][0]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
            flag=False
    if flag:
        break
print(list1)

