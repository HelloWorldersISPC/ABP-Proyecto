from app.database.db_conn import ConexionDB

if __name__ == "__main__":
    db = ConexionDB()
    db.close()
