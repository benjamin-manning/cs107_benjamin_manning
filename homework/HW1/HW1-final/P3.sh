#!/bin/bash
grep "[0-9]" apollo13.txt | wc -l > apollo_out.txt
grep --help | grep -- --count
ls -l | grep -c "\.py$"
ls -lR | grep "^\-......\-\-." | wc -l
ls -l | grep "^\-*d*.......\-\-." | wc -l
