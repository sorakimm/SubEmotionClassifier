from mylogging import MyLogger
import db
from SubScraper import gomSubScraper
import SubEditor


subScrapDataLogFile = 'log/subScrapData.log'
subScrapDataLogger = MyLogger(subScrapDataLogFile)


if __name__ == '__main__':
    gomSubScraper = gomSubScraper()
    # gomLastPage = gomSubScraper.getLastPage()
    # for page in range(1, gomLastPage + 1):
    #     smiList = gomSubScraper.getSortSmiList(str(page))
    # SubEditor.sortTxt(smiList[0])

    SubEditor.sortTXT(gomSubScraper.getSortSmiList('0'))
    # print(SubEditor.sortTXT(smi))



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
