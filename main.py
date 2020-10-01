
# Reads the poem file then return a list of strings containing the lines of the file
def get_file_lines(filename):
    read_file = open(filename, 'r')
    return read_file.readlines()

print(get_file_lines('poem.txt'))

