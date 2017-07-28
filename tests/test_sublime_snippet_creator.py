#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sublime_snippet_creator
----------------------------------

Tests for `sublime_snippet_creator` module.
"""

import docopt
import pytest

from sublime_snippet_creator import cli
from sublime_snippet_creator import sublime_snippet_creator


@pytest.fixture
def command_line_args():
    """Function to simulate command line arguments using docopt."""
    args = dict()

    # TODO: Add command line arguments here (see: https://github.com/docopt/docopt#api)

    return args


def test_command_line_interface(command_line_args):
    """Test the command line usage of this project."""
    # TODO: Add more robust testing here
    with pytest.raises(docopt.DocoptExit) as exc_info:
        cli.main()

    # get the error message
    error_message = exc_info.value
    # make sure the error message contains the expected usage output
    assert "Usage:" in str(error_message)

# TODO: Add more robust tests here (1)
