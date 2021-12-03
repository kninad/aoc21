'''
Problem 02
==========

Reading in from the text file

Loading the numbers in the file in an array

Algorithm --> 
'''

INPUT_FILE_PATH = "input/prob2.input.txt"

def parse_input(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    
    # new_format = [''] * len(lines)
    depth = 0
    horzp = 0
    # for idx, l in enumerate(lines):
    for line in lines:
        command, value = line.split()

        if command == 'forward':
            horzp += int(value)
        elif command == 'up':
            depth -= int(value)
        elif command == 'down':
            depth += int(value)

    print("Horizontal Position: ", horzp)
    print("Depth: ", depth)  
    
    return depth * horzp

def main():
    print("Answer: ", parse_input(INPUT_FILE_PATH))


if __name__ == "__main__":
    main()
