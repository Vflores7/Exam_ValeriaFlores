def days_since_birthday(birthday):
    birth_day, birth_month, birth_year = map(int, birthday.split("-"))
    current_year = 2024
    current_month = 2
    current_day = 26

    total_days_passed = (current_year - birth_year - 1) * 365
    total_days_passed += (30 - birth_day) + (31 - 4)
    total_days_passed += current_day

    return total_days_passed



birthday = "17-04-2003"
print(days_since_birthday(birthday))