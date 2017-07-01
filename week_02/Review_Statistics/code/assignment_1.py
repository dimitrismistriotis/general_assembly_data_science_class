import numpy as np
import scipy.stats as scs


def get_mean(lst):
    """Return the mean of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, mean value of the input list

    Do not use np.mean().
    """
    if len(lst) == 0:
        return None
    else:
        return float(sum(lst)) / len(lst)    


def get_median(lst):
    """Return the median of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, median value of the input list

    Do not use np.median().
    """
    l = len(lst)
    if l == 0:
        return None

    slst = sorted(lst)
    if l % 2 == 0:
       return (float(slst[(l/2) - 1]) + float(slst[(l/2)])) / 2
    else:
       return float(slst[(l/2)])

def get_mode(lst):
    """Return the mode of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, mode value of the input list (FLOAT)

    Do not use scs.mode().
    """
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return max(freq, key=lambda f: freq[f])


def get_range(lst):
    """Return the range of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, range of the input list
    """
    return float(max(lst)) - float(min(lst))


def get_IQR(lst):
    """Return the interquartile range of all the values in lst

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    float, interquartile range of the input list (FLOAT)

    Hint: you may use np.percentile
    """
    return (float(np.percentile(lst, 75)) - float(np.percentile(lst, 25)))


def remove_outliers(lst):
    """Return all the values in lst in sorted order without the outliers

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    list, sorted lst with any data points 3 interquartile range below Q1
    (25th percentile) or 3 interquartile range above Q3 (75th percentile)
    """
    slst = sorted(lst)
    three_iqr = 3 * get_IQR(lst)
    low_boundary = float(np.percentile(lst, 25)) - three_iqr
    high_boundary = float(np.percentile(lst, 75)) + three_iqr

    return filter(lambda x: x >= low_boundary and x <= high_boundary, slst)


def run_check(lst):
    """Check the output of functions implemented (mean, median and mode)

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    None, prints out the results of the test comparing hand implemented
        functions to corresponding 'np' or 'scs' methods.
    """
    print('Mean: ', get_mean(lst) == np.mean(lst))
    print('Median: ', get_median(lst) == np.median(lst))
    print('Mode: ', get_mode(lst) == scs.mode(lst).mode[0])


def print_summary_metrics(lst):
    """Print an overview of all summary statistics mentioned in this exercise

    Parameters
    ----------
    lst : list of ints/floats

    Returns
    -------
    None, prints out the values of the summary statistics studied in
        this exercise.
    """
    print('*' * 50)
    print(' ' * 16 + 'Summary statistics')
    print('*' * 50)
    print('mean: {} | median: {} | mode: {}'.format(get_mean(lst),
                                                    get_median(lst),
                                                    get_mode(lst)))
    print('range: {} | IQR: {}'.format(get_range(list_nums),
                                       get_IQR(list_nums)))
    print('\n')
    print('original list: \n          {}'.format(lst))
    print('sorted list: \n          {}'.format(sorted(lst)))
    print('List without outliers: \n          {}'.format(
                                                remove_outliers(list_nums)))


if __name__ == '__main__':
    list_nums = [100, 9, 4, 7, 22, 37, 44, 22, 79, 88, 200, 37, 22, 1000]
    run_check(list_nums)
    print_summary_metrics(list_nums)
