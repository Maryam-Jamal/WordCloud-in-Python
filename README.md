# WordCloud-in-Python
This Python program generates a visually appealing word cloud using text from the book "Alice in Wonderland" and a custom image mask. The word cloud highlights the most frequently used words in the text while excluding common stopwords to ensure meaningful content. The design and color scheme of the word cloud are customized to match an image of Alice from "Alice in Wonderland," creating a thematic visual representation.

1. **Libraries Used:**
   - `wordcloud`: To create the word cloud.
   - `ImageColorGenerator`: To match the word cloud's colors to the input image.
   - `STOPWORDS`: To filter out common words.
   - `numpy`: To handle image arrays.
   - `pandas`: For data manipulation (though not used directly in this code).
   - `PIL (Python Imaging Library)`: To open and manipulate the image.
   - `matplotlib`: To display the generated word cloud.

2. **Text Input:**
   - The text is read from a file named `Alice.txt`, which contains the entire content of "Alice in Wonderland." This text is the source from which the most common words are extracted.

3. **Stopwords:**
   - A set of stopwords is created to remove common words that do not add significant meaning, such as "the," "and," and "said." The word "said" is explicitly added to this set to be excluded from the word cloud.

4. **Image Mask:**
   - An image file named `Alice.png` is loaded and converted into a NumPy array to be used as a mask. The word cloud will take the shape of this image.

5. **Word Cloud Configuration:**
   - The `WordCloud` class is used to create a word cloud object with the following settings:
     - `background_color='white'`: Sets the background color to white.
     - `max_words=50`: Limits the word cloud to display the top 50 words.
     - `mask=alice_image`: Uses the Alice image mask to shape the word cloud.
     - `stopwords=stopwords`: Applies the defined stopwords to filter out common words.
     - `max_font_size=40`: Sets the maximum font size of words in the cloud.
     - `contour_width=1`: Adds a slight contour around the words.

6. **Color Customization:**
   - The `ImageColorGenerator` is used to recolor the word cloud to match the color scheme of the Alice image.

7. **Visualization:**
   - `matplotlib.pyplot` is used to display the generated word cloud. The figure is set to a size of 10x5 inches, and the word cloud is displayed without axis labels for a cleaner look.

**How to Run:**

1. Ensure you have the necessary libraries installed (`wordcloud`, `numpy`, `PIL`, `matplotlib`).
2. Place the `Alice.txt` text file and `Alice.png` image file in the specified paths or update the paths in the code to match the locations of these files on your system.
3. Run the script to generate and display the word cloud.

This program is a creative way to visualize text data, offering insights into the most frequently used words in a given text, while also producing visually engaging graphics.
<img width="724" alt="wordcloud" src="https://github.com/user-attachments/assets/3ae70d8e-4f3f-430c-9c7d-b87c3f411d1a">

