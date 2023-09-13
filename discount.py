from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-09-13
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2023-09-13 10:48:25.086067
print(type(time))  # <class 'datetime.datetime'>

print(time.hour)
print(today.day)

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 13/09/2023

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 10:51

formated_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(formated_datetime)  # 2023-09-13 10:52:47

# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0
tommorow = today + timedelta(days=1)
print(tommorow)  # 2023-09-14
# t2 = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'

# 11:30

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tommorow, 'price': 80.0},
    {'sku': 3, 'exp_date': today, 'price': 30},
]
print(products)

for product in products:
    if product['exp_date'] != today:
        continue  # nie wykona kolejnych instrukcji, pobierze kolejny elemnt z listy
    product['price'] *= 0.8  # p = p * 0.8
    print(f"""
    Price for sku = {product['sku']}
    is now {product['price']}""")
