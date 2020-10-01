
# Reads the poem file then return a list of strings containing the lines of the file
def get_file_lines(filename):
    read_file = open(filename, 'r')
    return read_file.readlines()

def lines_printed_backwards(lines_list):
    lines_list_reverse = lines_list[::-1]
    for string in lines_list_reverse:
        line_number = lines_list.index(string) + 1
        print(line_number, string)

lines_printed_backwards(get_file_lines('poem.txt'))