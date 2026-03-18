import sqlite3
from datetime import datetime
from watermark import generate_watermark

def create_log(user, status):

    conn = sqlite3.connect("access_system.db")
    cursor = conn.cursor()

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 🔐 génération du watermark
    watermark = generate_watermark(user + status + time)

    cursor.execute(
        "INSERT INTO logs(user,time,status,watermark) VALUES(?,?,?,?)",
        (user, time, status, watermark)
    )

    conn.commit()
    conn.close()