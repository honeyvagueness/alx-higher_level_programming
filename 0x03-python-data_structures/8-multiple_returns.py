#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]


if __name__ == '__main__':
    l, f = multiple_returns("At school, i learnt C!")
    print("Length: {:d} - First character: {}".format(l, f))
