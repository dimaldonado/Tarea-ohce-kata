import pytest
from app.ohce_kata import ohce_kata
from app.ohce_kata import ohce_kata_palindromo


def test_hora_noche():
    assert ohce_kata(20)=="¡Buenas noches!"
    assert ohce_kata(21)=="¡Buenas noches!"
    assert ohce_kata(22)=="¡Buenas noches!"
    assert ohce_kata(23)=="¡Buenas noches!"
    assert ohce_kata(1)=="¡Buenas noches!"
    assert ohce_kata(2)=="¡Buenas noches!"
    assert ohce_kata(3)=="¡Buenas noches!"
    assert ohce_kata(4)=="¡Buenas noches!"
    assert ohce_kata(5)=="¡Buenas noches!"

    
def test_hora_manana():
    assert ohce_kata(6)=="¡Buenos dias!"
    assert ohce_kata(7)=="¡Buenos dias!"
    assert ohce_kata(8)=="¡Buenos dias!"
    assert ohce_kata(9)=="¡Buenos dias!"
    assert ohce_kata(10)=="¡Buenos dias!"
    assert ohce_kata(11)=="¡Buenos dias!"

def test_hora_tade():
    assert ohce_kata(12)=="¡Buenas tardes!"
    assert ohce_kata(13)=="¡Buenas tardes!"
    assert ohce_kata(14)=="¡Buenas tardes!"
    assert ohce_kata(15)=="¡Buenas tardes!"
    assert ohce_kata(16)=="¡Buenas tardes!"
    assert ohce_kata(17)=="¡Buenas tardes!"
    assert ohce_kata(18)=="¡Buenas tardes!"
    assert ohce_kata(19)=="¡Buenas tardes!"

def test_palindromo():
    assert ohce_kata_palindromo("hola")=="aloh"
    assert ohce_kata_palindromo("oto")=="¡Bonita palabra!"