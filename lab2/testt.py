import unittest
import time
from finite_field import PolBasis
from finite_field import NormBasis


class TestPolBasis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Pol Basis')

    def setUp(self):
        self.a1 = PolBasis(3, [3, 1, 0], '011')
        self.b1 = PolBasis(3, [3, 1, 0], '101')
        self.c1 = PolBasis(3, [3, 1, 0])
        self.abig = PolBasis(179, [179, 4, 2, 1, 0], '11101001001011100011100100111001001111101111000110001010110001011011100111001111000000110000001010011110010011001000001101101100111000111001010000010110001111000100010100010001001')
        self.bbig = PolBasis(179, [179, 4, 2, 1, 0], '10010001110100100011101100111110000010111111111001100101011101110000011011110011000110001011100011110101010010110001001111000001110011110011001000100111011001001101110010101010110')
        self.cbig = PolBasis(179, [179, 4, 2, 1, 0], '00100010001011111100010110111001101010011000111000100001110010010110000100011101101111111000000010100000101001110000111011010100100001000011010100111100100100000010101100110101000')
        self.time_my = 0

    def test_add_pol2(self):
        self.start_time = time.time()
        for _ in range(10000):
            self.cbig = self.abig + self.bbig
        self.time_my = (time.time() - self.start_time) / 10000
        print('time_add = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '01111000111111000000001000000111001101010000111111101111101100101011111100111100000110111011101001101011000001111001000010101101001011001010011000110001010110001001100110111011111')

    def test_find_neutral_add2(self):
        self.start_time = time.time()
        for _ in range(10000):
            self.cbig = self.abig.find_neutral_to_add()
        self.time_my = (time.time() - self.start_time) / 10000
        print('time_find_neutral_to_add = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

    def test_find_neutral_mul2(self):
        self.start_time = time.time()
        for _ in range(10000):
            self.cbig = self.abig.find_neutral_to_mul()
        self.time_my = (time.time() - self.start_time) / 10000
        print('time_find_neutral_to_mul = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001')

    def test_find_trace1(self):
        trace = 0
        self.start_time = time.time()
        for _ in range(5):
            trace = self.abig.find_trace()
        self.time_my = (time.time() - self.start_time) / 5
        print('time_find_trace = ', '%f' % self.time_my)
        self.assertEqual(trace, 0)

    def test_mul2(self):
        self.start_time = time.time()
        for _ in range(1000):
            self.cbig = self.abig * self.bbig
        self.time_my = (time.time() - self.start_time) / 1000
        print('time_mul_big = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '11101010100001001100111100000111100000101110111011111000111100110101100101110101100100110001001001011010001000110110101001001000100010111111101001101001101101001000111001011100110')

    def test_to_square1(self):
        self.start_time = time.time()
        for _ in range(100):
            self.cbig = self.abig.to_square()
        self.time_my = (time.time() - self.start_time) / 100
        print('time_to_square = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '11101001111101010101001001001100110011000101010101001110111111111110110101101010010110110011100011001101000110001011100111000010101001000101001100110100011100110000100001001000101')

    def test_find_converse_to_mul(self):
        self.start_time = time.time()
        for _ in range(5):
            self.cbig = self.abig.find_converse_to_mul()
        self.time_my = (time.time() - self.start_time) / 5
        print('time_converse_to_mul = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '00010001010101011100000011110001110011010011011010101111010001111010100110001010010010001000010100011011111101110000110001000011001101001100100111001001000001111100110010000101101')

    def test_to_hight_degree(self):
        self.start_time = time.time()
        for _ in range(10):
            self.bbig = self.abig.to_hight_degree(self.cbig)
        self.time_my = (time.time() - self.start_time) / 10
        print('time_to_hight_degree = ', '%f' % self.time_my)
        self.assertEqual(self.bbig.ret_polynomial_str(), '10101101100001001001110000111000000110101011001101101001000010111110101100001100100001101001010000011101100010001100000010101100010010111000011101111101011000100110010100001111001')


class TestNormBasis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('ON basis')

    def setUp(self):
        self.a1 = NormBasis(3, [3, 1, 0], '011')
        self.b1 = NormBasis(3, [3, 1, 0], '101')
        self.c1 = NormBasis(3, [3, 1, 0])
        self.abig = NormBasis(179, [179, 4, 2, 1, 0], '11101001001011100011100100111001001111101111000110001010110001011011100111001111000000110000001010011110010011001000001101101100111000111001010000010110001111000100010100010001001')
        self.bbig = NormBasis(179, [179, 4, 2, 1, 0], '10010001110100100011101100111110000010111111111001100101011101110000011011110011000110001011100011110101010010110001001111000001110011110011001000100111011001001101110010101010110')
        self.cbig = NormBasis(179, [179, 4, 2, 1, 0], '00100010001011111100010110111001101010011000111000100001110010010110000100011101101111111000000010100000101001110000111011010100100001000011010100111100100100000010101100110101000')

    def test_find_neutral_add2(self):
        self.start_time = time.time()
        for _ in range(10000):
            self.cbig = self.abig.find_neutral_to_add()
        self.time_my = (time.time() - self.start_time) / 10000
        print('time_find_neutral_to_add = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

    def test_find_neutral_mul2(self):
        self.start_time = time.time()
        for _ in range(10000):
            self.cbig = self.abig.find_neutral_to_mul()
        self.time_my = (time.time() - self.start_time) / 10000
        print('time_find_neutral_to_mul = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')

    def test_add2(self):
        self.start_time = time.time()
        for _ in range(10000):
            self.cbig = self.abig + self.bbig
        self.time_my = (time.time() - self.start_time) / 10000
        print('time_add = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '01111000111111000000001000000111001101010000111111101111101100101011111100111100000110111011101001101011000001111001000010101101001011001010011000110001010110001001100110111011111')

    def test_find_trace2(self):
        trace = 0
        self.start_time = time.time()
        for _ in range(10000):
            trace = self.abig.find_trace()
        self.time_my = (time.time() - self.start_time) / 10000
        print('time_find_trace = ', '%f' % self.time_my)
        self.assertEqual(trace, 0)

    def test_mul(self):
        self.start_time = time.time()
        for _ in range(50):
            self.cbig = self.abig * self.bbig
        self.time_my = (time.time() - self.start_time) / 50
        print('time_mul_big = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '10010110111001001011010111111101001110001111010110010100010011110000110000101101110111011100000111010010111000011111110001001110100101110100111001011000101110001000101100001000001')

    def test_to_square2(self):
        self.start_time = time.time()
        for _ in range(10000):
            self.cbig = self.abig.to_square()
        self.time_my = (time.time() - self.start_time) / 10000
        print('time_to_square = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '11110100100101110001110010011100100111110111100011000101011000101101110011100111100000011000000101001111001001100100000110110110011100011100101000001011000111100010001010001000100')

    def test_find_converse_to_mul(self):
        self.start_time = time.time()
        for _ in range(1):
            self.cbig = self.abig.find_converse_to_mul()
        self.time_my = (time.time() - self.start_time) / 1
        print('time_converse_to_mul = ', '%f' % self.time_my)
        self.assertEqual(self.cbig.ret_polynomial_str(), '10001100100100101011101101101111110010110001100001000010010100101001001001100001001000010101111001101000110111011110110000011101011111101100000010101001000101110010001001100111000')

    def test_to_hight_degree(self):
        self.start_time = time.time()
        for _ in range(5):
            self.bbig = self.abig.to_hight_degree(self.cbig)
        self.time_my = (time.time() - self.start_time) / 5
        print('time_to_hight_degree = ', '%f' % self.time_my)
        self.assertEqual(self.bbig.ret_polynomial_str(), '01010111110101100000111011100000011111101100101011101000011100110010000001010111001111110011010011101001101100011100111011000010001100111011111010111001011000011000010111010110000')
