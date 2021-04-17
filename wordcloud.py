from collections import Counter
import wordcloud
from matplotlib import pyplot as plt

f = open(r'The_Left_Hand_of_Darkness.txt', encoding='utf-8')
file_contents = f.read()


def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~—’'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just", "on", "in", "for", "so",
                           "there", "not", "us", "then", "up", "out", "one", "would", "down", "like", "said", "could",
                           "about", "went", "came", "go", "than", "into", "off", "now", "first", "only", "over", "well",
                           "must", "come", "got", "see", "still", "after", "get", "back", "even", "through", "most",
                           "much", "though", "made", "other", "yet", "while", "last", "before", "never", "between",
                           "left", "another", "might", "dont", "should", "these"]


    for character in file_contents:
        if character in punctuations:
            file_contents = file_contents.replace(character, "")

    words_tmp = file_contents.split()
    words = [word.lower() for word in words_tmp]
    words = [word for word in words if word not in uninteresting_words]
    frequencies = dict(Counter(words))

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.figure(figsize=(10, 5))
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()