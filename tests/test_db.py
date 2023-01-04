import unittest
from notes import db


class TestDB(unittest.TestCase):
    def setUp(self):
        self.db_name = "unit-tests"
        self.conn = db.create_connection()

    def tearDown(self):
        self.conn.close()
        conn = db.create_connection()
        conn.execute("DROP DATABASE unit-tests;")
        conn.close()

    def test_create_table(self):
        db.create_table(self.conn)

        conn = db.create_connection()
        res = conn.execute("SELECT name FROM sqlite_schema WHERE type='table';")
        nameExists = False
        
        for name in res:
            if "'notes'," in str(name):
                nameExists = True

        conn.close()
        self.assertTrue(nameExists, "Test failed, couldn't find database table 'test'")
