def solution(s):
    answer = ''
    temp = s.split(" ")
    
    for idx, word in enumerate(temp):
        if len(word) >=1 :
            x1 = word[0]
            x2 = word[1:]
            if  'a'<=x1<='z':
                x1 = x1.upper()
            temp[idx] = x1 + x2.lower()
        elif word == ' ':
            pass
        else:
            temp[idx] = word.upper()

    print(temp)

    return " ".join(temp)