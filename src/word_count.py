import sys

def word_count_dict(filename):
  word_count = {}  # Map each word to its count
  input_file = open(filename, 'r')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      # Special case if we're seeing this word for the first time.
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close()  # Not strictly required, but good form.
  return word_count


def get_count(word_count_tuple):
  return word_count_tuple[1]


def print_top(filename):
  word_count = word_count_dict(filename)
  items = sorted(word_count.items(), key=get_count, reverse=True)

  # Print the first 10
  index = 0
  for sl in range(10):
	if index == len(items):
		break
	fr = items[index][1]
	temp = index
	for item in items[temp:]:
		if item[1] < fr:
			break
		print item[0], item[1]
		index = index + 1
	
def main():
  if len(sys.argv) != 2:
    print 'usage: ./word_count.py file'
    sys.exit(1)

  filename = sys.argv[1]
  print_top(filename)

if __name__ == '__main__':
  main()
