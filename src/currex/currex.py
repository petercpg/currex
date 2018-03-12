# coding=utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Simple currency converter.
"""

from __future__ import division, print_function

import sys

from builtins import input  # pylint: disable=redefined-builtin


def curr_convert(curr, rate):
    inp = input("What is your desired %s amount? (Type \"q\" to quit) " % curr)
    if inp == "q":
        sys.exit(0)
    else:
        out = "%s%.2f" % ("USD", float(inp) / rate)
    return out


def main():
    inp_curr = input("What is your desired currency? ")
    curr_rate = float(input("What is your desired rate? USD1:%s" % inp_curr))
    while True:
        print(curr_convert(inp_curr, curr_rate))


if __name__ == "__main__":
    main()
