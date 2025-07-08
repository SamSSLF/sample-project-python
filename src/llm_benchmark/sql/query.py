import sqlite3
from textwrap import dedent


class SqlQuery:
    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        """
        conn = sqlite3.connect("data/chinook.db")
        cur = conn.cursor()

        # Optimized query to check for existence
        cur.execute(f"SELECT EXISTS(SELECT 1 FROM Album WHERE Title = '{name}')")
        return cur.fetchone()[0] == 1

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        """
        conn = sqlite3.connect("data/chinook.db")
        cur = conn.cursor()

        # Using JOINs for efficient data retrieval
        cur.execute(
            dedent(
                """\
                SELECT 
                    t.Name AS TrackName,
                    a.Title AS AlbumName,
                    ar.Name AS ArtistName
                FROM Track t
                JOIN Album a ON t.AlbumId = a.AlbumId
                JOIN Artist ar ON a.ArtistId = ar.ArtistId
                """
            )
        )
        return cur.fetchall()

    @staticmethod
    def top_invoices() -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        """
        conn = sqlite3.connect("data/chinook.db")
        cur = conn.cursor()

        # Limiting results in the query for better performance
        cur.execute(
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
        return cur.fetchall()