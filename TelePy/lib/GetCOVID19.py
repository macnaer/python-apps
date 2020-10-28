import mysql.connector
import requests
if __name__ == "__main__":
    pass


class GetCOVID19:
    def __init__(self, HOSTNAME, USERNAME, PASSWORD, COVID19API):
        self.__COVID19API = COVID19API
        self.__get_covid19_info()
        self.__db = mysql.connector.connect(
            host=HOSTNAME,
            user=USERNAME,
            password=PASSWORD
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS telepy")
        self.__cursor.execute("USE telepy")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS Countries (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(64), CountryCode VARCHAR(3), Slug VARCHAR(128), NewConfirmed INT, TotalConfirmed INT, NewDeaths INT, TotalDeaths INT, NewRecovered INT, TotalRecovered INT, Date VARCHAR(128))")

    def __get_covid19_info(self):
        print("Inside")
        responce = requests.get(self.__COVID19API)
        covid_data = responce.json()
        print("API => ", covid_data)
