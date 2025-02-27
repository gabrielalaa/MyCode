class ScriptTooShortException(Exception):
    """Custom exception for scripts that are too short."""
    pass


class this_file_reader:
    def __init__(self):
        pass

    def __enter__(self):
        # Open the current script file
        self.file = open(__file__, 'r')

        # Read the file content
        content = self.file.read().strip()

        # Check if the content length is less than 200 characters
        if len(content) < 200:
            raise ScriptTooShortException("The script has less than 200 characters")

        # Return the opened file object
        return self.file

    def __exit__(self, type, value, traceback):
        # Close the file when exiting the context
        self.file.close()


# Using the context manager to read and print the file content
with this_file_reader() as fm:
    print(fm.read())  # Print the file content

# Verify that the file is closed
print(fm.closed)