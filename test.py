

def register(activie):
    def decorate(func):
        print('i got func')
        if activie:
            print('also i get true')
        else:
            print('also i got false')
        return func

    return decorate


if __name__ == '__main__':
    @register(activie=False)
    def f1(a, b):
        print('f1 start')


    f1(2, 3)
