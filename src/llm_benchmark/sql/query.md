import sqlite3

class SqlQuery:
    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        """
        with sqlite3.connect("data/chinook.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM Album WHERE Title = ?", (name,))
            return cur.fetchone()[0] > 0

    @staticmethod
    def join_albums() -> None:
        """Join 3 tables: Album, Artist, and Track

        Returns:
            None
        """
        with sqlite3.connect("data/chinook.db") as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT Album.Title, Artist.Name, Track.Name
                FROM Album
                JOIN Artist ON Album.ArtistId = Artist.ArtistId
                JOIN Track ON Album.AlbumId = Track.AlbumId
            """)
            results = cur.fetchall()
            for row in results:
                print(row)

# Example usage
if __name__ == "__main__":
    print(SqlQuery.query_album("Presence"))
    SqlQuery.join_albums()