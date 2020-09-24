import numpy as np
import jieba
import sys
from sklearn.feature_extraction.text import CountVectorizer


def CutSame(str1,str2):
    sign='· ~ ！ @ # ￥ % …… & * （ ） —— - + = ] } [ { \ | ; :  " " < > , . /  ？ $ ^ _'
    for word in sign:
        str1=str1.replace(word,'') #循环文本，删去标点符号
        for word in sign:
            str2=str2.replace(word,'')
            def JCKSM(str1, str2):#jaccard
                def add_space(s):
                    s_list=jieba.cut(s,cut_all=False)
                    return ' '.join(list(s_list))# 将字中间加入空格
                str1, str2=add_space(str1), add_space(str2)# 转化为TF矩阵
                cv=CountVectorizer(tokenizer=lambda s: s.split())
                corpus=[str1, str2]
                vectors=cv.fit_transform(corpus).toarray()# 求交集
                NUM=np.sum(np.min(vectors, axis=0))# 求并集
                DEN=np.sum(np.max(vectors, axis=0))# 计算杰卡德系数
                return 1.0 * NUM / DEN
    return JCKSM(str1,str2)  


try:
    with open(sys.argv[1],"r",encoding="UTF-8") as f:
        str1=f.read()#输入str1
except FileNotFoundError:
    print('can not find the file')
try: 
    with open(sys.argv[2],"r",encoding="UTF-8") as f:
        str2=f.read()#输入str2
except FileNotFoundError:
    print('can not find the file')
else:
    f.close()

CutSame(str1,str2)          
#print("orig_0.8_dis_1的测试结果：{:f}".format(JCKSM(str1, str2)))#输出查重结果
f=open("G:\\3118005341xzb\\ORIG\\result.txt","w",encoding="UTF-8")
f.write( str(CutSame(str1, str2))[0:4] )
f.close()

