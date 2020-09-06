from src.main.structural.adapter.adapter import Adapter, Bosnian, English


def test_adapter():
    bos = Bosnian()
    eng = English()
    #wrap Bosninan and map pozdravi_se to hi
    adapterBos = Adapter(bos, hi=bos.pozdravi_se)
    #wrap Bosninan and map say_hello to hi
    adapterEng = Adapter(eng, hi=eng.say_hallo)
    ##call hi methods on adapted
    assert 'Vozdra. Sta ima ?' == adapterBos.hi()
    assert 'Hi, how are You?' == adapterEng.hi()
