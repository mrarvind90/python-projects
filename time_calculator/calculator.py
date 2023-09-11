from typing import Dict

DAYS_OF_WEEK = {
    "sunday": 1,
    "monday": 2,
    "tuesday": 3,
    "wednesday": 4,
    "thursday": 5,
    "friday": 6,
    "saturday": 7
}


def convert_to_24_hour_obj(time: str, am_pm: str, day_of_week: str) -> Dict[str, int]:
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    if am_pm.lower() == "am" and hours == 12:
        hours = 0
    elif am_pm.lower() == "pm" and hours < 12:
        hours += 12

    return {
        "days": 0,
        "hours": hours,
        "minutes": minutes,
        "day_of_week": DAYS_OF_WEEK[day_of_week.lower()] if day_of_week else 1
    }


def format_time_string(time: Dict[str, int], day_of_week: str) -> str:
    formatted_time_string = ""
    formatted_minute = str(time["minutes"]).rjust(2, "0")

    if time["hours"] > 12:
        formatted_time_string += f"{str(time['hours'] - 12)}:{formatted_minute} PM"
    elif time["hours"] == 12:
        formatted_time_string += f"{str(time['hours'])}:{formatted_minute} PM"
    elif time["hours"] == 0:
        formatted_time_string += f"12:{formatted_minute} AM"
    else:
        formatted_time_string += f"{str(time['hours'])}:{formatted_minute} AM"

    if day_of_week:
        for key, value in DAYS_OF_WEEK.items():
            if value == time["day_of_week"]:
                formatted_time_string += f", {key.capitalize()}"

    if time["days"] > 0:
        formatted_time_string += " (next day)" if time["days"] < 2 else f" ({time['days']} days later)"

    return formatted_time_string


def add_time(start: str, duration: str, day_of_week: str = "") -> str:
    time, am_pm = start.split(" ")
    new_time: Dict[str, int] = convert_to_24_hour_obj(time, am_pm, day_of_week)
    dur_hours, dur_minutes = duration.split(":")

    total_mins = new_time["minutes"] + int(dur_minutes)
    if total_mins >= 60:
        new_time["hours"] += total_mins // 60
        new_time["minutes"] = total_mins % 60
    else:
        new_time["minutes"] = total_mins

    total_hours = new_time["hours"] + int(dur_hours)
    if total_hours >= 24:
        new_time["days"] += total_hours // 24
        new_time["hours"] = total_hours % 24
    else:
        new_time["hours"] = total_hours

    upd_dow = (new_time["day_of_week"] + new_time["days"]) % 7
    if upd_dow >= 7:
        new_time["day_of_week"] += upd_dow - 1
    else:
        new_time["day_of_week"] = upd_dow

    return format_time_string(new_time, day_of_week)
