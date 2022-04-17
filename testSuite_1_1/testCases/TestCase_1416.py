import unittest
import os, sys
import time
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test1 import CheckingRules1416

cr = CheckingRules1416()

# Проверка на определение интерфейса
def test_ip_link():
    assert (cr.check_working_interface()[0] == "Интерфейс определен")

# Проверка статистики прерываний на запущенном интерфейсе
def test_cat():
    cat = cr.check_interrupts(cr.check_working_interface()[1])
    assert (cat == True)

def test_down():
    assert (cr.check_interface_is_down() == True)

def test_is_up():
    assert (cr.check_interface_is_up() == True)

def test_interrupts():
    assert (type(cr.get_interrupts()) == int)
