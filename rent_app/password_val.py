def isupper(password):
    return any([x for x in password if x.isupper()])

def islower(password):
    return any([x for x in password if x.islower()])

def isdigit(password):
    return any([x for x in password if x.isdigit()])

def isspecial(password):
    return any([x for x in password if x in """!@#$%^&*(){}:"|?></.,\|"""])

def check_password(password):
     validateors = [isupper, islower, isdigit, isspecial]
     for validator in validateors:
         if not validator(password):
             return False
     return True


def test_check_correct_password():
    assert check_password("Aa1")

def test_no_big_letter():
    assert not check_password("a1")

def test_no_low_letter():
    assert not check_password("A1")

def test_no_digit():
    assert not check_password("Aa")
