import itertools as iter
def particles(li):
    global m
    if len(li)>1:
        for i in iter.combinations(li, 2):
            print(i)
            temp = abs(i[0] - i[1])
            if m > temp:
                m = temp
            k = li.copy()
            k.remove(i[0])
            k.remove(i[1])
            k.append(temp)
            print("---------")
            particles(k)
            
n = int(input())
lst = list((map(int,input().split())))
m = min(lst)
particles(lst)
print(m)
