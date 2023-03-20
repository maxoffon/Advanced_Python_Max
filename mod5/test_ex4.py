import unittest
from ex4 import Redirect


class MyTestCase(unittest.TestCase):
    def test_both_parameters_given(self):
        print('Hello stdout')
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')

        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        print('Hello stdout again')

        stdout_file = open('stdout.txt', 'r')
        stderr_file = open('stderr.txt', 'r')

        self.assertTrue('Hello stdout.txt' in stdout_file.readline())
        self.assertTrue('Hello stderr.txt' in '\n'.join(stderr_file.readlines()))

        stdout_file.close()
        stderr_file.close()

    def test_out_parameter_given(self):
        print('Hello stdout')
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')
        stderr_file.close()

        with Redirect(stdout=stdout_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        print('Hello stdout again')

        stdout_file = open('stdout.txt', 'r')
        stderr_file = open('stderr.txt', 'r')

        self.assertTrue('Hello stdout.txt' in stdout_file.readline())
        self.assertEqual(stderr_file.readline(), '')

        stdout_file.close()
        stderr_file.close()

    def test_err_parameter_given(self):
        print('Hello stdout')
        stderr_file = open('stderr.txt', 'w')
        stdout_file = open('stdout.txt', 'w')
        stdout_file.close()

        with Redirect(stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        print('Hello stdout again')

        stdout_file = open('stdout.txt', 'r')
        stderr_file = open('stderr.txt', 'r')

        self.assertEqual(stdout_file.readline(), '')
        self.assertTrue('Hello stderr.txt' in '\n'.join(stderr_file.readlines()))

        stdout_file.close()
        stderr_file.close()

    def test_none_parameter_given(self):
        print('Hello stdout')

        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')

        with Redirect():
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        print('Hello stdout again')

        stdout_file = open('stdout.txt', 'r')
        stderr_file = open('stderr.txt', 'r')

        self.assertEqual(stdout_file.readline(), '')
        self.assertEqual(stderr_file.readline(), '')

        stdout_file.close()
        stderr_file.close()
