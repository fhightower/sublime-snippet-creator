#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

import requests

SNIPPET_TEMPLATE = """<snippet>
    <content><![CDATA[
{}
]]></content>
    <description>{}</description>
    <scope>source.python</scope>
    <tabTrigger>{}</tabTrigger>
</snippet>"""


def _request_code(target_url):
    """Request a code file."""
    r = requests.get(target_url)
    code = r.text.encode('utf-8')

    return code


def _find_functions(code):
    """Find functions from the code."""
    # find non-private functions and the first line of their doc-string
    function_pattern = '(@.*\n)?.*def ([^_].*)\((.*)\):\n.*?"""(.*)'

    # find and return all of the functions
    functions = re.findall(function_pattern, code)
    return functions


def main(args):
    """Create sublime text snippets automatically from code."""
    CLASS_PREFIX = args['<class_prefix>']

    # define the prefix used when saving a new snippet and for the snippet's tab trigger
    if args['--snippet_prefix']:
        SNIPPET_PREFIX = args['--snippet_prefix']
    else:
        SNIPPET_PREFIX = CLASS_PREFIX

    # if we are pulling the code from a location on the internet (e.g. a raw file on github), get the code
    if args['<target_file>'].startswith("http"):
        code = _request_code(args['<target_file>'])
    else:
        with open(args['<target_file>'], 'r') as f:
            code = f.read().encode('utf-8')

    # find all of the functions in the code
    functions = _find_functions(code)

    # create a snippet for each function (as appropriate)
    for function in functions:
        # remove the newline from the end of the decorator
        decorator = function[0].strip()

        # handle a property decorator
        if decorator == "@property":
            pass
        # handle functions
        else:
            # split up the arguments for the function
            arguments = function[2].split(", ")
            # remove 'self' as an argument to the function (just move on if 'self' isn't an argument)
            try:
                arguments.remove('self')
            except ValueError as e:
                pass

            # create a string with the arguments to the function formatted for a sublime text snippet
            argument_string = ""
            count = 0

            for argument in arguments:
                count += 1
                argument_string += "${"
                argument_string += "{}:{}".format(count, argument)
                argument_string += "}"

                # if there are more arguments, add a trailing comma
                if count < len(arguments):
                    argument_string += ", "

            # create a name for the snippet based on the name of the function
            snippet_name = SNIPPET_PREFIX + function[1].replace("_", "")
            # create a description for the snippet based on the function's doc string
            snippet_description = function[3].replace('"""', '')

            # create the snippet's code for static methods
            if decorator == "@staticmethod":
                # create snippet code without the class prefix in front of it
                snippet_code = function[1] + "(" + argument_string + ")"
            # create the snippet's code for non-static methods
            else:
                # create snippet code (with the class prefix in front of it)
                snippet_code = CLASS_PREFIX + "." + function[1] + "(" + argument_string + ")"

            # create a snippet
            new_snippet = SNIPPET_TEMPLATE.format(snippet_code, snippet_description, snippet_name)

            # write the new snippet
            with open(args['<output_directory>'] + '/{}.sublime-snippet'.format(snippet_name), 'w') as f:
                f.write(new_snippet)


if __name__ == '__main__':
    main()
