import sys

import physiofit4galaxy.ui.cli

def main():
    """The main routine"""

    if len(sys.argv) > 1:
        physiofit4galaxy.ui.cli.main()
    else:
        return "To launch the GUI, please use the original Physiofit package " \
               "and not PhysioFit4Galaxy"

if __name__ == "__main__":
    sys.exit(main())