import pytest
from manager import (
    contact_dict,
    load_contact_file,
    save_contacts_to_csv,
    display_menue,
    choice_handling,
    view_contacts,
    add_contact,
    edit_contact,
    delete_contact,
    search_contact,
)
from contact import Contact

@pytest.fixture(autouse=True)
def clear_contacts():
    contact_dict.clear()
    yield
    contact_dict.clear()


def test_load_empty(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    load_contact_file()
    assert contact_dict == {}


def test_add_contact_new(monkeypatch, capsys):
    inputs = iter([
        "Alice Example",    
        "555-123-4567",     
        "alice@example.com",
        "Met at conference",
        "01/02/1990"        
    ])
    monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
    add_contact()
    out, _ = capsys.readouterr()
    assert "has been added successfully" in out
    assert "Alice Example" in contact_dict


def test_view_contacts_empty(capsys):
    view_contacts()
    out, _ = capsys.readouterr()
    assert "no saved contacts" in out.lower()


def test_view_contacts_with_data(capsys):

    contact_dict['Bob Builder'] = Contact(
        "Bob Builder",
        "555-234-5678",
        "bob.builder@example.com",
        "Contractor",
        "03/15/1985"
    )
    view_contacts()
    out, _ = capsys.readouterr()
    assert "Bob Builder" in out
    assert "bob.builder@example.com" in out


def test_delete_contact(monkeypatch, capsys):
    contact_dict['Carol Singer'] = Contact(
        "Carol Singer",
        "555-345-6789",
        "carol@example.com",
        "Singer",
        "07/22/1992"
    )
    monkeypatch.setattr('builtins.input', lambda prompt="": "Carol Singer")
    delete_contact()
    out, _ = capsys.readouterr()
    assert 'deleted' in out.lower()
    assert 'Carol Singer' not in contact_dict


def test_search_by_name(monkeypatch, capsys):
    contact_dict['Dan Miller'] = Contact(
        "Dan Miller",
        "555-456-7890",
        "dan.miller@example.com",
        "Friend",
        "12/05/1988"
    )
    inputs = iter(["1", "Dan"])
    monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
    search_contact()
    out, _ = capsys.readouterr()
    assert "Dan Miller" in out
    assert "dan.miller@example.com" in out