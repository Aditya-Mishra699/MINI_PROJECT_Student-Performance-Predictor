# count lines and words in text file

with open("data.txt", "r") as f:
    lines = f.readlines()

line_count = len(lines)

word_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)

print("Lines:", line_count)
print("Words:", word_count)