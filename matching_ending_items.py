# https://www.hackerrank.com/challenges/matching-ending-items/problem

import re

Regex_Pattern = r'^[a-zA-Z]*s$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
