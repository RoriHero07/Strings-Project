
letter = ("q","w","e","r","t","y","u","i","o","p",
          "a","s","d","f","g","h","j","k","l",
          "z","x","c","v","b","n","m")

unique_words = {}
# """Letter Frequency"""
# for i in letter:
#     letter_frequency= a.count(i)
#     print(i, ":", letter_frequency)
"""In a function"""
def textanalyzer():
    for i in letter:
        letter_frequency = p.count(i)
        print(i, ":", letter_frequency)


    words = paragraph.split()
    for word in words:
        if word not in unique_words:
            unique_words[word] =  1
        else:
            unique_words[word] = unique_words[word] + 1
    print(unique_words)
    for i in unique_words:
        word_frequency= words.count(i)
        print(i, ":", word_frequency)

lines = []
print("Type in a Paragraph")
while True:
    line = input()
    if line == "end":
        break
    lines.append(line)


paragraph = " ".join(lines)

p = paragraph.lower()
textanalyzer()
