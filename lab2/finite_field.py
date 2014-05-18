from random import choice
import time


def exist_onb(dimension):
    p = 2 * dimension + 1
    if not is_prime(p):
        return False
    k = 1
    while 2 ** k % p != 1:
        k += 1
    if k == 2 * dimension:
        return True
    elif p % 4 == 3 and k == dimension:
        return True
    return False


def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


class Basis():
    def __init__(self, power, field_gen, polynomial=None):
        """(int, list(int), str) -> None"""
        self.power = power
        self.field_generator = [0 for _ in range(power + 1)]
        self.polynomial = [0 for _ in range(power)]
        if self.power == len(field_gen) - 1:
            self.set_field_generator_bits_arr(field_gen)
        else:
            self.set_field_generator_arr(field_gen)
        if polynomial is not None:
            self.set_polynomial_bits_str(polynomial)

    def set_field_generator_arr(self, field_gen):
        """(list(int)) -> None"""
        for elem in field_gen:
            self.field_generator[elem] = 1
        self.field_generator = self.field_generator[::-1]

    def set_field_generator_bits_arr(self, field_gen):
        """(list(int)) -> None"""
        self.field_generator = field_gen

    def set_polynomial_bits_str(self, pol):
        """(str) -> None"""
        self.polynomial = [0 for _ in range(self.power)]
        for elem in range(self.power):
            self.polynomial[elem] = int(pol[elem])

    def ret_field_generator_arr(self):
        """(None) -> list(int)"""
        return self.field_generator

    def ret_field_generator_str(self):
        """(None) -> str"""
        ret_res = ''
        for elem in self.field_generator:
            ret_res += str(elem)
        return ret_res

    def ret_polynomial_arr(self):
        """(None) -> (list(int))"""
        return self.polynomial

    def ret_polynomial_str(self):
        """(None) -> str"""
        ret_res = ''
        for elem in self.polynomial:
            ret_res += str(elem)
        return ret_res

    def gener_polynomial(self):
        """(None) -> None"""
        for i in range(self.power):
            self.polynomial[i] = choice([0, 1])

    def print_polynomial_arr(self):
        """"(None) -> None"""
        print(self.polynomial)

    def print_polynomial_str(self):
        """"(None) -> None"""
        for i in range(len(self.polynomial)):
            print(self.polynomial[i], end='')
        print()


class PolBasis(Basis):
    def find_neutral_to_add(self):
        """(None) -> PolBasis"""
        ret_nmb = PolBasis(self.power, self.field_generator)
        respol = [0 for _ in range(self.power)]
        ret_nmb.polynomial = respol
        return ret_nmb

    def find_neutral_to_mul(self):
        """(None) -> PolBasis"""
        ret_nmb = PolBasis(self.power, self.field_generator)
        respol = [0 for _ in range(self.power - 1)]
        respol.append(1)
        ret_nmb.polynomial = respol
        return ret_nmb

    def __add__(self, numb2):
        """(PolBasis, PolBasis) -> PolBasis"""
        ret_nmb = PolBasis(self.power, self.field_generator)
        for elem in range(ret_nmb.power):
            ret_nmb.polynomial[elem] = self.polynomial[elem] ^ numb2.polynomial[elem]
        return ret_nmb

    def __mul__(self, numb2):
        """(PolBasis, PolBasis) -> PolBasis"""
        ret_nmb = PolBasis(self.power, self.field_generator)
        respol = [0 for _ in range(2 * self.power - 1)]
        tmp = self.polynomial
        for i in range(self.power):
            if numb2.polynomial[i] == 1:
                for elem in range(self.power):
                    respol[elem + i] ^= tmp[elem]
        arr = []
        for i in range(self.power + 1):
            if self.field_generator[i] == 1:
                arr.append(i)
        while len(respol) >= self.power + 1:
            if respol[0] == 0:
                respol.pop(0)
            else:
                for elem in arr:
                    respol[elem] ^= 1
        ret_nmb.polynomial = respol
        return ret_nmb

    def find_trace(self):
        """(None) -> int"""
        res = PolBasis(self.power, self.field_generator)
        temp = PolBasis(self.power, self.field_generator, self.polynomial)
        for i in range(self.power):
            res = res + temp
            temp = temp.to_square()
        return res.polynomial[self.power - 1]

    def to_square(self):
        """(None) -> PolBasis"""
        a = PolBasis(self.power, self.field_generator, self.polynomial)
        ret_nmb = a * a
        return ret_nmb

    def find_converse_to_mul(self):
        temp = PolBasis(self.power, self.field_generator, self.polynomial)
        ret_res = PolBasis(self.power, self.field_generator, self.polynomial)
        for _ in range(self.power - 2):
            temp = temp.to_square()
            ret_res *= temp
        ret_res = ret_res.to_square()
        return ret_res

    def to_hight_degree(self, degree):
        """(PolBasis) -> PolBasis"""
        p = PolBasis(self.power, self.field_generator, self.polynomial)
        res = p.find_neutral_to_mul()
        for elem in degree.polynomial[::-1]:
            if elem == 0:
                p = p.to_square()
            elif elem == 1:
                res = res * p
                p = p.to_square()
        return res


