# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import requests
from requests.compat import urljoin
from mylogging import MyLogger
import SubEditor

subScrapLogFile = 'log/subScrap.log'
subScrapLogger = MyLogger(subScrapLogFile)


gomBaseUrl = 'http://gom.gomtv.com'



def getHtml(url):
   html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      html = resp.text
   return html


class gomSubScraper():
    def __init__(self):
        self.url = ""
        self.dbTuple = tuple()
        self.gomKorEnBoardUrl = "http://gom.gomtv.com/main/index.html?ch=subtitles&pt=l&menu=subtitles&lang=3&page="
        self.titleList = []


    def getGomLastBoard(self):
        subScrapLogger.info("getGomLastBoard")

        GomFirstBoard = requests.get(urljoin(self.gomKorEnBoardUrl, '1'))
        firstPageBSObj = BeautifulSoup(GomBoard, "html.parser")
        lastPage = firstPageBSObj.find('a', {'class' : 'next_last'}).get('onclick')
        return lastPage


    def getGomTitleLink(self):
        subScrapLogger.info("getGomTitleLink")

        lastPage = getGomeLastBoard()
        for pageNum in lastPage :
            bsObj = BeautifulSoup(urljoin(gomKorEnBoardUrl, pageNum), "html.parser")
            for titleLink in self.bsObj.findAll("a", href=re.compile("/main/index.html\?ch=subtitles&pt=v&menu=subtitles&seq=\d+&prepage=1&md5key=&md5skey=")):
                self.titleList.append(urljoin(gomBaseUrl, titleLink.get('href')))


    def getGomDownLink(self, url):
        subScrapLogger.info("getGomeDownLink")

        downPattern = re.compile("\'(.+?)\'")
        gom_boardUrl = 'http://gom.gomtv.com/main/index.html/'
        gom_DownCHPT_Url = 'ch=subtitles&pt=down&'


        downHtml = getHtml(url)
        bsObj= BeautifulSoup(downHtml, 'html.parser')
        downSeq = downPattern.findall(bsObj.find('a', {'class' : 'btn_type3 download'}).get('onclick'))

        intSeq = downSeq[0]
        capSeq = downSeq[1]
        fileName = downSeq[2]

        downCommand = fileName + '?' + gom_DownCHPT_Url + 'intSeq=' + intSeq + '&capSeq=' + capSeq
        fullDownUrl = urljoin(gom_boardUrl, downCommand)
        smi = getHtml(fullDownUrl)

        return smi
        


if __name__ == '__main__':
    gom = gomSubScraper()
    smi = gom.getGomDownLink('http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=913992&prepage=1&md5key=&md5skey=')
    # print(SubEditor.checkKREN(smi))
    print(SubEditor.sortTXT(smi))



    # print('starting Gom Crawl.py...')
    # lastBoardNum = getGomLastBoard(gom_mainBoardPage)
    # # lastBoardNum = 1
    # # print ("lastBoardNum : ", lastBoardNum)
    # pageURLList = []
    # pageURLList = getGomAllBoardPageURL(lastBoardNum)
    # titleList = []
    #
    # getGomTitleLink(pageURLList)
    #
    # while True:
    #     time.sleep(0.5)
    #     db.connect(HOST, PORT)
    #     db.reqURL()  # titleURL 요청
    #     titleURL = db.recvURL()
    #     db.closesocket()
    #
    #     if (len(titleURL) == 0):  # 가져온 titleURL의 길이가 0일 때 (받은 패킷의 URL 길이가 0이면 종료)
    #         break;
    #     titleList.append(titleURL)

    # titleList = [
    # 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=910913&prepage=1&md5key=&md5skey=',
    # 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=910903&prepage=1&md5key=&md5skey=',
    # 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=910882&prepage=1&md5key=&md5skey=',
    # 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=910844&prepage=1&md5key=&md5skey=',
    # 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=910834&prepage=1&md5key=&md5skey='
    # ]
    # print (titleList[0])
    # titleList = ['http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=911016&prepage=1&md5key=&md5skey=']
    # for i in range(0, len(titleList)):
    #     contentsList = getGomDownLink(titleList[i])
    #     contentsEditSend(contentsList)
    #
    # while 1:
    #     print("checkUpdatedDownURL START! ")
    #     updatedTitleList = []
    #     time.sleep(100)
    #     updatedTitleList = checkUpdatedDownURL()
    #     # updatedTitleList = ['http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=908441&prepage=5&md5key=&md5skey=', 'http://gom.gomtv.com/main/index.html?ch=subtitles&pt=v&menu=subtitles&seq=907827&prepage=7&md5key=&md5skey=']
    #
    #     for i in range(0, len(updatedTitleList)):
    #         updatedContentsList = getGomDownLink(updatedTitleList[i])
    #         contentsEditSend(updatedContentsList)
    #
