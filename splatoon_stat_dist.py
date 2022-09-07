import numpy as np


def compute_stationary_distribution(win_prob):
    history_length = 50
    transition_probs = np.zeros(shape=(history_length, history_length))

    for i in range(history_length):
        if i == 0:
            transition_probs[i][i] = 1 - win_prob
            transition_probs[i][i + 1] = 1 - win_prob
        elif i == history_length - 1:
            transition_probs[i][i - 1] = win_prob
            transition_probs[i][i] = win_prob
        else:
            transition_probs[i][i - 1] = win_prob
            transition_probs[i][i + 1] = 1 - win_prob

    eigen_values, eigen_vectors = np.linalg.eig(transition_probs)
    eigen_vector = eigen_vectors[:,np.isclose(eigen_values, 1)]
    eigen_vector = eigen_vector[:,0]
    eigen_vector = eigen_vector / eigen_vector.sum()
    stationary_distribution = eigen_vector.real
    return stationary_distribution


def main():
    win_prob = 0.6
    distribution = compute_stationary_distribution(win_prob)
    print(f'distribution for probability: {win_prob} is:')
    print(f'{distribution}')


if __name__ == '__main__':
    main()
