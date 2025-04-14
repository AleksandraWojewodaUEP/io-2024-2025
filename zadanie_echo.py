import string

def echo(text):
    text = text.strip()

    if text and text[-1] in string.punctuation:
        text = text[:-1]
    last_word = text.split()[-1]

    return f"{last_word.upper()} {last_word.capitalize()} {last_word.lower()}"

# Testy
assert echo("Lubię placki!") == "PLACKI Placki placki"
assert echo("Linux śmierdzi.") == "ŚMIERDZI Śmierdzi śmierdzi"
assert echo("Mentzen na prezydenta") == "PREZYDENTA Prezydenta prezydenta"
assert echo("Po co aż 5 testów") == "TESTÓW Testów testów"
assert echo("Mam dość.") == "DOŚĆ Dość dość"
