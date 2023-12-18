import calendar
str_date = input("Nhap ngay thang nam dd/mm/yyyy: ")
list_date = str_date.split('/')
_day = int(list_date[0])
_month = int(list_date[1])
_year = int(list_date[2])
tup_day = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
_date = calendar.weekday(_year,_month,_day)
print(str_date,"is",tup_day[_date])