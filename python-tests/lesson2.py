# Step 1: Create a list of test cases
test_cases = ["Login", "Search", "Checkout", "Logout"]

# Step 2: Loop through the list and print each one
for index, test in enumerate(test_cases, start=1):
    print(f"Test {index}: {test}")


# Step 3: Print the total number of tests
print(f"Total tests: {len(test_cases)}")