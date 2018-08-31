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
            `smiFileName` VARCHAR(200) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
            `engSentence` VARCHAR(500) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
            `korSentence` VARCHAR(500) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
            `emotion` VARCHAR(45) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
            PRIMARY KEY (`id`))
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8mb4
            COLLATE = utf8mb4_unicode_ci;
        """

        dbLogger.debug("makeSubDB")
        try:
            return dbi.query(makeTableQuery)
        except Exception as e:
            return dbLogger.error(e)

    def insertSubDB(self, dbTuple):
        insertDBQuery = """
            INSERT INTO sub (smiFileName, engSentence, korSentence, emotion)
            VALUES (%s, %s, %s, %s)
        """

        dbLogger.debug('insertSubDB')
        try:
            return dbi.insert(insertDBQuery, dbTuple)
        except Exception as e:
            return dbLogger.error(e)

    def countRows(self):
        dbLogger.debug("countRows")
        try:
            return dbi.rows()
        except Exception as e:
            return dbLogger.error(e)
