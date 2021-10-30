import streamlit as st
from mtranslate import translate
import pyautogui
import stanza
import pandas as pd
import os
import codecs
from nltk.tokenize import sent_tokenize
import ast

t1,t2 = st.columns(2)

with t1:
    st.title('Multilingual NLP App')
with t2:
    st.markdown("\n" + 'https://stanfordnlp.github.io/stanza/' + "\n\n\n" + '**Pretrained neural models supporting 66 (human) languages**')

clear = st.button("CLEAR")

# read dataset
df = pd.read_excel(os.path.join('data', 'stanza_supported_languages.xlsx'),sheet_name='langtable')
# read language column
language = df["Language"].to_list()
# read stanza language 2-letter code column
nlplangcode = df["nlp_langid"].to_list()
# read mtranslate language 2-letter code column
langcode = df["transid"].to_list()

# map(create dict) Language with stanza language 2-letter code and mtranslate language 2-letter code
trans_langid = {language[i]: langcode[i] for i in range(len(langcode))}
nlp_langid = {language[i]: nlplangcode[i] for i in range(len(nlplangcode))}
# map(create dict) nlp language 2-letter code to actual Language
lang_word = {nlplangcode[i]: language[i] for i in range(len(language))}

def Clear():
    pyautogui.press("tab", interval=0.15)
    pyautogui.hotkey("ctrl", "a",'del', interval=0.15)
    pyautogui.press("tab", interval=0.15)

def Tokenize(langid,sentstr):
    nlp = stanza.Pipeline(lang=langid, processors='tokenize')
    doc = nlp(sentstr)
    f = codecs.open("out.txt","w",encoding="utf-8")
    for i, sentence in enumerate(doc.sentences):
        f.write(f'====== Sentence {i+1} tokens =======\n')
        for token in sentence.tokens:
            f.write(str(token.id) + '\t\t' + token.text + '\n')
    f.close()
    o = open("out.txt", "r",encoding="utf-8").read()
    return o

def Mwt(langid,sentstr):
    nlp = stanza.Pipeline(lang=langid, processors='tokenize,mwt')
    doc = nlp(sentstr)
    f = codecs.open("out.txt", "w", encoding="utf-8")
    for token in doc.sentences[0].tokens:
        f.write(f'token: {token.text}\twords: {", ".join([word.text for word in token.words])}' + "\n")
    f.close()
    o = open("out.txt", "r",encoding="utf-8").read()
    return o

def Parts_Of_Speech(langid,sentstr):
    nlp = stanza.Pipeline(lang=langid, processors='tokenize,mwt,pos')
    doc = nlp(sentstr)
    f = codecs.open("out.txt", "w", encoding="utf-8")
    for sent in doc.sentences:
        for word in sent.words:
            s = f'word: {word.text}\t\t' + f'upos: {word.upos}\t\t' \
            + f'xpos: {word.xpos}\t\t' + f'feats: {word.feats if word.feats else "_"}' + "\n"
            f.write(s)
    f.close()
    o = open("out.txt", "r",encoding="utf-8").read()
    return o

def Limitz(langid,sentstr):
    nlp = stanza.Pipeline(lang=langid, processors='tokenize,mwt,pos,lemma')
    doc = nlp(sentstr)
    f = codecs.open("out.txt", "w", encoding="utf-8")
    # print(*[f'word: {word.text + " "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
    for sent in doc.sentences:
        for word in sent.words:
            s = f'word: {word.text + " "}\t\t\t\t' + f'lemma: {word.lemma}' + "\n"
            f.write(s)
    f.close()
    o = open("out.txt", "r", encoding="utf-8").read()
    return o

def Syntactic_Dependency_Information(langid,sentstr):
    nlp = stanza.Pipeline(lang=langid, processors='tokenize,mwt,pos,lemma,depparse')
    doc = nlp(sentstr)
    f = codecs.open("out.txt", "w", encoding="utf-8")
    for sent in doc.sentences:
        for word in sent.words:
            s = f'id: {word.id}\t' + f'word: {word.text}\t' + f'head id: {word.head}\t' + f'head: {sent.words[word.head - 1].text if word.head > 0 else "root"}\t' + f'deprel: {word.deprel}' + "\n\n"
            f.write(s)
    f.close()
    o = open("out.txt", "r", encoding="utf-8").read()
    return o

def Named_Entity_Recognition(langid,sentstr):
    nlp = stanza.Pipeline(lang=langid, processors='tokenize,ner')
    doc = nlp(sentstr)
    f = codecs.open("out.txt", "w", encoding="utf-8")
    for sent in doc.sentences:
        for token in sent.tokens:
            s = f'token: {token.text}\tner: {token.ner}' + '\n'
            f.write(s)
    f.close()
    o = open("out.txt", "r", encoding="utf-8").read()
    return o


