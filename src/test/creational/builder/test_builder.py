import src.main.creational.builder.builder as b


def test_builder():
    builder = b.ToyotaBuilder()
    director = b.Director(builder)

    car = director.construct_car()

    assert 'Toyota' == car.model
    assert 'Good Year' == car.tires
    assert 'Diesel' == car.engine