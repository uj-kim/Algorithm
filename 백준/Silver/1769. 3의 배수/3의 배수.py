def solve():
    X = input().strip()  # 입력된 숫자를 문자열로 처리
    count = 0  # 변환 횟수

    # 자릿수의 합이 한 자리수가 될 때까지 반복
    while len(X) > 1:
        X = str(sum(map(int, X)))  # 자릿수 합 계산
        count += 1  # 변환 횟수 증가

    # 결과 출력
    print(count)
    print("YES" if int(X) % 3 == 0 else "NO")

solve()
