from unittest.mock import patch, call, Mock

import datools
from datools.train import initialize_nn

SAMPLES='Our Samples'


def mock_fetch_samples(url):
    return SAMPLES


@patch('datools.train.train_nn')
@patch('datools.train.fetch_samples', mock_fetch_samples)
def test_initialize_nn_all_ok(fake_train_nn):
    fake_train_nn.return_value = 'NN'

    with patch('datools.train.print') as fake_print, \
        patch('datools.train.sleep') as fake_sleep:
        result = initialize_nn('http://example.org/data')

    fake_train_nn.assert_called_once_with(SAMPLES)

    assert result == fake_train_nn.return_value

    fake_sleep.asser_called_once_with(3000)

    assert fake_print.call_args_list == [call('going to fetch samples'), call('going to traing NN'), call('finished')]
