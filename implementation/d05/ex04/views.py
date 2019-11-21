from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
from django.forms import Form

# def drop_table(connection, tablename):
#     curr = connection.cursor()
#     print("""DROP TABLE %s CASCADE""" % tablename)
#     curr.execute("""DROP TABLE %s CASCADE""" % tablename)
#     connection.commit()
#
# def create_table(connection, tablename, content):
#     sql_string = "(\n"
#     i = 0
#     curr = connection.cursor()
#     for key, value in content.items():
#         i += 1
#         if i < len(content):
#             sql_string += "    %s %s,\n" % (key, value)
#         else:
#             sql_string += "    %s %s\n" % (key, value)
#     sql_string += ")"
#     curr.execute("""CREATE TABLE %s %s""" % (tablename, sql_string))
#     connection.commit()
#     return connection


def remove_row(connection, tablename, key, value):
    try:
        sql_string = ''
        curr = connection.cursor()
        curr.execute(f"DELETE FROM {tablename} WHERE {tablename}.{key}='{value}';")
        connection.commit()
    except Exception as e:
        print('Error : ', e)
    return connection


def init(request):
    try:
        connection = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
            title varchar(64) UNIQUE NOT NULL,
            episode_nb serial PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            """)
        connection.commit()
        if cursor and not cursor.closed:
            cursor.close()
    except psycopg2.Error as e:
        print('Error : ', e)
        resp_str = 'Error :' + str(e)
        return HttpResponse(resp_str)
    finally:
        if connection and not connection.closed:
            connection.close()
            # print("PostgreSQL connection is closed")
    return HttpResponse('OK')


def populate(request):
    buf = ""
    data = [
        {
            'title': "The Phantom Menace",
            'episode_nb': 1,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "Attack of the Clones",
            'episode_nb': 2,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-16"
        },
        {
            'title': "Revenge of the Sith",
            'episode_nb': 3,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-19"
        },
        {
            'title': "A New Hope",
            'episode_nb': 4,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "The Empire Strikes Back",
            'episode_nb': 5,
            'opening_crawl': "",
            'director': "Irvin Kershner",
            'producer': "Gary Kutz, Rick McCallum",
            'release_date': "1980-05-17"
        },
        {
            'title': "Return of the Jedi",
            'episode_nb': 6,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        },
        {
            'title': "The Force Awakens",
            'episode_nb': 7,
            'opening_crawl': "",
            'director': "J. J. Abrams",
            'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            'release_date': "2015-12-11"
        },
    ]
    try:
        connection = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        cursor = connection.cursor()
        for item in data:
            try:
                cursor.execute("""
                INSERT INTO ex04_movies 
                (title, episode_nb, opening_crawl,
                 director, producer, release_date) 
                VALUES (%(title)s, %(episode_nb)s, %(opening_crawl)s, 
                %(director)s, %(producer)s, %(release_date)s)""", item)
                connection.commit()
                buf += "OK<br>"
            except Exception as e:
                print('Error : ', e)
                buf += f"Error: {item['title']} ::{e}<br>"
        if cursor and not cursor.closed:
            cursor.close()
    except psycopg2.Error as e:
        print('Error : ', e)
    finally:
        if connection and not connection.closed:
            connection.close()
        # print("PostgreSQL connection is closed")
    return HttpResponse(buf)


def display(request):
    response = None
    try:
        connection = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        cursor = connection.cursor()
        cursor.execute("""SELECT
        episode_nb,
        title,
        opening_crawl,
        director,
        producer,
        release_date
        from ex04_movies
        ORDER BY episode_nb""")
        response = cursor.fetchall()
    except Exception as e:
        print('Error : ', e)
        return HttpResponse("No data available")
    finally:
        if connection and not connection.closed:
            connection.close()
    if response:
        return render(request, 'ex04/display.html', {'data': response})
    else:
        return HttpResponse("No data available")


def remove(request):
    response = None
    try:
        connection = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )

        if request.method == 'POST':
            form = Form(request.POST)
            if form.is_valid() and request.POST['select']:
                remove_row(connection, 'ex04_movies', 'episode_nb', request.POST['select'])

        cursor = connection.cursor()
        form = Form()
        try:
            cursor.execute("""SELECT episode_nb,
            title,
            opening_crawl,
            director,
            producer,
            release_date
            from ex04_movies
            ORDER BY episode_nb""")
            response = cursor.fetchall()
        except Exception as e:
            print('Error : ', e)
            return HttpResponse("No data available")
        if cursor and not cursor.closed:
            cursor.close()
    except psycopg2.Error as e:
        print('Error : ', e)
    finally:
        if connection and not connection.closed:
            connection.close()
    if response:
        return render(request, 'ex04/remove.html', {'data': response, 'form': form})
    else:
        return HttpResponse("No data available")


