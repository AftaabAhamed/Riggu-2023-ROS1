import subprocess,os

proc = subprocess.Popen('echo "ibase=16; `wmctrl -l | grep -i rviz | cut -c 3-11 | tr a-z A-Z`" | bc',
                    env=os.environ,
                    stdout=subprocess.PIPE,
                    universal_newlines=True,
                    shell=True)


out = proc.communicate()[0]
print(out)

