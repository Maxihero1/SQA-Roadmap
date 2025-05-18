from pytest import mark

@mark.api
def test_prueba01():
    assert True

@mark.marlon
def test_prueba02():
    assert True

@mark.ui
@mark.parametrize('nombre', ['juan', 'luis', 'restituyo'])
def test_prueba03(nombre):
    print ("valor parametro: " + nombre)
    assert nombre in ['juan', 'luis', 'restituyo', 'sanchez']
