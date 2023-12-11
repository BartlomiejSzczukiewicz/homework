import re

def f(first_letter,last_letter):
    with open('data.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        regex =  r'\b[' + first_letter + r']\w*' + last_letter + r'\b'
        words = re.findall(regex,text)
    return len(words)

print(f("w","d"))