import src.main.structural.decorator.decorator as decorator

def test_decorator():
    result = decorator.echo('hi how are you')
    assert 'HI HOW ARE YOU' == result
    # next 2 assertions would fail if there was no @wraps(fun)
    # values will be form decorating function
    assert decorator.echo.__name__ == 'echo'
    assert decorator.echo.__doc__ == 'original function'