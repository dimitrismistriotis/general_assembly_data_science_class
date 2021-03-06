import pickle
import numpy as np
import scipy.stats as scs

# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)


# This loads in the list of numbers you are going to deal with
def load_pickle(file_name):
    """INPUT:
    - file_name(STR) [The name of the file]

    OUTPUT:
    - population(NUMPY ARRAY) [A array of numbers for the exercise]
    """
    return pickle.load(open(file_name))


def draw_sample(population, n):
    """INPUT:
    - population(NUMPY ARRAY) [The array containing all the numbers]
    - n(INT) [The number of sample you wanna draw]

    OUTPUT:
    - sample(NUMPY ARRAY) [A array that contains a subset of the population]

    Hint: Use np.random.choice(). Google it. Google is your best friend
    """
    # random_positions = np.random.choice(len(population), n)
    # return population[random_positions]
    # One liner:
    return population[np.random.choice(len(population), n)]


def get_mean(lst):
    """INPUT:
    - lst(NUMPY ARRAY) [The array of numbers where we find the mean of]

    OUTPUT:
    - mean_value(FLOAT)

    Hint: Don't use np.mean().
    Then use np.mean(arr) to see if you got the same value
    """
    l = len(lst)
    return float(sum(lst)) / l if l != 0 else None


def get_variance(lst, sample=True):
    """INPUT:
    - lst(NUMPY ARRAY) [Either the sample or the population]
    - sample(BOOL) [True if sample variance, False if population variance]

    OUTPUT:
    - lst_variance(FLOAT) [Sample or population variance depending]
    """
    n = len(lst)
    if n == 0 or (n == 1 and sample == True):
        return None

    denominator = n - 1 if sample else n
    m = get_mean(lst)

    return float(sum([(x - m)**2 for x in lst])) / denominator


def get_sem(sample):
    """INPUT:
    - sample(NUMPY ARRAY)

    OUTPUT:
    - sem(FLOAT) [Standard Error Mean]
    """
    variance = get_variance(sample, True)

    if variance == -1: # Error value
        return -1
    return float(np.sqrt(variance)) / np.sqrt(float(len(sample) - 1))


if __name__ == '__main__':
    population = load_pickle('../data/population.pkl')
    print 'First 10 element of the population: ', population[:5]

    #
    # Assignment, checking functions:
    #
    print('Population mean from custom function: %f, and from np.mean: %f' %
        (get_mean(population), np.mean(population)))

    print('Selecting %d random elements: %s' % (5, draw_sample(population, 5)))

    print('Variance of population: %f' % get_variance(population, False))
    one_pct_sample = draw_sample(population, (len(population) / 100))
    print('Variance of 1%% sample of population: %f' %
        get_variance(one_pct_sample, True))
    print('Standard Error of Mean of 1%% sample of population: %f' %
        get_sem(one_pct_sample))
    print('-' * 80)

    #
    # Assignment parts 2 to 4
    #

    # Part 2
    sample_100 = draw_sample(population, 100)
    sample_1000 = draw_sample(population, 1000)

    # Part 3
    sem_100 = get_sem(sample_100)
    sem_1000 = get_sem(sample_1000)
    print('Standard Error of Mean of 100 sample of population: %f' % sem_100)
    print('Standard Error of Mean of 1000 sample of population: %f' % sem_1000)

    print('Population mean from custom function: %f, and from np.mean: %f' %
        (get_mean(population), np.mean(population)))
    print("Sample mean of 100-sample: %f" % get_mean(sample_100))
    print("Sample mean of 1000-sample: %f" % get_mean(sample_1000))

    print("Variance of population: %f" % get_variance(population))
    variance_100 = get_variance(sample_100)
    print("Variance of 100-sample: %f" % variance_100)
    variance_1000 = get_variance(sample_1000)
    print("Variance of 1000-sample: %f" % variance_1000)
    print("Variance pcf difference: %f" % (
        ((variance_1000 - variance_100) * 100) / variance_1000))

    # Part 4
    print("Sem pct difference: %f" % (((sem_1000 - sem_100) * 100) / sem_1000))
