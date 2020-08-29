import  src.main.creational.factory.abstract_factory as abs_factory

def test_abs_factory_generates_dog():
    #concrete factory
    factory = abs_factory.DogFactory()
    #abstract factory
    store = abs_factory.PetStore(factory)
    assert store.get_pet_food() == 'Dog food'
    assert store.get_pet().speak() == 'Av Av'


def test_abs_factory_generates_cat():
    # concrete factory
    factory = abs_factory.CatFactory()
    # abstract factory
    store = abs_factory.PetStore(factory)
    assert store.get_pet_food() == 'Cat food'
    assert store.get_pet().speak() == 'Mjau'




