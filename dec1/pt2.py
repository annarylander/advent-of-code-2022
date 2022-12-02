f = open("input.txt", "r")

data = f.read().split("\n")
data.append("")

sum = 0
sum_list = []

for numb in data:
    if len(numb) == 0:
        sum_list.append(sum)
        sum = 0
    else:
        sum += int(numb)
        
three_most_calories = sorted(sum_list, reverse=True)[0:3]

sum_calories = 0
for calories in three_most_calories:
    sum_calories += calories

print(sum_calories)