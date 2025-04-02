from nltk import word_tokenize


def get_features(text):
    features = {}
    word_list = [word for word in word_tokenize(text.lower())]
    for word in word_list:
        features[word] = True
    return features


# all_features = [(get_features(email), label) for (email, label) in all_emails]

print(get_features("Participate in Put New Lottery NOW!"))
