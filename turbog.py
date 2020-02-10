"""
Usage:
  turbog.py
  turbog.py (-h | --help)
  turbog.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

import os
from docopt import docopt
import url_parser


def main():
    """
    TurboGVideos Downloader

        1 for page index based downloading
        2 for searching query based downloading
        3 for specific URL downloading

        """
    if os.path.exists('./Watchlist.txt'):
        os.remove('./Watchlist.txt')
    if os.path.exists("./Openload.txt"):
        os.remove("./Openload.txt")
    if os.path.exists("./download_link.txt"):
        os.remove("./download_link.txt")
    url_parser.main()


if __name__ == "__main__":

    arguments = docopt(__doc__, version='TurboGVideos Downloader 1.0')
    # print(arguments)
    print(main.__doc__)
    main()

