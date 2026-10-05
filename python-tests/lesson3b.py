

def print_test_cases(case):
    print(f"Test Case: {case['name']}")
    print(f"Username: {case['username']}")
    print(f"Password: {case['password']}")
    print(f"Expected Result: {case['expected']}")
    print("---")


test_cases = [
    {"name": "Valid Login", "username": "tomsmith", "password": "SuperSecretPassword!", "expected": "You logged into a secure area!"},
    {"name": "Invalid Password", "username": "tomsmith", "password": "wrongpass", "expected": "Your password is invalid!"},
    {"name": "Invalid Username", "username": "wronguser", "password": "SuperSecretPassword!", "expected": "Your username is invalid!"}
]
for case in test_cases:
    print_test_cases(case)