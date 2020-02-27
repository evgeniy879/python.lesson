line_str = 'hello world and people everywhereee!'
for number, i in enumerate(line_str.split(),1):
    if len(i) > 10:
        print(number, i[:10])
    else:
        print(number, i)
