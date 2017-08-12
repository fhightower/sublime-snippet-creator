# -*- coding: utf-8 -*-
"""Sublime Snippet Creator.

Usage:
  sublime_snippet_creator <target_file> <output_directory> <class_prefix> [--snippet_prefix=<snippet_prefix>]
  sublime_snippet_creator (-h | --help)
  sublime_snippet_creator --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --snippet_prefix=<snippet_prefix>  The prefix used for each snippet file and its tab trigger (default is the class_prefix)
"""

from docopt import docopt

from .__init__ import __version__ as VERSION
import sublime_snippet_creator


def main(args=None):
    """Console script for sublime_snippet_creator"""
    arguments = docopt(__doc__, version=VERSION)
    sublime_snippet_creator.main(arguments)


if __name__ == "__main__":
    main()
