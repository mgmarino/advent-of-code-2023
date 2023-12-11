import numpy as np

ListOfIndices = tuple[np.array, np.array]


def get_rows_and_columns_to_expand(arr: np.array) -> ListOfIndices:
    non_galaxies = arr == "."

    return (
        # rows
        np.argwhere(np.sum(non_galaxies, axis=1) == arr.shape[1]).flatten(),
        # cols
        np.argwhere(np.sum(non_galaxies, axis=0) == arr.shape[0]).flatten(),
    )


def find_distances_between_galaxies_scaled(arr: np.array, scale: int = 1) -> int:
    idxs = np.argwhere(arr == "#")
    row_idxs, col_idx = get_rows_and_columns_to_expand(arr)

    rows_to_expand = set(row_idxs)
    cols_to_expand = set(col_idx)
    total_distance = 0

    for i in range(idxs.shape[0]):
        total_distance += np.abs(idxs[i] - idxs[i:]).sum()
        #  This would generally be the summed distance between all the points,
        #  but if we need to scale some space, then we need to do the following
        #  checks.

        for j in range(i + 1, idxs.shape[0]):
            all_vals = np.sort(idxs[[i, j]], axis=0)

            # Get all indices between the two galaxies, in both row and column
            rows_to_check = set(range(*tuple(all_vals[:, 0])))
            cols_to_check = set(range(*tuple(all_vals[:, 1])))

            # The total number of times we need to expand is simply the length
            # of the overlap of these sets
            total_to_expand = len(cols_to_check & cols_to_expand) + len(
                rows_to_check & rows_to_expand
            )

            # If we do need to expand, make sure to remove the steps we've already counted
            total_distance += scale * total_to_expand - total_to_expand

    return total_distance


def part_one_and_two(all_lines: str, scale: int) -> int:
    arr = np.array(list(map(list, all_lines.split("\n"))))
    return find_distances_between_galaxies_scaled(arr, scale)
