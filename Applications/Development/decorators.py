def dec_func(func):
    def inner():
        print('hi')
        func()
        return
    return inner