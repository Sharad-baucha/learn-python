from profanity_filter import ProfanityFilter

pf = ProfanityFilter()
print(pf.censor("You've stolen my money, you bastard!"))

# Censor individual words
print(pf.censor_word('lesbian'))