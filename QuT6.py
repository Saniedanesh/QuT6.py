from datetime import datetime
d= str(input())
date = datetime.strptime(d, '%Y-%m-%d')
print("day:", date.day)
print("month:", date.month)
print("year:", date.year)
x = "Hello"
y = 15

print(bool(x))
print(bool(y))