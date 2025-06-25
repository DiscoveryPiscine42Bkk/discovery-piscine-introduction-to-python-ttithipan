import re
import sys
pattern_for_scan, input_string = sys.argv[1], sys.argv[2] # After the script name, we expect two arguments: the pattern and the input string
print(len(re.findall(pattern_for_scan, input_string)))

