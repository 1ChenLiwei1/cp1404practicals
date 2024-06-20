"""
 Word Occurrences
 Estimate: 30 minutes
 Actual:   41 minutes
 """
word_counts = {}
text = input("TEX: ")
for word in text.split():
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
sorted_words = sorted(word_counts.items())
max_word = max(len(word)for word in word_counts)
for word, count in sorted_words:
    print(f"{word:{max_word}} : {count}")

