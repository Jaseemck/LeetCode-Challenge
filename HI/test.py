def getways(n,c):
    # Complete this function
    n_perms = [1]+[0]*n
    for coin in c:
        for i in range(coin, n+1):
            n_perms[i] += n_perms[i-coin]
            print(coin,i,n_perms[i])
            print("------------")
        print("??????????????")

n, m = map(int,input().split())
c = list((map(int,input().split())))
getways(n,c)

