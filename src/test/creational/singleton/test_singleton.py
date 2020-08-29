import  src.main.creational.singleton.singleton as singleton

def test_singleton():
    a = singleton.Singleton(HTTP='Hypertext Transfer Protocol')

    b = singleton.Singleton(SIP = 'Session Initiation Protocol')

    assert 2 == len(a.__dict__)
    assert 'Hypertext Transfer Protocol' == a.__dict__['HTTP']
    assert 'Session Initiation Protocol' == a.__dict__['SIP']

    assert 2 == len(b.__dict__)
    assert 'Hypertext Transfer Protocol' == b.__dict__['HTTP']
    assert 'Session Initiation Protocol' == b.__dict__['SIP']
