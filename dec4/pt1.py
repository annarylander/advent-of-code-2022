#load input data
def load_data():
    with open("input.txt", "r") as input_file:
        data = input_file.read().split("\n")
    return data

data = load_data()


pair_overlaps = 0

#loop through all pairs and check if they overlap
for line in data:
    pair = line.replace(",", "-").split("-")
    if int(pair[2]) >= int(pair[0]) and int(pair[3]) <= int(pair[1]):
        pair_overlaps += 1
    elif int(pair[2]) <= int(pair[0]) and int(pair[3]) >= int(pair[1]):
        pair_overlaps += 1
print("pair overlaps:", pair_overlaps)
