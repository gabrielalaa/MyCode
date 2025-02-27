# Write a function which takes the file I have to read from, and the file I want to create
def write_file(filename, outputfile):
    # Read the content of the file as a list of lines without removing spaces because I need them
    with open(filename, 'r') as f:
        content = f.readlines()
    # Create the new file using enumerate
    with open(outputfile, 'w') as f2:
        for line in enumerate(content):
            # Create a list in which I add the index of each line, adding one for each because the start is from 1 not 0
            c = []
            c.append(str(line[0]+1))
            c.append('\t')
            c.append(line[1])
            # Join the list, creating a new string with the wanted output and write it in my file
            f2.write(''.join(c))

    # print(f2)
    with open(outputfile, 'r') as f3:
        text = f3.read()
    print(text)

    # print(content)


write_file('givenfile.txt', 'output.txt')