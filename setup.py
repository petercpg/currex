# coding=utf-8
# pylint: disable=missing-docstring
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from setuptools import setup

if __name__ == "__main__":
    setup(name="currex",
          version="0.0.1",
          entry_points={
              "console_scripts": ["currex = currex.currex:main"]
          },
          package_dir={"": "src"},
          install_requires=[
              "future>=0.16.0",
          ],
          zip_safe=False)
