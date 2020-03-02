def user_data(sec_name, name, birth, city, email, phone):
    return f'name - {name}, sec_name - {sec_name}, birth - {birth}, city - {city}, email - {email}, phone - {phone}'


print(user_data(name='John', sec_name='Wick', birth=2014, city='Minsk', email='JohnWick@gmail.com', phone='unknown'))
