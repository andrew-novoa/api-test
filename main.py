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
    return {"message": "welcome to my API :)"}


### General user details ###
@app.get("/user")
async def user_details():
    return {"instrument": default_instrument, "user progress": user_progress, "user language": default_language}


### Used to get general details about the book type: "theory", "listen", or "rhythm" ###
### Can query the chapter number to get more info about the queried chapter ###
@app.get("/{book}")
async def book_details(book: str, chapter: Optional[int] = None):
    if book not in ["theory", "listen", "rhythm"]:
        return {"Error:" "Not a valid book type"}
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
    return question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]


### Is used to generate any number of questions and answers ###
@app.get("/{book}/{lesson_id}/generate")
async def generate_lesson(book: str, lesson_id: str):
    number_of_questions = 20
    user_level = book[0].upper() + lesson_id
    question_dict = {}
    question_dict["lessons"] = {}
    while len(question_dict["lessons"]) != number_of_questions:
        question_type = random.choice(list(question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]["question choices"].keys()))
        answer_type = random.choice(list(question_levels[default_instrument][book][int(lesson_id[0])]["lessons"][int(lesson_id[-1])]["question choices"][question_type].keys()))
        screen = generate_screen(question_type, answer_type, user_level, default_language)

        prompt_text = screen[0]
        question_render = str(screen[1]) ### can be None
        question_text = screen[2]
        answer_elements = str(screen[3]) ### can be many formats, if multiple choice, will return tuple

        question_dict["lessons"][len(question_dict["lessons"]) + 1] = [prompt_text, question_render, question_text, answer_elements]

    return question_dict

