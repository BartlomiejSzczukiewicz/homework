def f(dice):
    max_count = 0  # Initialize the maximum count of consecutive dice
    current_count = 1  # Initialize the current count of consecutive dice
    most_frequent_dice = dice[0]  # Initialize the most frequent dice to the first digit

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                most_frequent_dice = dice[i - 1]
            current_count = 1

    # Check one last time after the loop ends
    if current_count > max_count:
        max_count = current_count
        most_frequent_dice = dice[-1]

    return int(most_frequent_dice)

# Test cases
print(f("5233165554211"))  # Should return 5
print(f("2133"))  # Should return 3
