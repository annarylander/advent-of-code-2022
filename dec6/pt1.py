def load_data():
    with open("input.txt", "r") as input_file:
        data = input_file.read().replace("\n", "")
    return data

data = load_data()

def get_marker(data):
    marker = 0
    unique_chars = []
    for i, letter in enumerate(data):
        if len(unique_chars) == 4:
            marker = i
            break    
        if letter not in unique_chars:
            unique_chars.append(letter)
        else:
            unique_chars = unique_chars[unique_chars.index(letter)+1:]
            unique_chars.append(letter)
            
    return marker

print(get_marker(data))