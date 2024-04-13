
def filter_out(words, first_letter):
    return [word for word in words if word.lower().startswith(first_letter.lower())]
