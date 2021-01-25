# Words from n-grams
#### Generate words/acronyms from given ngrams

## Setup

### Installation

Use [poetry](https://github.com/sdispater/poetry) to install Python dependencies:

    poetry install

### Prepare Input

Create a CSV file named `ngrams.csv` containing one ngram per line. The first column should be the ngram and the second column should be the expanded form (for developing acronyms).

Here is an example `ngrams.csv`:
```
B,Broadcast
ER,Emergency Response
AM,America's Missing
```

## Usage

Run `poetry run python words.py` to generate possible 2-6 letter words from the given n-grams:

```
AMBER
```
