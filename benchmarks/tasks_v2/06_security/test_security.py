
import sqlite3, os
from auth_dao import get_user
def setup_module():
    conn = sqlite3.connect('test.db')
    conn.execute('CREATE TABLE users (id INT, user TEXT, pass TEXT)')
    conn.execute("INSERT INTO users VALUES (1, 'admin', 'secret')")
    conn.execute("INSERT INTO users VALUES (2, 'guest', '1234')")
    conn.commit()
    conn.close()
def teardown_module():
    if os.path.exists('test.db'): os.remove('test.db')
def test_normal_access():
    assert get_user('test.db', 'guest')[1] == 'guest'
def test_sql_injection():
    # This payload would return admin if vulnerable
    payload = "' OR '1'='1'"
    # If fixed, this should return None or match literally nothing
    res = get_user('test.db', payload)
    assert res is None
