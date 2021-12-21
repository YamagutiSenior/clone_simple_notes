import os
import time
import unittest
import notes
from notes import db


class TestDBCreate(unittest.TestCase):

    def setup(self):
        self.db_name = "my_database"
        self.conn = db.create_connection(name=self.db_name)
        db.create_connection(name="test")

    def tearDown(self):
        pass
        #db.drop_table(self.conn, )
    
    def test_create_table(self):
        db.create_table(self.conn, notes.sql_create_notes_table)
        time.sleep(2)
        
        res = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        nameExists = False
        for name in res:
            if "'test'," in str(name):
                nameExists = True
        
        self.assertTrue(nameExists, "Test failed, couldn't find database table 'test'")
