import unittest
from app import app

class TestSquareEquation(unittest.TestCase):
    def test_normal(self):
        tester = app.test_client(self)
        response = tester.post('/', content_type='multipart/form-data', data={'a': 1, 'b': 4, 'c': 3})
        self.assertIn('Дискриминант > 0, следовательно уравнение имеет <span class="answer__span">два</span> действительных корня:', response.data.decode())
        self.assertIn('-1', response.data.decode()) # Проверка первого корня
        self.assertIn('-3', response.data.decode()) # Проверка второго корня

    def test_zeroes(self):
        tester = app.test_client(self)
        response = tester.post('/', content_type='multipart/form-data', data={'a': 0, 'b': 0, 'c': 0})
        self.assertIn('Ни один из коэффициентов не должен быть равным нулю!', response.data.decode())

    def test_discriminant_less_than_zero(self):
        tester = app.test_client(self)
        response = tester.post('/', content_type='multipart/form-data', data={'a': 3, 'b': -1, 'c': 5})
        self.assertIn('Дискриминант < 0, следовательно уравнение <span class="answer__span">не имеет</span> действительных корней!', response.data.decode())

    def test_discriminant_equals_zero(self):
        tester = app.test_client(self)
        response = tester.post('/', content_type='multipart/form-data', data={'a': 3, 'b': -18, 'c': 27})
        self.assertIn('Дискриминант = 0, следовательно уравнение имеет <span class="answer__span">один</span> действительный корень:', response.data.decode())
        self.assertIn('3', response.data.decode()) # Проверка корня

unittest.main()
