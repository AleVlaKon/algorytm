def get_oldest(ages: dict):
    oldest_name = ''
    oldest_age = 1

    for name, age in ages.items():
        if age > oldest_age:
            oldest_age = age
            oldest_name = name
        elif age == oldest_age and oldest_name > name:
            oldest_name = name

    return oldest_name


print(get_oldest({'Елисей': 49, 'Сидор': 31, 'Василиса': 21, 'Мирон': 40, 'Юрий': 26}))