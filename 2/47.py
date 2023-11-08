def f(text):

    changed = text[0]
    for i in range (len(text)):
        changed += text[i]
        changed += '-'
    if changed == '':
        return ''
    return changed

if __name__ == '__main__':
    print(f('University'))