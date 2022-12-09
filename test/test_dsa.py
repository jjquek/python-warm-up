
# add src directory to list of directories that Interpreter will search for imports.
from src.dsa import foo
import sys
sys.path.append('/../src')


def test_foo():
    assert foo() == 0
