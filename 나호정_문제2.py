items = ["", "노트북", "카메라", "책", "옷", "휴대용 충전기"]
weights = [0, 3, 1, 2, 2, 1]
values = [0, 12, 10, 6, 7, 4]

n = 5 # 물건의 개수
W = int(input("배낭 용량을 입력하세요 : "))

#(A[i][w] : i번째 물건까지 고려했을 때, 배낭 용량이 w일 경우의 최대 만족도)
A = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, W + 1):
        if weights[i] > w:          # 현재 물건 i의 무게가 w보다 크면 -> 배낭에 아예 못 넣음
            A[i][w] = A[i - 1][w]
        else:                         # 현재 물건 i가 배낭에 들어갈 수 있는 경우
            not_take = A[i - 1][w]    # i를 넣는 경우
            take = values[i] + A[i - 1][w - weights[i]]    # i를 넣지 않는 경우        
            A[i][w] = max(not_take, take)    # 둘 중 더 만족도가 큰 쪽을 A[i][w]에 저장
            
print("최대 만족도:", A[n][W])

# 선택한 물건 역추적
selected = [] # 선택할 물건들 저장할 리스트
w = W

for i in range(n, 0, -1): # 물건 뒤에서부터 하나씩 확인
    if A[i][w] != A[i - 1][w]: # 현재 값 A[i][w]가 이전 값 A[i-1][w]와 다르면 i번째 물건을 선택했다는 의미
        selected.append(items[i])  # i번째 물건 선택
        w -= weights[i] # 그 물건 무게만큼 용량 감소

selected.reverse() # 순서 다시 원래대로 정렬
print("선택된 물건:", selected)