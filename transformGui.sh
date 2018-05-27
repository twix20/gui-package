#!/bin/sh
rm -rf GUI/*.py

for file in GUI/*.ui; do
	echo ${file::-3}
	pyuic5 $file -o ${file::-3}UI.py
done

touch GUI/__init__.py