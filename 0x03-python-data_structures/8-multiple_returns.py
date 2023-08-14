#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        sentence_len = len(sentence)
        if not sentence:
            sentence = None
    else:
        sentence_len = 0
    return (sentence_len(sentence), if not sentence else sentence[:0])
