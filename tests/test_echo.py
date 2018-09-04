import unittest
import subprocess
from echo import *

class TestStringMethods(unittest.TestCase):

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        
        self.assertEquals(stdout, usage)
    
    def test_upper(self):
        self.assertEqual(upper('cat'), 'CAT')

    def test_lower(self):
        self.assertEqual(lower('DoG'), 'dog')

    def test_title(self):
        self.assertEqual(title('kid'), 'Kid')


if __name__ == '__main__':
    unittest.main()


