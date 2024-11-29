N = int(input())
temp = []

for _ in range(N):
    word = input()
    temp.append(word)


words = set(temp)

for w in temp:
    reversed_word = w[::-1]

    if reversed_word in words:
        print(len(w), w[len(w)//2])
        break
