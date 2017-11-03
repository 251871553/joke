# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import  hashlib


class JokePipeline(object):
    def __init__(self):
        #connect  to  db  ,not  to  close

        try:
            self.conn = pymysql.connect(host='10.0.17.165', user='admin', passwd='admin', db='scrapydb', port=3306, charset="utf8")
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def getmd5text(self,text):
        m = hashlib.md5()
        m.update(text)
        return m.hexdigest()

    def process_item(self, item, spider):
        self.cur = self.conn.cursor()
        md5_value = self.getmd5text(item['content'].encode('utf-8'))
        print(md5_value)
        cmd1="select   content_md5  from  qiubai  where  content_md5='%s' "  %  md5_value
        code = self.cur.execute(cmd1)
        sex=item['sex'][14:]
        sex=sex[:-4]
    #    print(sex)
        if code == 0:
            cmd2 = "insert into qiubai  values (NULL,'%s','%s','%s','%s','%s','%s','%s','%s')" % (item['author'], item['picture'], sex, item['age'], item['vote'], item['comment'], item['content'],md5_value)
            print(cmd2)
            self.cur.execute(cmd2)
        else:
            print('duplicate')
        self.cur.close()
        self.conn.commit()
        return item
      #  pass
    def __del__(self):
        #disconnect  with  db
        self.conn.close()