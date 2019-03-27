import unittest

class TestStringMethods(unittest.TestCase):

# check if the dataset can be split by ',' or not.
    def test_split(self):
        with open(input_file) as file:
            next(file)
            for line in file:
                self.assertEqual(len(line.split(",")), 5)
                with self.assertRaises(TypeError):
                    line.split(2)

if __name__ == '__main__':
    input_file = '/Users/newworld/Documents/Job/California Deamin/interview/insight/test10.txt'
    unittest.main()
