from app.utils import filter_dict


def test_filter_dict():
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    desired_keys = {'a', 'c'}
    filtered = filter_dict({'a': 1, 'b': 2, 'c': 3}, desired_keys)
    assert filtered == {'a': 1, 'c': 3}
