import numpy as np


def compute_expected_wins(win_prob):
    max_matches = 50
    probs = np.zeros(shape=(max_matches + 1, ))
    values = np.arange(max_matches + 1)

    for i in range(max_matches + 1):
        n_factorial = np.math.factorial(max_matches)
        i_factorial = np.math.factorial(i)
        n_i_factorial = np.math.factorial(max_matches - i)
        probs[i] = n_factorial / (i_factorial * n_i_factorial) * (win_prob ** i) * ((1 - win_prob) ** (max_matches - i))

    print(f'probs: {probs}: sum: {probs.sum()}')
    print(f'values: {values}')

    expectation = (probs * values).sum()

    print(f'expectation: {expectation}')


def main():
    compute_expected_wins(win_prob=0.35)


if __name__ == '__main__':
    main()
