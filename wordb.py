import sqlite3
import main

conn = sqlite3.connect('words.db')
# conn = sqlite3.connect(':memory:')
c = conn.cursor()

# c.execute("""CREATE TABLE words(
#              word text,
#              meaning text,
#              example text,
#              comment text
#         )""")

def insert_word():
    if(main.meaning_error==False and main.example_error == True and main.note == "NULL"):
        c.execute("INSERT INTO words VALUES (?,?,?,?)",
                  (main.word,main.word_slice, main.word_example, main.note))

    if(main.meaning_error==False and main.example_error == True and main.note != "NULL"):
        c.execute("INSERT INTO words VALUES (?,?,?,?)",
                  (main.word,main.word_slice, main.word_example, main.note))

    if(main.meaning_error==False and main.example_error != True and main.note != "NULL"):
        c.execute("INSERT INTO words VALUES (?,?,?,?)",
                  (main.word,main.word_slice, main.word_example, main.note))

    if (main.meaning_error == False and main.example_error != True and main.note == "NULL"):
        c.execute("INSERT INTO words VALUES (?,?,?,?)",
                  (main.word, main.word_slice, main.word_example, main.note))


def get_words():
    # c.execute("SELECT * FROM words where word=?",('hey'))
    c.execute("SELECT * FROM words")
    print(c.fetchall())
    # c.fetchmany()
    # c.fetchall()



def remove_word():
    pass

insert_word()



get_words()

ans = input("Want to Update")
if(ans == "Y"):
    updated_word = input("Which word you want to update").lower()
    new_comment = input("What is the new comment")

def update_word():
    new_word = updated_word
    with conn:
        c.execute("""UPDATE words SET comment = :new_comment WHERE word = :new_word""")

update_word()


conn.commit()

conn.close()