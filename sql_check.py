import pyodbc


server = 'mdfc-sentinel-demo-sqlsrv.database.windows.net'
database = 'MDfC-Sentinel-Demo-SQL'
username = 'testuser'
password = 'Password123!'
driver = '{ODBC Driver 18 for SQL Server}'


conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;'


try:
        print("[+] Connecting to Azure SQL Database")
        conn = pyodbc.connect(conn_str)
        print("[+] Successfully connected to Database")
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 5 name FROM sys.databases;")
        for row in cursor.fetchall():
               print(row)
        print()

except Exception as e:
        print(e)

