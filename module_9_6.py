def all_variants(text):
    for c in range(len(text)):
        for i in range(len(text) - c):
            yield text[c:i + c + 1]
a = all_variants("abc")
for i in a:
    print(i)