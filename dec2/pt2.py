import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

def load_data():
    with open("input.txt", "r") as input_file:
        data = input_file.read().split("\n")
    return data

loss = "X"
draw = "Y"
win = "Z"

rock = "A"
paper = "B"
scissor = "C"

game_score = {loss: 0, draw: 3, win: 6}
hand_score = {rock: 1, paper: 2, scissor: 3}

# get my hand
def get_hand(result, opponent):
    if result == draw:
        hand = opponent
    elif result == win:
        if opponent == rock:
            hand = paper
        elif opponent == paper:
            hand = scissor
        elif opponent == scissor:
            hand = rock
    elif result == loss:
        if opponent == rock:
            hand = scissor
        elif opponent == paper:
            hand = rock
        elif opponent == scissor:
            hand = paper
    return hand

# get my score
def get_hand_score(result, opponent):
    hand = get_hand(result, opponent)
    return hand_score[hand]

if __name__ == "__main__":
    # Loop through each round and calculate total score
    total_score = 0
    data = load_data()
    for line in data:
        opponent = line[0]
        result = line[2]

        # get score for win/loss/draw
        total_score += game_score[result]
        # get score for hand
        total_score += get_hand_score(result, opponent)

    print("total_score:", total_score)
