from contacts.forms import NameForm


def test_name_form_success():
    # Given
    data = {"your_name": "John Doe"}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is True


def test_name_form_fail_max_length():
    # Given
    data = {"your_name": "a" * 101}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is False
    assert (
        form.errors["your_name"][0]
        == "Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 101)."
    )


def test_name_form_fail():
    # Given
    data = {"your_name": ""}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is False
