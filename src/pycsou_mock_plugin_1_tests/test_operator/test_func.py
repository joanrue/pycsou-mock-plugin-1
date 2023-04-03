from pycsou_mock_plugin_1 import NullFunc


def test_nullfunc():
    assert NullFunc(1)._name == "ModifiedNullFunc"
