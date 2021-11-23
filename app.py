import subprocess

command = "11\n"
i = "1\n"*11
payload = ""
command += i + payload

proc = subprocess.Popen(['./a.out'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

proc.stdin.write(bytes(command, 'utf-8'))
stdout, stderr = proc.communicate()


print(stderr)