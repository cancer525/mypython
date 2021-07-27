from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import nltk


def tiquac(infile, outfile):
    f=open(infile,encoding="utf-8").read()
    #分句
    tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    data=tokenizer.tokenize(f)
    #print(data)

    climate_dic=['climate','Climate']
    climate_dic1=['climate','energy','environment','warm','renewable','sustainable','gas','green','greenhouse','carbon','oil','petroleum','coal','biofuel','sun','wind','capture','biofuels','storage']
    climate_dir_neg=['warm','green','greenhouse','carbon','oil','petroleum','coal']
    delete=['www','®','■','www.shell.com/sustainability','•']

    data9=[]

    for m in range(0,len(data)-1):
        for one in delete:
            if one in nltk.word_tokenize(data[m]):
                data9.append(data[m])
    #print(len(data9))

    data0 = [i for i in data if i not in data9]
    #print(len(data0))
    data1=[]
    for m in range(0,len(data0)-1):
        for one in climate_dic:  # 遍历列表
            if one in nltk.word_tokenize(data0[m]):
                if one in nltk.word_tokenize(data0[m+1]):
                    data1.append(data0[m])
                else:
                    data1.append(data0[m])
                    data1.append(data0[m+1])

    #print(len(data1))
    outfopen = open(outfile, 'w',encoding="utf-8")
    for i in range(len(data1)):
        s = str(data1[i]) + ' '
        outfopen.write(s)
    outfopen.close()


tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2010.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2011.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2012.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2013.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2014.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2015.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2016.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2017.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2018.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2019.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\一\\BP2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2020.txt")

tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2010.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2011.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2012.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2013.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2014.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2015.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2016.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2017.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2018.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2019.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\一\\Chevron2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2020.txt")

tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2010.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2011.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2012.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2013.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2014.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2015.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2016.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2017.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2018.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2019.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\一\\Eni2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2020.txt")

tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2010.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2011.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2012.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2013.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2014.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2015.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2016.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2017.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2018.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2019.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\一\\EM2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2020.txt")

tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2010.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2011.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2012.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2013.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2014.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2015.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2016.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2017.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2018.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2019.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\一\\Equinor2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2020.txt")

#tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2010.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2011.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2012.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2013.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2014.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2015.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2016.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2017.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2018.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2019.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\一\\Shell2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2020.txt")

tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2010.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2011.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2012.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2013.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2014.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2015.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2016.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2017.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2018.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2019.txt")
tiquac("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\一\\Total2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2020.txt")


