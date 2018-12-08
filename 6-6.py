favorite_languages = {
    'janelle': 'python',
    'rob': 'r',
    'sam': 'html',
    'austin': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['janelle', 'rob', 'sam', 'austin', 'leah', 'chelsea', 'amelia']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")