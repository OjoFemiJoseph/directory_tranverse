#test tranverse for extension

import os
import unittest
from tranverse_for_extension import traverse_for_extension



class TestSum(unittest.TestCase):
    
        def test_traverse_for_extension(self):
            
            test_data_path = os.path.join(os.getcwd(), "test_data")
            
            answer = traverse_for_extension(test_data_path,'*.log')
            
            self.assertEqual(len(answer), 2)
            self.assertEqual(answer[0], './aaa.log')
            self.assertEqual(answer[1], './a/bbb.log')
            self.assertNotIn('abc.txt', answer)


if __name__ == '__main__':
    unittest.main()