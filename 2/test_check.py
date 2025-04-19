import io
import sys
from contextlib import redirect_stdout
from zipfile import ZipFile

import pytest

filename = 'tests.zip'  # имя файла с тестами
module = 'asdf'       # имя файла python, в котором вы решаете задачи
test_fixtures = []

with ZipFile(filename, 'r') as zf:
    files = zf.filelist
    for i in range(0, len(files), 2):
        with (
            zf.open(files[i]) as reply,
            zf.open(files[i + 1]) as clue,
        ):
            reply = reply.read().decode('u8')
            clue = clue.read().decode('u8')
            test_fixtures.append((reply, clue))


@pytest.mark.parametrize('test_input,expected', test_fixtures)
def test_exec(test_input, expected):
    with redirect_stdout(io.StringIO()):
        exec(f'from {module} import *\n{test_input}')
        result = sys.stdout.getvalue().strip()
        assert result == expected