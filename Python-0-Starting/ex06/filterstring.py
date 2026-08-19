from ft_filter import ft_filter
import sys


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
    # print(res)


if __name__ == "__main__":
    main()
