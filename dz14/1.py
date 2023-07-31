# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

import unittest
import pytest


def get_number(number, mod = 10):
    """
    >>> get_number(123, 2)
    '1111011'
    >>> get_number(123, 8)
    '173'
    """
    result = ''
    while number != 0:
        result = str(number % mod) + result
        number //= mod
    return result


class TestCaseNumbers(unittest.TestCase):
    def test_2(self):
        self.assertEqual(get_number(123, 2), '1111011', msg='Test failed')

    def test_8(self):
        self.assertEqual(get_number(123, 8), '173', msg='Test failed')


def test_2():
    assert get_number(123, 2) == '1111011', 'Test failed'

def test_8():
    assert get_number(123, 8) == '173', 'Test failed'


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    unittest.main(verbosity=2)
    pytest.main()
