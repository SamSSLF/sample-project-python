class SqlQuery:
    @staticmethod
    def join_albums():
        # Assuming we have a database connection and cursor setup
        query = """
        SELECT album.title, track.name, artist.name
        FROM album
        JOIN track ON album.album_id = track.album_id
        JOIN artist ON album.artist_id = artist.artist_id
        """
        # Execute the query and fetch results
        cursor.execute(query)
        return cursor.fetchall()

def test_join_albums() -> None:
    assert SqlQuery.join_albums()[0] == (
        "For Those About To Rock (We Salute You)",
        "For Those About To Rock We Salute You",
        "AC/DC",
    )

def test_benchmark_join_albums(benchmark) -> None:
    benchmark(SqlQuery.join_albums)