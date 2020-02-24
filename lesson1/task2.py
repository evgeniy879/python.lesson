time = int(input())
time = time % (24 * 3600)
hour = time // 3600
min = (time % 3600) // 60
sec = (time % 3600) % 60
print(f'{hour:02d}:{min:02d}:{sec:02d}')
