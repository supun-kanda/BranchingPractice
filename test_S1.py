from S1 import A, B

def test_A():
    a = A(1,'a')

    assert a.number == 1
    assert a.string == 'a'

def test_B():
    b = B(1)

    assert b.number == 1

    b.string = 'a'

    assert b.string == 'a'
