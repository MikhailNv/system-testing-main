import subprocess
import os
class FirstCheckingRules:

    def create_file(self):
        os.chdir('/home/user/')
        touch_file = ['touch', 'tfile']
        ps = subprocess.run(touch_file, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
        if ps.returncode != 0:
            return ps
        else:
            ls = subprocess.run(['ls', '-l', 'tfile'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding='utf-8')
            print(ls.stdout)
            output_file = open('tfile', 'w')
            cf = subprocess.call(['echo', '123'], stdout=output_file, stderr=subprocess.PIPE, encoding='utf-8')
            output_file.close()
            if cf == 0:
                touch_file = ['cat', 'tfile']
                ps = subprocess.run(touch_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
                if ps.stdout.split('\n')[0] == '123':
                    return True
                else:
                    return ps.stderr
            else:
                return cf.stderr

    def change_the_right(self):
        sudo_password = 'qwerty'
        p = subprocess.Popen(['sudo', '-i'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(p.stdout)
        p.communicate(sudo_password + '\n')
        touch_file = ['chmod', 'u-rw', '/home/user/tfile']
        chmod = subprocess.run(touch_file, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
        if chmod.returncode != 0:
            return chmod.stderr
        else:
            ls = subprocess.run(['ls', '-l', '/home/user/tfile'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding='utf-8')
            print(ls.stdout)

    # def rm_file(self):
    #     os.chdir('/home/user/')
    #     p = subprocess.Popen(['rm', 'tfile'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #     p.communicate('y' + '\n')
ch = FirstCheckingRules()
# print(ch.create_file())
print(ch.change_the_right())
# print(ch.change_the_right())
# print(ch.rm_file())