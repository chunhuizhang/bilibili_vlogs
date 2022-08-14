
import subprocess
from subprocess import Popen, PIPE

# cmd = 'sleep 2'

cmd = 'df -h'

p = Popen(cmd.split(' '),
          # shell=True,
          # stdout=subprocess.DEVNULL,
          stdout=PIPE,
          universal_newlines=True
          )


p.wait()
out = p.communicate()
print('out: {}'.format(out))

if p.returncode == 0:
    print('{} success'.format(cmd))
else:
    print('{} failed'.format(cmd))

