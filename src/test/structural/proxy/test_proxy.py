from src.main.structural.proxy.proxy import Producer, Proxy

def test_proxy():
    proxy = Proxy()
    assert 'Producer is busy' == proxy.produce()
    proxy.occupied = False
    assert 'Producer has time to meet You now' == proxy.produce()
    proxy.occupied = True
    assert 'Producer is busy' == proxy.produce()
