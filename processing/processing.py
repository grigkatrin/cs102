from pool_of_process import ProcessPool
import time


def math_operation(x):
    res = x ** 100
    return 'Done'


if __name__ == '__main__':
    pool = ProcessPool()
    results = pool.map(math_operation, [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                                        1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                                        1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                                        1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                                        1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,])
    print('results: ', results)