import tempfile
from io import BytesIO
import pandas as pd
import arrow
import hanshu
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, LongTable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.enums import TA_CENTER

story=[]
#获取年月日
time=arrow.now()
year=time.year
month=time.month-1
day=(time.shift(days=-time.day)).day
month0=str(int(month)-5)
month1=time.month-2
month2=time.month-3
month3=time.month-4
month4=time.month-5
month5=time.month-6
    #input('起始月份：')
#累计检测应用数
appacc=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'累计检测应用数')
appnum_acc=appacc['检测应用数'].sum()
appnum_now=appacc.values.tolist()
#print(appacc.检测应用数.tolist()[-1])
#累计检测次数
numacc=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'累计检测次数')
num_acc=numacc['检测次数'].sum()
num_now=numacc.values.tolist()
#累计检测代码行数
codeacc=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'累计代码行数')
codenum_acc=codeacc['代码行数'].sum()
code_now=codeacc.values.tolist()
#累计缺陷数
defectacc=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'累计缺陷类型及占比')
defectnum_acc=defectacc['数量'].sum()
#语言占比
language=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'本月语言占比')
language0=language.values.tolist()
#当月缺陷占比
defectnow=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'本月安全缺陷')
defectnownum=defectnow['爆发数'].sum()
defectnow0=defectnow.values.tolist()
#计算省份个数
pronumnow=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'当月省公司检测次数')
pronumnow0=hanshu.zyzh(pronumnow)
pronumnow1=hanshu.btcs(pronumnow0['org_id'])
#统计当月未检测省公司
pronan=hanshu.diff(pronumnow)
#查找检测次数排名前五的省公司
pronumtop5=hanshu.top5(pronumnow)
#print(pronumtop5.org_id)
#统计检测次数排名靠前的应用，省公司、应用名、检测次数
appnum=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'当月应用检测次数')
appnum0=hanshu.zyzh(appnum)
appnumtop5=hanshu.top52(appnum0)
apptop5pro=appnumtop5.org_id.tolist()
apptop5=appnumtop5.app_name.tolist()
apptop5num=appnumtop5.次数.tolist()
#潮汐分析
datenum=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'当月检测潮汐分析')
datetop1=hanshu.top1(datenum)
dateno1=pd.to_datetime(datetop1.datetime.tolist()[0])
cxyear=dateno1.year
cxmonth=dateno1.month
cxday=dateno1.day
#缺陷类型及爆发频率
defectype=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'当月缺陷类型及占比')
defectype0=defectype.sort_values(by='爆发频率', axis=0, ascending=False)
defectype1=defectype0.head(5)

#省公司缺陷密度
prodef=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'当月各省公司缺陷密度')
prodef00=hanshu.zyzh(prodef)
prodef0=prodef00.sort_values(by='midu', axis=0, ascending=False).head(3)
prodef1=prodef00.sort_values(by='midu', axis=0, ascending=True).head(5)
#当月应用缺陷密度
appdef=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'当月应用缺陷密度')
appdef00=hanshu.zyzh(appdef)
appdef0=appdef00.sort_values(by='rat', axis=0, ascending=False).head(5)
#筛选检测超过1次的应用
appnum2=appnum.loc[appnum["次数"] > 1]
#携带审计情况
xdsj=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'携带审计情况')
#计算携带审计利用率

