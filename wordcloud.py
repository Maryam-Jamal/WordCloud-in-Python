from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

text = open('C:/Users/test/Downloads/Alice.txt').read()

stopwords = set(STOPWORDS)
stopwords.add("said")
alice_image = np.array(Image.open('C:/Users/test/Downloads/Alice.png'))

wc = WordCloud(
    background_color='white',
    max_words=50,
    mask=alice_image,
    stopwords=stopwords,
    max_font_size=40,
    contour_width = 1
)


wc.generate_from_text(text)
image_colors = ImageColorGenerator(alice_image)
wc.recolor(color_func=image_colors)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
