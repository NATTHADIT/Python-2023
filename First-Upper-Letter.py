def cap(sen):
    result = ''
    nochange = ['for', 'and' , 'with' , 'of']
    sen = sen.split(' ')
    for word in sen:
        if word in nochange:
            result += word
        else:
            result += word.capitalize()
        result += ' '
    
    print(result)



s = str(input())
cap(s)