shenji2=xdsj["app_name"].value_counts().reset_index()
jiance2=appnum[appnum.app_name.isin(xdsj['app_name'])]
shenji2.columns=['app_name','携带审计次数']
hebing=pd.merge(shenji2, jiance2, on = 'app_name')
hebing['携带审计利用率']=list(map(lambda x,y: (x/y), hebing['携带审计次数'], hebing['次数']))
xdsjtop3=hebing.sort_values(by='携带审计利用率', axis=0, ascending=False).head(3)
#table1
proapp=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'省公司-月份-检测应用数')
proapp1=hanshu.suanzzeng(hanshu.zyzh((proapp)))
#TABLE2
data=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'省公司-月份-应用平均缺陷密度')
data1=hanshu.suanzzeng(hanshu.zyzh((data)))
#TABLE3
tab3=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'本月安全缺陷')
tab3['缺陷数0']=round(tab3['爆发数']/10000,1)
tab3['缺陷数'] = [str(i) + '万' for i in tab3['缺陷数0']]
tab3['平均缺陷数/应用']=round(tab3['爆发数']/appnum_now[-1][-1],2)
tab30=tab3.T.values.tolist()
#table4
dataa0=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'应用第一次检测最后一次检测')
dataa=hanshu.zyzh(dataa0)
appno11=pd.DataFrame()
appno11['app_name']=dataa['app_name']
appno11['org_id']=dataa['org_id']
appno11['总检测数']=dataa['检测次数']
appno11['第1次检测']=dataa['第一次密度']
appno11['最后1次检测']=dataa['最后一次密度']
appno11['变动']=round((dataa['最后一次密度']-dataa['第一次密度'])/dataa['第一次密度']*100,2)
appno11['变动率']=[str(i)+'%' for i in appno11['变动']]
appno111 = appno11.sort_values(by='变动', axis=0, ascending=True)#按从小到大排序
appno112=appno111.values.tolist()

appaccnum=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'省公司每月检测应用数')
appaccnum0=hanshu.zyzh(appaccnum)
pro_acc=hanshu.btcs(appaccnum0['org_id'])


appaccnum1 = appaccnum0.groupby(by=['org_id'],as_index = False)['appCount'].sum()
appaccnum2=appaccnum1.sort_values(by = 'appCount',axis = 0,ascending = False)#按大小顺序排名
appaccnumt=appaccnum2.head(5).values.tolist()

pdefect0=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\月报数据.xlsx",'省公司每月检测缺陷密度')
pdefect1=hanshu.zyzh(pdefect0)


#print(appaccnum2.head(5))

pdfmetrics.registerFont(TTFont('SimSun', './SimSun.ttf'))  # 默认不支持中文，需要注册字体
pdfmetrics.registerFont(TTFont('SimSunBd', './simhei.ttf'))
pdfmetrics.registerFont(TTFont('Arial', './Arial.ttf'))
# registerFontFamily('SimSun', normal='SimSun', bold='SimSunBd', italic='VeraIt', boldItalic='VeraBI')

stylesheet = getSampleStyleSheet()   # 获取样式集
stylesheet1 = getSampleStyleSheet()
# 获取reportlab自带样式
Normal = stylesheet['Normal']
BodyText = stylesheet['BodyText']
Italic = stylesheet['Italic']
Title = stylesheet['Title']
Heading1 = stylesheet['Heading1']
Heading2 = stylesheet['Heading2']
Heading3 = stylesheet['Heading3']
Heading4 = stylesheet['Heading4']
Heading5 = stylesheet['Heading5']
Heading6 = stylesheet['Heading6']
Bullet = stylesheet['Bullet']
Definition = stylesheet['Definition']
Code = stylesheet['Code']
# 自带样式不支持中文，需要设置中文字体，但有些样式会丢失，如斜体Italic。有待后续发现完全兼容的中文字体
Normal.fontName = 'SimSun'
Italic.fontName = 'SimSun'
BodyText.fontName = 'SimSun'
Title.fontName = 'SimSunBd'
Heading1.fontName = 'SimSunBd'
Heading2.fontName = 'SimSunBd'
Heading3.fontName = 'SimSunBd'
Heading4.fontName = 'SimSunBd'
Heading5.fontName = 'SimSun'
Heading6.fontName = 'SimSun'
Bullet.fontName = 'SimSun'
Definition.fontName = 'SimSun'
Code.fontName = 'SimSun'


