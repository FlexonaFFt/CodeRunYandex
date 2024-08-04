from datetime import datetime, timedelta

def time_to_minutes(time_string):
    h, m = map(int, time_string.split(":"))
    return h * 60 + m

def minutes_to_time(minutes):
    h = minutes // 60
    m = minutes % 60
    return f'{h:02}:{m:02}'

def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

def find_meeting_time(start_a, start_b, lap_a, lap_b):
    start_a_min = time_to_minutes(start_a)
    start_b_min = time_to_minutes(start_b)
    lap_a_min = time_to_minutes(lap_a)
    lap_b_min = time_to_minutes(lap_b)

    cycle = lcm(lap_a_min, lap_b_min)

    for t in range(0, cycle * 7, lap_a_min):
        if (start_a_min + t - start_b_min) % lap_b_min == 0:
            meeting_time_min = start_a_min + t
            day_index = (meeting_time_min // (24 * 60)) % 7
            time_of_day = meeting_time_min % (24 * 60)

            days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            return f"{days[day_index]}\n{minutes_to_time(time_of_day)}"

    return "Never"


if __name__ == '__main__':
    start_a = input()
    start_b = input()
    lap_a = input()
    lap_b = input()
    print(find_meeting_time(start_a, start_b, lap_a, lap_b))
