from flask import Flask, render_template, request
from db import connect_to_db

app = Flask(__name__)


# Establish database connection
connection = connect_to_db()
cursor = connection.cursor(buffered=True)


def insert_person(first, last, city, address, country, email):
    insert_person = "INSERT INTO person (fName, lName, city, Address, country, email) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_person, (first, last, city, address, country, email))
    connection.commit()

def insert_courses(first_c, second_c, third_c, person_id):
    if first_c:
        cursor.execute("INSERT INTO course (courseName, person_idperson) VALUES (%s, %s)", (first_c, person_id))
        connection.commit()
    if second_c:
        cursor.execute("INSERT INTO course (courseName, person_idperson) VALUES (%s, %s)", (second_c, person_id))
        connection.commit()
    if third_c:
        cursor.execute("INSERT INTO course (courseName, person_idperson) VALUES (%s, %s)", (third_c, person_id))
        connection.commit()

def insert_projects(first_p, second_p, third_p, person_id):
    if first_p:
        cursor.execute("INSERT INTO project (projectName, person_idperson) VALUES (%s, %s)", (first_p, person_id))
        connection.commit()
    if second_p:
        cursor.execute("INSERT INTO project (projectName, person_idperson) VALUES (%s, %s)", (second_p, person_id))
        connection.commit()
    if third_p:
        cursor.execute("INSERT INTO project (projectName, person_idperson) VALUES (%s, %s)", (third_p, person_id))
        connection.commit()

def insert_languages(first_l, second_l, third_l, person_id):
    if first_l:
        cursor.execute("INSERT INTO language (languageName, person_idperson) VALUES (%s, %s)", (first_l, person_id))
        connection.commit()
    if second_l:
        cursor.execute("INSERT INTO language (languageName, person_idperson) VALUES (%s, %s)", (second_l, person_id))
        connection.commit()
    if third_l:
        cursor.execute("INSERT INTO language (languageName, person_idperson) VALUES (%s, %s)", (third_l, person_id))
        connection.commit()

def insert_hobbies(first_h, second_h, third_h, person_id):
    if first_h:
        cursor.execute("INSERT INTO hobby (hobbyName, person_idperson) VALUES (%s, %s)", (first_h, person_id))
        connection.commit()
    if second_h:
        cursor.execute("INSERT INTO hobby (hobbyName, person_idperson) VALUES (%s, %s)", (second_h, person_id))
        connection.commit()
    if third_h:
        cursor.execute("INSERT INTO hobby (hobbyName, person_idperson) VALUES (%s, %s)", (third_h, person_id))
        connection.commit()

def insert_trainings(first_t, second_t, third_t, person_id):
    if first_t:
        cursor.execute("INSERT INTO site (siteAddress, person_idperson) VALUES (%s, %s)", (first_t, person_id))
        connection.commit()
    if second_t:
        cursor.execute("INSERT INTO site (siteAddress, person_idperson) VALUES (%s, %s)", (second_t, person_id))
        connection.commit()
    if third_t:
        cursor.execute("INSERT INTO site (siteAddress, person_idperson) VALUES (%s, %s)", (third_t, person_id))
        connection.commit()




def read_person_query(first_name):
    select_person = "SELECT * FROM person WHERE fName = %s"
    cursor.execute(select_person, (first_name,))
    return cursor.fetchone()

def update_person_query(idperson, first, last, city, address, country, email):
    update_person = "UPDATE person SET fName = %s, lName = %s, city = %s, Address = %s, country = %s, email = %s WHERE idperson = %s"
    cursor.execute(update_person, (first, last, city, address, country, email, idperson))
    connection.commit()

def delete_person_query(idperson):
    delete_person = "DELETE FROM person WHERE idperson = %s"
    cursor.execute(delete_person, (idperson,))
    connection.commit()



