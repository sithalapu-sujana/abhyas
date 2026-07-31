n=int(input())
array=list(map(int,input().split()))
expected_sum=n*(n+1)//2
actual_sum=sum(array)
print(expected_sum-actual_sum)
