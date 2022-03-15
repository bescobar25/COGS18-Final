"""Test for my functions."""

from my_module.functions import begin, greet, their_sign, zodiac_sign, more_info, no_info
##
##

def test_begin():
    
    assert callable(begin)

def test_greet():

    assert callable(greet)

def test_their_sign():

    assert callable(their_sign)

def test_zodiac_sign():
    
    assert callable(zodiac_sign)
    
def test_more_info():
    
    assert callable(more_info)

def test_no_info():
    
    assert callable(no_info)

def all_tests():
    
    test_begin()
    test_greet()
    test_their_sign()
    test_zodiac_sign()
    test_more_info()
    test_no_info()
    


                 
    