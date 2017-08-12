import json
from models import getDB


class CategoryModel(object):
    def __init__(self, article_id, title):
        self.id = article_id
        self.title = title

    @staticmethod
    def getCat():
        conn = getDB()
        cursor = conn.cursor()
        sql = "select a.term_id,b.name from wp_term_taxonomy as a LEFT JOIN wp_terms as b on a.term_id=b.term_id WHERE a.taxonomy='category'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        ret = json.dumps([{'id': i[0], 'title': i[1]} for i in rows])
        conn.commit()
        cursor.close()
        conn.close()
        return ret
    @staticmethod
    def getAll(category_id=0, page=1):
        conn = getDB()
        cursor = conn.cursor()
        sql = "select a.id,a.post_title title from wp_posts as a LEFT JOIN wp_term_relationships as b on a.ID = b.object_id where b.term_taxonomy_id ="+str(category_id)+" AND a.post_status = 'publish' order by post_date desc"
        if (page > 1):
            sql += " LIMIT " + str((page - 1) * 10) + ",10"
        else:
            sql += " LIMIT 0,10"
        cursor.execute(sql)
        rows = cursor.fetchall()
        articles = []
        ret = json.dumps([{'ID': i[0], 'title': i[1]} for i in rows])
        # for r in rows:
        #     article = Article(r[0], r[1])
        #     articles.append(article)
        conn.commit()
        cursor.close()
        conn.close()
        return ret

    @staticmethod
    def data_to_json(data):
        return json.dumps([{'ID': i['id'], 'title': i['title']} for i in data])
