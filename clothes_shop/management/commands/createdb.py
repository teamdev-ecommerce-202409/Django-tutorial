import MySQLdb
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create database"

    def handle(self, *args, **options):
        print("create database!")
        db = MySQLdb.connect(host="localhost", user="root")
        cursor = db.cursor()
        cursor.execute(
            "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'"
        )
        cursor.execute("CREATE DATABASE django_db")
        cursor.execute("CREATE USER 'django'@'%' IDENTIFIED BY 'django'")
        cursor.execute("GRANT ALL PRIVILEGES ON django_db.* TO 'django'@'%'")
        cursor.execute("GRANT ALL PRIVILEGES ON test_django_db.* TO 'django'@'%'")
        cursor.execute("FLUSH PRIVILEGES")
        db.close()
