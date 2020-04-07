entered_day = int(input('Enter a day number please'))
dict_days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday',
             5: 'Thursday', 6: 'Friday', 7: 'Saturday'}


def daynumbers(entered_day):
    if entered_day in dict_days:
        print(dict_days.get(entered_day))
    else:
        print('you are out of range')


daynumbers(entered_day)
assert dict_days.get(entered_day) == 'Sunday'
