# Mobile_phone_analysis

​	如今的时代是数据的时代，采集数据和分析数据对企业显得尤为重要。而对于我们个人而言，运用数据进行理性抉择也是一个不错的选择。这次我分析了有关于vivo，appo，华为，iPhone等四款手机型号的的上千多条评论，首先主要数据是从淘宝，京东的商品评论中获取，采用的工具是Python的requests库。再运用concurrent库进行多线程爬取优化，使之爬取速度更快。之后再运用re库和json提取相应的评论信息，接着运用matplotlib，SnowNLP，wordcloud等库对采集的数据进行数据分析。最后用pyqt5库进行相应的图形界面开发。由于四款手机型号在采集和数据分析上有类似性，这里我们选择用vivo进行相应操作演示。

## 工具
- Python3.6.5
- Google Chrome浏览器
- Pycharm

## 设计步骤

（1）数据采集

（2）数据分析

（3）界面设计

（4）结构整合

## 数据采集

###  1.url提取

​	打开Chrome浏览器打开淘宝网页界面输入我们想要分析的手机型号，我们选择评论数量最高的几家店铺进行url提取。首先我们逐个的打开各家店铺，然后点击累计评论，在右键鼠标点击查看网页源代码，这时发现网页源代码并没有出现相应的评论信息，可能是用了json动态显示，这时右点击检查，然后点击Network键，根据以往的经验很容易发现评论所在的json链接。

​	接着上一步的操作打开链接查看确实有相关的评论信息，复制其url链接进行整合，最终得到淘宝采集的url链接，接着我们依次把多家店铺的url评论链接采集下来。类似京东的url链接也是如此操作。以及vivo官网的url链接也是如此操作，只不过类型为xhr。

