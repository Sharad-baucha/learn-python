import spacy
from profanity_filter import ProfanityFilter

pf = ProfanityFilter()

pf.censor("That's bullshit!")
# "That's ********!"