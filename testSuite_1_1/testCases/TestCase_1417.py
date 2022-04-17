import unittest
import os, sys
import subprocess
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test2 import CheckingRules1417

cr = CheckingRules1417()

def test_create_file():
    assert (cr.create_file() == "Файл создан")

def test_buffer():
    check_buffer_100 = cr.check_buffer('100K')
    check_buffer_1 = cr.check_buffer('1G')
    assert (check_buffer_100[0] == "Создание буфера выполнено корректно")
    assert (check_buffer_1[0] == "Создание буфера выполнено корректно")
    assert (check_buffer_100[1] != check_buffer_1[1])

def test_delete_file():
    assert (cr.delete_access_file() == 0)