# 添加自定义样式
stylesheet.add(
    ParagraphStyle(name='body',
                   fontName="SimSun",
                   fontSize=12,
                   textColor='black',
                   leading=20,                # 行间距
                   spaceBefore=10,             # 段前间距
                   spaceAfter=10,             # 段后间距
                   leftIndent=0,              # 左缩进
                   rightIndent=0,             # 右缩进
                   firstLineIndent=20,        # 首行缩进，每个汉字为10
                   alignment=TA_LEFT,      # 对齐方式

                   bulletFontSize=15,       #bullet为项目符号相关的设置
                   bulletIndent=-50,
                   bulletAnchor='start',
                   bulletFontName='Symbol'
                   )
)
# 添加自定义样式
stylesheet1.add(
    ParagraphStyle(name='body',
                   fontName="SimSun",
                   fontSize=10,
                   textColor='black',
                   leading=10,                # 行间距
                   spaceBefore=10,             # 段前间距
                   spaceAfter=0,             # 段后间距
                   leftIndent=0,              # 左缩进
                   rightIndent=0,             # 右缩进
                   firstLineIndent=0,        # 首行缩进，每个汉字为10
                   alignment=TA_CENTER,      # 对齐方式

                   bulletFontSize=15,       #bullet为项目符号相关的设置
                   bulletIndent=-50,
                   bulletAnchor='start',
                   bulletFontName='Symbol'
                   )
)
body = stylesheet['body']
body1=stylesheet1['body']
# 段落
content1="<font fontsize=12>&nbsp代码安全审计主要是通过找出代码中存在的潜在安全风险并修复，以提高应用系统代码质量，降低系统安全风险。自2020年9月份上线以来，代码安全子系统在云道平台安全审计中心稳定运行。<br/>&nbsp&nbsp&nbsp&nbsp本报告基于云道平台安全审计中心"\
         "代码安全检测子系统的检测数据进行统计分析，内容分为两大部分：第一部分介绍了2021年"+str(month0)+"-"+str(month)+"月每个月代码安全检测的情况以及趋势。第二部分介绍了"+str(month)+"月份的总体检测情况、安全缺陷情况。</font>"
content2 = "&nbsp<font fontsize=12>2021年"+str(month0)+"-"+str(month)+"月，云道安全审计中心代码安全检测引擎共检测了</font><font name=SimSunBd fontsize=12>"+str(appnum_acc)+"</font><font fontsize=12>个"\
           "应用系统，检测任务数<font name=SimSunBd fontsize=12>"+str(num_acc)+"</font>次，共计<font name=SimSunBd fontsize=12>"+str(round((codenum_acc/100000000),2))+"亿</font>行代码，"\
           "共检测出缺陷<font name=SimSunBd fontsize=12>"+str(round((defectnum_acc/10000),1))+"万</font>个，其中严重缺陷占比<font name=SimSunBd fontsize=12>"+str(round((defectacc['占比'][0]*100),2))+"%</font>，"\
           "高危缺陷占比<font name=SimSunBd fontsize=12>"+str(round((defectacc['占比'][1]*100),2))+"%</font>，中危缺陷占比<font name=SimSunBd fontsize=12>"+str(round((defectacc['占比'][2]*100),2))+"%</font>。"\
           "低危和警告占比<font name=SimSunBd fontsize=12>"+str(round((defectacc['占比'][3]*100+defectacc['占比'][4]*100),2))+"%。</font><br/>&nbsp&nbsp&nbsp&nbsp检测次数趋势如图2.1所示：</font>"
content3 = "&nbsp<font fontsize=12>从图中可以看出，1月份检测次数达到峰值，2月份急剧下降，3月份开始检测次数有所回升。</font>"
content4 = "&nbsp<font fontsize=12>"+str(year)+"年"+str(month0)+"-"+str(month)+"月，<font name=SimSunBd fontsize=12>"+str(pro_acc)+"</font>个省公司累计检测应用数为："\
           "<font name=SimSunBd fontsize=12>"+str(appnum_acc)+"</font>个。每个月的检测应用数及其变化如表2.1所示。可以看出，<font name=SimSunBd fontsize=12>"+str(appaccnumt[0][0])+"、"+str(appaccnumt[1][0])+"、"\
           ""+str(appaccnumt[2][0])+"、"+str(appaccnumt[3][0])+"、"+str(appaccnumt[4][0])+"</font>月均检测应用数排前五，<font name=SimSunBd fontsize=12>江西、山东、山西、四川</font>等省公司自2月份以来检测应用数呈上升趋势。</font>"
