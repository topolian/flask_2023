from flask import Flask, request

from utils import generate_password as gp, generate_users as gu, read_requirements_txt as rr, astros_number as astr, mean_height_weight as mean_hw

app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return 'Hello, World!'


@app.route('/generate-password/')
def generate_password():
    password_len = request.args.get('password-len')

    if not password_len:
        password_len = 10
    else:
        if password_len.isdigit():
            password_len = int(password_len)
        else:
            return 'invalid param. must be int'

    password = gp(password_len)
    print('password-len', password_len)
    return f'{password}'


@app.route('/requirements/')
def read_requirements_txt():
    requirements_content = rr()

    return requirements_content


@app.route('/generate-users/')
def generate_users():
    users = gu()

    return users


@app.route('/space/')
def astros_number():
    astros_number = str(astr())

    return astros_number


@app.route('/mean/')
def mean():
    mean_hw_params = mean_hw()

    return mean_hw_params


@app.route('/emails/create/')
def create_email():
    import sqlite3

    con = sqlite3.connect("example.db")
    #http://127.0.0.1:5000/emails/create/?contactName=Alex&emailValue=awdaw@mail.com
    contact_name = request.args['contactName']
    email_value = request.args['emailValue']

    cur = con.cursor()
    sql_query = f'''
    INSERT INTO emails (contactName, emailValue)
    VALUES ('{contact_name}', '{email_value}');
    '''
    cur.execute(sql_query)
    con.commit()
    con.close()

    return 'create_email'


@app.route('/emails/read/')
def read_email():
    import sqlite3

    con = sqlite3.connect("example.db")
    cur = con.cursor()
    sql_query = f'''
        SELECT * FROM emails;
        '''
    cur.execute(sql_query)
    result = cur.fetchall()
    con.close()

    return str(result)


@app.route('/emails/update/')
def update_email():
    import sqlite3

    #http://127.0.0.1:5000/emails/create/?contactName=Alex&emailValue=awdaw@mail.com
    contact_name = request.args['contactName']
    email_value = request.args['emailValue']

    con = sqlite3.connect("example.db")
    cur = con.cursor()
    sql_query = f'''
    UPDATE emails
    SET contactName = '{contact_name}'
    WHERE emailValue = '{email_value}';
    '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'update_email'


@app.route('/emails/delete/')
def delete_email():
    import sqlite3

    con = sqlite3.connect("example.db")
    cur = con.cursor()
    sql_query = f'''
            DELETE FROM emails;
            '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'delete_email'


@app.route('/phones/create/')
def create_phone():
    import sqlite3

    con = sqlite3.connect("example.db")
    contact_name = request.args['contactName']
    phone_value = request.args['phoneValue']

    cur = con.cursor()
    sql_query = f'''
    INSERT INTO phones (contactName, phoneValue)
    VALUES ('{contact_name}', '{phone_value}');
    '''
    cur.execute(sql_query)
    con.commit()
    con.close()

    return 'create_phone'


@app.route('/phones/read/')
def read_phone():
    import sqlite3

    con = sqlite3.connect("example.db")
    cur = con.cursor()
    sql_query = f'''
        SELECT * FROM phones;
        '''
    cur.execute(sql_query)
    result = cur.fetchall()
    con.close()

    return str(result)


@app.route('/phones/delete/')
def delete_phone():
    import sqlite3

    con = sqlite3.connect("example.db")
    cur = con.cursor()
    sql_query = f'''
            DELETE FROM phones;
            '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'delete_phone'


@app.route('/phones/update/')
def update_phone():
    import sqlite3

    contact_name = request.args['contactName']
    phone_value = request.args['phoneValue']

    con = sqlite3.connect("example.db")
    cur = con.cursor()
    sql_query = f'''
    UPDATE phones
    SET contactName = '{contact_name}'
    WHERE phoneValue = '{phone_value}';
    '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'update_phone'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
