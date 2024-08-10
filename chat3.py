
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f: #terminal: must use 'utf-8-sig' instead of 'utf-8'
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)