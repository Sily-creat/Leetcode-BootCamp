def reverseWords(s: str) -> str:
    # Step 1: Strip leading/trailing spaces and split the string into words
    words = s.strip().split()

    # Step 2: Reverse the list of words
    words.reverse()

    # Step 3: Join the reversed list into a single string with a single space separator
    return ' '.join(words)
