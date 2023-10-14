import mysql.connector 

#Committed on this file as well by @DevinDeSilva

# Connect to the MySQL get_planted_treesbase
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    get_planted_treesbase="tree_app"
)

# Function to insert a new tree record
def insert_tree(tree_id, tree_type, description, date_planted, geo_location, photos, date, user_id):
    cursor = db.cursor()
    sql = "INSERT INTO planted_trees (tree_id, tree_type, description, date_planted, geo_location, photos, date, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (tree_id, tree_type, description, date_planted, geo_location, photos, date, user_id)
    cursor.execute(sql, values)
    db.commit()
    print("Tree record inserted successfully!")

# Report 01: Details of Planted trees
def get_planted_trees():
    cursor = db.cursor()
    sql = "SELECT * FROM planted_trees"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Details of Planted Trees:")
    for row in result:
        print("Tree ID:", row[0])
        print("Tree Type:", row[1])
        print("Description:", row[2])
        print("Date Planted:", row[3])
        print("Geo Location:", row[4])
        print("Photos:", row[5])
        print("Date:", row[6])
        print("User ID:", row[7])
        print("---------------------------")

# Report 02: Users & Points
def report_users_and_points():
    cursor = db.cursor()
    sql = "SELECT users.first_name, users.last_name, users.email, SUM(points) as total_points FROM users JOIN points ON users.user_id = points.user_id GROUP BY users.user_id ORDER BY total_points DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Users and Points Report:")
    for row in result:
        print("Name:", row[0], row[1])
        print("Email:", row[2])
        print("Total Points:", row[3])
        print("---------------------------")

# Usage example
# Insert 2 new trees
insert_tree("Tree007", "Birch", "A beautiful birch tree planted in the garden.", "2023-06-20", "40.1234,-74.5678", "photo7.jpg", "2023-07-03", "U001")
insert_tree("Tree008", "Guava", "A small guava tree planted in the backyard.", "2023-05-01", "40.1484,-74.6278", "photo8.jpg", "2023-07-04", "U004")

# Generate 2 reports
get_planted_trees()
report_users_and_points()

# Close the get_planted_treesbase connection
db.close()
