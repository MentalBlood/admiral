description = 'Test subcommand'

args = [
    ('names',               'type',     'nargs',    'required',     'help',                     'default'),
    (['-s', '--string'],    str,        1,          True,           'Test string argument',     'string'),
    (['-i', '--int'],       int,        2,          True,           'Test int argument',        1),
    (['-f', '--float'],     float,      1,          True,           'Test float argument',      1.01)
]


def handler(args):
    return {
        name: getattr(args, name)
        for name in dir(args)
        if not name.startswith('_') and not name == 'handler'
    }