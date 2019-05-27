"""
GenQRCode.py - Generate QR Codes with qrcode library.
"""

import logging
import logging.config
from logging import getLogger, debug, error
from pathlib import Path
from typing import Any, Union, Optional

import qrcode
import yaml  # from PyYAML library

__author__ = 'Travis Risner'
__project__ = "play_qrcode"
__creation_date__ = "05/27/2019"
# Copyright 2019 by Travis Risner - MIT License

log = None


class GenQRCodeClass:
    """
    GenQRCodeClass - Generate QR Codes with qrcode library.
    """

    def __init__(self):
        pass

    def run_get_qr_code(self):
        """
        Top method for running Generate QR Codes with qrcode library..

        :return:
        """
        # Generate png QR code images of 40 sizes
        for box in range(10,51, 10):
            for ver in range(1, 11):

                qr = qrcode.QRCode(
                    version=ver,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4
                )
                qr.add_data(
                    f'Size {ver} in box {box} of a very long message that '
                    f'hopefully will be fully added into the QR code')
                qr.make(fit=True)

                img = qr.make_image(fill_color='black', back_color='white')
                filename = f'qrcode{ver:02}{box}.png'
                print(f'Saving to {filename}')
                with open(filename, mode='wb') as img_file:
                   img.save(img_file)
        return

class Main:
    """
    Main class to start things rolling.
    """

    def __init__(self):
        """
        Get things started.
        """
        self.GenQRCode = None
        return

    def run_GenQRCode(self):
        """
        Prepare to run Generate QR Codes with qrcode library..

        :return:
        """
        self.GenQRCode = GenQRCodeClass()
        debug('Starting up GenQRCode')
        self.GenQRCode.run_get_qr_code()
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
    main.run_GenQRCode()

# EOF
