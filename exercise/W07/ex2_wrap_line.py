import sys

OUTPUT_FILE = 'output.txt'


def divide_line(line, width):
    '''
    divide long line into multiple lines within specified width
    '''
    wrap_lines = []

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


        chopped_line = line[0:pos].rstrip() + '\n'
        wrap_lines.append(chopped_line)
        line = line[pos+1:].lstrip()

    wrap_lines.append(line)

    return wrap_lines

def wrap_file(file, width):

    wrapped_lines = []

    with open(file) as f_in:
        for line in f_in:
            wrapped_lines += divide_line(line, width)

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
            f_out.write(line)

    print(f'output is written to \"{OUTPUT_FILE}\"')
    
            

