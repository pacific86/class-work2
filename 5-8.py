usernames = ['sam', 'erica', 'admin', 'austin', 'leah']

for username in usernames:
    if username == 'admin':
        print("Hello admin, do you want to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")