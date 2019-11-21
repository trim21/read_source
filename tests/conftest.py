import jinja2
import os.path

test_dir = os.path.dirname(__file__)

ENCODING = {
    'utf-8',
    'latin-1',
    'ascii',
    'gbk',
    'gb2312',
    'gb18030',
}


def pytest_sessionstart(session):
    print('session start')
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.join(test_dir, 'source/template'))
    )
    for encoding in ENCODING:
        make_test_source_dir(encoding)
        for template in env.list_templates():
            source_str = env.get_template(template).render(encoding=encoding)
            with open(
                os.path.join(test_dir, 'source', encoding, template),
                'w+',
                encoding=encoding,
            ) as f:
                f.write(source_str)


def make_test_source_dir(encoding):
    os.makedirs(os.path.join(test_dir, 'source', encoding), exist_ok=True)
