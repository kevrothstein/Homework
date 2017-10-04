import re

file_re = open("regex_sum.txt")
file_re = file_re.read()
number = re.findall('[0-9]+', file_re)
lst_answer = []
for kevin in number:
	kevin = int(kevin)
	lst_answer.append(kevin)
print (sum(lst_answer))