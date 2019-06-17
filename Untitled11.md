

```python
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer








```


```python
chatbot = ChatBot('Ron Obvious')
```

    [nltk_data] Downloading package wordnet to C:\Users\Rajnish
    [nltk_data]     jaiswal\AppData\Roaming\nltk_data...
    [nltk_data]   Unzipping corpora\wordnet.zip.
    [nltk_data] Downloading package stopwords to C:\Users\Rajnish
    [nltk_data]     jaiswal\AppData\Roaming\nltk_data...
    [nltk_data]   Unzipping corpora\stopwords.zip.
    [nltk_data] Downloading package averaged_perceptron_tagger to
    [nltk_data]     C:\Users\Rajnish jaiswal\AppData\Roaming\nltk_data...
    [nltk_data]   Package averaged_perceptron_tagger is already up-to-
    [nltk_data]       date!
    


```python
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
```


```python
# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
```

    C:\Users\Rajnish jaiswal\AppData\Local\Continuum\anaconda3\lib\site-packages\chatterbot\corpus.py:38: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
      return yaml.load(data_file)
    

    Training ai.yml: [####################] 100%
    Training botprofile.yml: [####################] 100%
    Training computers.yml: [####################] 100%
    Training conversations.yml: [####################] 100%
    Training emotion.yml: [####################] 100%
    Training food.yml: [####################] 100%
    Training gossip.yml: [####################] 100%
    Training greetings.yml: [####################] 100%
    Training health.yml: [####################] 100%
    Training history.yml: [####################] 100%
    Training humor.yml: [####################] 100%
    Training literature.yml: [####################] 100%
    Training money.yml: [####################] 100%
    Training movies.yml: [####################] 100%
    Training politics.yml: [####################] 100%
    Training psychology.yml: [####################] 100%
    Training science.yml: [####################] 100%
    Training sports.yml: [####################] 100%
    Training trivia.yml: [####################] 100%
    


```python
chat = ''
```


```python
while True:
    
    if chat =='Bye' or chat =='bye':
        break
    else:
        chat = str(input())
        # Get a response to an input statement
        answer = chatbot.get_response(chat)
        print('chattbot :' + str(answer))
```

    hi
    chattbot :How are you doing?
    nothing
    chattbot :Or something
    something?
    chattbot :Tell me about your self.
    i am learner
    chattbot :I bet the MET department uses them.
    no it not about that thing
    chattbot :An electronic device capable of performing calculations at very high speed and with very high accuracy.
    you are wrong
    chattbot :holden caulfield
    how about america
    chattbot :what is chemistry
    russia
    chattbot :ARE YOU A FOOTBALL
    you are idiot
    chattbot :ave you read frankenstein
    Fuck you
    chattbot :what is mind children
    just go to hell
    chattbot :That's good to hear.
    bye
    chattbot :Do you feel pain
    


```python

```
