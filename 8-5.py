def describe_city(city, country='italy'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('rome')
describe_city('venice')
describe_city('paris', 'france')