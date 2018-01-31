"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    return "hi"
    pass

def give_me_an_integer():
    """
    This function returns an integer value
    """
    return 5
    pass

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    return True
    pass

def give_me_a_float():
    """
    This function returns a float value
    """
    return 5.8
    pass

def give_me_a_list():
    """
    This function returns a list
    """
    my_list=[1,2,3,4]
    return my_list
    pass

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    my_dict={'India':'Delhi','UK':'London','Germany':'Berlin'}
    return my_dict
    pass

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    my_tuple = ('p','e','r','m','i','t')
    return my_tuple
    pass

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    sum=0
    for num in range(1,11):
        sum=sum+num
    return sum
    pass

def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if number % 2 ==0:
        return True
    else:
        return False
    pass

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if number1<number2:
        return True
    else:
        return False
    pass

def sorting(my_list):
    """
    This function returns my_list in a sorted manner using the insertion sort
    """
    for indx in range(1,len(my_list)):
        i=indx
        while i>0:
            if my_list[i]<my_list[i-1]:
                temp=my_list[i-1]
                my_list[i-1]=my_list[i]
                my_list[i]=temp
            i=i-1
    return my_list

def perfect_num(number):
    """
    This function returns True if the number is perfect number False otherwise
    """
    new_list=[]
    for indx in range(1,number):
        if number % indx==0:
            new_list.append(indx)
    total=sum(new_list)
    if total==number:
        return True
    else:
        return False
