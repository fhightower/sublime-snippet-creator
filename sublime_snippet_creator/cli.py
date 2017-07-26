# -*- coding: utf-8 -*-
"""Sublime Snippet Creator.

Usage:
  # TODO: Add usage instructions here
  sublime_snippet_creator.py ship new <name>...
  sublime_snippet_creator.py ship <name> move <x> <y> [--speed=<kn>]
  sublime_snippet_creator.py ship shoot <x> <y>
  sublime_snippet_creator.py mine (set|remove) <x> <y> [--moored | --drifting]
  sublime_snippet_creator.py (-h | --help)
  sublime_snippet_creator.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  # TODO: Add options here
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""

from docopt import docopt

from .__init__ import __version__ as VERSION


def main(args=None):
    """Console script for sublime_snippet_creator"""
    arguments = docopt(__doc__, version=VERSION)
    print(arguments)
    print("You can modify the output of the CLI by making changes to sublime_snippet_creator.cli.main .")


if __name__ == "__main__":
    main()