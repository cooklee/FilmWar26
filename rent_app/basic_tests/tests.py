from datetime import datetime


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 1 else "female"
    month = int(pesel[2:4])
    skip = month // 20
    month %= skip * 20
    centry = {
        20: "20",
        40: "21",
        60: "22",
        80: '18',
        0: '19'
    }
    year = int(centry[skip*20] + pesel[:2])
    birth_date = datetime(year, month, int(pesel[4:6]))
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result


pesels = """
94080593293
73072337372
85050362676
"""
pesels = pesels.split()
pesels_invalid = """
95080593293
74072337372
86050362676
"""
pesels_invalid = pesels_invalid.split()


def test_check_if_valid():
    for pesel in pesels:
        assert analyze_pesel(pesel)['valid']


def test_check_if_invalid():
    for pesel in pesels_invalid:
        assert not analyze_pesel(pesel)['valid']


def test_check_if_men():
    for pesel in pesels:
        assert analyze_pesel(pesel)['gender'] == 'male'


def test_check_if_women():
    f_pessels = """
    83120877927
    96062521627
    67061985246""".split()
    for pesel in f_pessels:
        assert analyze_pesel(pesel)['gender'] == 'female'


def test_pesle_coerrct():
    f_pessels = """
    83120877927
    96062521627
    67061985246""".split()
    for pesel in f_pessels:
        assert analyze_pesel(pesel)['pesel'] == pesel


def test_data_1900_2000():
    pesels = (("83120877927", datetime(1983, 12, 8)),
              ("96062521627", datetime(1996, 6, 25)),
              ("67061985246", datetime(1967, 6, 19)))
    for pesel in pesels:
        assert analyze_pesel(pesel[0])['birth_date'] == pesel[1]


def test_data_2000_2100():
    pesels = (("83320877927", datetime(2083, 12, 8)),
              ("96262521627", datetime(2096, 6, 25)),
              ("67261985246", datetime(2067, 6, 19)))
    for pesel in pesels:
        assert analyze_pesel(pesel[0])['birth_date'] == pesel[1]
