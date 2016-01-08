### Chinese word vectors

This project uses Word2vec and GloVe tools to train word vectors for Chinese using data from wikipedia dump.

### Steps

1. Download wikipedia dump from: https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

2. Extract Chinese words from the downloaded xml files, using process_wiki.py. This step would take about 11 minutes(from 14:54:17 to 15:05:53) in my computer to finish iterating over Wikipedia corpus of 253646 documents (articles) with 56758668 positions (total 2724783 articles, 68096009 positions before pruning articles shorter than 50 words).

3. We want to get both Traditional version and Simplified version texts. Firstly, Traditional Chinese should be translated to Simplified Chinese, we use [opencc](https://github.com/BYVoid/OpenCC) package.

    ```
    opencc -i wiki.zh.text -o wiki.zh.text.simplified -c zht2zhs.ini
    ```
    Then, simplified Chinese should be translated to traditional Chinese:
    
    ```
    opencc -i wiki.zh.text -o wiki.zh.text.traditional -c zhs2zht.ini
    ```
    
4. Tokenization, split the sentence into words. Two tokennization mechanism are used: 

    * one character as a words all the time, 因为汉语中单个字往往也能表示许多信息. Namely, we segment the Chinese sentence into character level as follows:
     
     ```
     欧几里得 西元前三世纪的希腊数学家 现在被认为是几何之父
     欧 几 里 得 西 元 前 三 世 纪 的 希 腊 数 学 家 现 在 被 认 为 是 几 何 之 父
     ```
    
    * using Jieba packages to separate sentence. Run tokenization.py，考虑到常用分词工具来分词，使用词汇可提供更多信息
    
5. Train word vectors using train_word2vec_model.py and GloVe model.

   Hyper-parameters:
   
   * word vector dimension: 300
   * window: 5
   * min_count: 5
   * epochs: 3
   * Training algorithm: skip-gram (sg = 1)
   * Model training: hierarchical sampling (hs = 1)
   
   Word vectors statistical information: 
   
   |word vectors|corpus|words|sentences|dimensions|Time|
   |------|------|------|------|------|------|
   |word2vec|traditional Chinese|860,835|253,646|300|3,086.8s|
   |word2vec|simplified Chinese|686,601|253,646|300|3,186.9s|
   |GloVe|traditional Chinese|860,835|253,646|300|2,160.0s|
   |GloVe|simplified Chinese|686,601|253,646|300|2,280.0s|

   Character vectors ststistical information: (Hyper-parameter is the same as training word-level vectors)
   
   |Character vectors|corpus|character|dimensions|Time|
   |------|------|------|------|------|
   |GloVe|traditional|157,660|300|420s|
   |GloVe|simplified|157,379|300|410s|
   |word2vec|traditional||300||
   |word2vec|simplified||300||
   
### Download

1. word level and character level vectors trained by word2vec:

    |Level|Language|syn0|syn1|Text|
    |-----|-----|-----|-----|
    |word|simplified|[Download]()|[Download]()|[Download]()|
    |word|traditional|[Download]()|[Download]()|[Download]()|
    |character|simplified|[Download]()|[Download]()|[Download]()|
    |character|traditional|[Download]()|[Download]()|[Download]()|
    
    Note: syn0 and syn1 files are produced by saving model using model.save(), which allows to continue training the model when loaded. The Text file is produced by saving model using model.save_word2vec_format(), which allows to view the vectors by a sublime-like software.
    
2. word level and character level vectors trained by GloVe:

    |Level|Language|vocab.txt|vectors.txt|cooccurrence.bin|
    |-----|-----|-----|-----|
    |word|simplified|[Download]()|[Download]()|[Download]()|
    |word|traditional|[Download]()|[Download]()|[Download]()|
    |character|simplified|[Download]()|[Download]()|[Download]()|
    |character|traditional|[Download]()|[Download]()|[Download]()|
    
    Note: vectors.txt is the vectors produced by GloVe model and vocab.txt is the vocabulary-index mapping file.


### Contact

* [Yunchao He] (https://plus.google.com/+YunchaoHe)
* yunchaohe@gmail.com
* [YZU](http://www.yzu.edu.tw/) at Taiwan
* [Weibo](http://weibo.com/heyunchao)
* [Facebook](https://www.facebook.com/yunchao.h)
* [Twitter](https://twitter.com/candlewill)