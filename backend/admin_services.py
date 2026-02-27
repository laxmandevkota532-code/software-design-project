from database.db_connect import get_connection


# MOVIES

def add_movie(title, description, duration, genre):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movies (title, description, duration, genre)
        VALUES (?, ?, ?, ?)
    """, (title, description, duration, genre))

    conn.commit()
    conn.close()
    return True


def get_all_movies():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM movies")
    movies = cursor.fetchall()

    conn.close()
    return movies


# SHOWS

def add_show(movie_id, show_date, show_time, ticket_price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO shows (movie_id, show_date, show_time, ticket_price)
        VALUES (?, ?, ?, ?)
    """, (movie_id, show_date, show_time, ticket_price))

    conn.commit()
    conn.close()
    return True


#  BOOKINGS 

def get_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            b.id,
            m.title,
            s.show_date,
            s.show_time,
            b.total_price
        FROM bookings b
        JOIN shows s ON b.show_id = s.id
        JOIN movies m ON s.movie_id = m.id
    """)

    bookings = cursor.fetchall()
    conn.close()
    return bookings


# REVENUE 

def get_total_revenue():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(total_price) FROM bookings")
    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0
