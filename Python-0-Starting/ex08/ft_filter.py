def ft_filter(func, data):
    """Return an iterator yielding those items of iterable for which
    function(item) is true.  If function is None, return the items that
    are true."""
    if func is None:
        for i in data:
            if i:
                yield i
    else:
        for i in data:
            if func(i):
                yield i


def main():
    """Demonstrate the usage of the ft_filter function."""
    pass


if __name__ == "__main__":
    main()
