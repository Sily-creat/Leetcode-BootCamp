def decodeString(s: str) -> str:
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            # Build the number (could be more than one digit)
            current_number = current_number * 10 + int(char)
        elif char == "[":
            # Push the current number and current string to the stack
            stack.append((current_number, current_string))
            current_string = ""  # Reset the current string for the new substring
            current_number = 0  # Reset the current number
        elif char == "]":
            # Pop from stack and repeat the current string
            prev_number, prev_string = stack.pop()
            current_string = prev_string + current_string * prev_number
        else:
            # Append character to the current string
            current_string += char

    return current_string
