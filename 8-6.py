def city_country(city, country):
    return(city.title() + ", " + country.title())

city = city_country('rome', 'italy')
print(city)

city = city_country('geneva', 'switzerland')
print(city)

city = city_country('athens', 'greece')
print(city)