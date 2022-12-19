import spacy

pln = spacy.load("pt_core_news_sm")


text = pln(
    "Estou aprendendo processamento de linguagem natural")

for token in text:
    print(token.text, token.pos_)
