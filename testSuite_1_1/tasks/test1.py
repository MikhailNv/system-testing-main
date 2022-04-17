#!/usr/bin/env python3
import subprocess
from get_nic import getnic
import time

class CheckingRules1416:
    # Создание конструктора класса для поиска всех доступных сетевых интерфейсов.
    def __init__(self):
        self.get_int = getnic.interfaces()

    # Проверка на наличие интерфейса, взаимодействующего с сетевым драйвером и уровнем IP.
    def check_working_interface(self):
        cmd = ['ip', 'r', 'g', '1.1.1.1']
        ps = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        if ps.returncode == 0:
            python_processes = ps.stdout.split('\n')
            process_list = python_processes[0].split()
            net_interface = [word for word in process_list if 'e' in word or 'w' in word][1]
            self.get_int = [i for i in self.get_int if i == net_interface]
            return ["Интерфейс определен", net_interface]
        else:
            return [ps.stderr]

    # Проверка статистики прерываний на запущенном интерфейсе
    def check_interrupts(self, net):
        cmd = ['cat', '/proc/interrupts']
        f = open("cat.txt", "w")
        ps = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, encoding='utf-8')
        f.close()
        if ps.returncode == 0:
            cmd = ['grep', f'{net}']
            input = open("cat.txt")
            grep = subprocess.run(cmd, stdin=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            input.close()
            cmd = ['rm', 'cat.txt']
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
            if grep.returncode == 0:
                python_processes = grep.stdout.split('\n')
                if len(python_processes[0]) > 1:
                    return True
                else:
                    return False
            else:
                return grep.stderr
        else:
            return ps.stderr
    
    # Проверка корректности отключения работающего интерфейса
    def check_interface_is_down(self):
        if len(self.get_int) == 1 and 'lo' in self.get_int:
            return self.get_int[0]
        else:
            cmd = ['ifconfig', f'{self.get_int[0]}', 'down']
            ps = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if ps.returncode == 0:
                return True
            else:
                return ps.stderr

    # Проверка корректности включения нужного интерфейса
    def check_interface_is_up(self):
        cmd = ['ifconfig', f'{self.get_int[0]}', 'up']
        ps = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        if ps.returncode == 0:
            time.sleep(3)
            cmd = ['ip', 'r', 'g', '1.1.1.1']
            ps = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            if ps.returncode == 0:
                return True
            else:
                return ps.stderr
        else:
            return ps.stderr

    # Проверка получения номера прерывания на запущенном интерфейсе
    def get_interrupts(self):
        try:
            cat = self.check_working_interface()[1]
        except IndexError:
            cat = self.check_working_interface()
        cmd = ['cat', '/proc/interrupts']
        f = open("cat.txt", 'w')
        ps = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, encoding='utf-8')
        f.close()
        if ps.returncode != 0:
            return ps.stderr
        cmd = ['grep', f'{cat}']
        input = open("cat.txt")
        grep = subprocess.run(cmd, stdin=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding='utf-8')
        input.close()
        cmd = ['rm', 'cat.txt']
        cf = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
        if grep.returncode != 0:
            return grep.stderr
        if cf.returncode == 0:
            python_processes = grep.stdout.split('\n')
            return int(python_processes[0][:4].lstrip().split(':')[0])
        else:
            return cf.stderr
