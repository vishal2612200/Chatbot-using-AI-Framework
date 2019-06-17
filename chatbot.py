#!/usr/bin/env python
# coding: utf-8

# In[17]:


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer








# In[18]:


chatbot = ChatBot('Ron Obvious')


# In[21]:


# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)


# In[22]:


# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")


# In[29]:


chat = ''


# In[32]:


while True:
    
    if chat =='Bye' or chat =='bye':
        break
    else:
        chat = str(input())
        # Get a response to an input statement
        answer = chatbot.get_response(chat)
        print('chattbot :' + str(answer))


# In[ ]:




