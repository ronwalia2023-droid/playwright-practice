def add(a, b):
    result = a + b
    return result

total = add(2, 3)
print(total)      # 5


def build_expected_url(a):
    result = f"https://ronisking.com/{a}"
    return result

login_url = build_expected_url("login")
checkout_url = build_expected_url("checkout")

print(login_url)
print(checkout_url)

