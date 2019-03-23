import unittest
import pool_of_process


def math_operation(x):
    res = x ** 100
    return 'Done'


class TestGameOfLife(unittest.TestCase):

    def test_min_number_of_workers(self):
        pool = pool_of_process.ProcessPool()
        num = pool.number_of_workers(1)
        self.assertEqual(2, num)

    def test_max_number_of_workers(self):
        pool = pool_of_process.ProcessPool()
        num = pool.number_of_workers(12)
        self.assertEqual(10, num)

    def test_number_of_workers(self):
        pool = pool_of_process.ProcessPool()
        num = pool.number_of_workers(5)
        self.assertEqual(5, num)

    def test_memory_usage(self):
        pool = pool_of_process.ProcessPool()
        results = pool.map(math_operation, [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                                            1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                                            1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                                            1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                                            1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, ])
        max_memory = pool.max_memory_use
        self.assertTrue(max_memory < 512)
