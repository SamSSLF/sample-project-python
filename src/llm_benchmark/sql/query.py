import sqlite3
from textwrap import dedent


class SqlQuery:
    def __init__(self, db_path="data/chinook.db"):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def query_album(self, name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        """

        self.cur.execute(f"SELECT * FROM Album WHERE Title = '{name}'")
        return len(self.cur.fetchall()) > 0

    def join_albums(self) -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        """

        self.cur.execute(
            dedent(
                """\
                SELECT 
                    t.Name AS TrackName, (
                        SELECT a2.Title 
                        FROM Album a2 
                        WHERE a2.AlbumId = t.AlbumId
                    ) AS AlbumName, 
                    (
                        SELECT ar.Name 
                        FROM Artist ar
                        JOIN Album a3 ON a3.ArtistId = ar.ArtistId
                        WHERE a3.AlbumId = t.AlbumId
                    ) AS ArtistName
                FROM 
                    Track t
                """
            )
        )
        return self.cur.fetchall()

    def top_invoices(self) -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        """

        self.cur.execute(
            dedent(
                """\
                SELECT 
                    i.InvoiceId, 
                    c.FirstName || ' ' || c.LastName AS CustomerName, 
                    i.Total
                FROM 
                    Invoice i
                JOIN Customer c ON c.CustomerId = i.CustomerId
                ORDER BY i.Total DESC
                LIMIT 10
                """
            )
        )
        return self.cur.fetchall()