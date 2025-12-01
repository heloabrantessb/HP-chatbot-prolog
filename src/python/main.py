import os
from dotenv import load_dotenv
from pyswip import Prolog
import mysql.connector

con = mysql.connector.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    database = os.getenv("DATABASE")
)