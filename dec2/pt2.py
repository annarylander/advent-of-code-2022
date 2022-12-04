import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))
with open("input.txt", "r") as input_file:
    data = input_file.read().split("\n")

game_score = {"X": 0,
"Y": 3,
"Z": 6}

hand_score = {"A": 1,
"B": 2,
"C": 3}

# get my hand
def get_hand(result, opponent):
    hand = ""
    if result == "Y":
        hand = opponent
    elif result == "Z":
        if opponent == "A":
            hand = "B"
        elif opponent == "B":
            hand = "C"
        elif opponent == "C":
            hand = "A"
    elif result == "X":
        if opponent == "A":
            hand = "C"
        elif opponent == "B":
            hand = "A"
        elif opponent == "C":
            hand = "B"
    print("hand:", hand)
    return hand


# get my score
def get_hand_score(hand):
    score = hand_score[hand]
    return score


# Loop through each round and calculate total score
total_score = 0
for i in range(len(data)):
    result = data[i][2]
    opponent = data[i][0]
    print("result:", result)
    print("opponent:", opponent)

    #get score for win/loss/draw
    total_score += game_score[result]

    #get score for hand
    hand = get_hand(result, opponent)
    score = get_hand_score(hand)
    total_score += score



print("total score:", total_score)

