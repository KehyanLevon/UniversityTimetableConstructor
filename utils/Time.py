from datetime import datetime, timedelta

def timeSum(time1, time2):
    time1 = datetime.strptime(time1, '%H:%M:%S')
    timesplit = time2.split(':')
    result = time1 + timedelta(hours=int(timesplit[0]))
    if len(timesplit) > 1:
        result += timedelta(minutes=int(timesplit[1]))
    return result.strftime('%H:%M:%S')


def timeDif(time1, time2):
    time2split = time2.split(':')
    time1split = time1.split(':')
    hour1, minute1, second1 = [int(i) for i in time1split]
    hour2, minute2, second2 = [int(i) for i in time2split]
    if hour1 > hour2 or (hour1 == hour2 and minute1 > minute2):
        time1 = datetime.strptime(time1, '%H:%M:%S')
        result = time1 - timedelta(hours=hour2, minutes=minute2)
    else:
        time2 = datetime.strptime(time2, '%H:%M:%S')
        result = time2 - timedelta(hours=hour1, minutes=minute1)
    return result.strftime('%H:%M:%S')

def IsDifMoreOrEqualToDuration(time1, time2, duration):
    result = timeDif(time1, time2)
    return compare(result,duration)

def compare(time1,time2):
    hour1, minute1, second1 = [int(i) for i in time1.split(':')]
    hour2, minute2, second2 = [int(i) for i in time2.split(':')]
    if hour1 > hour2 or (hour1 == hour2 and minute1 >= minute2):
        return True
    return False

def formaterToMinute(data):
    if data < 10:
        data = '0' + str(data)
    return '00:{}:00'.format(data)
