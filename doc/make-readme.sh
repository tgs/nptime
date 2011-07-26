#!/bin/bash

set -ev

make text

awk 'BEGIN{YES=1} ! /class class/ {if (YES) print} /class class/ {YES=0}' \
	< _build/text/index.txt \
	> ../README.rst


