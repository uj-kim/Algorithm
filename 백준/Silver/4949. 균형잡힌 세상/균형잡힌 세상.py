# import sys
# 입력
# 무한루프
# 무한루프 안에 입력을 받는 형식으로
while(True):
    line = input()
    # stack 선언
    stack = []
    # break (.) 종료
    if line == ".":
        break
    for char in line:
        # 열린 괄호 "(" or "["는 스택에 추가
        if char == "("or char == "[" :
            stack.append(char)
        # 닫힌 괄호 ") ]"는 짝이 맞는지 확인 후 제거
        elif char == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                # 비어있지 않으면 stack )을 추가
                stack.append(char)
        elif char == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                # 비어있지 않으면
                stack.append(char)
    # 스택이 비어있지 않으면
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
