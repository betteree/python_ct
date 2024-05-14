#서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
#첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.
#첫째 줄에 자연수 N의 최댓값을 출력한다.
#입력: S = 200 출력 :N 의 최댓 값 19

S= int(input())
cnt=0
for i in range(1,S+1):
    S -= i
    cnt += 1
    if S < 0:
        cnt -=1
        break
        
print(cnt)