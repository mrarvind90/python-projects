import unittest

from arithmetic_formatter.formatter import formatter
from parameterized import parameterized, param
from typing import List, Optional, Union


class UnitTests(unittest.TestCase):

    @parameterized.expand([
        param(name="test_two_problems_arrangement1",
              args=[['3801 - 2', '123 + 49']],
              expected='  3801      123\n-    2    +  49\n------    -----',
              msg='Expected different output when calling "formatter()" with ["3801 - 2", "123 + 49"]'),
        param(name="test_two_problems_arrangement2",
              args=[['1 + 2', '1 - 9380']],
              expected='  1         1\n+ 2    - 9380\n---    ------',
              msg='Expected different output when calling "arithmetic_arranger()" with ["1 + 2", "1 - 9380"]'),
        param(name='test_four_problems_arrangement',
              args=[['3 + 855', '3801 - 2', '45 + 43', '123 + 49']],
              expected='    3      3801      45      123\n+ 855    -    2    + 43    +  49\n'
                       '-----    ------    ----    -----',
              msg='Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", '
                  '"45 + 43", "123 + 49"]'),
        param(name='test_five_problems_arrangement',
              args=[['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']],
              expected='  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n'
                       '----    ------    ---    -----    ------',
              msg='Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", '
                  '"1 + 2", "123 + 49", "1 - 9380"]'),
        param(name='test_too_many_problems',
              args=[['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']],
              expected='Error: Too many problems.',
              msg='Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many '
                  'problems."'),
        param(name='test_incorrect_operator',
              args=[['3 / 855', '3801 - 2', '45 + 43', '123 + 49']],
              expected="Error: Operator must be '+' or '-'.",
              msg='''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return 
              "Error: Operator must be '+' or '-'."'''),
        param(name='test_too_many_digits',
              args=[['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']],
              expected='Error: Numbers cannot be more than four digits.',
              msg='Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to '
                  'return "Error: Numbers cannot be more than four digits."'),
        param(name='test_only_digits',
              args=[['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']],
              expected='Error: Numbers must only contain digits.',
              msg='Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the '
                  'number to return "Error: Numbers must only contain digits."'),
        param(name='test_two_problems_with_solutions',
              args=[['3 + 855', '988 + 40'], True],
              expected='    3      988\n+ 855    +  40\n-----    -----\n  858     1028',
              msg='Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with ['
                  '"3 + 855", "988 + 40"] and a second argument of `True`.'),
        param(name='test_five_problems_with_solutions',
              args=[['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True],
              expected='   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    '
                       '------    ----    -----    -----\n -666     -3800      88      172     1028',
              msg='Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with '
                  'five arithmetic problems and a second argument of `True`.')
    ])
    def test_arithmetic_formatter(self, name: str, args: List[Union[List[str], Optional[bool]]], expected: str,
                                  msg: str):
        actual: str = formatter(*args)
        self.assertEqual(actual, expected, msg)


if __name__ == "__main__":
    unittest.main()
