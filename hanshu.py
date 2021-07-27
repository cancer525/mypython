import pandas as pd
import arrow
def zyzh(infile):
    data=infile
    data['org_id']=data['org_id'].str.replace('ZHEJIANG','浙江')
    data['org_id']=data['org_id'].str.replace('ANHUI','安徽')
    data['org_id']=data['org_id'].str.replace('BEIJING','北京')
    data['org_id']=data['org_id'].str.replace('CHONGQING','重庆')
    data['org_id']=data['org_id'].str.replace('fujian','福建')
    data['org_id']=data['org_id'].str.replace('gansu','甘肃')
    data['org_id']=data['org_id'].str.replace('GUANGDONG','广东')
    data['org_id']=data['org_id'].str.replace('guangxi','广西')
    data['org_id']=data['org_id'].str.replace('guizhou','贵州')
    data['org_id']=data['org_id'].str.replace('hainan','海南')
    data['org_id']=data['org_id'].str.replace('hebei','河北')
    data['org_id']=data['org_id'].str.replace('HUNAN','湖南')
    data['org_id']=data['org_id'].str.replace('JIANGSU','江苏')
    data['org_id']=data['org_id'].str.replace('jiangxi','江西')
    data['org_id']=data['org_id'].str.replace('jilin','吉林')
    data['org_id']=data['org_id'].str.replace('liaoning','辽宁')
    data['org_id']=data['org_id'].str.replace('neimeng','内蒙古')
    data['org_id']=data['org_id'].str.replace('ningxia','宁夏')
    data['org_id']=data['org_id'].str.replace('qinghai','青海')
    data['org_id']=data['org_id'].str.replace('shandong','山东')
    data['org_id']=data['org_id'].str.replace('SHANGHAI','上海')
    data['org_id']=data['org_id'].str.replace('shanxi','山西')
    data['org_id']=data['org_id'].str.replace('山西_gongsi','陕西')
    data['org_id']=data['org_id'].str.replace('SICHUAN','四川')
    data['org_id']=data['org_id'].str.replace('tianjin','天津')
    data['org_id']=data['org_id'].str.replace('xinjiang','新疆')
    data['org_id']=data['org_id'].str.replace('yunnan','云南')
    data['org_id']=data['org_id'].str.replace('HEILONGJIANG','黑龙江')
    data['org_id']=data['org_id'].str.replace('henan','河南')
    data['org_id']=data['org_id'].str.replace('hubei','湖北')

    data0=data.values.tolist()
    pname=pd.read_excel("C:\\Users\\eric\\Desktop\\月报数据\\省份.xlsx")
    data2=data[data.org_id.isin(pname['省份'])]
    return data2

def btcs(input):
    aa = input.values.tolist()
    # 统计不同元素个数
    seta = set(aa)
    return len(seta)
def diff(infile):
    prname=pd.read_excel("C:\\Users\\eric\\Desktop\\省份.xlsx")
    data=infile.org_id.tolist()
    prname2=prname.省份.tolist()
    prnan=[i for i in prname2 if i not in data]
    prnan0='、'.join(prnan)
    return prnan0

def sum(infile):
    data = infile.groupby(by=['org_id'], as_index=False)['count'].sum()
    return data
def top5(infile):
    data = infile.sort_values(by='total', axis=0, ascending=False)
    return data.head(5)
def top52(infile):
    data = infile.sort_values(by='次数', axis=0, ascending=False)
    return data.head(5)
def top1(infile):
    data = infile.sort_values(by='count', axis=0, ascending=False)
    return data.head(1)

def suanzzeng(infile):
    time = arrow.now()
    year = time.year
    month = time.month - 1
    month1 = time.month - 2
    month2 = time.month - 3
    month3 = time.month - 4
    month4 = time.month - 5
    month5 = time.month - 6
    data0 = infile.copy()
    data0['增长率1'] = round((data0[str(month4) + '月'] - data0[str(month5) + '月']) / data0[str(month5) + '月'] * 100)
    data0['增长率2'] = round((data0[str(month3) + '月'] - data0[str(month4) + '月']) / data0[str(month4) + '月'] * 100)
    data0['增长率3'] = round((data0[str(month2) + '月'] - data0[str(month3) + '月']) / data0[str(month3) + '月'] * 100)
    data0['增长率4'] = round((data0[str(month1) + '月'] - data0[str(month2) + '月']) / data0[str(month2) + '月'] * 100)
    data0['增长率5'] = round((data0[str(month) + '月'] - data0[str(month1) + '月']) / data0[str(month1) + '月'] * 100)
    data0['增长率01'] = ['(' + str(i) + '%)' for i in data0['增长率1']]
    data0['增长率02'] = ['(' + str(i) + '%)' for i in data0['增长率2']]
    data0['增长率03'] = ['(' + str(i) + '%)' for i in data0['增长率3']]
    data0['增长率04'] = ['(' + str(i) + '%)' for i in data0['增长率4']]
    data0['增长率05'] = ['(' + str(i) + '%)' for i in data0['增长率5']]
    data2 = data0.fillna('-')
    data3 = data2.replace('(nan%)', '(-)')
    # data4=data3.replace(['(-)','-'])
    data1 = data3.values.tolist()
    return data1