from dataclasses import dataclass
import pandas as pd
from pandas.testing import assert_frame_equal
import unittest
from helloworkbench import render


@dataclass(frozen=True)
class Column:
    name: str
    type: str  # one of 'text', 'number' or 'datetime'


def P(*, colname: str = '', factor: float = 2.0):
    """Helper to build params."""
    return {
        'colname': colname,
        'factor': factor,
    }


class HelloWorkbenchTest(unittest.TestCase):
    def test_no_column_no_op(self):
        result = render(pd.DataFrame({'A': [1, 2]}), P(), input_columns={})
        expected = pd.DataFrame({'A': [1, 2]})
        assert_frame_equal(result, expected)

    def test_column_wrong_type(self):
        # TODO let the module-spec YAML specify type so we don't need to test
        # this case.
        result = render(pd.DataFrame({'A': [1, 2]}),
                        P(colname='A', factor=3.0),
                        input_columns={'A': Column('A', 'text')})
        self.assertEqual(result, 'Please select a Number column')

    def test_happy_path(self):
        result = render(pd.DataFrame({'A': [1, 2]}),
                        P(colname='A', factor=3.0),
                        input_columns={'A': Column('A', 'number')})
        expected = pd.DataFrame({'A': [3.0, 6.0]})
        assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
