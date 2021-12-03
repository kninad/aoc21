'''
Problem 02
==========

Reading in from the text file

Loading the numbers in the file in an array

Algorithm:

Brute Force approach -- for K-bit number, simply keep track of counts of 1 and 0 for
that bit position.
'''

import numpy as np
INPUT_FILE_PATH = "input/prob3.input.txt"


def parse_input(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    
    lines = [l.strip() for l in lines]
    return lines

def update_counts(bitmask: str, c_one, c_zero) -> None:
    for i, c in enumerate(bitmask):
        if c == '1':
            c_one[i] += 1
        else:
            c_zero[i] += 1


def bit_calc(array):
    bit_length = len(array[0])
    one_bits =  np.zeros(bit_length)
    zero_bits = np.zeros(bit_length)

    for bitmask in array:
        update_counts(bitmask, one_bits, zero_bits)
    
    gamma = ['0'] * bit_length
    epsilon = ['0'] * bit_length

    for i in range(bit_length):
        if one_bits[i] > zero_bits[i]:
            gamma[i] = '1'
        else:
            epsilon[i] = '1'
    
    gamma_val = int('0b' + ''.join(gamma), 2)
    epsilon_val = int('0b' + ''.join(epsilon), 2)

    return gamma_val * epsilon_val





def main():
    print("Answer: ", bit_calc(parse_input(INPUT_FILE_PATH)))


if __name__ == "__main__":
    main()