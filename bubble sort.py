li = []
n = int(input("enter no. of elements:"))
for i in range(0, n):
    ele = int(input())
    li.append(ele)

# 42 29 75 11 65 58 60 18
def sort(li):
    for k in range(len(li)-1, 0, -1):
        for j in range(k):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
                print(li)


sort(li)
# print(li)