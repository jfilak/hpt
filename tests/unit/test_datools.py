import pytest

import datools


BACKUP_SEED=datools._SEED


@pytest.fixture
def custom_seed():
    return '65535'


@pytest.fixture
def my_seed(custom_seed, request):
    assert my_seed != BACKUP_SEED

    def fin():
        print('restoring the saved seed')
        datools.set_seed(BACKUP_SEED)

    request.addfinalizer(fin)

    return custom_seed


def test_get_seed_default():
    assert datools.get_seed() == datools._SEED


def test_get_seed_fail_intended():
    assert datools.get_seed() == 12345


def test_get_seed_print(capsys):
    print(datools.get_seed())
    captured = capsys.readouterr()
    assert captured.out == '331999\n'


def test_set_seed_ok(my_seed):
    print('changing seed')
    datools.set_seed(my_seed)
    assert datools.get_seed() == my_seed


def test_get_seed_default_again():
    assert datools.get_seed() == BACKUP_SEED
