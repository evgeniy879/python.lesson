km = int(input())
limit_km = int(input())
count_day = 1
while km < limit_km:
    km = km * 110/100
    count_day += 1
print(f'номер дня {count_day}')
