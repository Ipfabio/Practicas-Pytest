# Models
from src.models.LanguageModel import LanguageModel

def test_get_languages_not():
    """Verifica que get_languages sea distinto de None"""
    languages = LanguageModel.get_languages()
    assert languages != None

def test_get_languages_has_elements():
    """Verifica que get_languages tenga elementos"""
    languages = LanguageModel.get_languages()
    assert len(languages) > 0
    
def test_get_languages_check_elements_length():
    """Verifica la longitud de cada elemento dentro de get_languages"""
    languages = LanguageModel.get_languages()
    for language in languages:
        assert len(language) > 0