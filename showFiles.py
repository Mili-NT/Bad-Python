#!/usr/bin/python3
import os
import sys
[print(f'Links loaded: {list({len(x):(("cat ", x), "n") for x in [[x for x in [x for x in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), x))] if x.lower().startswith(sys.argv[1].lower())]]})[0]}'), [os.system(f'{(({len(x):(("cat ", x), "n") for x in [[x for x in [x for x in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), x))] if x.lower().startswith(sys.argv[1].lower())]]}[list({len(x):(("cat ", x), "n") for x in [[x for x in [x for x in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), x))] if x.lower().startswith(sys.argv[1].lower())]]})[0]])[0])[0]}{x}' + ' && echo %s' % (({len(x):(("cat ", x), "\n") for x in [[x for x in [x for x in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), x))] if x.lower().startswith(sys.argv[1].lower())]]}[list({len(x):(("cat ", x), "n") for x in [[x for x in [x for x in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), x))] if x.lower().startswith(sys.argv[1].lower())]]})[0]])[1])) for x in (({len(x):(("cat ", x), "n") for x in [[x for x in [x for x in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), x))] if x.lower().startswith(sys.argv[1].lower())]]}[list({len(x):(("cat ", x), "n") for x in [[x for x in [x for x in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), x))] if x.lower().startswith(sys.argv[1].lower())]]})[0]])[0])[1]]] if __name__ == "__main__" and (1 < len(sys.argv) < 3) else print(f"Usage: {sys.argv[0]} <starting characters of file>")

"""
Function: prints all files starting with the string passed as sys.arg[1], and prints a newline
Original: https://github.com/Mili-NT/BinBot/blob/master/utils/showLinks
"""
