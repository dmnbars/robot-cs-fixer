from csfixer_conf import config
from fixer.fixer import Fixer

if __name__ == "__main__":
    try:
        fixer = Fixer(config)
        fixer.fix()
    except Exception as e:
        print(f'Error: {e}')
