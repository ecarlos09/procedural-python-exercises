import pytest
import io
import app

def test_get_user_name(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO('Elwin'))
    choose_name = app.get_user_name()
    app.print_result(choose_name, 'dragon', 'Draco')
    out, err = capsys.readouterr()
    assert 'Elwin' in out

def test_get_user_animal(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('dragon'))
    choose_dragon = app.get_user_animal()
    assert choose_dragon == 'dragon'

@pytest.mark.parametrize('month, expected', [("January", "Blaze"), ("February", "Fuego"), ("March", "Charmander")])
def test_handle_dragon_generator(month, expected, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO(month))
    chosen_month = app.get_user_birth_month()
    result = app.handle_dragon_generator(chosen_month)
    assert result == expected

@pytest.mark.parametrize('month, expected', [("January", "Mumble"), ("February", "Squeak"), ("March", "Skipper")])
def test_handle_penguin_generator(month, expected, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO(month))
    chosen_month = app.get_user_birth_month()
    result = app.handle_penguin_generator(chosen_month)
    assert result == expected