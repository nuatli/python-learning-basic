'''
pylint x.py -r y
'''
import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')
        
    def test_multiple_word(self):
        text = 'Nazim utku atli'
        result = cap.cap_text(text)
        self.assertEqual(result,'Nazim Utku Atli')
        
        
if __name__=='__main__':
    unittest.main()
        