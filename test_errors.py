from errors import convert_to_integer

def test_integer():
    convert_to_integer(123) == 123

def test_string():
    assert convert_to_integer('123') == 123

