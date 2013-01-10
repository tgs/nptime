#!/bin/bash
# Generate a README.rst file in the root directory of the project.

# The README is generated using Sphinx, from the documentation included inline in nptime.py.
# The class and method level documentation isn't included in the README.

set -ev

make text

awk 'BEGIN{YES=1} ! /class class/ {if (YES) print} /class class/ {YES=0}' \
	< _build/text/index.txt \
	> ../README.rst

