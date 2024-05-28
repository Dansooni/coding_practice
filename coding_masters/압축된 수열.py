# n은 정수의 갯수, size_limit은 파일의 크기제한
n, size_limit = map(int, input().split())

# 정수배열 입력받기
input_integers = list(map(int, input().split()))

# 10부터 시작하여 62까지 base 값을 바꿔가며 size_limit을 만족시키는 base 값 찾기
for b in range(10, 63):
    # 각 정수가 차지하는 자릿수를 tmp_size에 누적
    tmp_size = 0
    for i in input_integers:
        while i:
            tmp_size += 1
            i //= b
            
    # tmp_size가 size_limit을 만족시켰는지 확인
    if tmp_size + n - 1 <= size_limit:
        print(b)
        break
    elif b == 62:
        print(-1)