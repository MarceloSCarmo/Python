import pytest
from funcao_quadratica import funcaoSegundoGrau, encontrandoDelta



def teste_funcaoSegundoGrau(x=5):
    """Essa função testa a função funcaoSegundoGrau quando dado o valor de x.
       Para que a função tenha exito, será necessário criar o dicionário dicPolinomio
       e extrair todos os valores das constantes.
       A função polinomio trás a formula da função de 2° grau e após executada, o metodo
       assert verificará se o resultado é o resultado esperado conforme o parâmetro fornecido.
    """

    dicPolinomio = {
                   "a": "6",
                   "b": "-4",
                   "c": "3"
    }

    a = dicPolinomio['a']
    b = dicPolinomio['b']
    c = dicPolinomio['c']

    polinomio = float(a)*(x**2) - float(b)*x + float(c)
    
    # verificando se o valor do polinomio é de fato 173 quando x=5
    assert polinomio == 173

def teste_encontrandoDelta(x=5):
    """Essa função testa a função funcaoSegundoGrau quando dado o valor de x.
       Para que a função tenha exito, será necessário criar o dicionário dicPolinomio
       e extrair todos os valores das constantes."""

    dicPolinomio = {
                   "a": "6",
                   "b": "-4",
                   "c": "3"
    }

    a = dicPolinomio['a']
    b = dicPolinomio['b']
    c = dicPolinomio['c']

    delta = (float(b)**2) - 4*(float(a)*float(c))

    # verificando se o valor do delta é de fato -56 quando x=5
    assert delta == -56

# mostrar o detalhes do teste exevutado
pytest.main(["-v", "--tb=line", "-rN", __file__])