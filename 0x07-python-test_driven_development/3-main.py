#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Ayo", "")
try:
    say_my_name("A", "B", "C")
except Exception as e:
    print(e)
