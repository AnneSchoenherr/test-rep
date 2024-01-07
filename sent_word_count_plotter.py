import matplotlib.pyplot as plt
import re

data = 'chap_2.txt' #choose *.txt-file to open and read
file = open(data, encoding="utf8").read()
sentences = re.split(r'[.!?]',file)
print(type(file), type(sentences))

sent_word = {} # create a dictionary with the sentence number as key and the number of words as value
count = 0
for sent in sentences:
    if len(sent.split()) == 0: #exclude empty sentences
        continue
    else:
        count +=1
        sent_word[count] = len(sent.split())

def plot_word_per_sentence(dictionary):
    # this function asks user for a title and plots the number of words per sentence as a bar diagramm
    title = input("Enter a title for your diagram: ")
    plt.figure(figsize=(15, 8))
    plt.bar(dictionary.keys(), dictionary.values(), color='blue')
    plt.xlabel(f'Sentence No \n(total number of sentences in {data}: {len(sent_word)})')
    plt.ylabel(f'Count of words \n(max. number of words in a sentence in {data}: {max(sent_word.values())}')
    plt.title(title)
    plt.show()

plot_word_per_sentence(sent_word)

#Conclusion and summary: gets the values needed for summary, the user will be asked a summary should be generated (see line 68)
largest_sentence = max(sent_word.items(), key=lambda x: x[1])
shortest_sentence = min(sent_word.items(), key=lambda x: x[1])
avg_words_sentence = round(sum(sent_word.values())/ len(sent_word),2)

def get_readability(number):
    #this function evaluates if the article is easy or difficult to read, based on the average number of words per sentence
    if number < 9:
        readability = "This article contains in the average max. 8 words per sentence, so it is quite easy to read!"
    elif number >= 9 and number < 16:
        readability = "This article contains in the average 9 to 15 words per sentence, so it is not so easy to read!"
    elif number >= 16 and number < 30:
        readability = "This article contains in the average 16 to 29 words per sentence, so it is difficult to read!"
    if number >= 30:
        readability = "This article contains in the avarage at least 30 words per sentence,\nso it is very, very difficult to read!"
    return readability

summary = ("\n"f"Summary for '{data}':\n"
          "\n"
          f"The *.txt-file '{data}' contains {len(sent_word)} sentences and in total {sum(sent_word.values())} words.\n"
          f"The longest sentence in '{data}' is sentence no.{largest_sentence[0]}: It contains {largest_sentence[1]} words.\n"
          f"The shortest sentence in '{data}' is sentence no.{shortest_sentence[0]}: It contains {shortest_sentence[1]} words.\n"
          f"In the average a sentence in *.txt-file '{data}' contains {avg_words_sentence} words.\n\n"
          f"{get_readability(avg_words_sentence)}")

def plot_sent_statistics():
    # this function creates a boxplot diagram showing average number of words, shortest and last sentence and prints the summary
    # for the article on besides. In creating this plot ChatGPT was very helpful ;-)))
    data_coll = [(len(sent_word), avg_words_sentence), shortest_sentence, largest_sentence]
    fig, (ax0, ax1) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 2]}, figsize=(15, 7))
    boxplot = ax0.boxplot(data_coll) # Plot boxplot on the left side
    ax0.set_xlabel(['   1 = Sentence Length & Average Words per Sentence', '2 = Shortest Sentence', '3 = Largest Sentence'])
    ax0.set_ylabel('Number of words in sentences')
    ax0.set_title('Boxplot of Sentence Statistics')
    ax1.text(0.1, 0.5, summary, va='center', fontsize=12)
    ax1.axis('off')  # Hide axis on the right side
    plt.show()

final_question = input(f"Do you wish to print and plot a summary for {data}? If yes, enter 'y' or 'yes'. If not, enter any. ")
if final_question == 'y' or final_question == 'yes':
    plot_sent_statistics()
    print(summary)
else:
    print("Thank you for using Sentence-Word-Counter. The code finishes now. Have a nice Day :-)!")
