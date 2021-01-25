import csv


def get_ngrams_from_csv(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        ngrams = {ngram: expanded_form for ngram, expanded_form in csvreader}

    return ngrams
