import nltk
def shanchongfu(infile,outfile):
    with open(infile, "r",encoding='UTF-8') as f:
        data = f.read()  # 读取文件
    print(type(data))
#大小写转换
    data2=data.lower()
#print(data2)
#分句
    tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    data3=tokenizer.tokenize(data2)
    print(len(data3))
    data4=list(set(data3))
    print(len(data4))

    outfopen = open(outfile, 'w',encoding="utf-8")
    for i in range(len(data4)):
        s = str(data4[i]) + ' '
        outfopen.write(s)
    outfopen.close()
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2010.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2011.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2012.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2013.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2014.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2015.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2016.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2017.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2018.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2019.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\二\\BP2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2020.txt")

shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2010.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2011.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2012.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2013.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2014.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2015.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2016.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2017.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2018.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2019.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\二\\Chevron2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Chevron\\Chevron2020.txt")

shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2010.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2011.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2012.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2013.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2014.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2015.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2016.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2017.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2018.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2019.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\二\\Eni2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Eni\\Eni2020.txt")

shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2010.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2011.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2012.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2013.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2014.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2015.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2016.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2017.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2018.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2019.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\二\\EM2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\EM\\EM2020.txt")

shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2010.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2011.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2012.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2013.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2014.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2015.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2016.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2017.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2018.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2019.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\二\\Equinor2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Equinor\\Equinor2020.txt")

#shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2010.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2011.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2012.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2013.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2014.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2015.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2016.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2017.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2018.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2019.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\二\\Shell2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Shell\\Shell2020.txt")

shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2010.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2011.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2012.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2013.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2014.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2015.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2016.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2017.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2018.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2019.txt")
shanchongfu("C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\二\\Total2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\Total\\Total2020.txt")