import sqlite3

class DBHelper:
    def __init__(self, db_name="Uanglo.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS summary (
                id INTEGER PRIMARY KEY,
                budget_awal REAL DEFAULT 0,
                dana_darurat REAL DEFAULT 0,
                tabungan REAL DEFAULT 0
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transaksi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipe TEXT,
                jumlah REAL,
                tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("SELECT COUNT(*) FROM summary")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO summary (budget_awal, dana_darurat, tabungan) VALUES (0, 0, 0)")
        self.conn.commit()

    def get_summary(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM summary WHERE id=1")
        return cursor.fetchone()

    def update_budget(self, nominal):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE summary SET budget_awal = ? WHERE id = 1", (nominal,))
        self.conn.commit()

    def tambah_tabungan(self, nominal):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE summary SET tabungan = tabungan + ? WHERE id = 1", (nominal,))
        self.conn.commit()

    def tambah_darurat(self, nominal):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE summary SET dana_darurat = dana_darurat + ? WHERE id = 1", (nominal,))
        self.conn.commit()

    def catat_transaksi(self, tipe, jumlah):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO transaksi (tipe, jumlah) VALUES (?, ?)", (tipe, jumlah))
        self.conn.commit()