import subprocess
import time
import os
from typing import Union
from pyvirtualdisplay import Display



class GuiProgram:

    # Проверка корректности запуска программ на выполнение
    def check_running_app(self, app):
        display = Display(visible=0, size=(1366, 768))
        display.start()
        fr = subprocess.Popen([app], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
        cmd = ['ps', 'ax']
        f = open("cat.txt", 'w')
        ps = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, encoding='utf-8')
        f.close()
        if ps.returncode != 0:
            return ps.stderr
        cmd = ['grep', 'Xvfb']
        input = open("cat.txt")
        subprocess.run(cmd, stdin=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        input.close()
        cmd = ['rm', 'cat.txt']
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
        fr.terminate()
        display.stop()
        return True
