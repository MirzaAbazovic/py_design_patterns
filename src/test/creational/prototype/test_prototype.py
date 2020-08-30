import src.main.creational.prototype.prototype as proto


def test_prototype():
    car = proto.Car()
    prototype_inst = proto.Prototype()
    prototype_inst.register_object('toyota', car)
    cloned_car = prototype_inst.clone('toyota')
    assert car.name == cloned_car.name, 'Cloned car name is same'
    assert car.color == cloned_car.color, 'Cloned car name is same'
    assert car.options == cloned_car.options, 'Cloned car options are same'


def test_prototype_with_changed_attr():
    car = proto.Car()
    prototype_inst = proto.Prototype()
    prototype_inst.register_object('toyota', car)
    cloned_car = prototype_inst.clone('toyota', color='Blue')
    assert car.name == cloned_car.name, 'Cloned car name is same'
    assert 'Blue' == cloned_car.color, 'Cloned car color is changed to Blue'
    assert car.options == cloned_car.options, 'Cloned car options are same'
