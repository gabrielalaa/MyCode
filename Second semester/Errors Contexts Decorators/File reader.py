class this_file_reader:
    def __init__(self):
        pass

    def __enter__(self):
        self.file = open(__file__, 'r')
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

with this_file_reader() as fm:
    print (fm.read())

#file is closed when execution reaches this line
print (fm.closed)