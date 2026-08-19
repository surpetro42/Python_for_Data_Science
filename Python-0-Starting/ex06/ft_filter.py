def ft_filter(func, data):
    """Return an iterator yielding those items of iterable for which
    function(item) is true.  If function is None, return the items that
    are true."""
    if func is not None:
        return (i for i in data if func(i))
    return (i for i in data if i)
