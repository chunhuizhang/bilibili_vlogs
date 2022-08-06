
from gensim.models import word2vec, Word2Vec
from multiprocessing import cpu_count
import numpy as np
from gensim.matutils import unitvec

if __name__ == '__main__':

    # 包含了句子以及分词的处理
    # sentences = word2vec.Text8Corpus('text8')
    # # sentences = list of list of words
    # model = Word2Vec(sentences, workers=cpu_count()//2)
    # model.save('text8.model')

    model = Word2Vec.load('text8.model')

    # model.wv.vectors, model.wv.index2word
    # woman + king - man == ?
    # woman + king - man == queen
    print(model.most_similar(positive=['woman', 'king'], negative=['man'], topn=2))



    woman_vec = model.wv.word_vec('woman', use_norm=True)
    king_vec = model.wv.word_vec('king', use_norm=True)
    man_vec = model.wv.word_vec('man', use_norm=True)

    query = unitvec((woman_vec+king_vec-man_vec)/3)
    sims = np.dot(model.wv.vectors_norm, query)
    indices = sims.argsort()[::-1][:5]
    for index in indices:
        print(index, sims[index], model.wv.index2word[index])


