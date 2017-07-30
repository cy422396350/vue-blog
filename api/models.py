import MySQLdb


def getDB():
    host = "119.23.72.70"
    port = 3306
    db = "blog"
    user = "blog"
    password = "HUsv)daI4KNS4s$G0RPU2BBn..."
    conn = MySQLdb.connect(
        host=host, user=user, passwd=password, db=db, port=port, charset="utf8"
    )
    return conn
