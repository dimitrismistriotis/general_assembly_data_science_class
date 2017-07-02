# Assignment: Summary metrics

## Objectives

We want to describe a dataset thanks to some key summary metrics. We will be

  - implementing mean, median and mode as well as when to use each summary metric
  - investigating range, interquartile range and outliers

Remember that plotting out data is still the best way to understand it. Checkout [Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe's_quartet).

_______________________________________

## Questions & Answers

Brief recap: notice the `if __name__ == '__main__':` block in the `.py` file. The code in this block will run when you type in the command prompt `python assignment_1_summary_stats.py`. Here it is mostly a check for our functions.

1. Mean, median, mode

  (a) Fill in the functions `get_mean`, `get_median`, and `get_mode` in [assignment_1.py](../code/assignment_1.py). For the sake of practice, do not use `np.mean`, `np.median` and `scs.mode`.

  (b) Brief dataset description
    - dataset_1 : prices from used cars in my price range.
    - dataset_2 : prices of used cars I can afford and my dream car, a brand new Audi A8L.
    - dataset_3 : prices from used and new cars on Craiglist.

  Which summary metric would you choose to best describe datasets 1 to 3?

  YOUR ANSWER: Median

  YOUR EXPLANATION: So that I could get a feeling on where prices are about.
  I have a feeling that car prices would have many outliers both in the top
  of the market (ultra expensive custom-made) as well as in the bottom (cars
  that can be used for parts/scrap).

2. Range vs interquartile range
  Fill in the functions `get_range`, `get_IQR`, and `remove_outliers` in [assignment_1.py](../code/assignment_1.py). Look up how to use `np.percentile`.

  How are range and interquartile range similar? How are they different?

  YOUR ANSWER: Interquartile range would remove the outliers and maybe some
  high and low variables. Range has more information but is sensitive to
  very high and very low values.

  If there are outliers in your dataset, how do you decide if you are going to ignore them or keep them in your analysis?

  YOUR ANSWER: Intuition and needs of the problem? How many are they? How far
  away from the "body" data-set? Could they be partly because of chance or
  errors in measurement?

_______________________________________
## Extra resources

- These are relatively basic notions, they are defined in Khan Academy (https://www.khanacademy.org/math/statistics-probability/displaying-describing-data) and Udacity (https://classroom.udacity.com/courses/st101/) courses.
