f = open("input.txt", "r")

data = f.read().split("\n")

sum = 0
sum_list = []

for numb in data:
    if len(numb) == 0:
        sum_list.append(sum)
        sum = 0
    else:
        sum += int(numb)
        

most_calories = sorted(sum_list, reverse=True)[0]

print(most_calories)





