import numpy as np
from scipy.special import comb


def calculate_value(arr: np.array):
    """
    Pascal's triangle number 1!
    """
    n = len(arr)

    def calc_at_x(x: int) -> int:
        k_arr = np.arange(n - x, n + 1)
        k_arr_n = n - k_arr
        return (
            np.power(np.full(x + 1, -1), k_arr_n)
            * comb(np.full(x + 1, x), k_arr_n)
            * arr[n - (x + 1) :]
        ).sum()

    def _calc_all():
        for i in range(n):
            if (val := calc_at_x(i)) == 0:
                break
            yield (int(val))

    return sum(_calc_all())


def calculate_first_history(arr: np.array):
    """
    Pascal's triangle number 2!
    """

    def calc_at_x(x: int) -> int:
        k_arr = np.arange(x + 1)
        return (
            np.power(np.full(x + 1, -1), x - k_arr)
            * comb(np.full(x + 1, x), k_arr)
            * arr[: (x + 1)]
        ).sum()

    def _calc_all():
        n = len(arr)
        for i in range(n - 1, 0, -1):
            val = calc_at_x(i)
            yield (int(val))
        yield arr[0]

    ret_arr = np.array(list(_calc_all()))
    running_sum = ret_arr[0]
    for i in range(1, len(ret_arr)):
        running_sum = ret_arr[i] - running_sum
    return running_sum


def total_sum(anarr: np.array) -> int:
    return sum(calculate_value(anarr[i]) for i in range(anarr.shape[0]))


def total_sum_first_history(anarr: np.array) -> int:
    return sum(calculate_first_history(anarr[i]) for i in range(anarr.shape[0]))


def parse_all_lines(all_lines: str) -> np.array:
    return np.array(
        list(map(lambda x: x.split(" "), all_lines.strip().split("\n")))
    ).astype(np.int64)


def part_one(all_lines: str) -> int:
    return total_sum(parse_all_lines(all_lines))


def part_two(all_lines: str) -> int:
    return total_sum_first_history(parse_all_lines(all_lines))
