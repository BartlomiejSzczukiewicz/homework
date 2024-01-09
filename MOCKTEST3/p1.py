def f(word):
    wave = []
    for i in range(len(word)):
        wave.append(word[:i] + word[i].upper() + word[i+1:])
    return '-'.join(wave)

print(f("hello"))
