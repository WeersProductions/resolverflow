# Preprocessing

def text_preprocess():
    text = None
    # e.g. to lowercase
    return text


# Features

def text_length():
    text = None
    return len(text)

def has_bold():
    return False

def has_italic():
    return False

def has_underline():
    return False

def has_headers():
    return False

def has_rules():
    return False

def has_strike():
    return False

def has_bulletlists():
    return False

def has_numlists():
    return False

def has_links():
    return False

def has_greetings():
    return False

''' Mentions 'example', 'foo', 'bar', 'hello world', 'Alice', 'Bob'.
    But this might be mentioned in other ways that do not signify a user-given
    example. E.g. such keyword could be provided by default in someone's dataset. '''
def has_examples():
    return False

def ratio_newlines():
    return 0.0

def ratio_code():
    return 0.0

''' Number of edits. Also interesting could be ratio of edits in a timeframe.
    Or treat it as a timeseries. '''
def no_edits():
    return 0


# More advanced stuff

''' Measure of quality of spelling and/or grammar. '''
def ratio_typos():
    return 0.0

''' Take an existing NLP measure for readability. It can be very simple, using
    the average sentence length or word length. '''
def text_understandability():
    return 0.0 