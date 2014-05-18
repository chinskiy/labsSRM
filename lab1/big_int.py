from random import choice
import time


class BigInt():
    def __init__(self, bits, number='-1'):
        """(int) -> None"""
        self.numb = []
        self.bits = bits
        self.bytes_numb = self.bits / 8
        cell_numb = self.bytes_numb // 4
        extra_cell = self.bytes_numb % 4
        self.total_cell_number = round(cell_numb + extra_cell)
        if number == '-1':
            self.set_all_zeros(self.total_cell_number)
        else:
            self.set_numb_in_hex(number)

    def __eq__(self, numb):
        """(BigInt) -> None"""
        if numb != '-1':
            self.set_numb_in_hex(numb)
        else:
            return

    def print_all(self):
        """(None) -> None """
        self.print_numb_hex()
        self.print_numb_dec()
        self.print_numb_bin()
        print('Total cell number:', + self.total_cell_number, 'Number of bits:', + self.bits)

    def set_all_zeros(self, cell_numb):
        """(int) -> None"""
        all_zeros = '00000000'
        numb_cell = 0
        while cell_numb > numb_cell:
            self.numb.append(all_zeros)
            numb_cell += 1

    def gener_numb(self):
        """(int) -> None"""
        self.numb = []
        bytes_numb = self.bits / 8
        cell_numb = bytes_numb // 8
        extra_cell = bytes_numb % 8
        cell_numb += extra_cell
        gen_numb = 0
        while cell_numb > gen_numb:
            self.numb.append(self.gener_cell())
            gen_numb += 1

    def gener_cell(self):
        """(None) -> None"""
        gen_cell = ''
        symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        for i in range(8):
            gen_cell += choice(symbols)
        return gen_cell

    def add_cell_in_beg(self):
        """(None) -> None"""
        self.numb.insert(0, '0' * 8)
        self.bits += 64
        self.bytes_numb += 8
        self.total_cell_number += 1

    def set_numb_in_hex(self, bignumb):
        """(String) -> None"""
        self.numb = []
        fullcell = len(bignumb) // 8
        halfcell = len(bignumb) % 8
        bignumb = self.split_bignumb(bignumb)
        difference = self.total_cell_number - fullcell
        if halfcell > 0:
            difference -= 1
        self.set_all_zeros(difference)
        for cell in range(fullcell):
            self.numb.append(bignumb[cell])
        if halfcell > 0:
            bignumb[-1] += '0' * (8 - len(bignumb[-1]))
            self.numb.append(bignumb[-1])

    def set_numb_in_dec(self, numb_in_dec):
        """(int) -> None"""
        numb_in_hex = self.from_dec_to_hex(numb_in_dec)
        self.set_numb_in_hex(numb_in_hex)

    def set_numb_in_bin(self, numb_in_bin):
        """(String) -> None"""
        numb_in_hex = self.from_bin_to_hex(numb_in_bin)
        self.set_numb_in_hex(numb_in_hex)

    def split_bignumb(self, bignumb):
        """(list of str) -> list of char"""
        bignumb = str(bignumb)
        bignumbsep = []
        if len(bignumb) % 8 > 0:
            bignumbsep.append('0' * (8 - len(bignumb) % 8) + bignumb[:len(bignumb) % 8])
        beg = 0 + len(bignumb) % 8
        end = 8 + len(bignumb) % 8
        for i in range(len(bignumb) // 8):
            bignumbsep.append(bignumb[beg:end])
            beg = end
            end += 8
        return bignumbsep

    def print_numb_hex(self):
        """(None) -> None"""
        for elem in range(len(self.numb)):
            print(self.numb[elem])
        print()

    def print_numb_dec(self):
        """(None) -> None)"""
        numb_in_hex = ''
        for elem in range(len(self.numb)):
            numb_in_hex += self.numb[elem]
        numb_in_dec = self.from_hex_to_dec(numb_in_hex)
        print(numb_in_dec)

    def ret_numb_hex(self):
        """(None) -> str"""
        hex_numb = ''
        for elem in range(len(self.numb)):
            hex_numb += self.numb[elem]
        hex_numb = self.delete_zeros_from_left(hex_numb)
        return hex_numb

    def ret_numb_bin(self):
        """(None) -> str"""
        hex_numb = self.ret_numb_hex()
        bin_numb = self.from_hex_to_bin(hex_numb)
        bin_numb = self.delete_zeros_from_left(bin_numb)
        return bin_numb

    def ret_numb_dec(self):
        """(None) -> str"""
        hex_numb = ''
        for elem in range(len(self.numb)):
            hex_numb += self.numb[elem]
        dec_numb = self.from_hex_to_dec(hex_numb)
        return dec_numb

    def print_numb_bin(self):
        """(None) -> None)"""
        numb_in_hex = ''
        for elem in range(len(self.numb)):
            numb_in_hex += self.numb[elem]
        numb_in_hex = self.delete_zeros_from_left(numb_in_hex)
        numb_in_bin = self.from_hex_to_bin(numb_in_hex)
        for cell in range(len(numb_in_bin) // 4):
            print(numb_in_bin[cell * 4: (cell + 1) * 4], end=' ')
        print()

    def from_dec_to_bin(self, numb_in_dec):
        """(String) -> String"""
        numb_in_bin = ''
        numb_in_dec = int(numb_in_dec)
        if numb_in_dec == 0:
            return '0'
        while numb_in_dec > 1:
            if numb_in_dec & 1 == 1:
                numb_in_bin += '1'
            elif numb_in_dec & 0 == 0:
                numb_in_bin += '0'
            numb_in_dec >>= 1
        numb_in_bin += '1'
        numb_in_bin = numb_in_bin[::-1]
        return str(numb_in_bin)

    def from_dec_to_hex(self, numb_in_dec):
        """(String) -> String"""
        numb_in_hex = ''
        dict_of_transition = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                              0: '0', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while numb_in_dec >= 15 and numb_in_dec != 0:
            remnant = numb_in_dec % 16
            numb_in_hex += dict_of_transition[remnant]
            numb_in_dec //= 16
        numb_in_hex += dict_of_transition[numb_in_dec]
        if numb_in_hex[len(numb_in_hex) - 1] == '0':
            numb_in_hex = numb_in_hex[:len(numb_in_hex) - 1]
        numb_in_hex = numb_in_hex[::-1]
        if numb_in_hex == '':
            numb_in_hex = '0'
        return numb_in_hex

    def from_hex_to_bin(self, numb_in_hex):
        """(String) -> String"""
        numb_in_bin = ''
        dict_of_transition = {'1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                              '6': '0110', '7': '0111', '8': '1000', '9': '1001', '0': '0000',
                              'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
                              'F': '1111'}
        for elem in range(len(numb_in_hex)):
            numb_in_bin += dict_of_transition[numb_in_hex[elem]]
        return numb_in_bin

    def from_hex_to_dec(self, numb_in_hex):
        """(String) -> String"""
        dict_of_transition = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                              '9': 9, '0': 0, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        numb_in_hex = numb_in_hex[::-1]
        numb_in_dec = 0
        step = 1
        for elem in range(len(numb_in_hex)):
            numb_in_dec += dict_of_transition[numb_in_hex[elem]] * step
            step *= 16
        return str(numb_in_dec)

    def from_bin_to_dec(self, numb_in_bin):
        """(String) -> String"""
        numb_in_bin = numb_in_bin[::-1]
        numb_in_dec = 0
        for elem_numb in range(len(numb_in_bin)):
            temp = 1
            if numb_in_bin[elem_numb] == '1':
                temp <<= elem_numb
                numb_in_dec += temp
        return str(numb_in_dec)

    def from_bin_to_hex(self, numb_in_bin):
        """(String) -> String"""
        numb_in_hex = ''
        dict_of_transition = {'1000': '1', '0100': '2', '1100': '3', '0010': '4', '1010': '5',
                              '0110': '6', '1110': '7', '0001': '8', '1001': '9', '0000': '0',
                              '0101': 'A', '1101': 'B', '0011': 'C', '1011': 'D', '0111': 'E',
                              '1111': 'F'}
        numb_in_bin = numb_in_bin[::-1]
        tmp = len(numb_in_bin) % 4
        if tmp != 0:
            numb_in_bin += '0' * (4 - tmp)
        for numb in range(0, len(numb_in_bin), 4):
            numb_in_hex += dict_of_transition[numb_in_bin[numb:numb + 4]]
        numb_in_hex = numb_in_hex[::-1]
        return numb_in_hex

    def shift_left(self, numb, numb_of_shift):
        """(String) -> String"""
        if numb == '0':
            return numb
        else:
            return numb + '0' * numb_of_shift

    def shift_right(self, numb):
        """(String) -> String"""
        return '0' + numb[0:len(numb) - 1]

    def delete_zeros_from_left(self, numb):
        """(String) -> String """
        check = False
        while not check:
            if len(numb) == 1:
                check = True
            elif numb[0] == '0':
                numb = numb[1:len(numb)]
            elif numb[0] != '0':
                check = True
        return numb

    def ret_cell_dec(self, numb_cell):
        cell = self.numb[numb_cell]
        return int(self.from_hex_to_dec(cell))

    def __add__(self, numb2):
        """(BIgInt) -> String"""
        carry_bit = 0
        ret_numb = ''
        for cell in range(len(self.numb)):
            numb1_cell = self.ret_cell_dec(len(self.numb) - 1 - cell)
            numb2_cell = numb2.ret_cell_dec(len(numb2.numb) - 1 - cell)
            numb_temp = self.from_dec_to_hex(numb1_cell + numb2_cell + carry_bit)
            carry_bit = 0
            if len(numb_temp) > 8:
                numb_temp = numb_temp[1:len(numb_temp)]
                carry_bit = 1
            elif len(numb_temp) < 8:
                numb_temp = '0' * (8 - len(numb_temp)) + numb_temp
            ret_numb += numb_temp[::-1]
        ret_numb = ret_numb[::-1]
        if carry_bit == 1:
            ret_numb = '1' + ret_numb
        return ret_numb

    def __sub__(self, numb2):
        """(BigInt) -> String"""
        numb2 = BigInt(numb2.bits, numb2.ret_numb_hex())
        if self.senior_nonzero_bit() == '0':
            return '0'
        if self.senior_nonzero_cell_numb() <= numb2.senior_nonzero_cell_numb():
            numb1_cell = self.ret_cell_dec(len(self.numb) - self.senior_nonzero_cell_numb())
            numb2_cell = numb2.ret_cell_dec(len(self.numb) - numb2.senior_nonzero_cell_numb())
            if numb1_cell < numb2_cell:
                return '-1'
        carry_bit = 0
        ret_numb = ''
        for cell in range(len(self.numb)):
            numb1_cell = self.ret_cell_dec(len(self.numb) - 1 - cell) - carry_bit
            numb2_cell = numb2.ret_cell_dec(len(numb2.numb) - 1 - cell)
            carry_bit = 0
            if numb1_cell >= numb2_cell:
                numb_temp = self.from_dec_to_hex(numb1_cell - numb2_cell)
            else:
                carry_bit = 1
                carry_sub = int(self.from_hex_to_dec('100000000'))
                numb_temp = self.from_dec_to_hex(carry_sub + numb1_cell - numb2_cell)
            if len(numb_temp) < 8:
                numb_temp = '0' * (8 - len(numb_temp)) + numb_temp
            ret_numb += numb_temp[::-1]
        ret_numb = self.delete_zeros_from_left(ret_numb)
        return ret_numb[::-1]

    def __mul__(self, numb2):
        """(BigInt) -> String"""
        numb1s = self.ret_numb_dec()
        numb2s = numb2.ret_numb_dec()
        if numb2s == '0' or numb1s == '0':
            return '0'
        numb_res = 0
        temp_res = 0
        for numb in range(len(numb2s)):
            temp_res += self.mul_on_one_dec_numb(int(numb2s[len(numb2s) - numb - 1]))
            temp_res = self.shift_left(str(temp_res), numb)
            numb_res += int(temp_res)
            temp_res = 0
        return self.from_dec_to_hex(numb_res)

    def mul_on_one_bin_numb(self, bin_numb):
        if bin_numb == '1':
            return self.ret_numb_hex()
        else:
            return '0'

    def to_square(self):
        """(None) -> str"""
        return self.__mul__(self)

    def __lshift__(self, numb_shift):
        """(int) -> None"""
        numb_in_bin = self.ret_numb_bin()
        if numb_in_bin == '0':
            return '0'
        return self.from_bin_to_hex(numb_in_bin + '0' * numb_shift)

    def __rshift__(self, numb_shift):
        """(int) -> None"""
        numb_in_bin = self.ret_numb_bin()
        numb_in_bin = numb_in_bin[0:len(numb_in_bin) - numb_shift]
        if numb_in_bin == '':
            return '0'
        return self.from_bin_to_hex(numb_in_bin)

    def senior_nonzero_bit(self):
        """(None) -> int"""
        numb = self.ret_numb_bin()
        numb = self.delete_zeros_from_left(numb)
        if numb == '0':
            return '0'
        else:
            return len(numb)

    def senior_nonzero_cell_numb(self):
        numb = int(self.senior_nonzero_bit())
        cell_numb = numb // 32
        if numb % 32 != 0:
            cell_numb += 1
        return cell_numb

    def mul_on_one_dec_numb(self, numb):
        """(int) -> int"""
        bnumb = int(self.ret_numb_dec())
        return int(bnumb) * numb

    def bin_sub(self, numb1, numb2):
        """(str) -> str"""
        if int(numb1) < int(numb2):
            return '-1'
        elif len(numb1) > len(numb2):
            numb2 = (len(numb1) - len(numb2)) * '0' + numb2
        numb1 = list(numb1)
        numb2 = list(numb2)
        for elem in range(len(numb1)):
            if numb1[elem] == '1' and numb2[elem] == '1':
                numb1[elem] = '0'
            elif numb1[elem] == '0' and numb2[elem] == '1':
                numb1[elem] = '1'
                temp = elem - 1
                while numb1[temp] != '1':
                    numb1[temp] = '1'
                    temp -= 1
                numb1[temp] = '0'
            elif numb1[elem] == '1' and numb2[elem] == '0':
                pass
            elif numb1[elem] == '0' and numb2[elem] == '0':
                pass
        numb1 = "".join(numb1)
        numb1 = self.delete_zeros_from_left(numb1)
        return numb1

    def __floordiv__(self, denomin):
        """(BigInt) -> str"""
        numer = self.ret_numb_bin()
        denomin = denomin.ret_numb_bin()
        fraction = ''
        if denomin == '0':
            return '-1'
        elif int(numer) < int(denomin):
            return '0'
        div_numb = ''
        for elem in range(len(numer)):
            div_numb += numer[elem]
            res = self.bin_sub(div_numb, denomin)
            if res == '-1':
                fraction += '0'
            elif res == '0':
                div_numb = ''
                fraction += '1'
            else:
                div_numb = self.bin_sub(div_numb, denomin)
                fraction += '1'
        return self.from_bin_to_hex(fraction)

    def __mod__(self, denomin):
        """(BigInt) -> str"""
        numer = self.ret_numb_bin()
        denomin = denomin.ret_numb_bin()
        fraction = ''
        if denomin == '0':
            return '-1'
        elif int(numer) < int(denomin):
            return self.from_bin_to_hex(numer)
        div_numb = ''
        for elem in range(len(numer)):
            div_numb += numer[elem]
            res = self.bin_sub(div_numb, denomin)
            if res == '-1':
                fraction += '0'
            elif res == '0':
                div_numb = ''
                fraction += '1'
            else:
                div_numb = self.bin_sub(div_numb, denomin)
                fraction += '1'
        if div_numb == '':
            div_numb = '0'
        return self.from_bin_to_hex(div_numb)

    def __truediv__(self, denomin):
        """(BigInt) -> str"""
        numer = self.ret_numb_bin()
        denomin = denomin.ret_numb_bin()
        fraction = ''
        div_numb = ''
        if denomin == '0':
            return '-1'
        elif numer == '0':
            return '0'
        elif int(numer) < int(denomin):
            numer = self.from_bin_to_dec(numer)
            denomin = self.from_bin_to_dec(denomin)
            div_numb = str(int(numer) / int(denomin))
            result = '0,' + div_numb[2:len(div_numb)]
            return result
        for elem in range(len(numer)):
            div_numb += numer[elem]
            res = self.bin_sub(div_numb, denomin)
            if res == '-1':
                fraction += '0'
            elif res == '0':
                div_numb = ''
                fraction += '1'
            else:
                div_numb = self.bin_sub(div_numb, denomin)
                fraction += '1'
        fraction = self.from_bin_to_dec(fraction)
        div_numb = self.from_bin_to_dec(div_numb)
        denomin = self.from_bin_to_dec(denomin)
        if div_numb != '0':
            div_numb = str(int(div_numb) / int(denomin))
            div_numb = div_numb[2:len(div_numb)]
        result = fraction + '.' + div_numb
        return result

    def gcd(self, numb1, numb2):
        """(BigInt, BigInt) -> str"""
        if numb1 - numb2 == '-1':
            numb3 = BigInt(numb1.bits, numb1.ret_numb_hex())
            numb1 = numb2
            numb2 = numb3
        if numb2.senior_nonzero_bit() == '0':
            return numb1.ret_numb_hex()
        numb1 == numb1 % numb2
        return self.gcd(numb2, numb1)

    def lcm(self, numb1, numb2):
        """(BigInt, BigInt) -> str"""
        numb1 = BigInt(numb1.bits, numb1.ret_numb_hex())
        numb2 = BigInt(numb2.bits, numb2.ret_numb_hex())
        temp = BigInt(numb1.bits, self.gcd(numb1, numb2))
        numb1 == numb1 // temp
        numb1 == numb1 * numb2
        ret_numb = numb1.ret_numb_hex()
        return ret_numb

    def mul_by_module(self, numb1, numb2, numb3):
        """(BigInt, BigInt, BigInt) -> str"""
        numb1s = numb1.ret_numb_dec()
        numb2s = numb2.ret_numb_dec()
        numb3s = numb3.ret_numb_dec()
        if numb2s == '0' or numb1s == '0' or numb3s == '0':
            return '0'
        numb_res = 0
        temp_res = 0
        for numb in range(len(numb2s)):
            temp_res += self.mul_on_one_dec_numb(int(numb2s[len(numb2s) - numb - 1]))
            temp_res = self.shift_left(str(temp_res), numb)
            numb_res += int(temp_res)
            numb_res %= int(numb3s)
            temp_res = 0
        if numb_res == '':
            numb_res = 0
        return self.from_dec_to_hex(numb_res)

    def to_square_by_module(self, numb1, numb2):
        """(BigInt, BigInt) -> str"""
        return numb1.mul_by_module(numb1, numb1, numb2)

    def to_hight_degree_by_module(self, numb, degree, module, nyu):
        """(BigInt, BigInt, BigInt) -> str"""
        temp_numb_deg = BigInt(numb.bits)
        temp_numb_deg.set_numb_in_hex(numb.ret_numb_hex())
        degree_in_bits = degree.ret_numb_bin()
        degree_in_bits = degree_in_bits[::-1]
        result = BigInt(numb.bits)
        for numb_bit in range(len(degree_in_bits)):
            if numb_bit == 0 and degree_in_bits[numb_bit] == '1':
                result == temp_numb_deg.ret_numb_hex()
                ##result == result % module
                result == result.barret_reduction(result, module, nyu)
            else:
                ##temp_numb_deg == temp_numb_deg.to_square_by_module(temp_numb_deg, module)
                temp_numb_deg == temp_numb_deg.to_square()
                temp_numb_deg == temp_numb_deg.barret_reduction(temp_numb_deg, module, nyu)
                #temp_numb_deg == self.blackley_alg(temp_numb_deg, module)
                if degree_in_bits[numb_bit] == '1':
                    result == result * temp_numb_deg
                    result == result.barret_reduction(result, module, nyu)
                    ##result == result % module
                    #result == self.blackley_alg(temp_numb_deg, module)
        return result.ret_numb_hex()

    def barret_reduction(self, numb1, numb2, nyu):
        """(BigInt, BigInt, Bigint) -> str"""
        numb2 = BigInt(numb2.bits, numb2.ret_numb_hex())
        bkm1 = BigInt(numb1.bits)
        q = BigInt(numb1.bits)
        temp = 10 ** (len(numb2.ret_numb_dec()) - 1)
        bkm1 == self.from_dec_to_hex(temp)
        q == numb1 // bkm1
        bkm1 == self.from_dec_to_hex(temp * 100)
        q == q * nyu
        q == q // bkm1
        nyu == numb1 % bkm1
        q == q * numb2
        q == q % bkm1
        numb1 == numb1.from_dec_to_hex(int(nyu.ret_numb_dec()) - int(q.ret_numb_dec()))
        while int(numb1.ret_numb_dec()) > int(numb2.ret_numb_dec()):
            numb1 == numb1 - numb2
        return numb1.ret_numb_hex()

    def calculation_nyu(self, numb2):
        """(BigInt) -> BigInt"""
        nyu = BigInt(self.bits)
        nyu == nyu.from_dec_to_hex(10 ** (2 * len(numb2.ret_numb_dec())))
        nyu == nyu // numb2
        return nyu

    def blackley_alg(self, numb2, module):
        """(BigInt, BigInt, BigInt) -> str"""
        res = BigInt(self.bits)
        tmp1 = BigInt(self.bits)
        numb1b = self.ret_numb_bin()[::-1]
        for i in range(len(numb1b)):
            res == res << 1
            tmp1 == numb2.mul_on_one_bin_numb(numb1b[len(numb1b) - i - 1])
            if tmp1.senior_nonzero_bit() != '0':
                res == res + tmp1
            res == res % module
        return res.ret_numb_hex()

    def find_converse(self, numb1, module):
        numb1 = int(numb1.ret_numb_dec())
        module = int(module.ret_numb_dec())
        chk = 0
        if numb1 * 2 > module:
            chk = 1
        arr = self.rae(numb1, module)
        tmp1 = 0
        tmp2 = 1
        for elem in arr:
            tmp1 += elem * tmp2
            tmp1, tmp2 = tmp2, tmp1
        if chk == 1:
            return self.from_dec_to_hex(tmp2)
        else:
            return self.from_dec_to_hex(module - tmp2)

    def rae(self, numb1, module):
        ost = 0
        arr = []
        while ost != 1:
            arr.append(module // numb1)
            ost = module % numb1
            module = numb1
            numb1 = ost
        return arr

if __name__ == '__main__':

    a_big = BigInt(256, '82B19600B943B35D5A1446C3106FD113676E17ACB5AA02FDD5C68C373F7BC665')
    b_big = BigInt(256, '7BFC75B3ECD02B477B07FAEB9026D9AF74BBEF15238E40A6ACDDDFA7F5894E78')
    c_big = BigInt(256, 'B8D0595741E7C058383E123A2441173986E02FED03B5ABE3EE130C784DC25A16')
    t1 = time.time()
    a_big.to_hight_degree_by_module(a_big, c_big, b_big)
    print(time.time() - t1)