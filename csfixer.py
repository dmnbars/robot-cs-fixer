import sys

from fixer.fixer import Fixer

if __name__ == "__main__":
    try:
        fixer = Fixer(sys.argv[1:])
        fixer.fix()
    except Exception as e:
        print(f'Error: {e}')
