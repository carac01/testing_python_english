import sqlite3


class LanguagesDB:
    def create_db(self):
        conn = sqlite3.connect("backup.db")
        cur = conn.cursor()
        # create the table
        cur.execute("create table programming_languages (name, first_appeared)")

        # insert the data:
        cur.execute("insert into programming_languages values (?, ?)",
                    ("JavaScript", 1995))

        # save data to DB
        conn.commit()

        # insert multiple recordings - qmark style with executemany():
        languages_list = [
            ("Fortran", 1956),
            ("Python", 1991),
            ("Julia", 2012),
        ]
        cur.executemany("insert into programming_languages values (?, ?)",
                        languages_list)

        # save data to DB
        conn.commit()

    def delete_record(self, language):
        """
        Delete the record from the database
        """
        conn = sqlite3.connect("backup.db")
        cur = conn.cursor()

        sql = "delete from programming_languages where name = ?"

        cur.execute(sql, [language])
        conn.commit()
        cur.close()
        conn.close()

    def update_record(self, language, new_name):
        """
        Update the language name
        """
        conn = sqlite3.connect("backup.db")
        cur = conn.cursor()

        sql = "update programming_languages set name = ? where name = ?"

        cur.execute(sql, (new_name, language))
        conn.commit()
        cur.close()
        conn.close()

    def select_all_records(self, language):
        """
        Query the database for all the languages by a particular year
        """
        conn = sqlite3.connect("backup.db")
        cursor = conn.cursor()

        sql = "select * from programming_languages where first_appeared = ?"
        cursor.execute(sql, [language])
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
