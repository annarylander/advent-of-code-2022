def load_data():
    with open("input.txt", "r") as input_file:
        data = input_file.read().split("\n")
    return data


# split string into two parts
def split_string(line):
    firstpart = line[:len(line)//2]
    secondpart = line[len(line)//2:]
    return firstpart, secondpart

# get the character that appears in both parts
def get_char(firstpart, secondpart):
    secondpart_set = set(secondpart)
    for char in firstpart:
        if char in secondpart_set:
            return char
    return None


# convert character to number
def calculate_priority(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


if __name__ == "__main__":
    # sum up the priority-numbers
    sum_priority = 0

    data = load_data()
    for line in data:
        compartment_1, compartment_2 = split_string(line)
        char = get_char(compartment_1, compartment_2)
        prio = calculate_priority(char)
        sum_priority += prio

    print("sum_priority:", sum_priority)
