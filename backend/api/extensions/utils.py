from . import jalali 
from django.utils import  timezone

def convert_to_persian_number(string):
    numbers = {
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
        "0":"۰",
    }
    
    for e , p in numbers.items():
        string=string.replace(e,p)
    return string    


def jalali_convertor(time):
    listofmonth=["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]
    time = timezone.localtime(time)
    really_time="{},{},{}".format(time.year,time.month,time.day)
    jalali_date=jalali.Gregorian(really_time).persian_tuple()
    for index , text in enumerate(listofmonth):
        if jalali_date[1]==index+1:
            output=" در {} {} {} , ساعت {} : {}".format(
            jalali_date[2],text,jalali_date[0],
            time.minute,
            time.hour
            )
            break 
    return convert_to_persian_number(output)