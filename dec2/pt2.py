import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))


def load_data():
    with open("input.txt", "r") as input_file:
        data = input_file.read().split("\n")
    return data

X = "X"
Y = "Y"
Z = "Z"

A = "A"
B = "B"
C = "C"

game_score = {X: 0, Y: 3, Z: 6}
hand_score = {A: 1, B: 2, C: 3}

# get my hand
def get_hand(result, opponent):
    if result == Y:
        hand = opponent
    elif result == Z:
        if opponent == A:
            hand = B
        elif opponent == B:
            hand = C
        elif opponent == C:
            hand = A
    elif result == X:
        if opponent == A:
            hand = C
        elif opponent == B:
            hand = A
        elif opponent == C:
            hand = B
    return hand

# get my score
def get_hand_score(hand):
    score = hand_score[hand]
    return score

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
        hand = get_hand(result, opponent)
        total_score += get_hand_score(hand)

    print("total_score:", total_score)
