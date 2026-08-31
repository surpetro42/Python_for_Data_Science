import sys


def ft_filter(func, data):
    """Return an iterator yielding those items of iterable for which
    function(item) is true.  If function is None, return the items that
    are true."""
    if func is not None:
        return [i for i in data if func(i)]
    return [i for i in data if i]


def main():
    """The function that receives 2 arguments is the first line,
        and the second is N.
        in this line, she should find words longer than n:"""
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        exit()
    string = sys.argv[1].split(" ")
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        exit()
    print(list(ft_filter(lambda x: len(x) > n, string)))


if __name__ == "__main__":
    main()
