
import sqlite3


def get_user(db_path, username):
    """Return (id, user) for an exact username match or None if not found."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        # Use parameterized query to avoid SQL injection.
        cursor.execute("SELECT id, user FROM users WHERE user = ?", (username,))
        return cursor.fetchone()
