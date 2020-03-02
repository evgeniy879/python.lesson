def inc_func(text):
    text_change = ''
    text_change = text[0].upper()
    for i in range(1, len(text)):
        text_change += text[i].lower()
    return text_change


print(inc_func('eVErYbOdY'))
