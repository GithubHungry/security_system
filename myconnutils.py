import pymysql.cursors


def get_connection():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='non-root',
                                 password='123',
                                 db='diploma', )

    return connection