content5 = "&nbsp<font fontsize=12>"+str(year)+"年"+str(month0)+"-"+str(month)+"月，云道平台安全审计中心对来自<font name=SimSunBd fontsize=12>"+str(pro_acc)+"</font>个省公司的<font name=SimSunBd fontsize=12>"\
           +str(appnum_acc)+"</font>个应用，累计检测次数：<font name=SimSunBd fontsize=12>"+str(num_acc)+"次</font>，总发现缺陷数<font name=SimSunBd fontsize=12>"+str(round((defectnum_acc/10000),1))+"万</font>个，"\
           "平均千行代码缺陷密度为<font name=SimSunBd fontsize=12>"+str(round((defectnum_acc*1000/codenum_acc),2))+"</font>。省公司应用平均千行代码缺陷密度变化情况，如表2.2，可以看出，<font name=SimSunBd fontsize=12>安徽、北京、四川</font>三个"\
           "省公司的应用平均千行代码缺陷密度总体呈下降趋势。</font>"
content51="&nbsp<font fontsize=12>截至"+str(year)+"年"+str(month)+"月"+str(day)+"日，代码安全检测引擎"+str(month)+"月份共检测<font name=SimSunBd fontsize=12>"+str(appnum_now[-1][-1])+"</font>个应用系统，检测任务数<font name=SimSunBd fontsize=12>"\
          +str(num_now[-1][-1])+"</font>次，共计<font name=SimSunBd fontsize=12>"+str(round((code_now[-1][-1]/10000000),2))+"千万</font>行代码。<br/>&nbsp&nbsp&nbsp&nbsp检测的应用系统中，使用数量最多的两种编程语言为<font name=SimSunBd fontsize=12>"\
          +str(language0[0][0])+"、"+str(language0[1][0])+"</font>，对应的应用数量分别为<font name=SimSunBd fontsize=12>"+str(language0[0][1])+"</font>个和<font name=SimSunBd fontsize=12>"+str(language0[1][1])+"</font>个。可以看出，"\
          "各公司在进行应用开发时的首选语言是<font name=SimSunBd fontsize=12>"+str(language0[0][0])+"</font>语言，占比高达<font name=SimSunBd fontsize=12>"+str(round(language0[0][1]*100/(language['存在应用数'].sum()),2))+"%</font>。编程语言的总体分布情况如图3.1所示。</font>"
content6 = "&nbsp<font fontsize=12>共检测出缺陷<font name=SimSunBd fontsize=12>"+str(round((defectnownum/10000),1))+"万</font>个，其中严重缺陷占比<font name=SimSunBd fontsize=12>"+str(round((defectnow0[0][1]/defectnownum*100),2))+"%</font>，"\
           "高危缺陷占比<font name=SimSunBd fontsize=12>"+str(round((defectnow0[1][1]/defectnownum*100),2))+"%</font>，中危缺陷占比<font name=SimSunBd fontsize=12>"+str(round((defectnow0[2][1]/defectnownum*100),2))+"%</font>，"\
           "低危和警告占比<font name=SimSunBd fontsize=12>"+str(round(((defectnow0[3][1]+defectnow0[4][1])/defectnownum*100),2))+"%</font>。具体详情将从应用检测情况、应用安全缺陷情况、缺陷改善情况以及缺陷审计情况四个角度展开。</font>"
content7 = "&nbsp<font fontsize=12>截至"+str(month)+"月"+str(day)+"日，共有来自<font name=SimSunBd fontsize=12>"+str(pronumnow1)+"</font>个省公司（不包括"+str(pronan)+"）的<font name=SimSunBd fontsize=12>"+str(appacc.检测应用数.tolist()[-1])+"</font>个应用进行代码安全检测<font name=SimSunBd fontsize=12>"+str(numacc.检测次数.tolist()[-1])+"次</font>，"\
           "各省公司应用检测总数如图3.2所示，颜色越深表示检测次数越多，可以看出，排在前面的省份是<font name=SimSunBd fontsize=12>"+str('、'.join(pronumtop5.org_id.tolist()))+"</font>，均超过了<font name=SimSunBd fontsize=12>"+str(min(pronumtop5.total.tolist())-1)+"</font>次。</font>"
