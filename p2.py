def solution(a, b):
    # 1. a와 b를 문자열로 변환하여 이어 붙인 후, 다시 정수로 변환
    z = int(str(a) + str(b))
    
    # 2. 2 * a * b 계산
    y = 2 * a * b
    
    # 3. z와 y 중 더 큰 값을 반환
    return max(z, y)