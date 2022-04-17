import subprocess


class CheckingRules1417:

    # Проверка корректности создания файла.
    def create_file(self):
        find_created_file = ['find', 'access.log']
        ps = subprocess.run(find_created_file, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
        if ps.returncode == 0:
            return "Файл создан"
        else:
            cmd = ['dd', 'if=/dev/zero', 'of=access.log', 'bs=1M', 'count=1']
            cf = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
            if cf.returncode == 0:
                return "Файл создан"
            else:
                return cf.stderr
    
    # Проверка вывода информации в файла и создания буфера различного размера.
    def check_buffer(self, size):
        cmd = ['strace', '-f', '-y', '-P', 'access.log', 'stdbuf', f'-i{size}', 'cut', '-f1']
        input = open('access.log')
        cf = subprocess.run(cmd, stdin=input, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
        if cf.returncode == 0:
            input.close()
            return ["Создание буфера выполнено корректно", len(cf.stderr.split('\n'))]
        else:
            var = cf.stderr
            return var

    # Удаление файла.
    def delete_access_file(self):
        cmd = ['rm', 'access.log']
        cf = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
        return cf.returncode
