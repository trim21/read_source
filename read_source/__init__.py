import contextlib
import re
import itertools

_pattern = re.compile(r'^[ \t\f]*#.*?coding[:=][ \t]*([-_.a-zA-Z0-9]+)')


def get_encoding(file_path: str):
    with open(file_path, 'rb') as f:
        source_lines = itertools.islice(f.readlines(), 2)
    for line in source_lines:
        line = line.decode('ascii')
        result = _pattern.search(line)
        if result:
            return result.groups()[0]

    return 'utf-8'


@contextlib.contextmanager
def read(path: str, mode='r'):
    with open(
        path,
        mode=mode,
        encoding=get_encoding(path),
    ) as f:
        yield f


if __name__ == '__main__':
    with read('./read_source/__init__.py') as f:
        print(f.readlines())