class NormBasis(Basis):
    def find_neutral_to_add(self):
        """(None) -> NormBasis"""
        ret_nmb = NormBasis(self.power, self.field_generator)
        respol = [0 for _ in range(self.power)]
        ret_nmb.polynomial = respol
        return ret_nmb

    def find_neutral_to_mul(self):
        """(None) -> NormBasis"""
        ret_nmb = NormBasis(self.power, self.field_generator)
        respol = [1 for _ in range(self.power)]
        ret_nmb.polynomial = respol
        return ret_nmb

    def __add__(self, numb2):
        """(NormBasis, NormBasis) -> NormBasis"""
        ret_nmb = NormBasis(self.power, self.field_generator)
        for elem in range(len(self.polynomial)):
            ret_nmb.polynomial[elem] = self.polynomial[elem] ^ numb2.polynomial[elem]
        return ret_nmb

    def __mul__(self, numb2):
        """(NormBasis, NormBasis) -> NormBasis"""
        ret_nmb = NormBasis(self.power, self.field_generator)
        matrix = self.find_mul_matrix()
        u = self.polynomial
        v = numb2.polynomial
        tmp = [0 for _ in range(self.power)]
        for j in range(self.power):
            el = 0
            for elem in matrix:
                tmp[elem[0]] ^= u[elem[1]] & 1
            for i in range(len(tmp)):
                el ^= tmp[i] & v[i]
            ret_nmb.polynomial[j] = el
            u = u[1:] + u[:1]
            v = v[1:] + v[:1]
            tmp = [0 for _ in range(self.power)]
        return ret_nmb

    def find_trace(self):
        """(None) -> int"""
        tmp = 0
        for elem in self.polynomial:
            tmp ^= elem
        return tmp

    def to_square(self):
        """(None) -> NormBasis"""
        ret_nmb = NormBasis(self.power, self.field_generator)
        ret_nmb.polynomial = self.polynomial[-1:] + self.polynomial[:-1]
        return ret_nmb

    def find_mul_matrix(self):
        """(None) -> list(tuple)"""
        matrix = []
        p = 2 * self.power + 1
        x, y = 1, 1
        for i in range(self.power):
            for j in range(self.power):
                if (x + y) % p == 1 or (x - y) % p == 1 or \
                                        (y - x) % p == 1 or (-x - y) % p == 1:
                    matrix.append((i, j))
                y <<= 1
            x <<= 1
            y = 1
        return matrix

    def find_converse_to_mul(self):
        """(None) -> NormBasis"""
        temp = NormBasis(self.power, self.field_generator, self.polynomial)
        ret_res = NormBasis(self.power, self.field_generator, self.polynomial)
        for _ in range(self.power - 2):
            temp = temp.to_square()
            ret_res *= temp
        ret_res = ret_res.to_square()
        return ret_res

    def to_hight_degree(self, degree):
        """(NormBasis) -> NormBasis"""
        p = NormBasis(self.power, self.field_generator, self.polynomial)
        res = p.find_neutral_to_mul()
        for elem in degree.polynomial[::-1]:
            if elem == 0:
                p = p.to_square()
            elif elem == 1:
                res = res * p
                p = p.to_square()
        return res


if __name__ == "__main__":
    abig = NormBasis(179, [179, 4, 2, 1, 0],
                     '11101001001011100011100100111001001111101111000110001010110001011011100111001111000000110000001010011110010011001000001101101100111000111001010000010110001111000100010100010001001')
    bbig = NormBasis(179, [179, 4, 2, 1, 0],
                     '10010001110100100011101100111110000010111111111001100101011101110000011011110011000110001011100011110101010010110001001111000001110011110011001000100111011001001101110010101010110')
    cbig = NormBasis(179, [179, 4, 2, 1, 0],
                     '00100010001011111100010110111001101010011000111000100001110010010110000100011101101111111000000010100000101001110000111011010100100001000011010100111100100100000010101100110101000')
    a1 = NormBasis(3, [3, 1, 0], '001')
    b1 = NormBasis(3, [3, 1, 0], '110')