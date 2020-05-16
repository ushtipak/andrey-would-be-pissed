import logging
from sys import stdout

from numpy.random import choice as rnd


def yield_pairs(_words):
    for i in range(len(_words) - 1):
        yield _words[i], _words[i + 1]


def train(_words, _last):
    _field = {}
    logging.warning("_last: %s", _last)

    for w1, w2 in _words:
        if w1 in _field.keys():
            _field[w1].append(w2)
        else:
            _field[w1] = [w2]

    longest_key = None
    max_length = 0
    for k, v in _field.items():
        if len(v) > max_length:
            max_length = len(v)
            longest_key = k

    logging.debug("longest_key: %s", longest_key)
    _field[_last] = [longest_key]

    return _field


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', stream=stdout, level=logging.DEBUG)

    pattern = "C6Q R/0.16666666666666607 G5T. R/0.036458333333333925 EB5I R/0.040104166666667496 G5/0.203125 " \
              "R/0.04843749999999858 C5/0.5833333333333334 RH C6Q R/0.16666666666666607 G5T. R/0.036458333333333925 " \
              "EB5I R/0.040104166666667496 G5/0.203125 R/0.04843749999999858 C5/0.5833333333333334 RH BB5Q " \
              "R/0.16666666666666607 A5T. R/0.036458333333333925 G5I R/0.040104166666667496 A5/0.203125 " \
              "R/0.04843749999999858 D5/0.5833333333333334 R/0.5078125 A5/0.1234375 R/0.02083333333333215 " \
              "G5/0.0484375 R/0.0442708333333357 F5/0.12083333333333333 R/0.0390625 C5/0.4817708333333333 " \
              "R/0.11093749999999858 A5/0.140625 R/0.014062500000001421 G5/0.052083333333333336 " \
              "R/0.04322916666666643 F5/0.11197916666666667 R/0.02708333333333357 C5/0.45208333333333334 " \
              "R/0.16145833333333215"
    pattern = pattern.replace("/", "-")
    logging.debug("pattern: %s", pattern)

    words = pattern.split()
    logging.debug("words: %s", words)

    pairs = yield_pairs(words)
    logging.debug("pairs: %s", pairs)

    field = train(pairs, words[-1])
    logging.debug("field: %s", field)

    chain = [rnd(words)]
    for _ in range(80):
        chain.append(rnd(field[chain[-1]]))
    logging.debug("chain: %s", chain)

    result = ' '.join(chain).replace("-", "/")
    logging.info("result: %s", result)
