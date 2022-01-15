import nltk

nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import wikipedia
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

lemmatizer = WordNetLemmatizer()


def lemma_sentence(sentence):
    sentence_tokens = nltk.word_tokenize(sentence.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    # iterate each word in sentence and check for word's tag (NNS / VBP / IN / other...)
    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas


def find_similarity_text_question(text_data, question_of_user):
    sentence_tokens = nltk.sent_tokenize(text_data)
    sentence_tokens.append(question_of_user)
    tv = TfidfVectorizer(tokenizer=lemma_sentence)
    tf = tv.fit_transform(sentence_tokens)
    values = cosine_similarity(tf[-1], tf)
    index = values.argsort()[0][-2]
    values_flat = values.flatten()
    values_flat.sort()

    coeff = values_flat[-2]

    if coeff > 0.3:
        return sentence_tokens[index]


def generate_bot(subject):
    text = wikipedia.page(subject).content
    while True:
        question = input(f"Hi welcome to {subject} chatbot, what do you want to know?\n")
        output = find_similarity_text_question(text, question)
        if output:
            print(output)
        elif question == 'quit':
            break
        else:
            print("I don't know. Please try again.")


# generate_bot("COVID-19")
generate_bot("Israel")

# examples - COVID-19:
# Why WHO recommend face coverings?
# Does WHO recommend self-isolation?
# what are the symptoms?
# what is the main covid variants?
# how is it diagnosed?


# examples - Israel:
# When was Israel admitted?
# When did Yizhak Rabin was assassinated?
# When did Israel join the OECD?
# What is the Temperature in Israel?
# How many major metropolitan areas israel has?
