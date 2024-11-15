def convert_to_24_hour(time_str):
    components = time_str.split()
    time = components[0].split(":")
    hours = int(time[0])
    minutes = int(time[1])
    am_pm = components[1].lower()

    if am_pm == "pm" and hours != 12:
        hours += 12
    elif am_pm == "am" and hours == 12:
        hours = 0

    return f"{hours:02d}:{minutes:02d}"


def convert_to_12_hour(time_str):
    components = time_str.split(":")
    hours = int(components[0])
    minutes = components[1]

    am_pm = "AM" if hours < 12 else "PM"
    hours = hours % 12
    if hours == 0:
        hours = 12

    return f"{hours}:{minutes} {am_pm}"

        # Example usage:
time_str = input("Enter a time in AM/PM format: ").lower()
if "am" or "pm" in time_str:
    converted_time = convert_to_12_hour(time_str)
    print("Converted to 12-hour format:", converted_time)
else:   
    converted_time = convert_to_24_hour(time_str)
    print("Converted to 24-hour format:", converted_time)
