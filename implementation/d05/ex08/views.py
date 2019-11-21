from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import psycopg2

def init(request):
    command1 ="""CREATE TABLE IF NOT EXISTS ex08_planets (
                id serial PRIMARY KEY,
                name varchar(64) UNIQUE NOT NULL,
                climate text,
                diameter int,
                orbital_period int,
                population bigint,
                rotation_period int,
                surface_water float,
                terrain varchar(128)
            )"""
    command2 = """CREATE TABLE IF NOT EXISTS ex08_people (
                id serial PRIMARY KEY,
                name varchar(64) UNIQUE NOT NULL,
                birth_year varchar(32),
                gender varchar(32),
                eye_color varchar(32),
                hair_color varchar(32),
                height int,
                mass float,
                homeworld varchar(64) REFERENCES ex08_planets(name)
            )"""
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='',
            user='djangouser',
            password='secret'
        )
        cur = conn.cursor()
        cur.execute(command1)
        cur.execute(command2)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return HttpResponse(str(error.pgerror.replace('\n', '<br />')))
    finally:
        if conn is not None:
            conn.close()
    return HttpResponse("OK.")


def populate(request):
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='',
            user='djangouser',
            password='secret'
        )
        cur = conn.cursor()
        cols1 = ('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period',
                        'surface_water', 'terrain')
        cols2 = ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height',
                        'mass', 'homeworld')
        with open('ex08/resources/planets.csv', 'r') as file:
            cur.copy_from(file, 'ex08_planets', columns=cols1, null='NULL')
        with open('ex08/resources/people.csv', 'r') as file:
            cur.copy_from(file, 'ex08_people', columns=cols2, null='NULL')
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return HttpResponse(str(error.pgerror.replace('\n', '<br />')))
    finally:
        if conn is not None:
            conn.close()
    return HttpResponse("OK.")


def display(request):
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='',
            user='djangouser',
            password='secret'
        )
        cur = conn.cursor()
        cur.execute("""SELECT people.name, people.homeworld, planets.climate  
    FROM ex08_people AS people
    JOIN ex08_planets AS planets ON (people.homeworld = planets.name)
    WHERE planets.CLIMATE LIKE '%windy%'
    ORDER BY people.name
    """)
        response = cur.fetchall()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError):
        return HttpResponse('No data available')
    finally:
        if conn is not None:
            conn.close()
    if response:
        response = [list(item) for item in response]
        for i in range(len(response)):
            response[i][-1] = str(response[i][-1])
        return render(request, 'ex08/display.html', {'people': response})
    else:
        return HttpResponse('No data available')
