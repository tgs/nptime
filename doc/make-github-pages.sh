#!/bin/bash


set -euv
make singlehtml

rm -rf _build/gh-pages
git clone git@github.com:tgs/nptime.git _build/gh-pages

cd _build/gh-pages
git checkout -t -b gh-pages origin/gh-pages

rm -rf *
cp -r ../singlehtml/* .
git add -A
git commit -m "auto-update site"

set +v

echo
echo "**************************"
echo "     YOU'RE NOT DONE      "
echo "**************************"
echo 
echo "now run:"
echo
echo "cd `pwd`; git push origin gh-pages; cd -"
echo

