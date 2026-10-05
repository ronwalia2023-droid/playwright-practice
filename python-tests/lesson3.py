login_test = {
    "username": "TomSmith",
    "password": "SuperSecretPassword!",
    "expected" : "You logged into a secure area!",
    "note": "You are a superstar"}

print(f"Testing Login for:{login_test['username']}")
print(f"Expected Result:{login_test['expected']}")
print(f"Note to customer:{login_test['note']} {login_test['username']}")
