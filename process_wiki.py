#!/usr/bin/env python
# coding: utf-8

import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    # if len(sys.argv) < 3:
    #     print(globals()['__doc__'] % locals())
    #     sys.exit(1)
    # python process_wiki.py zhwiki-latest-pages-articles.xml.bz2 wiki.zh.text
    # inp, outp = sys.argv[1:3]
    # set the input and output filenames
    inp, outp = '/home/hs/Data/wikipedia/zhwiki-latest-pages-articles.xml.bz2', '/home/hs/Data/wikipedia/wiki.zh.text'

    space = " "
    i = 0
    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    texts = wiki.get_texts()
    for text in texts:
        # print((text[0]).decode("utf-8"))
        # exit()
        output.write(space.join([t.decode('utf-8') for t in text]) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles")