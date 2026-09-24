# make an algorithm that makes gray code - binary where it changes just one digit at a time
#

number_of_bits = int(input("Enter the number of bits: "))
binary_list = [0] * number_of_bits
binary = [0, 1]

for i in range(number_of_bits):
    # start with all zeros
    # then change one digit at a time
    for j in range(len(binary)):
        binary_list[i] = binary[j]
        print(binary_list)
