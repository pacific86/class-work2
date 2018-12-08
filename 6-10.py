favorite_numbers = {
    'janelle': [13, 86],
    'austin': [99, 393, 10],
    'charlotte': [3, 22],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))