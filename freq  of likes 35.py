def calculate_frequency_distribution(likes_data):
    frequency_distribution = {}

    for likes in likes_data:
        if likes in frequency_distribution:
            frequency_distribution[likes] += 1
        else:
            frequency_distribution[likes] = 1

    return frequency_distribution

# Example dataset containing likes received by each post
likes_data = [10, 5, 20, 10, 15, 5, 10, 20, 15, 10]

# Calculate frequency distribution
frequency_distribution = calculate_frequency_distribution(likes_data)

# Print the frequency distribution
print("Likes\tFrequency")
print("-----------------")
for likes, frequency in frequency_distribution.items():
    print(f"{likes}\t{frequency}")
