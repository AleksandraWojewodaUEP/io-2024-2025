# Inżynieria Oprogramowania

Ulubiony serial:
- Silo



### Zadanie 1 - Silo - zrobione

Twoim zadaniem jest obliczenie liczby piętrem do przejścia. 

Dane wejściowe: piętro startowe, piętro końcowe

Przykład: `15, 166`

Dane wyjściowe: ciąg znaków (string)

Przykład: `151 w dół`

Funkcja nazywać się ma: `oblicz_pietra`

Kod do uzupełnienia:
```python
def oblicz_pietra(pietro_startowe, pietro_koncowe):
    pass

```

### Zadanie 2 - W pustyni i w puszczy

Twoim zadaniem jest wysłanie wiadomości ratunkowej, którą Stanisław Tarkowski 
wysyłał za pomocą latawców zrobionych z płuc ryb.

Aby obsłużyć proces szerzej, jako dane wejściowe przyjmij imię i nazwisko (`name_lastname`), 
i kierunek ucieczki (`direction`).

Funkcja `wyslij_latawca()` powinna znajdować się w pliku `main.py` i zwracać (`return`)
w postaci ciągu znaków.

Dane wejściowe: str, str

Przykład: `Jan Kowalski`, `północ`

Dane wyjściowe: str

Przykład: `Nazywam sie Jan Kowalski, zmierzam na północ`

Kod do uzupełnienia:
```python
def wyslij_latawca(name_lastname, direction):
    pass

```


### Zadanie 3 - Echo

Twoim zadaniem jest napisanie funkcji oraz testów (5 typu assert), które przyjmują dane wejściowe tekst i powtarzają 
3 razy osoatnie słowo, przy czym ostatnie słowo ma być dużymi, średnimi i małymi. W najstepującym schemacie:

`Lubię placki!` --> `PLACKI Placki placki`

Funkcja ma się nazywać `echo()` i znajdować się na branchu `main`.
