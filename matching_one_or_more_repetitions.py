# https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem

import re

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
