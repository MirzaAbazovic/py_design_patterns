import  src.main.creational.factory.factory as factory

def test_factory_generates_dog():
    dog = factory.get_pet('dog')
    assert dog.speak() == 'Av Av'


def test_factory_generates_cat():
    cat = factory.get_pet('cat')
    assert cat.speak() == 'Mjau'
