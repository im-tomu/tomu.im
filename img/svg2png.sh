#!/bin/bash
for i in *.svg; do
	o=$(basename $i .svg).png
	inkscape $i --export-png=$o --export-dpi=300
	git add $o
done
