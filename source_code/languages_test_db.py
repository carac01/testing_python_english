import os
from unittest import TestCase, main
from languages_db import LanguagesDB


class TestLanguageDatabase(TestCase):
    def setUp(self) -> None:
        self.my_languages_db = LanguagesDB()

    def tearDown(self):
        os.remove("backup.db")

    def test_db_created(self):
        self.my_languages_db.create_db()
        actual = self.my_languages_db.select_all_records(1995)
        expected = [('JavaScript', 1995)]
        self.assertListEqual(actual, expected)

    def test_db_updated(self):
        self.my_languages_db.create_db()
        self.my_languages_db.update_record("Python", "Python🐍")
        actual = self.my_languages_db.select_all_records(1991)
        expected = [('Python🐍', 1991)]
        self.assertListEqual(expected, actual)

    def test_db_deleted(self):
        self.my_languages_db.create_db()
        self.my_languages_db.delete_record("Fortran")
        result = self.my_languages_db.select_all_records("Fortran")
        self.assertFalse(result)


if __name__ == "__main__":
    main()
