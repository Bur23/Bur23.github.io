#!/usr/bin/env python3

import cgi
import random

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>My first server-side script. </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')
def getData():
    form = cgi.FieldStorage()
    answer = form.getvalue('birth')
    if answer == 'August':
        print('You are correct, his birthday is in August!')
    else:
        print('You are incorrect, his birthday is in August.')
    answer2 = form.getvalue('name')
    if answer2 == 'Mitchell':
       print('You are correct, his full name is Cole Mitchell Sprouse!')
    else:
       print('You are incorrect, his full name is Cole Mitchell Sprouse.')

    answer3 = form.getvalue('parents')
    if answer3 == 'Melanie Matthew':
        print('You are correct, Melanie and Matthew are the names of his parents!')
    else:
        print('You are incorrect, Melanie and Matthew are the names of his parents.')

    answer4 = form.getvalue('fiction')
    if answer4 == 'Jughead':
        print('You are correct, his fictional name in Riverdale is indeed Jughead!')
    else:
        print('You are incorrect, Jughead is his fictional name.')

    answer5 = form.getvalue('location')
    if answer5 == 'Italia':
        print('You are correct, Cole is from Italia!')
    else:
        print('You are incorrect, Cole is from Italia.')

    answer6 = form.getvalue('twin')
    if answer6 == 'Thomas':
        print('You are correct, his twin brother is Dylan!')
    else:
        print('You are incorrect, his twin brother is Dylan.')

    answer7 = form.getvalue('friends')
    if answer7 == 'Ben':
        print('You are correct, it is Ben Geller!')
    else:
        print('You are incorrect, it is Ben Geller.')

    answer8 = form.getvalue('role')
    if answer8 == 'Daddy':
        print('You are correct, it is Big Daddy!')
    else:
        print('You are incorrect, it is Big Daddy.')

    answer9 = form.getvalue('girlfriend')
    if answer9 == 'Lili':
        print('You are correct, it is Lili!')
    else:
        print('You are incorrect, it is Lili.')

    answer10 = form.getvalue('age')
    if answer10 == '26':
        print('You are correct, he is currently 26 years old!')
    else:
        print('You are incorrect, he is currently 26 years old.')
        
 

def main():
    htmlTop()
    print(''.format(getData()))
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()