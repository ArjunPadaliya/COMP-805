import unittest
if __name__ == '__main__':
    try:
        import lab4
        print("lab4.py module found.Testing...")
        unittest.main( )
    except ImportError:
        print("Missing lab4.py module")
