# coding = gbk
with open("C:/Users/Shayla/Desktop/BP演讲/BP2010年.txt", "r",encoding='UTF-8') as f:  # 打开文件
    data = f.read()
#去标点符号
import re
import string
x=re.compile('[%s]' % re.escape(string.punctuation))
data7 = []
for review in data:
    new_review = []
    for token in review:
        new_token = x.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    data7.append(new_review)
print(len(data7))

import logging
from gensim import corpora
from six import iteritems
from gensim.models import ldaseqmodel
from gensim.corpora import Dictionary, bleicorpus

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) #输出日志信息，便于了解程序运行情况
stoplist = set('a able  about  above  according i accordingly  "i  across  actually  after  afterwards  again  against  ain’t -  all  allow  allows  almost  alone  along  already  also  although  always  am  among  amongst  an  and  another  any  anybody  anyhow  anyone  anything  anyway  anyways  anywhere  apart  appear  appreciate  appropriate  are  aren’t  around  as  a’s  aside  ask  asking  associated  at  available  away  awfully  be  became  because  become  becomes  becoming  been  before  beforehand  behind  being  believe  below  beside  besides  best  better  between  beyond  both  brief  but  by  came  can  cannot  cant  can’t  cause  causes  certain  certainly  changes  clearly  c’mon  co  com  come  comes  concerning  consequently  consider  considering  contain  containing  contains  corresponding  could  couldn’t  course  c’s  currently  definitely  described  despite  did  didn’t  different  do  does  doesn’t  doing  done  don’t  down  downwards  during  each  edu  eg  eight  either  else  elsewhere  enough  entirely  especially  et  etc  even  ever  every  everybody  everyone  everything  everywhere  ex  exactly  example  except  far  few  fifth  first  five  followed  following  follows  for  former  formerly  forth  four  from  further  furthermore  get  gets  getting  given  gives  go  goes  going  gone  got  gotten  greetings  had  hadn’t  happens  hardly  has  hasn’t  have  haven’t  having  he  hello  help  hence  her  here  hereafter  hereby  herein  here’s  hereupon  hers  herself  he’s  hi  him  himself  his  hither  hopefully  how  howbeit  however  i’d  ie  if  ignored  i’ll  i’m  immediate  in  inasmuch  inc  indeed  indicate  indicated  indicates  inner  insofar  instead  into  inward  is  isn’t  it  it’d  it’ll  its  it’s  itself  i’ve  just  keep  keeps  kept  know  known  knows  last  lately  later  latter  latterly  least  less  lest  let  let’s  like  liked  likely  little  look  looking  looks  ltd  mainly  many  may  maybe  me  mean  meanwhile  merely  might  more  moreover  most  mostly  much  must  my  myself  name  namely  nd  near  nearly  necessary  need  needs  neither  never  nevertheless  new  next  nine  no  nobody  non  none  noone  nor  normally  not  nothing  novel  now  nowhere  obviously  of  off  often  oh  ok  okay  old  on  once  one  ones  only  onto  or  other  others  otherwise  ought  our  ours  ourselves  out  outside  over  overall  own  particular  particularly  per  perhaps  placed  please  plus  possible  presumably  probably  provides  que  quite  qv  rather  rd  re  really  reasonably  regarding  regardless  regards  relatively  respectively  right  said  same  saw  say  saying  says  second  secondly  see  seeing  seem  seemed  seeming  seems  seen  self  selves  sensible  sent  serious  seriously  seven  several  shall  she  should  shouldn’t  since  six  so  some  somebody  somehow  someone  something  sometime  sometimes  somewhat  somewhere  soon  sorry  specified  specify  specifying  still  sub  such  sup  sure  take  taken  tell  tends  th  than  thank  thanks  thanx  that  thats  that’s  the  their  theirs  them  themselves  then  thence  there  thereafter  thereby  therefore  therein  theres  there’s  thereupon  these  they  they’d  they’ll  they’re  they’ve  think  third  this  thorough  thoroughly  those  though  three  through  throughout  thru  thus  to  together  too  took  toward  towards  tried  tries  truly  try  trying  t’s  twice  two  un  under  unfortunately  unless  unlikely  until  unto  up  upon  us  use  used  useful  uses  using  usually  value  various  very  via  viz  vs  want  wants  was  wasn’t  way  we  we’d  welcome  well  we’ll  went  were  we’re  weren’t  we’ve  what  whatever  what’s  when  whence  whenever  where  whereafter  whereas  whereby  wherein  where’s  whereupon  wherever  whether  which  while  whither  who  whoever  whole  whom  who’s  whose  why  will  willing  wish  with  within  without  wonder  won’t  would  wouldn’t  yes  yet  you  you’d  you’ll  your  you’re  yours  yourself  yourselves  you’ve  zero  zt  ZT  zz  ZZ'.split())
dictionary = corpora.Dictionary(line.lower().split() for line in open('datasets/myCorpus.txt'))
stop_ids = [
    dictionary.token2id[stopword]
    for stopword in stoplist
    if stopword in dictionary.token2id
]
once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids)  # 去除只出现过一次的词
dictionary.compactify()       # 删除去除单词后的空格
dictionary.save('datasets/news_dictionary')  # 保存词典
#将文档加载成构造语料库
class MyCorpus(object):
    def __iter__(self):
        for line in open('datasets/myCorpus.txt'):
            yield dictionary.doc2bow(line.lower().split())
corpus_memory_friendly = MyCorpus()
corpus = [vector for vector in corpus_memory_friendly]  # 将读取的文档转换成语料库
corpora.BleiCorpus.serialize('datasets/news_corpus', corpus)  # 存储为Blei lda-c格式的语料库

try:
    dictionary = Dictionary.load('datasets/news_dictionary')
except FileNotFoundError as e:
    raise ValueError("SKIP: Please download the Corpus/news_dictionary dataset.")
corpus = bleicorpus.BleiCorpus('datasets/news_corpus')
time_slice = [438, 430, 456]   #设置这个语料库的间隔，此处分为三个时期，第一个时期内有438条新闻，第二为430条，第三个为456条。
#num_topics = 5  #设置主题数，此处为5个主题
ldaseq = ldaseqmodel.LdaSeqModel(corpus=corpus, id2word=dictionary, time_slice=time_slice, num_topics=5) #将语料库、词典、参数加载入模型中进行训练
corpusTopic = ldaseq.print_topics(time=0)  # 输出指定时期主题分布，此处第一个时期主题分布
print(corpusTopic)
topicEvolution = ldaseq.print_topic_times(topic=0) # 查询指定主题在不同时期的演变，此处为第一个主题的
print(topicEvolution)
doc = ldaseq.doc_topics(0) # 查询指定文档的主题分布,此处为第一篇文档的主题分布
print (doc)