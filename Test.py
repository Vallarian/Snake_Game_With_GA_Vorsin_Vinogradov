import unittest
import random
from Snake import with_border, with_snake_body, snake

class TestSnakeFunctions(unittest.TestCase):
    def test_with_border(self):
        # Проверяем, что функция правильно определяет выход за границы поля
        self.assertEqual(with_border((400, 200)), 1)
        self.assertEqual(with_border((-1, 200)), 1)
        self.assertEqual(with_border((200, 400)), 1)
        self.assertEqual(with_border((200, -1)), 1)

    def test_with_snake_body(self):
        # Проверяем, что функция правильно определяет столкновение с телом змеи
        snake_head = (100, 100)
        snake_body = [(101, 100), (102, 100)]
        self.assertEqual(with_snake_body(snake_head, snake_body), 0)  # Голова не совпадает с телом

        snake_head = (100, 100)
        snake_body = [(100, 100), (100, 100)]
        self.assertEqual(with_snake_body(snake_head, snake_body), 1)  # Голова совпадает с телом

if __name__ == '__main__':
    unittest.main()