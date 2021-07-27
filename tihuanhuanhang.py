

def delblankline(infile, outfile):
    infopen = open(infile, 'r',encoding="utf-8")
    outfopen = open(outfile, 'w',encoding="utf-8")
    db = infopen.read()
    outfopen.write(db.replace('\n',' '))
    infopen.close()
    outfopen.close()

delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2010.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2010.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2011.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2011.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2012.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2012.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2013.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2013.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2014.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2014.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2015.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2015.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2016.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2016.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2017.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2017.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2018.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2018.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2019.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2019.txt")
delblankline("C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\原\\BP2020.txt", "C:\\Users\\Shayla\\Desktop\\毕业论文\\BP\\BP2020.txt")


