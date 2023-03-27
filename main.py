from fastapi import FastAPI
from typing import Optional
import random
import user
from generate import generate_screen
from levels import question_levels

app = FastAPI()

### User Defaults ###
default_instrument = user.instrument
user_progress = user.level_progress
default_language = user.lang


def get_user_level_details(user_level):
    if user_level[0] == "T":
        book = "theory"
    elif user_level[0] == "R":
        book = "rhythm"
    elif user_level[0] == "L":
        book = "listen"

    lesson_id = user_level[1:]

    return book, lesson_id

def generate_question_list(user_level, number_of_questions):

    if type(user_level) == str:
        user_level_details = get_user_level_details(user_level)
        book = user_level_details[0]
        lesson_id = user_level_details[1]

    question_dict = {}
    question_dict["lessons"] = {}
    while len(question_dict["lessons"]) != number_of_questions:
        if type(user_level) == list:
            user_level = random.choice(user_level)
            user_level_details = get_user_level_details(user_level)
            book = user_level_details[0]
            lesson_id = user_level_details[1]

        question_type = random.choice(list(question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]["question choices"].keys()))
        answer_type = random.choice(list(question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]["question choices"][question_type].keys()))
        screen = generate_screen(question_type, answer_type, user_level, default_language)

        prompt_text = screen[0]
        question_render = screen[1] ### can be None
        question_text = screen[2]
        answer_elements = str(screen[3]) ### can be many formats, if multiple choice, will return tuple

        question_dict["lessons"][len(question_dict["lessons"]) + 1] = [prompt_text, question_render, question_text, answer_elements]

    return question_dict


@app.get("/")
async def root():
    return {"message": "welcome to my API :)"}


### General user details ###
@app.get("/user")
async def user_details():
    return {"instrument": default_instrument, "user progress": user_progress, "user language": default_language}


@app.get("/practice")
async def practice_details():
    return {"user progress": user_progress}


@app.get("/practice/generate")
async def generate_practice(q: Optional[int] = None):
    if q:
        number_of_questions = q
    else:
        number_of_questions = 20
    user_levels = user_progress
    question_dict = generate_question_list(user_levels, number_of_questions)

    return question_dict


### Used to get general details about the book type: "theory", "listen", or "rhythm" ###
### Can query the chapter number to get more info about the queried chapter ###
@app.get("/{book}")
async def book_details(book: str, chapter: Optional[int] = None):

    if book not in ["theory", "listen", "rhythm"]:
        return {"Error": "Not a valid book type"}
    
    output_dict = {}
    if chapter:
        lesson_names = []
        for l in list(question_levels[default_instrument][book][chapter]["lessons"].keys()):
            lesson_names.append(question_levels[default_instrument][book][chapter]["lessons"][l]["lesson name"])
        return {"number": chapter, "name": question_levels[default_instrument][book][chapter]["chapter name"], "lesson names": lesson_names}
    
    for chapter_num in list(question_levels[default_instrument][book].keys()):
        lesson_length = len(list(question_levels[default_instrument][book][chapter_num]["lessons"].keys()))
        lesson_names = []
        for l in list(question_levels[default_instrument][book][chapter_num]["lessons"].keys()):
            lesson_names.append(question_levels[default_instrument][book][chapter_num]["lessons"][l]["lesson name"])
        output_dict[chapter_num] = {"number": chapter_num, "name": question_levels[default_instrument][book][chapter_num]["chapter name"], "length": lesson_length, "lesson names": lesson_names}
    return output_dict


### Lesson ids are in "chapter-lesson" format, e.g. "3-1". Used to see what question and answer types are available ###
@app.get("/{book}/{lesson_id}")
async def lesson_details(book: str, lesson_id: str):

    if book not in ["theory", "listen", "rhythm"]:
        return {"Error": "Not a valid book type"}
    if int(lesson_id[0]) not in list(question_levels[default_instrument][book].keys()):
        return {"Error": "Not a valid chapter number"}
    if int(lesson_id[-1]) not in list(question_levels[default_instrument][book][int(lesson_id[0])]["lessons"].keys()):
        return {"Error": "Not a valid lesson number"}
    
    return question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]


### Is used to generate any number of questions and answers ###
@app.get("/{book}/{lesson_id}/generate")
async def generate_lesson(book: str, lesson_id: str):

    if book not in ["theory", "listen", "rhythm"]:
        return {"Error": "Not a valid book type"}
    if int(lesson_id[0]) not in list(question_levels[default_instrument][book].keys()):
        return {"Error": "Not a valid chapter number"}
    if int(lesson_id[-1]) not in list(question_levels[default_instrument][book][int(lesson_id[0])]["lessons"].keys()):
        return {"Error": "Not a valid lesson number"}
    
    number_of_questions = 20
    user_level = book[0].upper() + lesson_id
    question_dict = generate_question_list(user_level, number_of_questions)

    return question_dict


