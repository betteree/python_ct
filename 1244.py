# 입력받기
N = int(input())  # 스위치 개수
switches = list(map(int, input().split()))  # 스위치 초기 상태
M = int(input())  # 학생 수

for _ in range(M):
    gender, number = map(int, input().split())
    
    if gender == 1:  # 남학생
        for i in range(number - 1, N, number):
            switches[i] = 1 - switches[i]  # 스위치 상태 반전
            
    elif gender == 2:  # 여학생
        left = number - 2
        right = number
        switches[number - 1] = 1 - switches[number - 1]  # 중심 스위치 반전
        
        while left >= 0 and right < N and switches[left] == switches[right]:
            switches[left] = 1 - switches[left]
            switches[right] = 1 - switches[right]
            left -= 1
            right += 1

# 출력 (한 줄에 20개씩 출력)
for i in range(N):
    print(switches[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
