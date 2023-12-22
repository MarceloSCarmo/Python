import pytest
from condicoes_para_neve import main, tempNuvem


def teste_tempNuvem():
    """teste if:
    1 - temepratura > 0 and vento < 15 and umidade < 70
    2 - temperatura > 0 and vento > 15 and umidade > 70
    3 - temperatura > 0 and vento > 15 and umidade < 70
    3 - temperatura > 0 and vento < 15 and umidade > 70

    4 - temperatura <= 0 and vento < 15 and umidade < 70 So vai nevar se essa condição for atendida
    5 - temperatura <= 0 and vento > 15 and umidade > 70
    6 - temperatura <= 0 and vento > 15 and umidade < 70
    7 - temperatura <= 0 and vento < 15 and umidade > 70""" 

    assert tempNuvem() <= 0
    
pytest.main(["-v", "--tb=line", "-rN", __file__])