def Sentiment_Analysis(langid,sentstr):
    nlp = stanza.Pipeline(lang=langid, processors='tokenize,sentiment')
    doc = nlp(sentstr)
    f = codecs.open("out.txt", "w", encoding="utf-8")
    l = sent_tokenize(sentstr)
    for i, sentence in enumerate(doc.sentences):
        if sentence.sentiment == 0:res = "Negative Sentiment : "
        if sentence.sentiment == 1: res = "Neutral Sentiment"
        if sentence.sentiment == 2: res = "Positive Sentiment"
        f.write(res + str(l[i-0] + "\n"))
    f.close()
    o = open("out.txt", "r", encoding="utf-8").read()
    return o


def Language_Detection(sample_list):
    from stanza.models.common.doc import Document
    from stanza.pipeline.core import Pipeline
    nlp = Pipeline(lang="multilingual", processors="langid")
    # convert string list to list
    docs = ast.literal_eval(sample_list)
    f = codecs.open("out.txt", "w", encoding="utf-8")
    docs = [Document([], text=text) for text in docs]
    nlp(docs)
    f.write("\n\n".join(f"{doc.text}\t" + lang_word[doc.lang] for doc in docs))
    f.close()
    o = open("out.txt", "r", encoding="utf-8").read()
    return o


# LHS panel layout
translation_option = st.sidebar.radio('TRANSLATION',('OFF','ON'))
selected_lang = st.sidebar.radio("SELECT LANGUAGE", language)
nlp_function = st.sidebar.radio("SELECT NLP FUNCTION", ('Tokenization and Sentence Segmentation','Multi Word Tokenization','Part of Speech',
                                                        'Lemmatization','Dependency Parsing',
                                                         'Named Entity Recognition','Sentiment Analysis',
                                                        'Language Detection'))

# RHS panel layout
c1,c2 = st.columns(2)

with c1:
    inputtext = st.text_area("INPUT TEXT", height=100)
with c2:
    # translate selected text based on selected language
    if len(inputtext) > 0:
        if translation_option == 'ON':
            translation = translate(inputtext, trans_langid[selected_lang])
            st.text_area("TRANSLATED TEXT",translation, height=100)

# get nlp language 2-letter id based on selected language
nlp_languageid = nlp_langid[selected_lang]

# calling out NLP functions
if nlp_function == 'Tokenization and Sentence Segmentation' and translation_option == 'ON' and len(inputtext) > 0:
    try:
        output = str(Tokenize(nlp_languageid, translation))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)
elif nlp_function == 'Tokenization and Sentence Segmentation' and len(inputtext) > 0:
    try:
        output = str(Tokenize(nlp_languageid, inputtext))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)

if nlp_function == 'Multi Word Tokenization' and translation_option == 'ON' and len(inputtext) > 0:
    try:
        output = str(Mwt(nlp_languageid, translation))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)
elif nlp_function == 'Multi Word Tokenization' and len(inputtext) > 0:
    try:
        output = str(Mwt(nlp_languageid, inputtext))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)

if nlp_function == 'Part of Speech' and translation_option == 'ON' and len(inputtext) > 0:
    try:
        output = str(Parts_Of_Speech(nlp_languageid, translation))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)
elif nlp_function == 'Part of Speech' and len(inputtext) > 0:
    try:
        output = str(Parts_Of_Speech(nlp_languageid, inputtext))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)

if nlp_function == 'Lemmatization' and translation_option == 'ON' and len(inputtext) > 0:
    try:
        output = str(Limitz(nlp_languageid, translation))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)
elif nlp_function == 'Lemmatization' and len(inputtext) > 0:
    try:
        output = str(Limitz(nlp_languageid, inputtext))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)

if nlp_function == 'Dependency Parsing' and translation_option == 'ON' and len(inputtext) > 0:
    try:
        output = str(Syntactic_Dependency_Information(nlp_languageid, translation))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)
elif nlp_function == 'Dependency Parsing' and len(inputtext) > 0:
    try:
        output = str(Syntactic_Dependency_Information(nlp_languageid, inputtext))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)

if nlp_function == 'Named Entity Recognition' and translation_option == 'ON' and len(inputtext) > 0:
    try:
        output = str(Named_Entity_Recognition(nlp_languageid, translation))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)
elif nlp_function == 'Named Entity Recognition' and len(inputtext) > 0:
    try:
        output = str(Named_Entity_Recognition(nlp_languageid, inputtext))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)

if nlp_function == 'Sentiment Analysis' and translation_option == 'ON' and len(inputtext) > 0:
    try:
        output = str(Sentiment_Analysis(nlp_languageid, translation))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)
elif nlp_function == 'Sentiment Analysis' and len(inputtext) > 0:
    try:
        output = str(Sentiment_Analysis(nlp_languageid, inputtext))
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)

if nlp_function == 'Language Detection' and len(inputtext) > 0:
    try:
        output = Language_Detection(inputtext)
        st.text_area("NLP Output",output,height=1200)
    except Exception as e:
        st.error(e)

# Clear I/O
if clear:
    Clear()