content8 = "&nbsp<font fontsize=12>各应用检测次数排名如图3.3所示。可以看出，排在前5的应用分别是："\
           "来自"+str(apptop5pro[0])+"省公司的<font name=SimSunBd fontsize=12>"+str(apptop5[0])+"</font>检测了<font name=SimSunBd fontsize=12>"+str(apptop5num[0])+"次</font>；"\
           "来自"+str(apptop5pro[1])+"省公司的<font name=SimSunBd fontsize=12>"+str(apptop5[1])+"</font>检测了<font name=SimSunBd fontsize=12>"+str(apptop5num[1])+"次</font>；"\
           "来自"+str(apptop5pro[2])+"省公司的<font name=SimSunBd fontsize=12>"+str(apptop5[2])+"</font>检测了<font name=SimSunBd fontsize=12>"+str(apptop5num[2])+"次</font>；"\
           "来自"+str(apptop5pro[3])+"省公司的<font name=SimSunBd fontsize=12>"+str(apptop5[3])+"</font>检测了<font name=SimSunBd fontsize=12>"+str(apptop5num[3])+"次</font>；"\
           "来自"+str(apptop5pro[4])+"省公司的<font name=SimSunBd fontsize=12>"+str(apptop5[4])+"</font>检测了<font name=SimSunBd fontsize=12>"+str(apptop5num[4])+"次</font>。</font>"
content9 = "&nbsp<font fontsize=12>"+str(year)+"年"+str(month)+"月，云道安全审计中心代码安全检测引擎总共检测了<font name=SimSunBd fontsize=12>"+str(numacc.检测次数.tolist()[-1])+"次</font>，平均每天检测<font name=SimSunBd fontsize=12>"+str(round(numacc.检测次数.tolist()[-1]/int(day),2))+"次</font>。每天检测次数如图3.4所示。"\
           "可以看出，<font name=SimSunBd fontsize=12>"+str(cxyear)+"年"+str(cxmonth)+"月"+str(cxday)+"日</font>应用检测最为密集，且各应用相对集中在<font name=SimSunBd fontsize=12>4月6日-4月14日</font>提交检测。</font>"
content10 = "&nbsp<font fontsize=12>据统计，<font name=SimSunBd fontsize=12>"+str(appnum_now[-1][-1])+"</font>个应用总共检测出代码安全缺陷总数为：<font name=SimSunBd fontsize=12>"+str(round((defectnum_acc/10000),1))+"万</font>个，平均每个应用存在<font name=SimSunBd fontsize=12>"+str(int(defectnum_acc/appnum_now[-1][-1]))+"</font>个安全缺陷问题，"\
            "各类安全缺陷出现次数及平均在每应用中的出现次数如表3.3内容所示。</font>"
content11 = "&nbsp<font fontsize=12><font name=SimSunBd fontsize=12>"+str(appnum_now[-1][-1])+"</font>个检测的应用中，安全缺陷类型覆盖了<font name=SimSunBd fontsize=12>"+str(len(defectype))+"种</font>，如图3.5所示。可以看出，排名前五的安全缺陷类型占总缺陷爆发数的<font name=SimSunBd fontsize=12>"\
            +str(round((defectype1['爆发频率'].sum()/defectype0['爆发频率'].sum())*100,2))+"%</font>，这六种缺陷类型的爆发频率均超过<font name=SimSunBd fontsize=12>"+str(round((defectype1.爆发频率.tolist()[4]-1)/10000,2))+"万</font>，它们分别为：<font name=SimSunBd fontsize=12>"\
            +str(defectype1.defect_cname.tolist()[0])+"、"+str(defectype1.defect_cname.tolist()[1])+"、"+str(defectype1.defect_cname.tolist()[2])+"、"+str(defectype1.defect_cname.tolist()[3])+"、"+str(defectype1.defect_cname.tolist()[4])+"</font>。</font>"
