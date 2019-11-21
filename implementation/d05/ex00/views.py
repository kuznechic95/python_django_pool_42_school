# from django.shortcuts import render
import psycopg2
from django.http import HttpResponse


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
            CREATE TABLE IF NOT EXISTS ex00_movies (
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
