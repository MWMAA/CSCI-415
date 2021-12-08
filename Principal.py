#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer

if __name__ == '__main__':
    Buffer = Buffer()
    Analyzer = LexicalAnalyzer()

    # Tokenize and reload of the buffer
    for i in Buffer.load_buffer():
        Analyzer.tokenize(i)
