import sys
import psycopg2


class Postgres(object):

    def __init__(self, host, pgdb, user, password, port=5432):
        self.__host = host
        self.__db = pgdb
        self.__user = user
        self.__pass = password
        self.__port = port
        self.__conn = None
        self.__cur = None
        try:
            self.__conn = psycopg2.connect(
                host=self.__host,
                user=self.__user,
                password=self.__pass,
                port=self.__port,
                dbname=self.__db)
            self.__cur = self.__conn.cursor()
        except (Exception,  psycopg2.DatabaseError) as e:
            print(e)
            sys.exit()

    def query(self, query):
        try:
            self.__cur.execute(query)
        except (Exception, psycopg2.DatabaseError)as e:
            print(f"Error Occurred while trying to query on DataBase => {e} ")

    def fetchall(self):
        try:
            return(self.__cur.fetchall())
        except (Exception, psycopg2.DatabaseError)as e:
            print(f"Error Occurred while trying to retrieving data from curr => {e} ")

    def __del__(self):
        if (self.__cur):
            self.__cur.close()
        if (self.__conn):
            self.__conn.close()


# Create objects
if __name__ == '__main__':
    db = Postgres('vlptk-jenkinit01', 'csvDB', 'dockeruser', 'dockerPasswd')
    #db.query("select 1")
    commands = "CREATE TABLE vendors (vendor_id SERIAL PRIMARY KEY,vendor_name VARCHAR(255) NOT NULL)"
    #db.query(commands)
    db.query("SELECT * FROM vendors")
    print(db.fetchall())
