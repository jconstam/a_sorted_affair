#!/bin/bash

SIZE=$1

python3 a_sorted_affair.py -s ${SIZE} -d random all
python3 a_sorted_affair.py -s ${SIZE} -d reverse all
python3 a_sorted_affair.py -s ${SIZE} -d saw4 all
python3 a_sorted_affair.py -s ${SIZE} -d saw8 all
python3 a_sorted_affair.py -s ${SIZE} -d saw4rev all
python3 a_sorted_affair.py -s ${SIZE} -d saw8rev all
python3 a_sorted_affair.py -s ${SIZE} -d sin all
python3 a_sorted_affair.py -s ${SIZE} -d sin2 all
python3 a_sorted_affair.py -s ${SIZE} -d sin4 all