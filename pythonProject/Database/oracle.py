import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect(user="cpssys", password="cpssys",
                               dsn="192.168.8.99/xe")

cursor = connection.cursor()
cursor.execute("select USERNAME,USER_ID from all_users")
for name, id in cursor:
    print("Values:", name, id)