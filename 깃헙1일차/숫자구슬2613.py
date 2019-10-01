# import math
# def maxc(array,mid):
#     lSum = 0
#     Sum = 0
#     for i in range(mid,-1,-1):
#       Sum = Sum + array[i]
#       if Sum > lSum:
#        lSum =Sum
#     rSum = 0
#     Sum = 0
#     for i in range(mid+1, len(array)):
#       Sum = Sum + array[i]
#       if Sum > rSum:
#          rSum = Sum
#     return lSum + rSum
#
#
# def maxARRAY(array):
#     if len(array) == 0:
#         return 0
#     elif len(array)==1:
#         return array[0]
#     else:
#         mid = math.floor((1+len(array))/2)
#         return max(maxARRAY(array[1:mid+1]),maxARRAY(array[mid+1:len(array)+1]),maxc(array,mid))
#
#

N = int(input("size of array : "))
M = int(input("count of group : "))

A = (input().split())
A = list(map(int,A))

high = sum(A)
low = 1
# low = 그룹이 가질수있는 최대값 중 최소값
# high = 전체 그룹이 가질수 있는 최대값

if(high>30000 or len(A)> N):
    print("잘못된 입력입니다.")
    exit(0)
# 구슬은 항상 자연수 "> 0" 이고 구슬의 개수가 300개 이하이므로
# 구슬의 전체합은 항상 30000이하가 됩니다.

for i in range(0,N):
     low = max(low, A[i])
# 구슬중 하나의 구슬이 이상값(너무 큰값)일 경우 그 구슬의 값이
# 최대값중 최소값이 됩니다.

while(low != high):
     Sum = 0
     Gcnt = 1
# Sum = 최대값중 최소값을 찾기위한 비교변수 입니다.
# Gcnt = 실제 생성되는 그룹의 갯수를 찾기위한 비교변수 입니다.

     for i in range(0,N):
        Sum += A[i]
        if(Sum > low): # low보다 큰 값인 경우 최대값중
             Sum = A[i] # 최소값을 초과했다는 의미 입니다.
             Gcnt += 1

     if(Gcnt > M): # 설정 그룹수보다 실제 그룹수가 많은경우
        low += 1   # 최대값중 최소값을 증가시켜줍니다.
     else:         # 작거나 같을 경우 최대값중 최소값이
         high -= 1 # 더 커질수 있다는 것을 의미합니다.

print(low) # 최대값중 최소값 출력

Sum = 0
cnt = 0

for i in range(0,N):
   Sum += A[i]
   cnt += 1
   if(Sum >= low):# 위와 같은 검사 방법으로 각 그룹의 개수를 출력해 줍니다.
     print(cnt)
     Sum = A[i]
     cnt = 0

