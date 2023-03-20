import subprocess


def run_server(port: int):
    data = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True)
    if data.returncode == 1:
        subprocess.run(['python3', 'test_server.py'])
    else:
        code = data.stdout.decode().split('\n')[1].split()[1]
        subprocess.run(['kill', code])
    subprocess.run(['python3', 'test_server.py'])


if __name__ == "__main__":
    run_server(5000)