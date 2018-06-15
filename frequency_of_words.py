s = input()
freq = {}
for word in s.split():
    freq[word] = freq.get(word, 0) + 1
    print(freq.get(word, 0))

print(freq)

words = list(freq.keys())
print(words)
words.sort()

for w in words:
    print(f"{w}:{freq[w]}")
