import unittest
import os, sys
import subprocess
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test4 import CheckingRules1419

cr = CheckingRules1419()

def test_add():
    assert (cr.check_add_users_and_groups() == True)

def test_change_password_testuser():
    assert (cr.check_change_password_testuser('q1w2e3r4') == True)

def test_prohibition_of_change():
    assert (cr.prohibition_of_change() == True)

def test_check_change_passwd_with_root():
    assert (cr.check_change_passwd_with_root() == True)

def test_delete_data():
    assert (cr.delete_data() == True)
