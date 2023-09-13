from src.main import sum, is_greater_than


"""Assert es una palabra reservada que verifica que la función responda como le decimos"""
def test_sum():
    """Verifica que la suma de 2 y 5 sea 7"""
    assert sum(2,5) == 7

def test_is_greater_than():
    """Verifica que 10 sea mayor que 2"""
    assert is_greater_than(10,2)