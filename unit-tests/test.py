import unittest
import file_to_test


class TestMain(unittest.TestCase):
    # Setting up tests
    def setUp(self) -> None:
        print('About to test a function')

    def test_number_passed(self):
        """Hi"""
        test_param = 10
        result = file_to_test.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_string_passed(self):
        test_param = 'a'
        result = file_to_test.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_none_passed(self):
        test_param = None
        result = file_to_test.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def test_empty_string_passed(self):
        test_param = ''
        result = file_to_test.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    # Tearing down after tests
    def tearDown(self) -> None:
        print('Cleaning up')


if __name__ == '__main__':
    unittest.main()
