#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))


    inp = '/home/hs/Data/wikipedia/wiki.zh.text.simplified_seg'
    outp1 = '/home/hs/Data/wikipedia/wiki.zh.text.simplified.wordvecs'
    outp2 = '/home/hs/Data/wikipedia/wiki.zh.text.simplified_wordvecs.txt'

    model = Word2Vec(LineSentence(inp), size=300, window=5, min_count=5,
            workers=multiprocessing.cpu_count(), iter=3)

    # trim unneeded model memory = use(much) less RAM
    #model.init_sims(replace=True)
    model.save(outp1)
    model.save_word2vec_format(outp2, binary=False)
    print('OK')

