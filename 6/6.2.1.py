def check_letters(s: str) -> str:
    result = ''
    lower_s = s.lower()
    alphebet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alphebet)):
        result += str(int(alphebet[i] in lower_s))
    return result

print(check_letters('ABcd'))
print(check_letters('A-Z'))