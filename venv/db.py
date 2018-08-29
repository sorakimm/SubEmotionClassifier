# -*- coding:utf-8 -*-
from mylogging import MyLogger
import dbConnect
import pymysql

dbLogFile = 'log/db.log'
dbLogger = MyLogger(dbLogFile)

dbi = dbConnect.DBConnect()

class DB():
    def makeSubTable(self):
        makeTableQuery = """
        CREATE TABLE IF NOT EXISTS `sub_db`.`sub` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `smiFileName` VARCHAR(200) NOT NULL,
            `engSentence` VARCHAR(500) NOT NULL,
            `korSentence` VARCHAR(500) NOT NULL,
            `emotion` VARCHAR(45) NULL,
            PRIMARY KEY (`id`));
        """

        dbLogger.debug("makeSubDB")
        try:
            return dbi.query(makeTableQuery)
        except Exception as e:
            return dbLogger.error(e)

    def insertSubDB(self, dbTuple):
        insertDBQuery = """
            INSERT INTO sub (fileName, engSentence, korSentence, emotion)\
            VALUES (%s, %s, %s)
        """

        dbLogger.debug('insertSubDB')
        try:
            return dbi.insert(insertDBQuery, dbTuple)
        except Exception as e:
            return dbLogger.error(e + dbTuple)

    def countRows(self):
        dbLogger.debug("countRows")
        try:
            return dbi.rows()
        except Exception as e:
            return dbLogger.error(e)
