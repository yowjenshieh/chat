
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: #mac不需要encoding
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	allen_wordcount = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_wordcount = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_wordcount += len(m) 
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_wordcount += len(m)
	print(f"Allen typed {allen_wordcount} words and sent {allen_sticker_count} sticker(s) and {allen_image_count} image(s)")
	print(f"Viki typed {viki_wordcount} words and sent {viki_sticker_count} sticker(s) and {viki_image_count} image(s)")
#		print(s)

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output1.txt', lines)

main()