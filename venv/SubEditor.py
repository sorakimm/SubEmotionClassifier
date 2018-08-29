# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import *
import re
# import konlpy
# import nltk
# from konlpy.tag import Komoran
# from konlpy.tag import Twitter
# from nltk.tokenize import RegexpTokenizer
from mylogging import MyLogger

tokenizer = None
tagger = None

subEditorLogFile = 'log/subEditor.log'
subEditorLogger = MyLogger(subEditorLogFile)

pStyle1 = re.compile('<br>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle2 = re.compile('<font color=.*?>', re.IGNORECASE)
pStyle3 = re.compile('</font>', re.IGNORECASE)
pStyle4 = re.compile('<HEAD(.*?)>(.*?)</HEAD>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle5 = re.compile('<!--(.*?)-->', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle6 = re.compile('<br>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle7 = re.compile('<SAMI>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle8 = re.compile('<BODY>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle9 = re.compile('</SAMI>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle10 = re.compile('</BODY>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle11 = re.compile('<i>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle12 = re.compile('</i>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle13 = re.compile(r'<SYNC Start=\d+><P Class=KR.*>&nbsp;')
pStyle14 = re.compile(r'<SYNC Start=\d+><P Class=EN.*>&nbsp;')
pStyle15 = re.compile(r' \r\n{1}$\r\n', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle16 = re.compile(r' \r\n{2,}', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle17 = re.compile(r'\n$', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle18 = re.compile(r'[ ]{2,}', re.MULTILINE | re.DOTALL)
pStyle19 = re.compile(r'\r\n', re.IGNORECASE | re.MULTILINE | re.DOTALL)
pStyle20 = re.compile(r'\w+: ', re.IGNORECASE | re.MULTILINE | re.DOTALL)


def checkKREN(contents):
    "다운받은 smi 파일이 정상인지 체크"
    subEditorLogger.debug("checkKREN")

    pKRCC = re.compile(r'<P Class=K(R.*|OR)>', re.IGNORECASE)
    pENCC = re.compile(r'<P Class=EN.*>', re.IGNORECASE)

    try:
        if (bool(re.search(pKRCC, contents))):
            if (bool(re.search(pENCC, contents))):
                return True

    except Exceptiona as e:
        subEditorLogger.error(e)
        return False

def dictIntersect(dict1, dict2):
    comm_keys = dict1.keys()
    comm_keys &= dict2.keys()

    result = {key:(dict1[key], dict2[key]) for key in comm_keys}
    return result



def sortTXT(contents):
    "smi파일내용 정렬"
    subEditorLogger.debug("sortTXT")

    contents = pStyle1.sub(' ', contents)
    contents = pStyle2.sub(' ', contents)
    contents = pStyle3.sub(' ', contents)
    contents = pStyle4.sub('', contents)
    contents = pStyle5.sub('', contents)
    contents = pStyle6.sub(' ', contents)
    contents = pStyle7.sub('', contents)
    contents = pStyle8.sub('', contents)
    contents = pStyle9.sub('', contents)
    contents = pStyle10.sub('', contents)
    contents = pStyle11.sub('', contents)
    contents = pStyle12.sub('', contents)
    contents = pStyle13.sub('', contents)
    contents = pStyle14.sub('', contents)
    contents = pStyle15.sub('', contents)
    contents = pStyle16.sub(r'\r\n', contents)
    contents = pStyle17.sub('', contents)
    contents = pStyle18.sub(' ', contents)
    contents = pStyle19.sub(' ', contents)
    contents = pStyle20.sub('', contents)

    contentsKR = {}
    contentsEN = {}
    # pStyleKR = re.compile(r'<SYNC Start=(\d+)><P Class=K(R.*|OR)>(.+?)<', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    pStyleKR = re.compile(r'<SYNC Start=(\d+)><P Class=K.*?>(.+?)<', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    pStyleEN = re.compile(r'<SYNC Start=(\d+)><P Class=EN.*?>(.+?)<', re.IGNORECASE | re.MULTILINE | re.DOTALL)
    contentsKR = dict(pStyleKR.findall(contents))
    contentsEN = dict(pStyleEN.findall(contents))

    contentsDict = {}
    contentsDict = dictIntersect(contentsKR, contentsEN)
    subEditorLogger.info(contentsDict)

    lenKR = len(contentsKR)





    # for i in range(0, lenKR):
    #     if contentsKR[i][0] in contentsDict:
    #         contentsDict[contentsKR[i][0]].append(contentsKR[i][2])
    #     else:
    #         contentsDict[contentsKR[i][0]] = [contentsKR[i][2]]
    #
    # lenEN = len(contentsEN)
    # for i in range(0, lenEN):
    #     if contentsEN[i][0] in contentsDict:
    #         contentsDict[contentsEN[i][0]].append(contentsEN[i][1])
    #     else:
    #         contentsDict[contentsEN[i][0]] = [contentsEN[i][1]]

    # 시간key로 교집합 사용해 dict에 한/영 모두 있는 자막만 선별해 return


    return contentsDict


def makeFileName(_FileList):
    mkFileNameList = _FileList[:]
    pStyle = re.compile('./smi/')
    for i in range(0, len(FileList)):
        mkFileNameList[i] = pStyle.sub('', mkFileNameList[i])

    return mkFileNameList


def getKorNoun(body):  # 태그없앤 content에서 명사만 추출하기
    contents = body[:]

    contents = re.sub('[^가-힣 \n]+', '', contents)
    # print (contents)

    kkma = konlpy.tag.Kkma()  # -Xmx128m 로 바꾸기
    # print("Get nouns from contents...")
    keywords = kkma.nouns(contents)
    # print (type(keywords))
    # print ("kkma   : ", keywords)
    pSub = re.compile("sub_")
    for i in range(0, len(keywords)):
        keywords[i] = re.sub(keywords[i], "sub_" + str(keywords[i]), keywords[i])
    # keywords = list(set(keywords))
    print("Keywords : ", keywords)
    return keywords


def getEngNoun(contents):
    tokenizer = RegexpTokenizer("[\w']+")
    keywords = tokenizer.tokenize(contents)
    pStyle = re.compile("'")
    pStyle2 = re.compile(r"\.")
    # pSub = re.compile("sub_")
    for i in range(0, len(keywords)):
        keywords[i] = pStyle.sub("", keywords[i])
        keywords[i] = pStyle2.sub("", keywords[i])
        keywords[i] = re.sub(keywords[i], "sub_" + str(keywords[i]), keywords[i])
    keywords = list(set(keywords))
    print("keywords : ", keywords)
    return keywords

