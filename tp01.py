import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# cleaning
text = "Hi Tarik!\nHow are you doing today? I love Python!!!"
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)
print("After Cleaning:")
print(text)
#tokenization
tokens = word_tokenize(text)
print("\nAfter Tokenization:")
print(tokens)
#remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
print("\nAfter Removing Stopwords:")
print(filtered_tokens)