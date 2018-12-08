from user import Admin

austin = Admin('austin', 'breedveld', 'a_breedveld', 'a_breedveld@test.com', 'arizona')
austin.describe_user()

austin_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
austin.privileges.privileges = austin_privileges

print("\nThe admin " + austin.username + " has these privileges: ")
austin.privileges.show_privileges()