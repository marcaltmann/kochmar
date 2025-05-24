import codecs
import os
import random

import nltk
from nltk import word_tokenize

nltk.download("punkt")


def tokenize(input: str) -> list[str]:
    return word_tokenize(input)


def get_features(text: str) -> dict:
    features = {}
    word_list = word_tokenize(text.lower())
    for word in word_list:
        features[word] = True
    return features


def read_text_files(directory: str) -> list[str]:
    files = os.listdir(directory)
    text_list = []
    for filename in files:
        if not filename.startswith("."):
            f = codecs.open(
                directory + filename, "r", encoding="ISO-8859-1", errors="ignore"
            )
            text_list.append(f.read())
            f.close()

    return text_list


def read_and_sort():
    spam_list = read_text_files("enron1/spam/")
    ham_list = read_text_files("enron1/ham/")
    all_emails = [(email_content, "spam") for email_content in spam_list]
    all_emails += [(email_content, "ham") for email_content in ham_list]

    random.seed(42)
    random.shuffle(all_emails)
    print(f"Dataset size = {len(all_emails)} emails")

    all_features = [(get_features(email), label) for (email, label) in all_emails]
    print(get_features("Participate in lottery now!"))
    print(all_features[0])

if __name__ == "__main__":
    read_and_sort()
