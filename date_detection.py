import re
full_date = re.compile(r'(\d+)/(\d+)/(\d{4})$')

mo = full_date.search('29/02/2019')

day = mo.group(1)
if len(day) != 2:
    day = '0' + day
month = mo.group(2)
if len(month) != 2:
    month = '0' + month
year = mo.group(3)

#Check if the date is valid
if month == '04' or month == '06' or month == '09' or month == '11':
    if day >'30':
        print('Invalid date!')
elif month == '02':
    if day == "29":
        if int(year)%4 == 0:
            if int(year)%100 == 0 and int(year)%400 == 0:
                pass
        else:
            print('Invalid date!')
    if day >'29':
        print('Invalid date!')
else:
    if day>'31':
        print('Invalid date!')

print(f'Date found : {day}/{month}/{year}')
