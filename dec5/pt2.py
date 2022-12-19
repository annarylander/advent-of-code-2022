#load input data
def load_data():
    with open("input.txt", "r") as input_file:
        data = input_file.read().split("\n")
    return data

data = load_data()

#Parse data
def parse_data(data):
    instructions = data.replace("move", "").replace("from", "").replace("to", "").split()
    return [int(i) for i in instructions]


crate = {1: ["Q", "M", "G", "C", "L"], 
        2: ["R", "D", "L", "C", "T", "F", "H", "G"], 
        3: ["V", "J", "F", "N", "M", "T", "W", "R"], 
        4: ["J", "F", "D", "V", "Q", "P"], 
        5: ["N", "F", "M", "S", "L", "B", "T"], 
        6: ["R", "N", "V", "H", "C", "D", "P"], 
        7: ["H", "C", "T"], 
        8: ["G", "S", "J", "V", "Z", "N", "H", "P"], 
        9: ["Z", "F", "H", "G"]}

#move crate
def move_crate(instructions, crate_input):
    move_from = instructions[1]
    move_to = instructions[2]
    number_of_crates = instructions[0]
    if number_of_crates > len(crate_input[move_from]):
        number_of_crates = len(crate_input[move_from])
    
    if number_of_crates == 1:
        crate_input[move_to].append(crate_input[move_from].pop())
    else:   
        stack_to_move = crate_input[move_from][-number_of_crates:]
        crate_input[move_to].extend(stack_to_move)
        crate_input[move_from] = crate_input[move_from][:-number_of_crates]
    
    return crate_input
        
                
for line in data:
    instructions = parse_data(line)
    move_crate(instructions, crate)


#Get top crates
for i in range(1, 10):
    print(crate[i][-1], end=" ")