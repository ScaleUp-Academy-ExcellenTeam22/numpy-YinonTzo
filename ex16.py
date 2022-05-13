import numpy as np
import nptyping


def sort_by_student_id_and_height(student_id: nptyping.ndarray,
                                  student_height: nptyping.ndarray) -> nptyping.ndarray:
    """
    https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html
    lexsort takes k arrays (with same shape) and makes sort by the kth array.
    If same keys are provided, lexsort would sort by the k-1th array.
    For example- a = [1, 2, 1]
                 b = [0, 5, 9]
                 and: lexsort((b, a)) # first by a then by b.
    There are 1 twice. So to determine who be first, we take a look in b
    and see that in index 0 there is 0 and in index 2 there is 9.
    So we take 0. and so on.
    :param student_id: To sort by.
    :param student_height: To sort by.
    :return: Array of indexes which represent a sort.
    """
    return np.lexsort((student_id, student_height))


def main() -> None:
    """
    https://www.w3resource.com/python-exercises/numpy/python-numpy-sorting-and-searching-exercise-4.php
    Create student_id and height arrays,
    sort the student id with increasing height of the students
    from given students id and height.
    Print the integer indices that describes the sort order by
    multiple columns and the sorted data
    https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html
    """
    student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
    student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

    # Sort by studen_id then by student_height
    indices = sort_by_student_id_and_height(student_id, student_height)
    print("Sorted indices:")
    print(indices)
    print("Sorted data:")
    for n in indices:
        print(student_id[n], student_height[n])


if __name__ == '__main__':
    main()
