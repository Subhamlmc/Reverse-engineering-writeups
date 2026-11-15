username = input("Enter username: ")

result = 0

for letter in username:
    result += ord(letter)

print("Sum:", result)

final_result = result * ord("{")

print("Final result:", final_result)