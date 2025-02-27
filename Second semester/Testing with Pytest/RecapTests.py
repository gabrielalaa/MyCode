from RecapFunctions import max_element, triangles, greetme, revWord

def test_max_element():
    assert max_element([3, 16, 4, 32, 9])==32

###

def test_triangles():
    assert(triangles(3, 3, 3)=='Equilateral')
    assert(triangles(5, 5, 3)=='Equal-sided')
    assert(triangles(3, 4, 5)=='Orthogonal')
    assert(triangles(3, 5, 7)=='Others')

    assert(triangles(0, 0, 0)=='Invalid')
    assert(triangles(3, 4, -5)=='Invalid')

###

# White Box Testing
def test_greetme():
    assert(greetme(6) == 'hello')
    assert(greetme(7) == 'hello')

    assert(greetme(5) == 'goodbye')
    assert(greetme(4) == 'goodbye')
    assert(greetme(0) == 'goodbye')
    assert(greetme(-5) == 'goodbye')
    assert(greetme(int('-4')) == 'goodbye')

###

# Black Box Testing
def test_revWord():
    assert(revWord("this is an interesting task")=='task interesting an is this')
    assert(revWord("12 34 56 789")=='789 56 34 12')
    assert(revWord("# hello # you !")=="! you # hello #")