content12 = "&nbsp<font fontsize=12>云道平台安全审计中心对来自<font name=SimSunBd fontsize=12>"+str(pronumnow1)+"</font>个省公司的<font name=SimSunBd fontsize=12>"+str(appnum_now[-1][-1])+"</font>个应用源代码进行检测，平均每个省公司"\
            "存在<font name=SimSunBd fontsize=12>"+str(round((defectnownum/10000/pronumnow1),2))+"万</font>个代码缺陷问题，平均千行代码缺陷密度为：<font name=SimSunBd fontsize=12>"+str(round((defectnownum*1000/code_now[-1][-1]),2))+"</font>。"\
            "其中，<font name=SimSunBd fontsize=12>"+str(prodef0.org_id.tolist()[0])+"、"+str(prodef0.org_id.tolist()[1])+"、"+str(prodef0.org_id.tolist()[2])+"</font>是千行代码缺陷密度最高的三家省公司，均超过了"+str(round((prodef0.midu.tolist()[2]-1),2))+"；"\
            "<font name=SimSunBd fontsize=12>"+str(prodef1.org_id.tolist()[0])+"、"+str(prodef1.org_id.tolist()[1])+"、"+str(prodef1.org_id.tolist()[2])+"、"+str(prodef1.org_id.tolist()[3])+"、"+str(prodef1.org_id.tolist()[4])+"</font>是千行代码缺陷密度最低的五家省公司，说明"\
            "这五家省公司应用的安全性较高。各省公司缺陷密度分布情况如图3.6所示，颜色越深表示千行代码缺陷密度越大。</font>"
content13 = "&nbsp<font fontsize=12>应用千行代码缺陷密度分布情况如图3.7所示，排在前五名的应用情况具体为："\
            "来自"+str(appdef0.org_id.tolist()[0])+"省公司的<font name=SimSunBd fontsize=12>"+str(appdef0.app_name.tolist()[0])+"</font>千行代码缺陷密度为"+str(round(appdef0.rat.tolist()[0],2))+"；来自"+str(appdef0.org_id.tolist()[1])+"的<font name=SimSunBd fontsize=12>"+str(appdef0.app_name.tolist()[1])+"</font>千行代码缺陷密度为"+str(round(appdef0.rat.tolist()[1],2))+"；"\
            "来自"+str(appdef0.org_id.tolist()[2])+"的<font name=SimSunBd fontsize=12>"+str(appdef0.app_name.tolist()[2])+"</font>千行代码缺陷密度为"+str(round(appdef0.rat.tolist()[2],2))+"；来自"+str(appdef0.org_id.tolist()[3])+"的<font name=SimSunBd fontsize=12>"+str(appdef0.app_name.tolist()[3])+"</font>千行代码缺陷密度为"+str(round(appdef0.rat.tolist()[3],2))+"；"\
            "来自"+str(appdef0.org_id.tolist()[4])+"的<font name=SimSunBd fontsize=12>"+str(appdef0.app_name.tolist()[4])+"</font>千行代码缺陷密度为"+str(round(appdef0.rat.tolist()[4],2))+"。</font>"
content14 = "&nbsp<font fontsize=12>"+str(month)+"月份检测次数多于1次的应用有<font name=SimSunBd fontsize=12>"+str(len(appnum2))+"</font>个，占总应用数的<font name=SimSunBd fontsize=12>"+str(round((len(appnum2)/appnum_now[-1][-1]*100),2))+"%</font>。分析应用在4月份第1次检测和最后1次检测的千行代码缺陷密度如表3.2，"\
            "变动幅度为负数表示应用千行代码缺陷密度降低、安全性提高，而大部分应用的源代码安全缺陷情况都存在明显的改善趋势。</font>"
