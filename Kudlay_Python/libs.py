def get_count(string, symbol):
    cnt = 0
    for i in string:
        if i == symbol:
            cnt += 1
    return cnt


def get_len(string):
    cnt = 0
    for i in string:
        cnt += 1
    return cnt


if __name__ == '__main__':
    print(__name__)
    print('Hello, I am libs.py')
