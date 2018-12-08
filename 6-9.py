favorite_places = {
    'janelle': ['england', 'italy', 'new orleans'],
    'austin': ['kauai', 'montana', 'alaska'],
    'megan': ['italy', 'wales', 'prague']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())