content15 = "&nbsp<font fontsize=12>"+str(year)+"年"+str(month)+"月，<font name=SimSunBd fontsize=12>"+str(appnum_now[-1][-1])+"</font>个应用发起了<font name=SimSunBd fontsize=12>"+str(numacc.检测次数.tolist()[-1])+"次</font>检测请求，携带审计<font name=SimSunBd fontsize=12>"+str(len(xdsj))+"</font>次，"\
            "审计功能利用率（发起审计次数/总检测次数）为：<font name=SimSunBd fontsize=12>"+str(round(len(xdsj)/numacc.检测次数.tolist()[-1]*100,2))+"%</font>，对应用进行分析，如图3.8所示。可以看出，<font name=SimSunBd fontsize=12>"+str(xdsjtop3.app_name.tolist()[0])+"、"+str(xdsjtop3.app_name.tolist()[1])+"、"+str(xdsjtop3.app_name.tolist()[2])+"</font>的审计功能利用率较高。</font>"
content16 = "&nbsp<font fontsize=12>"+str(year)+"年"+str(month)+"月发起人工审计的应用有<font name=SimSunBd fontsize=12>"+str()+"个</font>，分别为：<font name=SimSunBd fontsize=12>"+str()+"、"+str()+"、"+str()+"、"+str()+"、"+str()+"、"+str()+"、"+str()+"</font>，"\
            "只占参与检测应用总数的<font name=SimSunBd fontsize=12>2.45%</font>，说明目前人工审计的使用率并不高。</font>"
content17 = "&nbsp<font fontsize=12>针对"+str(month)+"月份的检测及审计数据进行分析后，提出以下建议：<br/>&nbsp&nbsp&nbsp&nbsp①"+str(defectype1.defect_cname.tolist()[0])+"、"+str(defectype1.defect_cname.tolist()[1])+"是最频繁爆发的缺陷，建议各省公司在应用维护时注意防范这两类安全问题。<br/>&nbsp&nbsp&nbsp&nbsp②分析表明，静态检测存在一定的误报，目前审计功能的使用率较低，"\
            "建议各个省公司对缺陷进行审计，提高代码的安全性。</font>"



# Table 表格

image = Image('./1.jpg')
image.drawWidth = 160
image.drawHeight = 100
body = stylesheet['body']
table_data0 = [['省份', str(month5)+'月', str(month4)+'月',str(month3)+'月',str(month2)+'月',str(month1)+'月',str(month)+'月'],
              ]
table_data40=[['应用名','省公司','总检测数','第1次检测','最后1次检测','变动'],
              ]

table_data=table_data0
table_data1=table_data0
table_data4=table_data40
for i in range(0,len(data1)-1):
    tabledata=[[Paragraph(str(data1[i][0]),body1), str(data1[i][1]),  str(data1[i][2])+str(data1[i][-5]), str(data1[i][3])+str(data1[i][-4]), str(data1[i][4])+str(data1[i][-3]), str(data1[i][5])+str(data1[i][-2]), str(data1[i][6])+str(data1[i][-1])],
               ]
    table_data=table_data+tabledata
    i=i+1
for j in range(0,len(proapp1)-1):
    tabledata1=[[Paragraph(str(proapp1[j][0]),body1), str(proapp1[j][1]),  str(proapp1[j][2])+str(proapp1[j][-5]), str(proapp1[j][3])+str(proapp1[j][-4]), str(proapp1[j][4])+str(proapp1[j][-3]), str(proapp1[j][5])+str(proapp1[j][-2]), str(proapp1[j][6])+str(proapp1[j][-1])],
               ]
    table_data1=table_data1+tabledata1
    j=j+1
table_data2 =[['缺陷类型','严重','高危','中等','低风险','警告'],
              [Paragraph('缺陷数',body1),str(tab30[3][0]),str(tab30[3][1]),str(tab30[3][2]),str(tab30[3][3]),str(tab30[3][4])],
              [Paragraph('平均缺陷数/应用',body1),str(tab30[4][0]),str(tab30[4][1]),str(tab30[4][2]),str(tab30[4][3]),str(tab30[4][4])],
              ]
for m in range(0,len(appno112)-1):
    tabledata4=[[Paragraph(str(appno112[m][0]),body1), str(appno112[m][1]),  str(appno112[m][2]), str(appno112[m][3]), str(appno112[m][4]), str(appno112[m][6])],
               ]
    table_data4=table_data4+tabledata4
    m=m+1
