import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')


number_list={
  "0": "zero","1": "one","2": "two","3": "three","4": "four","5": "five","6": "six","7": "seven","8": "eight","9": "nine","10": "ten"
}
def normalizing(txts):
    txt = txts.lower()
    clean = ""
    for c in txt:
        if c.isalnum() or c == " ":
            clean += c
        else:
            clean += " "
    tokans = clean.split()
    result = []
    for mot in tokans:
        if mot in number_list:
            result.append(number_list[mot])
        else:
            result.append(mot)
    stop_words = set(stopwords.words('english'))
    tokan = [word for word in result if word not in stop_words]
    return tokan
    

def run(text):
 result = normalizing(text)
 print("resultat: \n")
 print("\t",result)

run("Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza.")