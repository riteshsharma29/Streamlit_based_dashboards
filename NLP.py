import streamlit as st
import pyautogui
import nltk
from autocorrect import Speller
from gensim.summarization import summarize as g_sumn

clear = st.button("CLEAR")

inputtext = st.text_area("Input",height=200)

def nlp(text,operation):
    if operation == 'Lower Case':
       return text.lower()
    if operation == 'Sent Tokenize':
        sent_tokenize = nltk.sent_tokenize(text)
        result = {
        # remove str() if you want the output as list
        "result": str(sent_tokenize)
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Word Tokenize':
        word_tokenize = nltk.word_tokenize(text)
        result = {
            "result": str(word_tokenize)  # remove str() if you want the output as list
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Lemmatize':
        from nltk.stem import WordNetLemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()

        word_tokens = nltk.word_tokenize(text)
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in
                           word_tokens]
        result = {
            "result": " ".join(lemmatized_word)
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Stemming':
        from nltk.stem import WordNetLemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()

        word_tokens = nltk.word_tokenize(text)
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in
                           word_tokens]
        result = {
            "result": " ".join(lemmatized_word)
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Remove Numbers':
        remove_num = ''.join(c for c in text if not c.isdigit())
        result = {
            "result": remove_num
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Remove Punctuation':
        from string import punctuation
        def strip_punctuation(s):
            return ''.join(c for c in s if c not in punctuation)

        text = strip_punctuation(text)
        result = {
            "result": text
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Spell Check':
        spell = Speller(lang='en')
        spells = [spell(w) for w in (nltk.word_tokenize(text))]
        result = {
            "result": " ".join(spells)
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Remove Stopwords':
        from nltk.corpus import stopwords
        stopword = stopwords.words('english')
        word_tokens = nltk.word_tokenize(text)
        removing_stopwords = [word for word in word_tokens if word not in stopword]
        result = {
            "result": " ".join(removing_stopwords)
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Keyword':
        word = nltk.word_tokenize(text)
        pos_tag = nltk.pos_tag(word)
        chunk = nltk.ne_chunk(pos_tag)
        NE = [" ".join(w for w, t in ele) for ele in chunk if isinstance(ele, nltk.Tree)]
        result = {
            "result": NE
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result'][0]
        return res
    if operation == 'Summarize':
        sent = nltk.sent_tokenize(text)
        if len(sent) < 2:
            summary1 = "please pass more than 3 sentences to summarize the text"
        else:
            summary = g_sumn(text)
            summ = nltk.sent_tokenize(summary)
            summary1 = (" ".join(summ[:2]))
        result = {
            "result": summary1
        }
        result = {str(key): value for key, value in result.items()}
        res = result['result']
        return res
    if operation == 'Remove Tags':
        import re
        cleaned_text = re.sub('<[^<]+?>', '', text)
        result = {
            "result": cleaned_text
        }
        result = {str(key): value for key, value in result.items()}
        res = re.sub(' +', ' ', result['result'])
        return res

def Clear():
    pyautogui.press("tab", interval=0.15)
    pyautogui.hotkey("ctrl", "a",'del', interval=0.15)
    pyautogui.press("tab", interval=0.15)

choice = st.sidebar.radio("SELECT NLP FUNCTION", ('Lower Case','Lemmatize','Summarize','Stemming',
                                    'Keyword','Spell Check','Remove Tags',
                                    'Sent Tokenize','Word Tokenize',
                                    'Remove Punctuation','Remove Numbers',
                                    'Remove Stopwords'))

if choice == 'Lower Case' and len(inputtext) > 0 :
    output = nlp(inputtext,'Lower Case')
    st.text_area("Output",output,height=200)
elif choice == 'Lemmatize' and len(inputtext) > 0:
    output = nlp(inputtext,'Lemmatize')
    st.text_area("Output", output, height=200)
elif choice == 'Summarize' and len(inputtext) > 0:
    output = nlp(inputtext,'Summarize')
    st.text_area("Output",output,height=200)
elif choice == 'Stemming' and len(inputtext) > 0:
    output = nlp(inputtext,'Stemming')
    st.text_area("Output",output,height=200)
elif choice == 'Keyword' and len(inputtext) > 0:
    output = nlp(inputtext,'Keyword')
    st.text_area("Output",output,height=200)
elif choice == 'Spell Check' and len(inputtext) > 0:
    output = nlp(inputtext,'Spell Check')
    st.text_area("Output",output,height=200)
elif choice == 'Remove Tags' and len(inputtext) > 0:
    output = nlp(inputtext,'Remove Tags')
    st.text_area("Output",output,height=200)
elif choice == 'Sent Tokenize' and len(inputtext) > 0:
    output = nlp(inputtext,'Sent Tokenize')
    st.text_area("Output",output,height=200)
elif choice == 'Word Tokenize' and len(inputtext) > 0:
    output = nlp(inputtext,'Word Tokenize')
    st.text_area("Output",output,height=200)
elif choice == 'Remove Numbers' and len(inputtext) > 0:
    output = nlp(inputtext,'Remove Numbers')
    st.text_area("Output",output,height=200)
elif choice == 'Remove Punctuation' and len(inputtext) > 0:
    output = nlp(inputtext,'Remove Punctuation')
    st.text_area("Output",output,height=200)
elif choice == 'Remove Stopwords' and len(inputtext) > 0:
    output = nlp(inputtext,'Remove Stopwords')
    st.text_area("Output",output,height=200)

# Clear I/O
if clear:
    Clear()
