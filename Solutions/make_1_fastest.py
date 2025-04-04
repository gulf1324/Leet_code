import numpy as np
a = int(input())

# a = 3
dp = [0] * (a + 1)  # 0 ~ 목표 숫자 a까지의 array 생성

# 숫자 2부터 목표 숫자 a까지:
for i in range(2, a + 1):
    """ 
    i = 숫자
    dp[i] = 숫자 i의 최단 거리(1까지의)
    
    """
    
    # 숫자 i의 최단거리는 "숫자 i-1의 최단거리에서 1을 더한 값"
    dp[i] = dp[i - 1] + 1

    # 숫자 i가 2로 나눠지면
    #   숫자 i의 최단거리는 "숫자 i-1의 최단거리에서 1을 더한 값"과 "숫자 i를 2로 나눈 몫의 최단거리 +1" 중 작은 값
    # 예) 숫자 i가 2라면 "1의 최단거리인 0에 1을 더한 값 1" 와 "2를 2로 나눈 몫인 1의 최단거리인 0 +1= 1" 중 작은 값인 1을 선택
    # 예) 숫자 i가 4라면 "3의 최단거리인 1에 1을 더한 값 2" 와 "4를 2로 나눈 몫인 2의 최단거리인 1 +1= 2" 중 작은 값인 2를 선택
    # 예) 숫자 i가 6이라면 "5의 최단거리인 4에 1을 더한 값 5" 와 "6을 2로 나눈 몫인 3의 최단거리인 1 +1= 2" 중 작은 값인 2을 선택
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 숫자 i가 3으로 나눠지면
    #   숫자 i의 최단거리는 "숫자 i-1의 최단거리에서 1을 더한 값"과 "숫자 i를 3으로 나눈 몫의 최단거리 +1" 중 작은 값
    # 예) 숫자 i가 3이라면 "2의 최단거리인 1에 1을 더한 값 2" 와 "3을 3으로 나눈 몫인 1의 최단거리인 1 +1= 2" 중 작은 값인 2를 선택
    # 예) 숫자 i가 6이라면 "5의 최단거리인 4에 1을 더한 값 5" 와 "6을 3으로 나눈 몫인 2의 최단거리인 1 +1= 2" 중 작은 값인 2을 선택
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    

# print(dp)
# [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3, 4, 3, 4]
print(dp[a])



        
