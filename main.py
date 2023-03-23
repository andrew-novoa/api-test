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


@app.get("/")
async def root():
    return {"message": "hello"}


@app.get("/user")
async def user_details():
    return {"instrument": default_instrument, "user progress": user_progress, "user language": default_language}


@app.get("/{book}")
async def book_details(book: str, chapter: Optional[int] = None):
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


@app.get("/{book}/{lesson_id}")
async def lesson_details(book: str, lesson_id: str):
    return question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]


@app.get("/{book}/{lesson_id}/generate")
async def generate_lesson(book: str, lesson_id: str, q: Optional[int] = None):
    user_level = book[0].upper() + lesson_id
    question_dict = {}
    for lesson_number in range(1, 21):
        question_type = random.choice(list(question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]["question choices"].keys()))
        answer_type = random.choice(list(question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]["question choices"][question_type].keys()))
        screen = generate_screen(question_type, answer_type, user_level, default_language)
        question_dict[lesson_number] = [screen[0], str(screen[1]), screen[2], str(screen[3])]
    if q:
        return question_dict[q]
    return question_dict

