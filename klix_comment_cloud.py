import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

url = 'https://www.klix.ba/vijesti/bih/odraz-palestine-i-izraela-u-bih-izmedju-zastave-i-inat-politike/210514049/komentari'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
res = soup.find_all('div', class_="mb-3 text-base break-words")
list_of_inner_text = [x.text for x in res]
# If you want to print the text as a comma separated string
raw_text = ', '.join(list_of_inner_text)

text=' '.join(word for word in raw_text.split() if len(word)>3)

# Generate word cloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)

# Plot
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
