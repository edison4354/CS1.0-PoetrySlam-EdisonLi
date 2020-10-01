import random

# Reads the poem file then return a list of strings containing the lines of the file
def get_file_lines(filename):
    read_file = open(filename, 'r')
    return read_file.readlines()

# Reverses the list of strings/lines from the poem then prints them line by line including the original line number 
def lines_printed_backwards(lines_list):
    lines_list_reverse = lines_list[::-1] # reverses the list of lines and assigned it to another varible
    for string in lines_list_reverse:
        line_number = lines_list.index(string) + 1 # assigned a varible the index of the string containing the line
        print(line_number, string)

def lines_printed_random(lines_list):
    for i in range(len(lines_list)):
        random_index = random.randint(0, len(lines_list))
        print(lines_list[random_index - 1])

# def lines_printed_random(lines_list):
#     random.shuffle(lines_list)
#     for string in lines_list:
#         print(string)


# def lines_printed_custom(lines_list):
#     pass

def main():
    lines_printed_backwards(get_file_lines('poem.txt'))
    lines_printed_random(get_file_lines('poem.txt'))
    # lines_printed_custom(get_file_lines('poem.txt'))

if __name__ == "__main__":
    main()