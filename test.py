import pytest
from app.ohce_kata import ohce_kata_hora
from app.ohce_kata import ohce_kata_palindromo
from app.ohce_kata import ohce_kata_stop

def test_hora_noche():
    assert ohce_kata_hora(20)=="¡Buenas noches!"
    assert ohce_kata_hora(21)=="¡Buenas noches!"
    assert ohce_kata_hora(22)=="¡Buenas noches!"
    assert ohce_kata_hora(23)=="¡Buenas noches!"
    assert ohce_kata_hora(1)=="¡Buenas noches!"
    assert ohce_kata_hora(2)=="¡Buenas noches!"
    assert ohce_kata_hora(3)=="¡Buenas noches!"
    assert ohce_kata_hora(4)=="¡Buenas noches!"
    assert ohce_kata_hora(5)=="¡Buenas noches!"

    
def test_hora_manana():
    assert ohce_kata_hora(6)=="¡Buenos dias!"
    assert ohce_kata_hora(7)=="¡Buenos dias!"
    assert ohce_kata_hora(8)=="¡Buenos dias!"
    assert ohce_kata_hora(9)=="¡Buenos dias!"
    assert ohce_kata_hora(10)=="¡Buenos dias!"
    assert ohce_kata_hora(11)=="¡Buenos dias!"

def test_hora_tade():
    assert ohce_kata_hora(12)=="¡Buenas tardes!"
    assert ohce_kata_hora(13)=="¡Buenas tardes!"
    assert ohce_kata_hora(14)=="¡Buenas tardes!"
    assert ohce_kata_hora(15)=="¡Buenas tardes!"
    assert ohce_kata_hora(16)=="¡Buenas tardes!"
    assert ohce_kata_hora(17)=="¡Buenas tardes!"
    assert ohce_kata_hora(18)=="¡Buenas tardes!"
    assert ohce_kata_hora(19)=="¡Buenas tardes!"

def test_palindromo():
    assert ohce_kata_palindromo("hola")=="aloh"
    assert ohce_kata_palindromo("oto")=="¡Bonita palabra!"
    assert ohce_kata_palindromo("radar") == "¡Bonita palabra!"
    assert ohce_kata_palindromo("python") == "nohtyp"
    assert ohce_kata_palindromo("reconocer") == "¡Bonita palabra!"
    assert ohce_kata_palindromo("hola") == "aloh"
    assert ohce_kata_palindromo("12321") == "¡Bonita palabra!"

def test_stop():
    assert ohce_kata_stop("Stop!")==True
    assert ohce_kata_stop("Stop!")==False