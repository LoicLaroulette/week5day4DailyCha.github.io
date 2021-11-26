class Text:
    def __init__(self, text):
        self.text = text
    
    def freq(self, word):
        if self.text.split(' ').count(word) > 0:
            return self.text.split(' ').count(word)
        else: 
            return None
    
    @classmethod
    def from_file(cls, text_file):
        with open(text_file) as f:
            lines = f.readlines()
            lines = [line.replace("\n", "") for line in lines]
            return Text("".join(lines))
    
    def common(self):
        text_set = list(set(self.text.split(" ")))
        highest = text_set[0]
        for word in text_set:
            if self.text.split(" ").count(word) > self.text.split(" ").count(highest):
                highest = word
        return highest
    
    def unique_words(self):
        return list(set(self.text.split(" ")))


from string import punctuation
from nltk.corpus import stopwords

class TextModification(Text):
    
    def __init__(self, text):
        super().__init__(text)
    
    def de_punctuation(self):
        return "".join([char for char in self.text if punctuation.count(char) == 0])
    
    def de_stopwords(self):
        return " ".join([word for word in self.text.split(" ") if stopwords.words('english').count(word) == 0])


book = Text.from_file('the_stranger.txt')
txt = book.text

#the_freq = book.freq('The')
#common_most = book.common()

txt_modified = TextModification(book.text)

print(txt_modified.de_stopwords())


book = Text.from_file('the_stranger.txt')
txt = book.text
the_freq = book.freq('The')

common_most = book.common()
