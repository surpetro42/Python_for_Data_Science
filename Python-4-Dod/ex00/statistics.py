from typing import Any


def valid_arg(args):
    if args:
        if all(isinstance(x, (int, float)) for x in args):
            return True
    print("ERROR")
    return False


def mean(args):
    return sum(args) / len(args)

def median(args):
    args = sorted(args)
    l = len(args)
    if l % 2 == 0:
        center_index_left = args[(l // 2) - 1]
        center_index_right = args[(l // 2)]
        center = (center_index_left + center_index_right) / 2
    else:
        center = args[l // 2]
    return center


def quartile(args):
    args = sorted(args)

    if len(args) == 1:
        return [float(args[0]), float(args[0])]
    pos25 = 0.25 * (len(args) - 1)
    index25 = int(pos25)
    fraction25 = pos25 - index25

    pos75 = 0.75 * (len(args) - 1)
    index75 = int(pos75)
    fraction75 = pos75 - index75

    q1 = args[index25] + fraction25 * (args[index25 + 1] - args[index25])
    q2 = args[index75] + fraction75 * (args[index75 + 1] - args[index75])
    return [q1, q2]


def std(args):
    average_nb = mean(args)
    variance = sum((x - average_nb) ** 2 for x in args) / len(args)
    return variance ** 0.5


def var(args):
    average_nb = mean(args)
    variance = sum((x - average_nb) ** 2 for x in args) / len(args)
    return variance


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for value in kwargs.values():
        match value:
            case "mean":
                if (valid_arg(args)):
                    print("mean :", mean(args))
            case "median":
                if (valid_arg(args)):
                    print("median :", median(args))
            case "quartile":
                if (valid_arg(args)):
                    print("quartile :", quartile(args))
            case "std":
                if (valid_arg(args)):
                    print("std :", std(args))
            case "var":
                if (valid_arg(args)):
                    print("var :", var(args))


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()


# $> python tester.py
# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
# -----
# std : 17982.70124086944
# var : 323377543.9183673
# -----
# -----
# ERROR
# ERROR
# ERROR