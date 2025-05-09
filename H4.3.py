MOD = 10 ** 9 + 7


def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    # dp[i] represents the number of people who know the secret on day i.
    dp = [0] * (n + 1)

    # The first person knows the secret on day 1
    dp[1] = 1

    # To track the number of new people learning the secret each day
    new_people = [0] * (n + 1)

    for day in range(2, n + 1):
        # Add new people who learned the secret today
        # Any person who learned the secret 'delay' days ago will share today
        if day > delay:
            dp[day] += new_people[day - delay]

        # The number of people who will forget the secret today
        if day >= forget:
            dp[day] -= new_people[day - forget]  # these people forget today

        # The number of people who learn the secret today
        new_people[day] = dp[day]

        # Ensure the number of people with the secret doesn't go negative
        dp[day] = max(dp[day], 0)  # ensure non-negative numbers

        # Keep the count modulo MOD
        dp[day] %= MOD

    # The result is the sum of people who still know the secret on the last day
    return sum(dp[n - forget + 1:]) % MOD  # Return the total people who know the secret at the end.

