def solution(n):
    if n == 1:
        return 1
    else:
        dp = [0] *(n+1) #결과값 담아야하니까 갯수보다 +1을 함
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = (dp[i-2]+dp[i-1]) % 1234567
    
    return dp[-1]