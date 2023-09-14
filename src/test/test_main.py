import pytest
from src.main import sum, is_greater_than


"""Assert es una palabra reservada que verifica que la función responda como le decimos"""
def test_sum():
    """Verifica que la suma de 2 y 5 sea 7"""
    assert sum(2,5) == 7

def test_is_greater_than():
    """Verifica que 10 sea mayor que 2"""
    assert is_greater_than(10,2)

# Esto me permite pasarle una serie de parametros que quisiera testear en formato lista
@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [   
        (5,1,6),
        (6,sum(4,2),12),
        (sum(19,1),15,35),
        (-7,10,sum(-7,10)),
    ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y)==expected