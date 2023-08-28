import pytest
from app.ohce_kata import ohce_kata

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

    
