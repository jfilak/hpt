"""Train neural network"""

from time import sleep


def fetch_samples(url):
    print(f'fetching from {url}')
    sleep(1000)


def train_nn(samples):
    print(f'training NN with {samples}')
    sleep(2000)


def initialize_nn(url):
    print('going to fetch samples')
    samples = fetch_samples(url)

    # just for fun!
    sleep(3000)

    print('going to traing NN')
    nn = train_nn(samples)

    print('finished')
    return nn
