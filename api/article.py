import json
import datetime
import decimal
from models import getDB

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

class ArticleModel(object):
    def __init__(self):
      return
    @staticmethod
    def getInfo(aid=0):
        conn = getDB()
        cursor = conn.cursor()
        sql = "select post_title,post_content,post_date from wp_posts where post_type='post' AND post_status='publish' and ID="+str(aid)
        cursor.execute(sql)
        row = cursor.fetchone()
        ret = json.dumps({'title': row[0], 'content': row[1], 'time': row[2]}, cls = MyEncoder).decode('utf8')
        conn.commit()
        cursor.close()
        conn.close()
        return ret

    @staticmethod
    def data_to_json(data):
        return json.dumps([{'ID': i['id'], 'title': i['title']} for i in data])
