st=["lone", "cat", "catastrophic", "udui"]
pre=["cat","udu","phic"]
a= list(map(str, input().split()))
print(a)

def solution(st, pre):
    count=0
    for i in st:
        for j in pre:

            if len(i)> len(j):
                if j in i[:len(j)]:
                    count += 1
                    print(i[:len(j)])
                if j in i[-len(j):]:
                    print(i[-len(j):])
                    count +=1

    print(count)
solution(st, pre)