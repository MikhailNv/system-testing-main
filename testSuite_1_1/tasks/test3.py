import subprocess
import time
import os
from typing import Union


class CheckingRules1418:

    # Создание вспомогательного метода по проверке работы команды.
    def check_command(self, command, shell):
        ps = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, shell=shell, encoding='utf-8')
        if ps.returncode == 0:
            return True
        else:
            return ps.stderr

    # Просмотр содержимого каталогов с последующим созданием тестовой директории.
    def view_list_of_directories(self):
        cd = self.check_command(['cd', '/..'], True)
        if cd == True:
            os.chdir("/..")
        else:
            return cd
        ls = self.check_command(['ls'], False)
        root_dir = self.check_command(['ls', '/usr', '/tmp'], False)
        command_list = [cd, ls, root_dir]
        for command in range(len(command_list)):
            if command_list[command] != True:
                return command_list[command]
        cd_to_tmp = self.check_command(['cd', 'tmp'], True)
        if cd_to_tmp == True:
            os.chdir("/tmp/")
        else:
            return cd_to_tmp
        mkdir = self.check_command(['mkdir', 'test_1'], False)
        if mkdir == True:
            return True
        else:
            return mkdir

    # Проверка на налчиие созданных файлов.
    def check_created_files(self):
        os.chdir('/../tmp')
        cd = self.check_command(['cd', 'test_1'], True)
        if cd == True:
            os.chdir("test_1")
        cd = self.check_command(['touch', 'myfile_1'], False)
        if cd == True:
            ps = subprocess.run(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if ps.stdout.split('\n')[0] == 'myfile_1':
                return True
            else:
                return ps.stderr
        else:
            return cd

    # Проверка налчия скопированного файла.
    def check_copy_file(self):
        os.chdir('/../tmp/test_1')
        copy = self.check_command(['cp', 'myfile_1', '/tmp'], False)
        if copy == True:
            os.chdir('..')
            ls = subprocess.run(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if 'myfile_1' in ls.stdout.split('\n'):
                return True
            else:
                return ls.stderr
        else:
            return copy

    # Проверка корректности работы рекурсивного копирования.
    def check_recursion_copy(self):
        os.chdir('/../tmp')
        catalog_copy = self.check_command(['cp', '-R', 'test_1', 'test_2'], False)
        if catalog_copy == True:
            ls = subprocess.run(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if 'test_2' in ls.stdout.split('\n'):
                return True
            else:
                return ls.stderr
        else:
            return catalog_copy

    # Проверка переноса и переименования каталогов и файлов.
    def check_move_file(self):
        os.chdir('/../tmp')
        catalog_copy = self.check_command(['mv', 'myfile_1', 'myfile_2'], False)
        if catalog_copy == True:
            ls = subprocess.run(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if 'myfile_2' in ls.stdout.split('\n'):
                move_catalog = self.check_command(['mv', 'myfile_2', '/tmp/test_1'], False)
                if move_catalog == True:
                    return True
                else:
                    return move_catalog
            else:
                return ls.stderr

    # Проверка удаления файла.
    def check_remove_file(self):
        os.chdir('/../tmp/test_1')
        rm = self.check_command(['rm', 'myfile_1'], False)
        if rm == True:
            ls = subprocess.run(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if 'myfile_1' not in ls.stdout.split('\n'):
                return True
            else:
                return False
        else:
            return rm
    # Проверка удаления каталога.
    def check_remove_catalog(self):
        os.chdir('/../tmp')
        rm = self.check_command(['rm', '-R', 'test_1'], False)
        if rm == True:
            ls = subprocess.run(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if 'test_1' not in ls.stdout.split('\n'):
                return True
            else:
                return False
        else:
            return rm

    # Проверка корректности поиска файлов и каталогов.
    def search_validation(self):
        os.chdir('/../tmp/test_2')
        touch = self.check_command(['touch', 'mf1.txt', 'mf2.txt', 'mf3.dat', 'mf4.exe'], False)
        if touch == True:
            mkdir = self.check_command(['mkdir', 'mf1', 'mf2'], False)
            if mkdir == True:
                find_txt = self.check_command(['find', '.', '-name', 'mf*.txt', '-print'], False)
                find_file = self.check_command(['find', '.', '-name', 'mf*', '-type', 'd', '-print'], False)
                check_list = [find_file, find_txt]
                for find in check_list:
                    if find != True:
                        return find
                os.chdir('/../tmp/')
                self.check_command(['rm', '-R', 'test_2'], False)
                return True

            else:
                return mkdir

        else:
            return touch
