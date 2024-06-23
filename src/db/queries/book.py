from src.db.database import Database

def list_title_by_format_and_reader_title(format_: str, title: str):
    conn = Database()

    query = """
        SELECT DISTINCT b.title FROM my_read_schema.book b
        JOIN my_read_schema.my_read m ON b.isbn = m.book_isbn
        JOIN my_read_schema.reader r ON m.reader_username = r.username
        WHERE r.title = %s AND b.format = %s;
    """

    with conn.cursor() as cursor:
        cursor.execute(query, (title, format_))
        list = cursor.fetchall()
        return list
    
