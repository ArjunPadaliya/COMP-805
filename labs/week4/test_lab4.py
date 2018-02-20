"""
test_lab4.py
Arjun Padaliya
1/30/2018
"""

import unittest
class Lab4Test(unittest.TestCase):
    def test_squared(self):
        """
        testing squared function
        """
        func=lab4.squared
        case1=[1, 2, 3]
        expected1=[1, 4, 9]
        self.assertEqual(func(case1), expected1)

    def test_check_title(self):
        """
        testing check_title function
        """
        func=lab4.check_title
        case2=["Hello World", "hi", "Hello"]
        expected2=["Hello World", "Hello"]
        self.assertEqual(func(case2), expected2)

    def test_restock_inventory(self):
        """
        testing restock_inventory function
        """
        func=lab4.restock_inventory
        case3={'a':10, 'b':5, 'c':7}
        expected3={'a':20, 'b':15, 'c':17}
        self.assertEqual(func(case3), expected3)

    def test_filter_0_items(self):
        """
        testing filter_0_items function
        """
        func=lab4.filter_0_items
        case4={'a':10, 'b':0, 'c':7}
        expected4={'a':10, 'c':7}
        self.assertEqual(func(case4), expected4)

    def test_average_grades(self):
        """
        testing average_grades function
        """
        func=lab4.average_grades
        case5={'Michael' :[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}
        expected5={'Michael': 89.0, 'Daniel': 79.0, 'Josh': 87.0}
        self.assertEqual(func(case5), expected5)



if __name__ == '__main__':
    try:
        import lab4
        print("lab4.py module found.Testing...")
        unittest.main( )
    except ImportError:
        print("Missing lab4.py module")
