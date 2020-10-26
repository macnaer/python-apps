import mysql.connector
if __name__ == "__main__":
    db_manager


class db_manager:
    def __init__(self, host, user, password):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS pylogin")
        self.__cursor.execute("USE pylogin")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(64), email VARCHAR(128), password VARCHAR(2048))")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Register\n2. Login\n3. Edit\n4. Delete\n5. Show all users\n6. Search by name\n0 Exit\n ===>> "))
            if choice == 1:
                answer = self.__register()
                print(answer)
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choice.")

    def __register(self):
        username = input("Username ")
        email = input("Email ")
        password = input("Password ")
        confirm_password = input("Confirm password ")

        if password != confirm_password:
            return "Password do not match."

        self.__cursor.execute(
            "SELECT email FROM users WHERE email = '" + email + "'")
        result = self.__cursor.fetchone()

        if result != None:
            return "User exists"

        else:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            val = (username, email, password)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            return "User successfully created"
