import sys

OUTPUT_FILE = 'output.txt'


def divide_line(line, width):
    '''
    divide the line into quotient and remainder
    '''
    quotients = []

    while (len(line) > width):
        # find a space from (width - 1) leftwards
        pos = width - 1
        while (not line[pos].isspace() and pos):
            pos -= 1

        if (pos == 0): # No space within width and do not break the word
            # find space from (width - 1) rightwards
            pos = width - 1
            while (not line[pos].isspace() and (pos < len(line))):
                pos += 1


        chopped_line = line[0:pos].rstrip()
        quotients.append(chopped_line)
        line = line[pos+1:].lstrip()

    return (quotients, line)

def wrap_file(file, width):

    wrapped_lines = []

    with open(file) as f_in:
        remain = ''
        for line in f_in:
            line = remain + line.rstrip()
            (quotient, remain) = divide_line(line, width)
            wrapped_lines += quotient
        wrapped_lines += [remain]

    return wrapped_lines

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Argument error\n Usage {sys.argv[0]} <wrapping_file> <wrap_width>')
        exit(1)
    file_name = sys.argv[1]
    width = int(sys.argv[2])
    lines = wrap_file(file_name, width)

    with open(OUTPUT_FILE, 'w') as f_out:
        for line in lines:
            print(line, file=f_out)
    
            

