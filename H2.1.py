def myAtoi(s: str) -> int:
    # Step 1: Remove leading whitespaces
    s = s.lstrip()

    # Step 2: Check if the string is empty after removing whitespaces
    if not s:
        return 0

    # Step 3: Handle the sign
    sign = 1  # Default sign is positive
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # Step 4: Convert the digits to an integer
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break

    # Apply the sign
    result *= sign

    # Step 5: Clamp the result to fit in a 32-bit signed integer range
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result
