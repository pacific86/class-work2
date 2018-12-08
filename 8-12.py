def make_sandwich(*items):
    print("\nI'll make you a tasty sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready to go!")

make_sandwich('turkey', 'havarti cheese', 'lettuce', 'mustard')
make_sandwich('salami', 'ham', 'tomato', 'mustard')
make_sandwich('hummus', 'cucumber', 'lettuce')