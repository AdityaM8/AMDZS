#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[3]:


nltk.download("popular")


# In[4]:


paragraph = """ Son Goku is a fictional character and main protagonist of the Dragon Ball manga series created by Akira Toriyama. He is based on Sun Wukong (known as Son Goku in Japan and Monkey King in the West), a main character in the classic Chinese novel Journey to the West (16th century), combined with influences from the Hong Kong martial arts films of Jackie Chan and Bruce Lee. Goku first made his debut in the first Dragon Ball chapter, Bulma and Son Goku, originally published in Japan's Weekly Shōnen Jump magazine on December 3, 1984. Born Kakarot, Goku is introduced as an eccentric, monkey-tailed boy who practices martial arts and possesses superhuman strength. He meets Bulma and joins her on a journey to find the magical seven Dragon Balls that can grant the user one wish. Along the way, he finds new friends who follow him on his journey to become a stronger fighter. As Goku grows up, he becomes the Earth's mightiest warrior and battles a wide variety of villains with the help of his friends and family, while also gaining new allies in the process. """


# In[5]:


sentences = nltk.sent_tokenize(paragraph)


# In[6]:


print(sentences, end=" ")


# In[7]:


words = nltk.word_tokenize(paragraph)


# In[8]:


print(words)


# In[ ]:




