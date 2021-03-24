from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
import csv


cnx = mysql.connector.connect(
    user='your-user', password='your-password', database='poses')
cursor = cnx.cursor()

add_pose = ("INSERT INTO poses "
            "(x, y) "
            "VALUES (%s, %s)")

with open('poseWithTime.csv') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_data:
        # print(f"{type(row[3])}")
        cursor.execute(add_pose, row[3:5])


# data_pose = (0.0, 0.0)

# Insert new pose
# cursor.execute(add_pose, data_pose)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
print(f"Done!")
