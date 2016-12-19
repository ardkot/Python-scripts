# om Python script uit te voeren, ga naar map, maakt bestandje eindigend op .py, rechtermuisknop Git Bash Here en type command: python ####.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_wordcloud(text, title):

    wc = WordCloud().generate(text)

    plt.figure(figsize=(18, 14))
    plt.imshow(wc)

    plt.savefig(title+".png")

if __name__ == "__main__":

    create_wordcloud("Test text met woorden")
