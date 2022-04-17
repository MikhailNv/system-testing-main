import unittest
import os, sys
import subprocess
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test3 import CheckingRules1418

cr = CheckingRules1418()

def test_view_list():
    assert (cr.view_list_of_directories() == True)

def test_file_creation():
    assert (cr.check_created_files() == True)

def test_file_copy():
    assert (cr.check_copy_file() == True)

def test_recursion_copy():
    assert (cr.check_recursion_copy() == True)

def test_move_file():
    assert (cr.check_move_file() == True)

def test_remove_file():
    assert (cr.check_remove_file() == True)

def test_remove_catalog():
    assert (cr.check_remove_catalog() == True)

def test_search_validation():
    assert (cr.search_validation() == True)