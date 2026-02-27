from database.db_connect import get_connection

# Get all Movies


def get_all_movies():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, duration, genre
        FROM movies
    """)

    movies = cursor.fetchall()
    conn.close()
    return movies

# Get Movie bY Id (For Details Sereen)

def get_movie_by_id(movie_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, description, duration, genre
        FROM movies
        WHERE id = ?
    """, (movie_id,))

    movie = cursor.fetchone()
    conn.close()
    return movie

# Search Movies

def search_movies(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, duration, genre
        FROM movies
        WHERE title LIKE ?
    """, ('%' + keyword + '%',))

    results = cursor.fetchall()
    conn.close()
    return results

# Get show Timing
def get_shows_by_movie(movie_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, show_date, show_time, price
        FROM shows
        WHERE movie_id = ?
    """, (movie_id,))

    shows = cursor.fetchall()
    conn.close()
    return shows

# Book Ticket

def book_ticket(user_id, show_id, seats, total_price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bookings (user_id, show_id, seats, total_price)
        VALUES (?, ?, ?, ?)
    """, (user_id, show_id, seats, total_price))

    conn.commit()
    conn.close()

# Get Booking History

def get_user_bookings(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT b.id, m.title, s.show_date, s.show_time, b.seats, b.total_price
        FROM bookings b
        JOIN shows s ON b.show_id = s.id
        JOIN movies m ON s.movie_id = m.id
        WHERE b.user_id = ?
        ORDER BY b.id DESC
    """, (user_id,))

    bookings = cursor.fetchall()
    conn.close()
    return bookings

# create booking

def create_booking(user_id, show_id, seats, total_price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bookings (user_id, show_id, seats, total_price)
        VALUES (?, ?, ?, ?)
    """, (user_id, show_id, seats, total_price))

    conn.commit()
    conn.close()