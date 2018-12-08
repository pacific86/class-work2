def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_corolla = make_car('toyota', 'corolla', color='silver', tow_package=True)
print(my_corolla)

my_soul = make_car('kia', 'soul', year=2016, color='white',
        headlights='popup')
print(my_soul)