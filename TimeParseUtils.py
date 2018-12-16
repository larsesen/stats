def get_time_in_minutes_and_seconds(time):
    period, timestamp = time.split('-')

    minutes = int(timestamp.split(':')[0].strip())
    seconds = int(timestamp.split(':')[1].strip())

    period = int(period)
    while period > 1:
        minutes += 20
        period -= 1

    minutes = pretty_print_time(minutes)
    seconds = pretty_print_time(seconds)
    return minutes, seconds


def pretty_print_time(number):
    if number < 10:
        number = '0' + str(number)
    return number


def get_period_number(time):
    return int(time.split('-')[0].strip())