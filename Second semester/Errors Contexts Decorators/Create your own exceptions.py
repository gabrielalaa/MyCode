# Define the custom exception
class LibraryNotEmptyException(Exception):
    """Raised when an attempt is made to delete a non-empty library."""
    pass


# A function that attempts to delete a library
def delete_library(library):
    if len(library) > 0:
        # Raise the custom exception if the library is not empty
        raise LibraryNotEmptyException("Cannot delete library because it is not empty!")
    else:
        # Proceed with library deletion
        print("Library deleted successfully.")


# Example usage
try:
    # Creating a non-empty library (a list for simplicity)
    my_library = ["book1", "book2", "book3"]

    # Attempt to delete the library
    delete_library(my_library)
except LibraryNotEmptyException as e:
    # Handle the exception
    print(e)