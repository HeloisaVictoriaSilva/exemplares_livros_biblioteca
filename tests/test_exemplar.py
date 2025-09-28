import pytest
from exemplar import Exemplar


#CT027
def test_perdido_exemplar_alterar_status():
    exemplar = Exemplar(id_Exemplar= 123)
    exemplar.status = 3
    resultado = exemplar.alterar_status(4)
    assert resultado is True
    assert exemplar.status == 4

#CT028
def test_disponibilizar_exemplar_restauração():
    exemplar = Exemplar(id_Exemplar=245)
    exemplar.status= 5
    resultado = exemplar.alterar_status(1)
    assert resultado is True
    assert exemplar.status == 1

#CT029
def test_descartar_exemplar_restauracao():
    exemplar= Exemplar(id_Exemplar=234)
    exemplar.status= 5
    resultado= exemplar.alterar_status(9)
    assert resultado is True
    assert exemplar.status ==9

#CT030  
def test_disponibilizar_exemplar_perdido():
    exemplar= Exemplar(id_Exemplar=765)
    exemplar.status= 4
    resultado= exemplar.alterar_status(1)
    assert resultado is False
    assert exemplar.status== 4

#CT031
def test_descartar_exemplar_perdido():
    exemplar= Exemplar(id_Exemplar=548)
    exemplar.status= 4
    resultado= exemplar.alterar_status(9)
    assert resultado is False
    assert exemplar.status==4

#CT032
def test_disponibiliar_exemplar_descartado():
    exemplar= Exemplar(id_Exemplar=865)
    exemplar.status= 9
    resultado= exemplar.alterar_status(1)
    assert resultado is False
    assert exemplar.status==9

