import math
def maxc(array,mid):
    lSum = 0
    Sum = 0
    for i in range(mid,-1,-1):
      Sum = Sum + array[i]
      if Sum > lSum:
       lSum =Sum
    rSum = 0
    Sum = 0
    for i in range(mid+1, len(array)):
      Sum = Sum + array[i]
      if Sum > rSum:
         rSum = Sum
    return lSum + rSum


def maxARRAY(array):
    if len(array) == 0:
        return 0
    elif len(array)==1:
        return array[0]
    else:
        mid = math.floor((1+len(array))/2)
        return max(maxARRAY(array[1:mid+1]),maxARRAY(array[mid+1:len(array)+1]),maxc(array,mid))



T = int(input("test: "))
result = []

for i in range(0,T):
    N = int(input("size of array :"))
    A = (input().split())
    A = list(map(int,A))
    result.append(maxARRAY(A))

for i in range(0,T):
    print(result[i])
