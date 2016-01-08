#!/bin/bash

# Makes programs, downloads sample data, trains a GloVe model, and then evaluates it.
# One optional argument can specify the language used for eval script: matlab, octave or [default] python
# 1.vocab_count:用于计算原文本的单词统计（生成vocab.txt,每一行为：单词  词频）
# 2.cooccur：用于统计词与词的共现，目测类似与word2vec的窗口内的任意两个词（生成的是cooccurrence.bin,二进制文件，呵呵）
# 3. shuffle：对于2中的共现结果重新整理（一看到shuffle瞬间想到hadoop，生成的也是二进制文件cooccurrence.shuf.bin）
# 4.glove：glove算法的训练模型，会运用到之前生成的相关文件（1&3），最终会输出vectors.txt和vectors.bin（前者直接可以打开，下文主要针对它做研究，后者还是二进制文件）
make

CORPUS=/home/hs/Data/wikipedia/wiki.zh.text.simplified.character
VOCAB_FILE=vocab.txt
COOCCURRENCE_FILE=cooccurrence.bin
COOCCURRENCE_SHUF_FILE=cooccurrence.shuf.bin
BUILDDIR=build
SAVE_FILE=vectors
VERBOSE=2
MEMORY=4.0
VOCAB_MIN_COUNT=5
VECTOR_SIZE=300
MAX_ITER=3
WINDOW_SIZE=5
BINARY=2
NUM_THREADS=8
X_MAX=10

$BUILDDIR/vocab_count -min-count $VOCAB_MIN_COUNT -verbose $VERBOSE < $CORPUS > $VOCAB_FILE
if [[ $? -eq 0 ]]
  then
  $BUILDDIR/cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE
  if [[ $? -eq 0 ]]
  then
    $BUILDDIR/shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE
    if [[ $? -eq 0 ]]
    then
       $BUILDDIR/glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -x-max $X_MAX -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE
       if [[ $? -eq 0 ]]
       then
           if [ "$1" = 'matlab' ]; then
               matlab -nodisplay -nodesktop -nojvm -nosplash < ./eval/matlab/read_and_evaluate.m 1>&2 
           elif [ "$1" = 'octave' ]; then
               octave < ./eval/octave/read_and_evaluate_octave.m 1>&2 
           else
               python eval/python/evaluate.py
           fi
       fi
    fi
  fi
fi
