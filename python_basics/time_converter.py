import pytz
from datetime import datetime
# print(set(pytz.all_timezones))

def get_country_localtime(country_name):
    print(f"Country: {country_name}")

    local_timezone = pytz.timezone(country_name)

    week_day_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    
    _date = datetime.now(local_timezone).date()
    week_day = week_day_dict[datetime.now(local_timezone).weekday()]
    _hour = datetime.now(local_timezone).hour
    _min = datetime.now(local_timezone).minute
    _time = str(_hour) + ":" + str(_min)

    return _date, week_day, _hour, _time
