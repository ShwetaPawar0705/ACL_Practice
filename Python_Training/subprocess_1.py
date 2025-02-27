import subprocess

# p1 = subprocess.run('ls -la', shell=True)

# print(p1.returncode)

# p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)

# print(p1.stdout)

with open('output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)