![淘宝json链接](https://upload-images.jianshu.io/upload_images/5498924-fc05251cee3984a2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：淘宝json链接

![京东json链接](https://upload-images.jianshu.io/upload_images/5498924-a2d138d9b529262f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：京东json链接

![vivo官网商城xhr链接](https://upload-images.jianshu.io/upload_images/5498924-62b05c36aa2040cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：vivo官网商城xhr链接

### 2.url请求

​	首先构造我们所需的url链接，接着默认设置每个店铺评论链接页面1000页，循环对淘宝和vivo官方以及京东网页的url进行请求操作，这里用到了requests库的get请求方法，发现淘宝和vivo的网页信息返回需要用utf-8进行解码，而京东则直接进行text返回即可。

### 3.请求信息分析与提取

#### 3.1淘宝信息分析与提取

​	这里用到的是re正则表达式库，直接用re正则表达式把需要的评论全部寻找出来。观察淘宝的json网页信息发现所有的评论都在"rateContent"的后面，于是我们的re正则表达式可以这么写r'rateContent":"(.*?)"'。然后用re库的findall方法进行操作，最终我们找到了淘宝json网页信息的评论。

#### 3.2京东信息分析与提取

​	这里用到的是json库的初始化，首先我们把不需要的字符串删除接着调用json的loads方法进行json格式信息初始化，对京东网页信息分析，发现所有的评论都在comments中的content里，对其json操作提取评论，最终得到了京东的网页信息评论。

#### 3.3vivo官网信息分析与提取

​	这里用到的是lxml库的页面标准化以及xpath定位方式。打开vivo官方商城的url链接发现并不是json格式信息，但是右键检查分析该页面为HTML页面，这时可以选择lxml进行页面初始化，之后继续进行分析发现所有的评论数据都在class="evaluate"属性的下一层p标签中，这时用//li[@class="evaluate"]/p/text()进行xpath定位就会得到vivo官方商城的评论信息

### 4.评论保存

​	用Python内置函数创建一个文本文件，已追加写的形式打开，编码设置为utf-8，把淘宝的和京东的还有vivo官方商城的评论全部写在这个文本文件中。

### 5.网页信息请求优化

​	由于Requests库是单线程操作，而每一个店铺循环操作1000次，这将耗费大量的时间去请求下载网页信息，于是这里用到了Python 的多线程操作，调用concurrent.futures下的ThreadPoolExecutor方法，设置CPU的数量以及采集的对象函数，这样就节省了大量的采集时间。

## 评论清洗

​	得到的评论文本文件中含有空格和未作评论的信息，首先创建另一个文本文件，在进行写操作中对每一行进行清洗和替换，得到最终想要的评论文本文件。

![图片4.png](https://upload-images.jianshu.io/upload_images/5498924-3c84e22f69e87c1e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：部分评论图

## 数据分析

### 1.评论情感系数处理

这里用到了一个中文文本情感分析库SnowNLP，它可以把我们的评论逐条的进行情感分析，情感系数越接近1则代表该评论为积极态度，越接近0则表示为消极态度。先逐行读入评论文本文件，调用snownlp库中的SnowNLP方法将每一行评论进行操作，然后将得到的情感系数保存在csv文件中以备接下来的情感系数分布图和评论分布图的制作。

### 2.词云图制作

首先读入清洗后的评论文本文件，对其进行字母小体化处理并用re库的findall方法分割关键词，re正则表达式为r'\w+'。接着我们用Python的内置库collections的Counter方法进行词频统计并挑选出现最多的200词。最后调用worldcloud库中的WorldCloud方法，设置宽，高，字体路径，最大字体尺寸，背景颜色等参数，最终我们成功得到了想要的词云图。

### 3.情感系数分布图制作

这里调用的是Matplotlib中的hist方法，用它可以绘制直方图。用numpy中的loadtext方法读入我们已经处理好的情感系数csv文件，设置直方图个数，颜色，间距，类型等参数，最后设置x,y轴名称，标题，这样我们就完成了对于情感系数分布图的制作。

### 4.评论分布图的制作

先将系数进行一个分类，把它化成三类，分别分为好评，中频，差评，并且分别计算他们的数量和所占总数的百分比。之后调用Matplotlib中的pie方法，设置标签，透明度，颜色，百分比格式等属性，然后设置标题，这样就完成了对评论分布图的制作。

### 5.图形页面布局

调用Matplotlib库的subplot2grid方法创建一个四乘以四的布局，规划词云图占二乘以四的大小，情感系数分析图忽然评论分布图分别占用二乘以二的页面布局。设置全局显示字体和大小参数。matplotlib.rcParams['font.family']='YouYuan'，matplotlib.rcParams['font.size']=10。

![图片5.png](https://upload-images.jianshu.io/upload_images/5498924-c870f68c8f973107.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：数据分析展示

## 界面设计

### 1.界面布局

​	打开Qtdesigner开始制作我们想要的图形界面，第一步先设置一个标签，显示为手机型号。第二步设置一个下拉菜单框，将其类型名称改为mobileComboBox，设置我们想要分析的手机型号。第三步，设置四个按钮，分别设置其名称为数据采集，数据分析，清空文本，清空文件，类型名称为analysisBtn，dataBtn，clearBtn，clearBtn2。

![图11.png](https://upload-images.jianshu.io/upload_images/5498924-7ef058e3170faa99.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：界面布局

### 2.界面按钮槽信号

​	对四个按钮分别设置槽信号clicked和其对应的函数，通过对对象函数的操控，可以触发函数所对应的内容。

![图片7.png](https://upload-images.jianshu.io/upload_images/5498924-604c396986da56ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：界面槽函数

### 3.界面保存并转化

​	完成上述步骤，我们将文件保存为Main_framework.ui。这时候在用命令行工具pyuic5将Main_framework.ui转化为.py文件。命令语句为pyuic5 -o Main_framework.py Main_framework.ui。

## 结构整合

​	新建一个Mobile_phone_analysis.py文件，将所有的手机型号的数据采集与数据分析全部导入进来，并将界面设计的文件也导入进来。分别编写data，data_analysis，clearFile，clearResult槽函数。下拉菜单框将获得手机型号，获得手机型号之后先进行相对应的文件存在判断，如果不存在则开始采集，如果存在请清空文件。之后判断文件若已采集则开始数据分析，若没有数据采集的文件则请求数据分析。最终完成了整个软件的设计与编程。

![图片8.png](https://upload-images.jianshu.io/upload_images/5498924-3af83bde666816ea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：文件结构图

## 总结
​	通过这次的项目设计，我更加了解了Python这门语言的强大，也熟悉了很多之前没有接触的第三方库。虽然在编写程序中出现了很多的问题，但我还是耐心的将其一一解决，这不仅锻炼了我的耐力，而且通过逻辑设计锻炼了我理性思维，通过不断地敲击代码锻炼了我的编程思维。基于Python的手机评论分析这个项目是我在之前的有关vivo_x23的八千条数据分析项目的再次升级，我相信在以后我会继续完善这个项目，使其变成包含所有的手机型号分析软件，或许在以后还将拓展到其他相关领域而不仅仅局限于对手机的分析。

![图12.png](https://upload-images.jianshu.io/upload_images/5498924-d417cfbd1d8c2fbe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图：界面运行结果
