import os
import time


def ft_tqdm(lst: range):
    total = len(lst)
    size_terminal = os.get_terminal_size().columns
    size = size_terminal - 36 - (len(str(total)) * 2 + 2)
    # size = size_terminal.columns - (size_terminal.columns - 100)

    for index, elem in enumerate(lst, 1):
        percent = index / total * 100
        filled = int(percent / 100 * size)
        remained = size - filled
        stripe = "█" * filled + " " * remained
        print(f"\r{percent:.3f}%|{stripe}| {index}/{total}", end="")
        yield elem


def main():
    """Repeats the operation of the TQDM function."""

    for elem in ft_tqdm(range(333)):
        time.sleep(0.005)
    print()


if __name__ == "__main__":
    main()
