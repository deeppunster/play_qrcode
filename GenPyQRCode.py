"""
GenPyQRCode.py - Generate QR codes using pyqrcode.
"""

import logging
import logging.config
from logging import getLogger, debug, error
from pathlib import Path
from typing import Any, Union, Optional

import pyqrcode
import yaml  # from PyYAML library

__author__ = 'Travis Risner'
__project__ = "play_qrcode"
__creation_date__ = "05/27/2019"
# Copyright 2019 by Travis Risner - MIT License

log = None


class GenPyQRCodeClass:
    """
    GenPyQRCodeClass - Generate QR codes using pyqrcode.
    """

    def __init__(self):
        pass

    def run_gen_pyqrcode(self):
        """
        Top method for running Generate QR codes using pyqrcode..

        :return:
        """
        # Generate png QR code images of various scales.
        for scale in range(1, 21):
            msg = (
                f'Scale {scale} of a very long message that hopefully '
                f'will be fully added into the QR code'
            )
            label_file_name = f'pyqrcode{scale:02}.svg'
            print(f'Saving to {label_file_name}')
            qr = pyqrcode.create(msg)
            qr.svg(label_file_name, scale=scale)
        return


class Main:
    """
    Main class to start things rolling.
    """

    def __init__(self):
        """
        Get things started.
        """
        self.PyQRCode = None
        return

    def run_PyQRCode(self):
        """
        Prepare to run Generate QR codes using pyqrcode..

        :return:
        """
        self.PyQRCode = GenPyQRCodeClass()
        debug('Starting up PyQRCode')
        self.PyQRCode.run_gen_pyqrcode()
        return

    @staticmethod
    def start_logging(work_dir: Path, debug_name: str):
        """
        Establish the logging for all the other scripts.

        :param work_dir:
        :param debug_name:
        :return: (nothing)
        """

        # Set flag that no logging has been established
        logging_started = False

        # find our working directory and possible logging input file
        _workdir = work_dir
        _logfilename = debug_name

        # obtain the full path to the log information
        _debugConfig = _workdir / _logfilename

        # verify that the file exists before trying to open it
        if Path.exists(_debugConfig):
            try:
                #  get the logging params from yaml file and instantiate a log
                with open(_logfilename, 'r') as _logdictfd:
                    _logdict = yaml.load(_logdictfd, Loader=yaml.SafeLoader)
                logging.config.dictConfig(_logdict)
                logging_started = True
            except Exception as xcp:
                print(f'The file {_debugConfig} exists, but does not contain '
                      f'appropriate logging directives.')
                raise ValueError('Invalid logging directives.')
        else:
            print(f'Logging directives file {_debugConfig} either not '
                  f'specified or not found')

        if not logging_started:
            # set up minimal logging
            _logfilename = 'debuginfo.txt'
            _debugConfig = _workdir / _logfilename
            logging.basicConfig(filename='debuginfo.txt', level=logging.INFO,
                                filemode='w')
            print(f'Minimal logging established to {_debugConfig}')

        # start logging
        global log
        log = logging.getLogger(__name__)
        logging.info(f'Logging started: working directory is {_workdir}')
        return


if __name__ == "__main__":
    workdir = Path.cwd()
    debug_file_name = 'debug_info.yaml'
    main = Main()
    main.start_logging(workdir, debug_file_name)
    main.run_PyQRCode()

# EOF
