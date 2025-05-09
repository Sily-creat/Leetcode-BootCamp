from collections import Counter


def findAnagrams(s: str, p: str):
    # List to store the start indices of the anagrams
    result = []

    # Length of the input strings
    len_s, len_p = len(s), len(p)

    # Edge case: If p is longer than s, no anagrams possible
    if len_p > len_s:
        return result

    # Initialize counters for p and the first window in s
    p_count = [0] * 26  # Counter for string p
    window_count = [0] * 26  # Counter for the sliding window in s

    # Populate the p_count array with the frequency of each character in p
    for char in p:
        p_count[ord(char) - ord('a')] += 1

    # Populate the window_count array with the frequency of the first window in s
    for i in range(len_p):
        window_count[ord(s[i]) - ord('a')] += 1

    # If the first window is a valid anagram, add index 0 to the result
    if window_count == p_count:
        result.append(0)

    # Sliding window: Iterate over s starting from the second window
    for i in range(len_p, len_s):
        # Add the new character to the window
        window_count[ord(s[i]) - ord('a')] += 1
        # Remove the old character from the window
        window_count[ord(s[i - len_p]) - ord('a')] -= 1

        # If the window matches p, record the start index
        if window_count == p_count:
            result.append(i - len_p + 1)

    return result
