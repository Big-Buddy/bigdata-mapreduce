import subprocess

def test_count():
    command="python3 ./answers/count.py ./data/frenepublicinjection2016.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read()=="27244\n")
