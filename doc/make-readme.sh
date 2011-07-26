#!/bin/bash

set -ev

make text

awk 'BEGIN{YES=1} ! /class class/ {if (YES) print} /class class/ {YES=0}' \
	< _build/text/index.txt \
	> ../README.rst

{
	cd ..
	if [ ! -e README.txt ]; then
		ln -s README.rst README.txt
	fi
}