def select_all_query(table_name):
    fetch_query = f"SELECT * FROM {table_name}"
    cursor.execute(fetch_query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return columns, result
def count_persons_by_country_query(country_name):
    count_persons = f"SELECT COUNT(*) FROM person WHERE country = '{country_name}'"
    cursor.execute(count_persons)
    result = cursor.fetchone()[0]
    return result

def count_id_sum_query(id_column_name,table_name):
    sum_id_query = f"SELECT SUM({id_column_name}) FROM {table_name}"
    cursor.execute(sum_id_query)
    result = cursor.fetchone()[0]
    return result

def count_rows_query(table_name):
    count_rows = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(count_rows)
    return cursor.fetchone()[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form.get('first')
        last_name = request.form.get('last')
        city = request.form.get('city')
        address = request.form.get('address')
        country = request.form.get('country')
        email = request.form.get('email')
        first_c = request.form.get('firstC')
        second_c = request.form.get('secondC')
        third_c = request.form.get('thirdC')
        first_p = request.form.get('firstP')
        second_p = request.form.get('secondP')
        third_p = request.form.get('thirdP')
        first_l = request.form.get('firstL')
        second_l = request.form.get('secondL')
        third_l = request.form.get('thirdL')
        first_h = request.form.get('firstH')
        second_h = request.form.get('secondH')
        third_h = request.form.get('thirdH')
        first_t = request.form.get('firstT')
        second_t = request.form.get('secondT')
        third_t = request.form.get('thirdT')

        insert_person(first_name, last_name, city, address, country, email)

        cursor.execute("SELECT LAST_INSERT_ID()")
        person_id = cursor.fetchone()[0]

        insert_courses(first_c, second_c, third_c, person_id)
        insert_projects(first_p, second_p, third_p, person_id)
        insert_hobbies(first_h,second_h,third_h,person_id)
        insert_languages(first_l,second_l,third_l,person_id)
        insert_trainings(first_t,second_t,third_t,person_id)

        return "Data inserted successfully!"
    else:
        return render_template('index.html')

# Flask routes for CRUD operations

@app.route('/read_person', methods=['POST'])
def read_person():
    first_name = request.form['first_name']
    # Get person details
    person = read_person_query(first_name)
    
    person_id = person[0]
    # Get courses for the person
    cursor.execute("SELECT courseName FROM course WHERE person_idperson = %s", (person_id,))
    courses = [row[0] for row in cursor.fetchall()]

    # Get languages for the person
    cursor.execute("SELECT languageName FROM language WHERE person_idperson = %s", (person_id,))
    languages = [row[0] for row in cursor.fetchall()]

    # Get hobbies for the person
    cursor.execute("SELECT hobbyName FROM hobby WHERE person_idperson = %s", (person_id,))
    hobbies = [row[0] for row in cursor.fetchall()]

    # Get training for the person
    cursor.execute("SELECT siteAddress FROM site WHERE person_idperson = %s", (person_id,))
    training = [row[0] for row in cursor.fetchall()]
    return render_template('person.html', person=person, courses=courses, languages=languages, hobbies=hobbies, training=training)

@app.route('/update_person', methods=['POST'])
def update_person():
    idperson = request.form['idperson']
    first = request.form['first']
    last = request.form['last']
    city = request.form['city']
    address = request.form['address']
    country = request.form['country']
    email = request.form['email']
    # Call  update_person function 
    update_person_query(idperson, first, last, city, address, country, email)
    updatedPerson = read_person_query(first)
    return render_template('person.html', person=updatedPerson,title = "UPDATED")

@app.route('/delete_person', methods=['POST'])
def delete_person():
    idperson = request.form['idperson']
    delete_person_query(idperson)
    return "Person deleted successfully!"

# Flask Code for Aggregation functions
@app.route('/count_persons_by_country', methods=['POST'])
def count_persons_by_country():
    country_name = request.form['country_name']
    result = count_persons_by_country_query(country_name)
    return render_template('aggregate_result.html', result=result)

@app.route('/sum_id_column', methods=['POST'])
def sum_id_column():
    table_name = request.form['table_name']
    id_column_name = f"id{table_name}"
    result = count_id_sum_query(id_column_name,table_name)
    return render_template('aggregate_result.html', result=result)

@app.route('/count_rows', methods=['POST'])
def count_rows():
    table_name = request.form['table_name']
    result = count_rows_query( table_name)
    return render_template('aggregate_result.html', result=result)

@app.route('/fetch_table_data', methods=['POST'])
def fetch_table_data():
    table_name = request.form['table_name']
    columns,result = select_all_query(table_name)
    return render_template('fetch_table_data.html', table_name=table_name, result=result, columns=columns)


if __name__ == '__main__':
    app.run(debug=True)