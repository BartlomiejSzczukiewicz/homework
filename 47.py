def f(text):
    result = ''
    for i in text:
        if i == text[len(text)-1]:
            result += i
            return result
        result += i + '-'

print(f("Univesity") )