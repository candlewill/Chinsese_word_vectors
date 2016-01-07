import time
import jieba

jieba.enable_parallel(8)

input = '/home/hs/Data/wikipedia/wiki.zh.text.traditional'
output = '/home/hs/Data/wikipedia/wiki.zh.text.traditional_seg'

content = open(input,"rb").read()
t1 = time.time()
words = " ".join(jieba.cut(content))          # 精确模式

t2 = time.time()
tm_cost = t2-t1

log_f = open(output,"wb")
log_f.write(words.encode('utf-8'))

print('speed %s bytes/second' % (len(content)/tm_cost))