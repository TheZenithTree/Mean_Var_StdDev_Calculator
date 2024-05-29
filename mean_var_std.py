import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    list = np.reshape(list, (3,3))

    means = mean_(list)
    variances = var_(list)
    standard_deviations = std_(list)
    maxes = max_(list)
    mins = min_(list)
    sums = sum_(list)

    calculations = {
        'mean' : means, 
        'variance' : variances,
        'standard deviation' : standard_deviations,
        'max' : maxes,
        'min' : mins,
        'sum' : sums
    }

    return calculations


def mean_(list):
    mean_by_column = np.mean(list, 0).tolist()
    mean_by_row = np.mean(list, 1).tolist()
    overall_mean = np.ravel(list).mean()

    return [mean_by_column, mean_by_row, overall_mean]


def var_(list):
    variance_by_column = np.var(list, 0).tolist()
    variance_by_row = np.var(list, 1).tolist()
    overall_variance = np.ravel(list).var()

    return [variance_by_column, variance_by_row, overall_variance]


def std_(list):
    standard_deviation_by_column = np.std(list, 0).tolist()
    standard_deviation_by_row = np.std(list, 1).tolist()
    overall_standard_deviation = np.ravel(list).std()

    return [standard_deviation_by_column, standard_deviation_by_row, overall_standard_deviation]


def max_(list):
    max_by_column = np.max(list, 0).tolist()
    max_by_row = np.max(list, 1).tolist()
    overall_max = np.ravel(list).max()

    return [max_by_column, max_by_row, overall_max]

def min_(list):
    min_by_column = np.min(list, 0).tolist()
    min_by_row = np.min(list, 1).tolist()
    overall_min = np.ravel(list).min()

    return [min_by_column, min_by_row, overall_min]


def sum_(list):
    sum_by_column = np.sum(list, 0).tolist()
    sum_by_row = np.sum(list, 1).tolist()
    overall_sum = np.ravel(list).sum()
    return [sum_by_column, sum_by_row, overall_sum]
