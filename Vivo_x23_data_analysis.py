import re,os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from wordcloud import WordCloud
from snownlp import SnowNLP
from collections import Counter


#打开我们获取的评论文本文件进行评论情感系数处理与保存
def Vivo_x23_sentiments_file():
    s_sentiments = []
    with open(r'Vivo_x23_clean.txt','r',encoding='utf-8') as f:
        for i in f.readlines():
            s = SnowNLP(i)
            s_sentiments.append(s.sentiments)
    with open('Vivo_x23_sentiments.csv','w',encoding='utf-8') as w:
        w.write(str(s_sentiments).strip('[]'))
        w.close()

#词云图制作
def Vivo_x23_wordcloud_plot():
    #出现最多的字段统计，取前200
    with open(r'Vivo_x23_clean.txt', 'r', encoding='utf-8') as f:
        words = re.findall(r'\w+', f.read().lower())
    word_number = Counter(words)
    common = word_number.most_common(200)
    w = WordCloud(font_path='youyuan.TTF',
                  background_color='white',
                  width=750,
                  height=150,
                  max_font_size=45)
    w.generate_from_frequencies(dict(common))
    ax = plt.subplot2grid((4,4), (0,0), rowspan=2,colspan=4)
    ax.imshow(w, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('评论词云图')

#情感系数分布图
def Vivo_x23_emotion_plot():

    b = np.loadtxt('Vivo_x23_sentiments.csv', delimiter=',', dtype=np.float64)
    ax1 = plt.subplot2grid((4,4), (2,0), rowspan=2,colspan=2)
    ax1.hist(b,
             bins=20,
             color='royalblue',
             histtype='bar',
             rwidth=0.8,)
    ax1.set_xlabel('情感系数', )
    ax1.set_ylabel('数量', )
    ax1.set_title('情感系数分布图')

#评论分布图
def Vivo_x23_comment_plot():
    b = np.loadtxt('Vivo_x23_sentiments.csv', delimiter=',', dtype=np.float64)
    good = [x for x in b if 2/3<=x<=1.0]
    medium = [x for x in b if 1/3<=x<=2/3]
    bad = [x for x in b if 0.0<=x<=1/3]
    comment_lenth = [len(x) for x in [good, medium, bad]]
    comment = [len(x)/sum(comment_lenth) for x in [good, medium, bad]]
    #颜色配置
    cmap = plt.get_cmap("tab20c")
    colors = cmap(np.arange(3))
    ax2 = plt.subplot2grid((4,4), (2,2), rowspan=2,colspan=2,)
    ax2.pie(comment,
            labels=['好评', '中评', '差评'],
            radius=0.75,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            wedgeprops={'width':0.45, 'edgecolor':'w'},
            pctdistance=0.7)
    ax2.axis('equal')
    ax2.set_title('评论分布图')
    plt.tight_layout()
    plt.show()

def Vivo_x23_data_analysis_main():
    matplotlib.rcParams['font.family']='YouYuan'
    matplotlib.rcParams['font.size']=10
    file = os.path.exists('Vivo_x23_sentiments.csv')
    #文本文件已进行情感处理判断
    if not file:
        Vivo_x23_sentiments_file()
        Vivo_x23_wordcloud_plot()
        Vivo_x23_emotion_plot()
        Vivo_x23_comment_plot()
    else:
        Vivo_x23_wordcloud_plot()
        Vivo_x23_emotion_plot()
        Vivo_x23_comment_plot()
