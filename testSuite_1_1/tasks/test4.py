import subprocess
import sys
from passlib.hash import sha512_crypt
import pexpect

class CheckingRules1419:

    # Проверка прав
    def check_rights(self, user):
        child = pexpect.spawn(f"su - {user}")
        child.expect_exact("$")
        child.sendline('echo "456" >> /tmp/share')
        child.expect_exact("$")
        if 'Permission denied' not in child.before.decode().split('\r\n')[1]:
            child.sendline('cat /tmp/share')
            child.expect_exact("$")
            if child.before.decode().split('\r\n')[1].isdigit() == True:
                return True
            else:
                return False
        else:
            return False

    def add_password(self, user, password):
        child = pexpect.spawn(f"su -")
        child.expect_exact("#")
        child.sendline(f'useradd {user}')
        child.expect_exact("#")
        child.sendline(f'passwd {user}')
        child.expect_exact("password:")
        child.sendline(password)
        child.expect_exact("password:")
        child.sendline(password)
        child.expect_exact("#")
        if 'tokens updated successfully' in child.before.decode().split('\r\n')[3]:
            return True
        else:
            return child.before.decode().split('\r\n')


    # Проверка добавления пользователей и группы.
    def check_add_users_and_groups(self):
        child = pexpect.spawn(f"su -")
        child.expect_exact("#")
        if self.add_password('test1', 'q1w2e3r4') == True and self.add_password('test2', '1q2w3e4r') == True:
            child.sendline('groupadd testgroup')
            child.expect_exact("#")
            child.sendline('gpasswd -M test1 testgroup')
            child.expect_exact("#")
            child.sendline('chgrp testgroup /tmp/share')
            child.expect_exact("#")
            child.sendline('chmod g+w /tmp/share')
            child.expect_exact("#")
            child.close()
            if self.check_rights('test1') == True and self.check_rights('test2') == False:
                return True

    # Проверка смены пароля у тестового пользователя.
    def check_change_password_testuser(self, password):
        child = pexpect.spawn("su - test1")
        child.expect_exact("$")
        child.sendline("passwd test1")
        child.expect_exact("password:")
        child.sendline(password)
        i = child.expect_exact(["password:", "$"])
        if i == 1:
            error_mg = child.before.decode().split('\r\n')[1]
            if 'passwd: Authentication token manipulation error' in error_mg:
                return True
            else:
                return error_mg
        else:
            child.sendline("ivk1419!")
            child.expect_exact("password:")
            child.sendline("ivk1419!")
            child.expect_exact("$")
            print(1)
            if 'updated successfully' in child.before.decode().split('\r\n')[2]:
                return True
            else:
                return child.before.decode().split('\r\n')

    # Запрет измения собственного пароля у тестового пользователя.
    def prohibition_of_change(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline("chage -m 36500 test1")
        child.close()
        return self.check_change_password_testuser('ivk1419!')

    # Проверка изменения пароля root-пользователем.
    def check_change_passwd_with_root(self):
        child = pexpect.spawn('su -')
        child.expect_exact("#")
        child.sendline('passwd test1')
        child.expect_exact("password:")
        child.sendline('q1w2e3r4')
        child.expect_exact("password:")
        child.sendline('q1w2e3r4')
        child.expect_exact("#")
        if 'successfully' in child.before.decode().split('\r\n')[3]:
            return True
        else:
            return child.before.decode().split('\r\n')

    # Удаление созданных пользователей, файлов и группы.
    def delete_data(self):
        child = pexpect.spawn('su -')
        child.expect_exact("#")
        child.sendline('userdel -r -f test1')
        child.expect_exact("#")
        child.sendline('userdel -r -f test2')
        child.expect_exact("#")
        child.sendline('groupdel testgroup')
        child.expect_exact("#")
        child.sendline('rm /tmp/share')
        child.expect_exact("?")
        child.sendline('yes')
        child.expect_exact("#")
        child.sendline('cat /etc/passwd')
        child.expect_exact("#")
        if 'test1' not in child.before.decode().split('\r\n')[-2] and \
                'test2' not in child.before.decode().split('\r\n')[-1]:
            child.sendline('ls /tmp/')
            child.expect_exact("#")
            if 'share' not in child.before.decode().split('\r\n'):
                return True
            else:
                child.before.decode().split('\r\n')
        else:
            return False
