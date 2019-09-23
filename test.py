def pretty(abc=True):
    def decorate(func):
        return func

    return decorate


def pretty2(abc=True):
    def decorate(func):
        def real(*_args):
            _result = func(*_args)
            return _result

        return real

    return decorate


@pretty()
def f1():
    print('f1')


@pretty2()
def f2():
    print('f2')

f1()
pretty()(f1)
f2()
