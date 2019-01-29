import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

file = 'results/results.csv'

df = pd.read_csv(file, names=["name", "company", "valid_from", "valid_to", "description"], encoding="ISO-8859-1")
df = df.drop_duplicates(subset=None, keep='first', inplace=False)

word_string = list(df["name"])
word_string = ''.join(word_string)

mask = np.array(Image.open("utils/background.png"))
image_colors = ImageColorGenerator(mask)

wordcloud = WordCloud(stopwords=STOPWORDS,
                      mask=mask,
                      background_color='white',
                      width=1200,
                      height=1000
                      ).generate(word_string)

plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
plt.show()
