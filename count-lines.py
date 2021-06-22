import sys

"""Adding some documentation here for demonstration purposes"""

count = 0

for line in sys.stdin:
    count += 1

print(count, 'lines in standard input')
