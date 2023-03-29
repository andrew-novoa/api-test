import random
from typing import Optional

from fastapi import FastAPI

import user
from generate import generate_screen
from levels import question_levels

app = FastAPI()

default_instrument = user.instrument
user_progress = user.level_progress
default_language = user.lang


def get_user_level_details(user_level):
    book_map = {"T": "theory", "R": "rhythm", "L": "listen"}
    book = book_map[user_level[0]]
    lesson_id = user_level[1:]
    return book, lesson_id


def generate_question_list(user_level, number_of_questions):
    question_dict = {"lessons": {}}

    while len(question_dict["lessons"]) < number_of_questions:
        if isinstance(user_level, list):
            user_level = random.choice(user_level)

        book, lesson_id = get_user_level_details(user_level)

        chapter, lesson = int(lesson_id[0]), int(lesson_id[-1])
        lessons = question_levels[default_instrument][book][chapter]["lessons"][lesson]
        question_type = random.choice(list(lessons["question choices"].keys()))
        answer_type = random.choice(list(lessons["question choices"][question_type].keys()))

        screen = generate_screen(question_type, answer_type, user_level, default_language)
        prompt_text, question_render, question_text, answer_elements = screen

        question_dict["lessons"][len(question_dict["lessons"]) + 1] = [prompt_text, question_render, question_text, answer_elements]

    return question_dict


@app.get("/")
async def root():
    return {"message": "welcome to my API :)"}


@app.get("/user")
async def user_details():
    return {"instrument": default_instrument, "user progress": user_progress, "user language": default_language}


@app.get("/practice")
async def practice_details():
    return {"user progress": user_progress}


@app.get("/practice/generate")
async def generate_practice(q: Optional[int] = None):
    number_of_questions = q or 20
    return generate_question_list(user_progress, number_of_questions)


@app.get("/{book}")
async def book_details(book: str, chapter: Optional[int] = None):
    if book not in ["theory", "listen", "rhythm"]:
        return {"Error": "Not a valid book type"}

    if chapter:
        chapter_details = question_levels[default_instrument][book][chapter]
        lesson_names = [lesson["lesson name"] for lesson in chapter_details["lessons"].values()]
        return {"number": chapter, "name": chapter_details["chapter name"], "lesson names": lesson_names}

    output_dict = {}
    for chapter_num, chapter_details in question_levels[default_instrument][book].items():
        lesson_length = len(chapter_details["lessons"])
        lesson_names = [lesson["lesson name"] for lesson in chapter_details["lessons"].values()]
        output_dict[chapter_num] = {"number": chapter_num, "name": chapter_details["chapter name"], "length": lesson_length, "lesson names": lesson_names}

    return output_dict


@app.get("/{book}/{lesson_id}")
async def lesson_details(book: str, lesson_id: str):
    if book not in ["theory", "listen", "rhythm"]:
        return {"Error": "Not a valid book type"}

    chapter, lesson = int(lesson_id[0]), int(lesson_id[-1])

    if chapter not in question_levels[default_instrument][book]:
        return {"Error": "Not a valid chapter number"}

    if lesson not in question_levels[default_instrument][book][chapter]["lessons"]:
        return {"Error": "Not a valid lesson number"}

    return question_levels[default_instrument][book][chapter]["lessons"][lesson]


@app.get("/{book}/{lesson_id}/generate")
async def generate_lesson(book: str, lesson_id: str):
    if book not in ["theory", "listen", "rhythm"]:
        return {"Error": "Not a valid book type"}

    chapter, lesson = int(lesson_id[0]), int(lesson_id[-1])

    if chapter not in question_levels[default_instrument][book]:
        return {"Error": "Not a valid chapter number"}

    if lesson not in question_levels[default_instrument][book][chapter]["lessons"]:
        return {"Error": "Not a valid lesson number"}

    number_of_questions = 20
    user_level = book[0].upper() + lesson_id

    return generate_question_list(user_level, number_of_questions)
