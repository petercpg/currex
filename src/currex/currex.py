# coding=utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Simple currency converter.
"""

from __future__ import division, print_function

from builtins import input  # pylint: disable=redefined-builtin


def main():
    inp_curr = input("What is your desired currency? ")
    curr_rate = float(input("What is your desired rate? USD1:%s" % inp_curr))
    while True:
        inp = input("What is your desired %s amount? (Type \"q\" to quit) " % inp_curr)
        if inp == "q":
            break
        else:
            print("%s%.2f" % ("USD", float(inp) / curr_rate))


if __name__ == "__main__":
    main()
