import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
import subprocess

def sanatize(output):
    return output.lower().replace("\n","").lstrip().rstrip()       

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(2)
    @tags("integration")
    def test_single_input(self):
        """Evaluating Hello World Output"""
        mytest = subprocess.Popen('java Hello'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output = mytest.stdout.readline()
        olower = sanatize(output)
        self.assertEqual(olower, "hello world")
        mytest.terminate()

