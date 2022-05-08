from subprocess import Popen
import subprocess
import logging


logger = logging.getLogger(__name__)

# Run a command line command and returns stdout


def _run(command):
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, text=True)
    return result.stdout


def _runRemove(command):
    proc = Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    yes_proc = Popen(["yes"], stdout=proc.stdin, text=True)
    proc_output = proc.communicate()[0]
    yes_proc.wait()


def list(repo):

    packageString = _run(["pacman", repo])
    packageList = packageString.splitlines()
    

    packageNamesWithIndex = []
    for names in packageList:
        index = packageList.index(names) + 1
        packageNamesWithIndex.append(str(index) + " -> " + names.strip())
    return packageNamesWithIndex


def remove(package):

    result = _runRemove(["pkexec", "pacman", "-R", package.split("->")[1].strip()])
    print(result)
