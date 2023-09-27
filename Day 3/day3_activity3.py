user_input = input("INPUT: ").upper()

reversed_str = ""

for i in range(len(user_input) - 1, -1, -1):
    reversed_str += user_input[i]

print(f"OUTPUT: {reversed_str} ({len(user_input)} characters)")
