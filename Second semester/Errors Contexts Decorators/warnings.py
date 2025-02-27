import warnings

from Tools.scripts.objgraph import ignore


# default
# This will display the warning only once (default behavior)
def default_warning():
    warnings.warn("This is a default warning!")

default_warning()  # This will show the warning
default_warning()  # This won't show the warning

###

# error
# Convert the warning into an exception
warnings.simplefilter('error')

try:
    warnings.warn("This warning is now an exception!")
except Warning as e:
    print(f"Caught an exception: {e}")
# Caught an exception: This warning is now an exception!

###

# ignore

# Ignore all warnings
warnings.simplefilter('ignore')

warnings.warn("This warning will be ignored")
print("No warning was shown!")
# No warning was shown!

###

# always

# Always show the warning, even if it's repeated
warnings.simplefilter('always')

def always_warning():
    warnings.warn("This is an always warning!")

always_warning()  # This will show the warning
always_warning()  # This will also show the warning