import unittest
import os, sys
import subprocess
sys.path.insert(1, os.path.join(sys.path[0], "testSuite_1_1/tasks"))
from test_gui_program import GuiProgram

cr = GuiProgram()

def test_firefox():
    assert (cr.check_running_app('firefox') == True)

def test_gimp():
    assert (cr.check_running_app('gimp') == True)

def test_vlc():
    assert (cr.check_running_app('vlc') == True)

def test_vim():
    assert (cr.check_running_app('vim') == True)
