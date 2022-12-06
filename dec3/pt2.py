def load_data():
    with open("input.txt", "r") as input_file:
        data = input_file.read().split("\n")
    return data

data = load_data()

# split input into groups of 3
def split_input(data):
    groups = []
    for i in range(0, len(data), 3):
        group = data[i:i+3]
        groups.append(group)
    return groups

groups = split_input(data)

#check if character is in group
def get_char(group):
    for char in group[0]:
        if char in group[1] and char in group[2]:
            return char
    return None

# calculate priority
def calculate_priority(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

#sum up the priorities
sum_priority = 0

for group in groups:
    char = get_char(group)
    prio = calculate_priority(char)
    sum_priority += prio

print("sum priority:", sum_priority)

