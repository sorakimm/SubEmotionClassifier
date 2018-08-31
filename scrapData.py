from mylogging import MyLogger
from db import DB
from SubScraper import gomSubScraper
from EmotionClassifier import emotion_classify


subScrapDataLogFile = 'log/subScrapData.log'
subScrapDataLogger = MyLogger(subScrapDataLogFile)

if __name__ == '__main__':
    gomSubScraper = gomSubScraper()
    db = DB()
    ec = emotion_classify()
    db.makeSubTable()

    gomLastPage = gomSubScraper.getLastPage()
    for page in range(1, gomLastPage + 1):
        sortSmiDictList = gomSubScraper.getSortSmiList(str(page))

        for sortSmiDict in sortSmiDictList:
            smiFileName = list(sortSmiDict.keys())[0]
            smiList = list(sortSmiDict.values())[0]
            for enSmi, korSmi in smiList:
                emotion = ec.classify_text(enSmi)
                subScrapDataLogger.info(smiFileName + enSmi+ korSmi + emotion)
                db.insertSubDB((smiFileName, enSmi, korSmi, emotion))
