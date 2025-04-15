'''
1.3 URLify:
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
(Note: If implementing in Java, 
please use a character array so that you can perform this operation in place.)

EXAMPLE
Input: "Mr John Smith      ", 13
Output: "Mr%20John%20Smith"
'''

def urlify(s, count):
    list_s = list(s)
    n = len(s)-1
    count = count-1
    
    # iterate from the back because there is space provided.
    while count >= 0:
        if list_s[count] != " ":
            list_s[n] = list_s[count]
        else:
            # insert %20 when there is a space.
            list_s[n] = "0"
            n -= 1
            list_s[n] = "2"
            n -= 1
            list_s[n] = '%'
        count -= 1
        n -= 1
    
    return "".join(list_s)


# ==== Test cases ====
# Test cases based on provided scenarios
test_cases = [
    {
        "description": "Basic example",
        "input": "Mr John Smith    ",
        "true_length": 13,
        "expected": "Mr%20John%20Smith"
    },
    {
        "description": "String without any spaces",
        "input": "HelloWorld",
        "true_length": 10,
        "expected": "HelloWorld"
    },
    {
        "description": "Multiple consecutive spaces in the middle",
        "input": "A  B    ",
        "true_length": 4,
        "expected": "A%20%20B"
    },
    {
        "description": "Empty string",
        "input": "",
        "true_length": 0,
        "expected": ""
    },
    {
        "description": "Combination of spaces in various positions",
        "input": "I  love  coding        ",
        "true_length": 15,
        "expected": "I%20%20love%20%20coding"
    }
]

# Run tests
for idx, test in enumerate(test_cases, start=1):
    result = urlify(test["input"], test["true_length"])
    print(f"Test Case {idx}: {test['description']}")
    print(f"Input: {test['input']!r}, True Length: {test['true_length']}")
    print(f"Output: {result!r}")
    print(f"Expected: {test['expected']!r}")
    assert result == test["expected"], f"Test case {idx} failed: expected {test['expected']!r} but got {result!r}"
    print("Passed\n")

print("All test cases passed!")