table_style = [
    ('FONTNAME', (1, 0), (-1, -1), 'SimSun'),  # 字体
    ('FONTNAME', (0, 0), (-1, 0), 'SimSunBd'),  # 字体
    ('FONTSIZE', (0, 0), (-1, 0), 11),  # 第一行的字体大小
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
    ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),  # 所有表格左右中间对齐
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),  # 所有表格左右中间对齐
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐

#    ('SPAN', (-2, -2), (-1, -1)),  # 合并
#    ('SPAN', (0, 4), (0, 5)),  # 合并
#    ('SPAN', (2, 4), (2, 5)),  # 合并
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),  # 设置第一行背景颜色
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # 设置表格内文字颜色
    ('GRID', (0, 0), (-1, -1), 0.75, colors.black),  # 设置表格框线为灰色，线宽为0.1
]
table_style1 = [
    ('FONTNAME', (1, 0), (-1, -1), 'SimSun'),  # 字体
    ('FONTNAME', (0, 0), (-1, 0), 'SimSunBd'),  # 字体
    ('FONTSIZE', (0, 0), (-1, 0), 11),  # 第一行的字体大小
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 所有表格左右中间对齐
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),  # 设置第一行背景颜色
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # 设置表格内文字颜色
    ('GRID', (0, 0), (-1, -1), 0.75, colors.black),  # 设置表格框线为灰色，线宽为0.1
]
table = Table(data=table_data,style=table_style, colWidths=75)
table1= Table(data=table_data1,style=table_style, colWidths=75)
table2= Table(data=table_data2,style=table_style1, colWidths=75)
table3=Table(data=table_data4,style=table_style1, colWidths=75)
#story.append(Paragraph("区块链", Title))
story.append(Paragraph("一、报告背景", Heading1))
story.append(Paragraph(content1, body))
story.append(Paragraph("二、"+str(month0)+"-"+str(month)+"月份检测情况", Heading1))
story.append(Paragraph(content2, body))
story.append(Paragraph(content3, body))
story.append(Paragraph("2.1 应用检测情况", Heading2))
story.append(Paragraph(content4, body))
story.append(table1)
story.append(Paragraph("2.2 缺陷密度分布情况", Heading2))
story.append(Paragraph(content5, body))
story.append(table)
story.append(Paragraph("三、"+str(month)+"月份检测情况", Heading1))
story.append(Paragraph(content51, body))
story.append(Paragraph(content6, body))
story.append(Paragraph("3.1 应用检测情况", Heading2))
story.append(Paragraph("3.1.1 应用检测次数排序", Heading3))
story.append(Paragraph(content7, body))
story.append(Paragraph(content8, body))
story.append(Paragraph("3.1.2 检测潮汐分析", Heading3))
story.append(Paragraph(content9, body))
story.append(Paragraph("3.2 缺陷密度分布情况", Heading2))
story.append(Paragraph(content10, body))
story.append(Paragraph("3.2.1 总体缺陷类型分布情况", Heading3))
story.append(Paragraph(content11, body))
story.append(table2)
story.append(Paragraph("3.2.2 应用缺陷密度排序", Heading3))
story.append(Paragraph(content12, body))
story.append(Paragraph(content13, body))
story.append(Paragraph("3.3 缺陷改善情况", Heading2))
story.append(Paragraph(content14, body))
story.append(table3)
story.append(Paragraph("3.4 审计情况", Heading2))
story.append(Paragraph("3.4.1 携带审计使用情况", Heading3))
story.append(Paragraph(content15, body))
story.append(Paragraph("3.4.2 人工审计使用情况", Heading3))
story.append(Paragraph(content16, body))
story.append(Paragraph("四、建议", Heading1))
story.append(Paragraph(content17, body))


# bytes
# buf = BytesIO()
# doc = SimpleDocTemplate(buf, encoding='UTF-8')
# doc.build(story)
# print(buf.getvalue().decode())

# file
doc = SimpleDocTemplate('C:\\Users\\eric\\Desktop\\hello.pdf')
doc.build(story)