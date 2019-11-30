import spacy
from spacy_langdetect import LanguageDetector


    def languageDetection(data):
        nlp = spacy.load("en")
        nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
        doc = nlp(data)
        averageLanguage = doc._.language['language']
        nonAverageWords = []
        if(averageLanguage=="id"):
            for i, sent in enumerate(doc.sents):
                if(sent._.language!="id"):
                    nonAverageWords.append(sent)
        elif(averageLanguage=="en")
            for i, sent in enumerate(doc.sents):
                if(sent._.language!="en"):
                    nonAverageWords.append(sent)
        return data,averageLanguage,nonAverageWords