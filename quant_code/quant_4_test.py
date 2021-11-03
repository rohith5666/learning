#  A number is divisible by 4 if the number formed by its last two digits is divisible by 4.
# Unit test
import unittest
from quant_4 import div_con_4

class test_div_con_4(unittest.TestCase):
    def test_input(self):
        result = div_con_4(444)
        self.assertEqual(result, 0 )

