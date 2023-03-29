import random

from googletrans import Translator
from music21 import (chord, harmony, interval, key, musicxml, note, pitch,
                     scale, stream)
from scamp import *

import user
from levels import question_levels
from qa_util import *
from theory import *

#149 possible combinations#
def generate_question(input_question_type, input_answer_type, input_user_level): #will need to take into consideration the blank notes

    if input_question_type == "text":
        question_options_dict = {
            "text":{
            "chord intervals": ["What are the intervals that make up a *chord*?", "chord"],
            "chord intervals half steps": ["How many half steps are there between each note in a *chord*?", "chord"],
            "interval semitones": ["How many semitones make up a *interval*?", "interval"],
            "scale dominant": ["What is the dominant of a *scale*?", "scale"],
            "scale degree": ["What is the *scale degree* of a *scale*?", "scale"],
            "key signature": ["How many accidentals are in the key of *key*?", "scale"],
            "note value subdivision": ["How many *subdivision*s add up to a *note value*?", "note value"],
            "note value duration": ["How many beats is a *note value* worth?", "note value"]
            },

            "piano":{
            "play pitch": ["Play a *pitch*.", "note"],
            "play chord tone": ["Play the *chord tone* of a *chord*.", "chord"],
            "play second note in interval": ["Use the piano to play the second note in a *simple interval*.", "interval"],
            "play interval": ["Play the interval of a *simple interval*.", "interval"],
            "play scale degree": ["Play the *scale degree* of a *scale*.", "scale"],
            "play arp chord tone": ["Play the *chord tone* of a *chord* arpeggio.", "arpeggio"]
            },

            "record":{
            "play pitch": ["Play a *pitch*.", "note"],
            "play chord": ["Play a *chord* chord.", "chord"],
            "play scale": ["Play a *scale* scale.", "scale"],
            "play arp": ["Play a *chord* arpeggio.", "arpeggio"]
            },

            "mc text":{
            "convert roman": ["What is *roman numeral* in the key of *key text*?", "chord progression"],
            "relative minor": ["Which is the relative minor of a *scale*?", "scale"],
            "diatonic chord": ["Which of these chords is diatonic to a *scale*?", "scale"],
            "nondiatonic chord": ["Which of these chords is nondiatonic to a *scale*?", "scale"],
            "note value subdivision": ["How many *subdivision*s add up to a *note value*?", "rhythm"],
            "note value duration": ["What is the duration of a *note value*?", "note value"]
            },

            "mc xml":{
            "correct inversion": ["Which of these is a *inversion* of a *chord*?", "chord"],
            "possible mode": ["Which of these options is a mode of a *scale*?", "scale"],
            "relative minor": ["Which of these scales is the relative minor of a *scale*?", "scale", {1: ["ionian"]}],
            "diatonic chord": ["Which of these chords is diatonic to a *scale*?", "scale"],
            "nondiatonic chord": ["Which of these chords is nondiatonic to a *scale*?", "scale"]   
            },

            "mc audio":{
            "chord quality": ["Which sample is of a *chord quality*?", "chord"],
            "chord inversion": ["Which sample is of a *chord quality* in *inversion*?", "chord"],
            "correct interval audio": ["Which sample correctly plays a *simple interval*?", "interval"],
            "correct scale mode audio": ["Which of these samples match a *scale mode*?", "scale"],   
            "correct arp quality": ["Which sample is of a *chord quality* arpeggio?", "arpeggio"],
            "correct arp inversion": ["Which sample is of a *chord quality* arpeggio in *simple interval*?", "arpeggio"]  
            },

            "drag drop keyboard":{
            #PASS
            },

            "drag drop snippet":{
            #PASS
            }
            }

    elif input_question_type == "audio":
        question_options_dict = {
            "text":{
            "chord quality": ["Identify the chord quality.", "chord"], 
            "chord inversion": ["This chord is in what inversion?", "chord"],
            "chord intervals": ["What are the intervals that make up this chord?", "chord"],
            "chord intervals half steps": ["How many half steps are there between each note?", "chord"],
            "diatonic or not": ["Is this chord progression diatonic or not?", "chord progression"],
            "identify interval": ["Identify this interval.", "interval"], 
            "interval semitones": ["How many semitones make up this interval?", "interval"],
            "up or down": ["Does this interval move up or down?", "interval"],
            "scale mode": ["Identify the scale mode.", "scale"],
            "note value subdivision": ["How many *subdivision*s add up to this note?", "rhythm"],
            "beats": ["How many beats does this whole rhythm take up?", "rhythm"],
            "note value duration": ["What is the duration of this note?", "rhythm"],
            "arp quality": ["This arpeggio is of what quality?", "arpeggio"],
            "arp inversion": ["This arpeggio is in what inversion?", "arpeggio"]
            },

            "piano":{
            #PASS
            },

            "record":{
            "play rhythm": ["Play this rhythm.", "rhythm"]
            },

            "mc text":{
            "quality": ["Which is the correct chord quality played?", "chord"], 
            "inversion": ["This chord is in what inversion?", "chord"],
            "roman numerals": ["Which is the correct roman numeral notation for this progression?", "chord progression"],
            "correct name": ["Which is the correct name for this interval?", "interval"],
            "mode name": ["Which of these options is the correct name for this mode?", "scale"],
            "note value subdivision": ["How many *subdivision*s add up to this note?", "rhythm"],
            "beats": ["How many beats does this whole rhythm take up?", "rhythm"],
            "note value duration": ["What is the duration of this note?", "rhythm"],
            "arp quality": ["This arpeggio is of what quality?", "arpeggio"],
            "arp inversion": ["This arpeggio is in what inversion?", "arpeggio"]
            },

            "mc xml":{
            "same duration": ["Which of these rhythms have the same duration as the example?", "rhythm"]
            },

            "mc audio":{
            "inversion": ["Which sample is the *inversion* of the chord played?", "chord"],
            "correct audio": ["Which sample correctly plays this interval?", "interval"],
            "correct quality": ["Which sample is the same quality as the one played?", "arpeggio"],
            "correct inversion": ["Which sample is the same inversion as the one played?", "arpeggio"]
            },

            "drag drop keyboard":{
            #PASS
            },

            "drag drop snippet":{
            #PASS
            }
            }

    elif input_question_type == "note":
        question_options_dict = {
            "text":{
            "identify": ["Identify this note.", "note"], 
            "black or white": ["Is this note on a white key or a black key?", "note"]
            },

            "piano":{
            "play pitch": ["Play the presented note.", "note"]
            },

            "record":{
            "play pitch": ["Play the presented note.", "note"]
            },

            "mc text":{
            "identify pitch": ["Identify this note.", "note"],
            "identify duration": ["Identify this duration.", "note"] 
            },

            "mc xml":{
            "match": ["Match to the correct notation.", "note"]
            },

            "drag drop keyboard":{
            "drag": ["Drag note into correct position.", "note"]
            }
            }

    elif input_question_type == "chord":
        question_options_dict = {
            "text": {
            "quality": ["Identify the chord quality.", "chord"], 
            "inversion": ["This chord is in what inversion?", "chord"],
            "intervals": ["What are the intervals that make up this chord?", "chord"],
            "intervals half steps": ["How many half steps are there between each note?", "chord"]
            },

            "piano":{
            "play chord tone": ["Play the *chord tone* of this chord.", "chord"]
            },

            "record":{
            "play chord": ["Play this *chord* chord.", "chord"]
            },

            "mc text":{
            "quality": ["Which is the correct chord quality?", "chord"], 
            "inversion": ["This chord is in what inversion?", "chord"]
            },

            "mc xml":{
            "correct inversion": ["Which of these are correctly inverted into *inversion*?", "chord"],
            "correct interval transposition": ["Which of these are a correctly transposed *directed interval*?", "chord"]
            },

            "mc audio":{
            "quality": ["Which sample is the correct chord quality?", "chord"],
            "inversion": ["Which sample is the correct inversion?", "chord"]
            },

            "drag drop keyboard":{
            "complete chord": ["Use the keyboard to complete this *chord symbol*.", "chord"],
            "add note": ["Use the keyboard to add this note to the chord.", "chord"],
            "build chord": ["Use the keyboard to build this *chord symbol*.", "chord"]
            }
            }

    elif input_question_type == "chord progression":
        question_options_dict = {
            "text":{
            "diatonic or not": ["Is this chord progression diatonic or not?", "chord progression"]
            },

            "record":{
            "play progression": ["Play this chord progression.", "chord progression"]
            },

            "mc text":{
            "determine key": ["Which key is this chord progression in?", "chord progression"],
            "find common tone": ["Which note do all of these chords share in common?", "chord progression"],
            "find non diatonic": ["Which of these chords are non diatonic?", "chord progression"],
            "roman numerals": ["Which is the correct roman numeral notation for this progression?", "chord progression"]
            },

            "mc xml":{
            "is transposition": ["Which of these is a correct transposition?", "chord progression"],
            "specific transposition": ["Which of these are transposed *directed interval*?", "chord progression"]
            },

            "mc audio":{
            "correct qualities": ["Which of these are the correct qualities for this progression?", "chord progression"]
            },

            "drag drop keyboard":{
            "build correct chord": ["Use the keyboard to build the correct chord to complete the progression.", "chord progression"]
            },

            "drag drop snippet":{
            "complete progression": ["Pick the right snippet to complete the progression.", "chord progression"]
            }
            }
    
    elif input_question_type == "interval":
        question_options_dict = {
            "text":{
            "identify": ["Identify this interval.", "interval"], 
            "semitones": ["How many semitones make up this interval?", "interval"],
            "up or down": ["Does this interval move up or down?", "interval"]
            },

            "piano":{
            "play interval": ["Use the piano to play the second note in this *simple interval*.", "interval"]
            },

            "record":{
            "play interval": ["Play this interval.", "interval"]
            },

            "mc text":{
            "correct name": ["Which is the correct name for this interval?", "interval"]
            },

            "mc xml":{
            "correct transposition": ["Which of these are correctly transposed *directed interval*?", "interval"]
            },

            "mc audio":{
            "correct audio": ["Which sample correctly plays this interval?", "interval"]
            },

            "drag drop keyboard":{
            "complete interval": ["Use the keyboard to complete the *simple interval*.", "interval"],
            "build interval": ["Use the keyboard to build a *simple interval*.", "interval"]
            }
            }
    
    elif input_question_type == "scale":
        question_options_dict = {
            "text":{
            "mode": ["Identify the scale mode.", "scale"], 
            "tonic": ["Identify the tonic of the scale", "scale"],
            "dominant": ["Identify the dominant of the scale", "scale"],
            "key signature": ["How many accidentals are in the key signature?", "scale"]
            },

            "piano":{
            "play scale degree": ["Play the *scale degree* of this scale.", "scale"]
            },

            "record":{
            "play scale": ["Play this scale.", "scale"]
            },

            "mc text":{
            "mode name": ["Which of these options is the correct name for this mode?", "scale"],
            "relative minor": ["Which of these scales are the relative minor?", "scale"],
            "diatonic chord": ["Which of these chords is diatonic to this scale?", "scale"],
            "nondiatonic chord": ["Which of these chords is nondiatonic to this scale?", "scale"]
            },

            "mc xml":{
            "possible mode": ["Which of these options is a mode of this scale?", "scale"],
            "relative minor": ["Which of these scales are the relative minor?", "scale"],
            "diatonic chord": ["Which of these chords is diatonic to this scale?", "scale"],
            "nondiatonic chord": ["Which of these chords is nondiatonic to this scale?", "scale"] 
            },

            "mc audio":{
            "correct mode audio": ["Which of these samples match the mode given?", "scale"]
            },

            "drag drop keyboard":{
            "complete scale": ["Use the keyboard to complete the scale.", "scale"],
            "build scale": ["Use the keyboard to build the scale.", "scale"]
            },

            "drag drop snippet":{
            "complete scale": ["Pick the right snippet to complete the scale.", "scale"]
            }
            }
    
    elif input_question_type == "excerpt":
        question_options_dict = {
            "text":{
            "key signature": ["What key signature could this excerpt be in?", "excerpt"]
            },

            "record":{
            "play excerpt": ["Play this excerpt.", "excerpt"]
            },

            "mc text":{
            "determine key": ["What key could this excerpt be in?", "excerpt"]
            },

            "mc xml":{
            "what measure": ["Which snippet is located in *measure*?", "excerpt", {2: [2,3,4]}],
            "what beat": ["Which snippet is located on *beat*?", "excerpt"]
            },

            "mc audio":{
            "correct audio": ["Which sample plays this excerpt correctly?", "excerpt"]
            },

            "drag drop keyboard":{
            "complete excerpt": ["Use this keyboard to complete this excerpt.", "excerpt"]
            },

            "drag drop snippet":{
            "complete excerpt": ["Drag in a snippet to complete this excerpt.", "excerpt"]
            }
            }

    elif input_question_type == "rhythm":
        question_options_dict = {
            "text":{
            "subdivision": ["How many *subdivision*s add up to this note?", "rhythm"],
            "beats": ["How many beats does this whole rhythm take up?", "rhythm"],
            "note value duration": ["How many beats is this note worth?", "note value"]
            },

            "record":{
            "play rhythm": ["Play this rhythm.", "rhythm"]
            },

            "mc text":{
            "subdivision": ["How many *subdivision*s add up to this note?", "rhythm"],
            "beats": ["How many beats does this whole rhythm take up?", "rhythm"],
            "note value duration": ["How many beats is this note worth?", "note value"]
            },

            "mc xml":{
            "same duration": ["Which of these rhythms have the same duration as the example?", "rhythm"]
            },

            "mc audio":{
            "correct audio": ["Which of these samples play this rhythm correctly?", "rhythm"]
            },

            "drag drop keyboard":{
            "fill in rhythm": ["Listen and use the keyboard to complete the rhythm.", "rhythm"]
            },

            "drag drop snippet":{
            "fill in rhythm": ["Listen and drag in the correct snippet to complete the rhythm.", "rhythm"]
            }
            }
        
    elif input_question_type == "arpeggio":
        question_options_dict = {
            "text":{
            "chord name": ["This arpeggio is of what chord?", "arpeggio"],
            "arp inversion": ["This arpeggio is in what inversion?", "arpeggio"]
            },

            "piano":{
            "play chord tone": ["Play the *chord tone* of this arpeggio.", "arpeggio"]
            },

            "record":{
            "play arp": ["Play this arpeggio.", "arpeggio"]
            },

            "mc text":{
            "chord name": ["This arpeggio is of what chord?", "arpeggio"],
            "arp inversion": ["This arpeggio is in what inversion?", "arpeggio"]
            },

            "mc xml":{
            "correct transposition": ["Which example is a correct transposition of this arpeggio?", "arpeggio"]
            },

            "mc audio":{
            "correct quality": ["Which sample is the same quality as the one presented?", "arpeggio"],
            "correct inversion": ["Which sample is the same inversion as the one presented?", "arpeggio"]
            }
            }

    book_map = {"T": "theory", "R": "rhythm", "L": "listen"}
    book = book_map[input_user_level[0]]

    question_choice_name = random.choice(question_levels[user.instrument][book][int(input_user_level[1])]["lessons"][int(input_user_level[-1])]["question choices"][input_question_type][input_answer_type])
    question_text = question_options_dict[input_answer_type][question_choice_name][0]
    xml_render = call_question_function(question_options_dict[input_answer_type][question_choice_name][1], input_user_level=input_user_level)
    question_content = None

    ### Text only ###
    if "*pitch*" in question_text:
        pitch_string = xml_render.flatten().notes.stream()[0].name
        if "-" in pitch_string:
            pitch_string = pitch_string.replace("-", "b")
        question_text = question_text.replace("*pitch*", pitch_string)

    if "*note value*" in question_text:
        if type(xml_render) == tuple:
            note_value_string = xml_render[1].duration.type + " note"
        else:
            note_value_string = xml_render.flatten().notes.stream()[0].duration.type + " note"
        question_text = question_text.replace("*note value*", note_value_string)

    if "*scale mode*" in question_text:
        question_text = question_text.replace("*scale mode*", xml_render[1].mode + " mode")

    if "*chord quality*" in question_text:
        if type(xml_render) == tuple:
            chord_quality_string = harmony.chordSymbolFigureFromChord(xml_render[2], includeChordType=True)[1] + " chord"
        else:
            chord_quality_string = harmony.chordSymbolFigureFromChord(chord.Chord(xml_render.pitches), includeChordType=True)[1] + " chord"
        question_text = question_text.replace("*chord quality*", chord_quality_string)

    if "*scale*" in question_text:
        if xml_render[1].name in ["Whole Tone", "Half Whole Diminished", "Whole Half Diminished"] or xml_render[1].mode == None:
            scale_string = xml_render[2][0].name + " " + xml_render[1].type + " scale"
        else:
            scale_string = xml_render[2][0].name + " " + xml_render[1].mode + " scale"
        question_text = question_text.replace("*scale*", scale_string)

    if "*key text*" in question_text:
        key_string = str(xml_render.keySignature.asKey())
        question_text = question_text.replace("*key text*", key_string)

    ### Return elements (sorted alphabetically) ###
    if "*beat*" in question_text:
        random_note = random.choice(xml_render.flatten().notesAndRests)
        random_note_measure = random_note.measureNumber
        random_note_beat = random_note.beat
        beat_string = "measure " + str(random_note_measure) + ", beat " + str(random_note_beat)
        question_text = question_text.replace("*beat*", beat_string)
        question_content = random_note

    if "*chord*" in question_text:
        if type(xml_render) == tuple:
            chord_symbol = harmony.chordSymbolFromChord(xml_render[2]).figure
            chord_string = xml_render[2].root().name + harmony.chordSymbolFigureFromChord(xml_render[2], includeChordType=True)[1]
        else:
            chord_symbol = harmony.chordSymbolFromChord(xml_render.flatten().notes.stream()[0]).figure
            chord_string = chord.Chord(xml_render.flatten().notes.stream()[0]).root().name + harmony.chordSymbolFigureFromChord(xml_render.flatten().notes.stream()[0], includeChordType=True)[1]
        question_text = question_text.replace("*chord*", random.choice([chord_symbol, chord_string]))
        question_content = chord_string

    if "*chord tone*" in question_text:
        if type(xml_render) == tuple:
            chord_intervals = xml_render[2].annotateIntervals(inPlace=False)
        else:
            chord_intervals = xml_render.measure(1)[0].annotateIntervals(inPlace=False)
        chord_intervals = [ly.text for ly in reversed(chord_intervals.lyrics)]
        chord_tone_dict = {"1": "root", "2": "second", "3": "third", "4": "fourth", "5": "fifth", "6": "sixth", "7": "seventh", "9": "ninth", "11": "eleventh", "13": "thirteenth"}
        chord_tone_keys = [tone for tone in chord_tone_dict.keys() if tone in chord_intervals]
        random_chord_tone = random.choice(chord_tone_keys)
        question_text = question_text.replace("*chord tone*", chord_tone_dict[random_chord_tone])
        question_content = int(random_chord_tone)

    if "*directed interval*" in question_text:
        random_int = random.randrange(-12, 12, 1)
        set_interval = interval.Interval(random_int)
        if random_int > 0:
            direction_string = "up a "
        elif random_int < 0:
            direction_string = "down a "
        else:
            direction_string = "by a "
        interval_string = direction_string + set_interval.niceName.lower()
        question_text = question_text.replace("*directed interval*", interval_string)
        question_content = set_interval

    if "*inversion*" in question_text:
        inversion_integer = xml_render.measure(1)[0].inversion()
        inversion_list = list(range(0, 7))
        inversion_list.remove(inversion_integer)
        possible_inversions = inversion_list[:len(xml_render.measure(1)[0].pitches) - 1]
        set_inversion_int = random.choice(possible_inversions)
        inverted_chord = chord.Chord(xml_render.measure(1)[0].pitches)
        inverted_chord.inversion(set_inversion_int)
        set_inversion_string = inverted_chord.inversionText()
        question_text = question_text.replace("*inversion*", set_inversion_string.lower())
        question_content = set_inversion_int
    
    if "*key*" in question_text:
        major_keys = ["C", "D-", "D", "E-", "E", "F", "F#", "G-", "G", "A-", "A", "B-", "B"]
        minor_keys = [x.lower() for x in major_keys]
        all_keys = major_keys + minor_keys
        key_select = key.Key(random.choice(all_keys)).name
        question_text = question_text.replace("*key*", key_select)
        question_content = key_select

    if "*measure*" in question_text:
        number_of_measures = xml_render.measure(-1).measureNumber
        random_measure = random.randrange(1, number_of_measures + 1)
        measure_string = "measure " + str(random_measure)
        question_text = question_text.replace("*measure*", measure_string)
        question_content = random_measure

    if "*roman numeral*" in question_text:
        random_scale_degree = random.randrange(1, len(xml_render.keySignature.asKey().getScale("major").pitches))
        roman_numeral = xml_render.keySignature.asKey().romanNumeral(random_scale_degree).figure
        question_text = question_text.replace("*roman numeral*", roman_numeral)
        question_content = random_scale_degree

    if "*scale degree*" in question_text:
        question_scale = scale.ConcreteScale(pitches=xml_render[0].pitches)
        random_scale_note = random.choice(xml_render[0].pitches)
        set_scale_degree = question_scale.getScaleDegreeFromPitch(random_scale_note)
        scale_degree_dict = {"1": "tonic", "2": "second", "3": "third", "4": "fourth", "5": "fifth", "6": "sixth", "7": "seventh", "8": "octave"}
        scale_degree_name_dict = {"1": "tonic", "2": "supertonic", "3": "mediant", "4": "subdominant", "5": "dominant", "6": "submediant", "7": "leading tone", "8": "tonic"}     
        question_text = question_text.replace("*scale degree*", scale_degree_dict[str(set_scale_degree)])
        question_content = set_scale_degree

    if "*simple interval*" in question_text:
        random_int = random.randrange(-12, 12, 1)
        set_interval = interval.Interval(random_int)
        interval_string = set_interval.niceName.lower()
        question_text = question_text.replace("*simple interval*", interval_string)
        question_content = set_interval

    if "*subdivision*" in question_text:
        original_duration = xml_render[1].duration.quarterLength #will have to tweak this
        subdivision_dict = {0.125: "32nd note", 0.25: "16th note", 0.5: "8th note", 0.75: "dotted 8th note", 1: "quarter note", 1.5: "dotted quarter note", 2: "half note", 4: "whole note"}
        subdiv_dict_keys = list(subdivision_dict.keys())
        choice_list = [s for s in subdiv_dict_keys if original_duration % s == 0 and s != original_duration]
        subdivision_choice = random.choice(choice_list)
        correct_answer = str(int(original_duration / subdivision_choice))
        question_text = question_text.replace("*subdivision*", subdivision_dict[subdivision_choice])
        question_content = correct_answer

    return question_choice_name, question_text, xml_render, question_content


def generate_answer(input_answer_type, input_question_type, question_dict, input_user_level):

    def generate_text_answer(input_question_type, question_dict): #complete

        if input_question_type == "text":
            if question_dict[0] == "chord intervals":
                return answer_chord_intervals(question_dict)
            
            elif question_dict[0] == "chord intervals half steps":
                chord_intervals = answer_chord_intervals(question_dict)
                half_step_intervals = [interval.Interval(h).semitones for h in chord_intervals]
                return half_step_intervals
            
            elif question_dict[0] == "interval semitones":
                return abs(question_dict[2][1].semitones)
            
            elif question_dict[0] == "scale dominant":
                pitched_scale = scale.ConcreteScale(pitches = question_dict[2][1]._net.realizePitch(question_dict[2][0].measure(1).pitches[0]))
                return pitched_scale.pitchFromDegree(5).name
            
            elif question_dict[0] == "key signature":
                pitched_scale = scale.ConcreteScale(pitches = question_dict[2][1]._net.realizePitch(question_dict[2][0].measure(1).pitches[0]))
                accidentals_list = [a.name for a in pitched_scale.pitches if len(a.name) > 1]
                return str(len(set(accidentals_list)))
            
            elif question_dict[0] == "note value subdivision":
                return question_dict[3]
            
            if question_dict[0] == "note value duration":
                return str(int(question_dict[2][1].duration.quarterLength))

        elif input_question_type == "audio":
            if question_dict[0] == "chord quality":
                chord_quality = harmony.chordSymbolFigureFromChord(question_dict[2].measure(1)[0])
                return chord_quality[1]
            
            elif question_dict[0] == "chord inversion":
                chord_inversion = question_dict[2].measure(1)[0].inversion()
                if chord_inversion == 0:
                    chord_inversion = "root"
                return chord_inversion
            
            elif question_dict[0] == "chord intervals":
                chord_intervals = question_dict[2].measure(1)[0].annotateIntervals(inPlace=False, stripSpecifiers=False)
                chord_intervals = [ly.text for ly in reversed(chord_intervals.lyrics)]
                return chord_intervals
            
            elif question_dict[0] == "chord intervals half steps":
                chord_intervals = question_dict[2].measure(1)[0].annotateIntervals(inPlace=False, stripSpecifiers=False)
                chord_intervals = [ly.text for ly in reversed(chord_intervals.lyrics)]
                half_step_intervals = [interval.Interval(h).semitones for h in chord_intervals]
                return half_step_intervals
            
            elif question_dict[0] == "diatonic or not":
                key_tonic = question_dict[2].keySignature.asKey().getTonic()
                major_scale = scale.DiatonicScale(key_tonic).pitches
                major_scale_string = [i.name for i in major_scale]
                chord_pitches = [c.name for c in question_dict[2].pitches]
                if len(set(major_scale_string)) > len(set(chord_pitches)):
                    diatonic_check = list(set(major_scale_string) - set(chord_pitches))
                else:
                    diatonic_check = list(set(chord_pitches) - set(major_scale_string))
                if len(diatonic_check) > 0:
                    return "Non diatonic"
                else:
                    return "Diatonic"
                
            elif question_dict[0] == "identify":
                return question_dict[2][1].name
            
            elif question_dict[0] == "semitones":
                return abs(question_dict[2][1].semitones)
            
            elif question_dict[0] == "up or down":
                if "-" in question_dict[2][1].directedName:
                    return "down"
                elif question_dict[2][1].name == "P1":
                    return "same"
                else:
                    return "up"
                
            elif question_dict[0] == "scale mode":
                pitched_scale = scale.ConcreteScale(pitches = question_dict[2][1]._net.realizePitch(question_dict[2][0].measure(1).pitches[0]))
                if question_dict[2][1].type in ["Whole Tone", "Whole Half Diminished", "Half Whole Diminished"]:
                    return question_dict[2][1].type
                else:
                    return question_dict[2][1].mode
                
            elif question_dict[0] == "note value subdivision":
                return question_dict[3]
            
            elif question_dict[0] == "beats":
                total = 0
                for element in question_dict[2].flatten().notesAndRests.stream():
                    total += element.duration.quarterLength
                return int(total)
            
            elif question_dict[0] == "note value duration":
                return question_dict[2].measure(1)[0].duration.type + " note"
            
            elif question_dict[0] == "arp quality":
                return question_dict[2][2].pitchedCommonName
            
            elif question_dict[0] == "arp inversion":
                arp_inversion = question_dict[2][2].inversion()
                if arp_inversion == 0:
                    arp_inversion = "root"
                return arp_inversion

        elif input_question_type == "note":
            if question_dict[0] == "identify":
                note_string_form = question_dict[2].flatten().notes.stream()[0].name
                if "-" in note_string_form:
                    note_string_form.replace("-", "b")
                return note_string_form
            elif question_dict[0] == "black or white":
                black_keys_list = ["C#", "D-", "D#", "E-", "F#", "G-", "G#", "A-", "A#", "B-" ]
                note_string_form = question_dict[2].measure(1)[0].name
                if note_string_form in black_keys_list:
                    return "Black"
                else:
                    return "White"
                
        elif input_question_type == "chord":
            if question_dict[0] == "quality": 
                chord_quality = harmony.chordSymbolFigureFromChord(question_dict[2].flatten().notes.stream()[0], includeChordType=True)
                return chord_quality[1]
            
            elif question_dict[0] == "inversion":
                chord_inversion = question_dict[2].measure(1)[0].inversion()
                if chord_inversion == 0:
                    chord_inversion = "root"
                return chord_inversion
            
            elif question_dict[0] == "intervals": #will need to change this so intervals are not calculated from root
                chord_intervals = question_dict[2].measure(1)[0].annotateIntervals(inPlace=False, stripSpecifiers=False)
                chord_intervals = [ly.text for ly in reversed(chord_intervals.lyrics)]
                return chord_intervals
            
            elif question_dict[0] == "intervals half steps": #will need to change this so intervals are not calculated from root
                chord_intervals = question_dict[2].measure(1)[0].annotateIntervals(inPlace=False, stripSpecifiers=False)
                chord_intervals = [ly.text for ly in reversed(chord_intervals.lyrics)]
                half_step_intervals = [interval.Interval(h).semitones for h in chord_intervals]
                return half_step_intervals

        elif input_question_type == "chord progression":
            if question_dict[0] == "diatonic or not":
                key_tonic = question_dict[2].keySignature.asKey().getTonic()
                major_scale = scale.DiatonicScale(key_tonic).pitches
                major_scale_string = [i.name for i in major_scale]
                chord_pitches = [c.name for c in question_dict[2].pitches]
                if len(set(major_scale_string)) > len(set(chord_pitches)):
                    diatonic_check = list(set(major_scale_string) - set(chord_pitches))
                else:
                    diatonic_check = list(set(chord_pitches) - set(major_scale_string))
                if len(diatonic_check) > 0:
                    return "Non diatonic"
                else:
                    return "Diatonic"
            
        elif input_question_type == "interval":
            if question_dict[0] == "identify":
                return question_dict[2][1].name
            elif question_dict[0] == "semitones":
                return abs(question_dict[2][1].semitones)
            elif question_dict[0] == "up or down":
                if "-" in question_dict[2][1].directedName:
                    return "down"
                elif question_dict[2][1].name == "P1":
                    return "same"
                else:
                    return "up"

        elif input_question_type == "scale":
            pitched_scale = scale.ConcreteScale(pitches = question_dict[2][1]._net.realizePitch(question_dict[2][0].measure(1).pitches[0]))
            if question_dict[0] == "mode":
                if question_dict[2][1].type in ["Whole Tone", "Whole Half Diminished", "Half Whole Diminished"]:
                    return question_dict[2][1].type
                else:
                    return question_dict[2][1].mode
                
            elif question_dict[0] == "tonic":
                return pitched_scale.tonic
            
            elif question_dict[0] == "dominant":
                return pitched_scale.pitchFromDegree(5).name
            
            elif question_dict[0] == "key signature":
                accidentals_list = [a.name for a in pitched_scale.pitches if len(a.name) > 1]
                return str(len(set(accidentals_list)))
            
        elif input_question_type == "excerpt":
            if question_dict[0] == "key signature":
                return question_dict[2].keySignature.asKey()

        elif input_question_type == "rhythm":
            if question_dict[0] == "subdivision":
                return question_dict[3]
            
            elif question_dict[0] == "beats":
                total = 0
                for element in question_dict[2].flatten().notesAndRests.stream():
                    total += element.duration.quarterLength
                return int(total)

            elif question_dict[0] == "duration":
                return question_dict[2].measure(1)[0].duration.type + " note"
            
            elif question_dict[0] == "note value duration":
                return str(int(question_dict[2][1].duration.quarterLength))

        elif input_question_type == "arpeggio":
            if question_dict[0] == "chord name":
                return question_dict[2][2].pitchedCommonName
            elif question_dict[0] == "arp inversion":
                arp_inversion = question_dict[2][2].inversion()
                if arp_inversion == 0:
                    arp_inversion = "root"
                return arp_inversion

    def generate_piano_answer(input_question_type, question_dict): #complete

        if input_question_type == "text":
            if question_dict[0] == "play pitch":
                return answer_play_pitch(question_dict)
            
            elif question_dict[0] == "play chord tone":
                return question_dict[2].measure(1)[0].getChordStep(question_dict[3]).name
            
            elif question_dict[0] == "play second note in interval":
                correct_note = question_dict[2][0].measure(1)[1].pitch
                return correct_note.name
            
            elif question_dict[0] == "play interval":
                pass

            elif question_dict[0] == "play scale degree":
                pitched_scale = scale.ConcreteScale(pitches = question_dict[2][1]._net.realizePitch(question_dict[2][0].measure(1).pitches[0]))
                if question_dict[0] == "play scale degree":
                    return pitched_scale.pitchFromDegree(question_dict[3]).name
                
            elif question_dict[0] == "play arp chord tone":
                return question_dict[2][2].getChordStep(question_dict[3])

        elif input_question_type == "note":
            if question_dict[0] == "play pitch":
                return answer_play_pitch(question_dict)
                
        elif input_question_type == "chord":
            if question_dict[0] == "play chord tone":
                return question_dict[2].measure(1)[0].getChordStep(question_dict[3]).name

        elif input_question_type == "interval":
            if question_dict[0] == "play interval":
                correct_note = question_dict[2][0].flatten().notes.stream()[1].pitch
                return correct_note.name

        elif input_question_type == "scale":
            pitched_scale = scale.ConcreteScale(pitches = question_dict[2][1]._net.realizePitch(question_dict[2][0].measure(1).pitches[0]))
            if question_dict[0] == "play scale degree":
                return pitched_scale.pitchFromDegree(question_dict[3]).name

        elif input_question_type == "arpeggio":
            if question_dict[0] == "play chord tone":
                return question_dict[2][2].getChordStep(question_dict[3])

    def generate_record_answer(input_question_type, question_dict): #complete

        if input_question_type == "text":
            if question_dict[0] == "play pitch":
                return answer_play_pitch(question_dict)
            
            elif question_dict[0] == "play chord":
                chord_symbol = harmony.chordSymbolFromChord(question_dict[2].measure(1)[0])
                return chord_symbol.figure
            
            elif question_dict[0] == "play scale":
                scale_pitch_list = [n.name for n in question_dict[2][0].pitches]
                return scale_pitch_list
            
            elif question_dict[0] == "play arp":
                return export_m21_to_xml(question_dict[2][1])

        elif input_question_type == "audio":
            if question_dict[0] == "play rhythm":
                return export_m21_to_xml(question_dict[2])

        elif input_question_type == "note":
            if question_dict[0] == "play pitch":
                return answer_play_pitch(question_dict)
                   
        elif input_question_type == "chord":
            if question_dict[0] == "play chord":
                chord_symbol = harmony.chordSymbolFromChord(question_dict[2].measure(1)[0])
                return chord_symbol.figure

        elif input_question_type == "chord progression":
            if question_dict[0] == "play progression":
                return export_m21_to_xml(question_dict[2])

        elif input_question_type == "interval":
            if question_dict[0] == "play interval":
                return export_m21_to_xml(question_dict[2][0])

        elif input_question_type == "scale":
            scale_pitch_list = [n.name for n in question_dict[2][0].pitches]
            if question_dict[0] == "play scale":
                return scale_pitch_list
            
        elif input_question_type == "excerpt":
            return export_m21_to_xml(question_dict[2])

        elif input_question_type == "rhythm":
            return export_m21_to_xml(question_dict[2])

        elif input_question_type == "arpeggio":
            return export_m21_to_xml(question_dict[2][1])

    def generate_mc_text_answer(input_question_type, question_dict, input_user_level): #complete

        if input_question_type == "text":
            if question_dict[0] == "convert roman":
                return answer_convert_roman(question_dict, input_user_level, mc=True)

            elif question_dict[0] == "relative minor":
                return answer_relative_minor_scale(question_dict, mc=True)
            
            elif question_dict[0] == "diatonic chord":
                return answer_diatonic_chord(question_dict, input_user_level, mc=True)

            elif question_dict[0] == "nondiatonic chord":
                return answer_non_diatonic_chord(question_dict, input_user_level, mc=True)
            
            elif question_dict[0] == "note value subdivision":
                answer_list = []
                correct_answer = question_dict[3]
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_difference = random.randrange(-2, 2)
                    wrong_answer = int(correct_answer) + random_difference
                    if str(wrong_answer) not in answer_list:
                        answer_list.append(str(wrong_answer))
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "note value duration":
                answer_list = []
                note_duration = int(question_dict[2][1].duration.quarterLength)
                correct_answer = str(note_duration) + " beats"
                if note_duration <= 1:
                    correct_answer = str(note_duration) + " beat"
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    duration_list = [0.25, 0.5, 1, 2, 3, 4]
                    random_duration = random.choice(duration_list)
                    wrong_answer = str(random_duration) + " beats"
                    if random_duration <= 1:
                        wrong_answer = str(random_duration) + " beat"
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "audio":
            if question_dict[0] == "quality":
                answer_list = []
                correct_answer = harmony.chordSymbolFigureFromChord(question_dict[2].measure(1)[0], True)
                answer_list.append(correct_answer[1])
                while len(answer_list) != 4:
                    wrong_answer = harmony.chordSymbolFigureFromChord(generate_chord(), True)
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer[1])
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(correct_answer[1]) + 1)
            
            elif question_dict[0] == "inversion":
                answer_list = []
                inversion_string_form = question_dict[2].measure(1)[0].inversion()
                inversion_map = {0: "root", 1: "first", 2: "second", 3: "third"}
                correct_answer = inversion_map[inversion_string_form]
                while len(answer_list) != 4:
                    inversion_list = ["root", "first", "second", "third", "fourth", "fifth", "sixth"]
                    wrong_answer = random.choice(inversion_list)
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "roman numerals":
                current_scale_pitches = question_dict[2].keySignature.getScale("major")
                answer_list = []
                chord_pitch_list = []
                correct_answer = []
                wrong_answer = []
                for el in question_dict[2].flatten().notes.stream():
                    correct_answer.append(convert_to_roman_numerals(el, question_dict[2].keySignature.asKey()))             
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_prog = call_question_function("chord progression", input_user_level=input_user_level)
                    for w in wrong_prog.flatten().notes.stream():
                        wrong_answer.append(convert_to_roman_numerals(w, wrong_prog.keySignature.asKey()))
                    answer_list.append(wrong_answer)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "correct name":
                answer_list = []
                answer_string = str(question_dict[2][1].directedName)
                answer_string = answer_string.replace("-", "")
                answer_list.append(answer_string)
                while len(answer_list) != 4:
                    wrong_interval = call_question_function("interval", input_user_level=input_user_level)
                    wrong_string = str(wrong_interval[1].directedName)
                    wrong_string = wrong_string.replace("-", "")
                    if wrong_string not in answer_list:
                        answer_list.append(wrong_string)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(answer_string) + 1)
            
            elif question_dict[0] == "mode name":
                scale_list_index = master_scale_dict.index(question_dict[2][1])
                answer_list = []
                if question_dict[2][1].type in ["Whole Tone", "Whole Half Diminished", "Half Whole Diminished"]:
                    correct_answer = question_dict[2][1].type
                    answer_list.append(correct_answer)
                else:
                    correct_answer = question_dict[2][1].mode
                    answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_mode = master_scale_dict[scale_list_index + random.choice([-3, -2, -1, 1, 2, 3])].mode
                    if wrong_mode not in answer_list:
                        answer_list.append(wrong_mode)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "note value subdivision":
                answer_list = []
                correct_answer = question_dict[3]
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_difference = random.randrange(-2, 2)
                    wrong_answer = int(correct_answer) + random_difference
                    if str(wrong_answer) not in answer_list:
                        answer_list.append(str(wrong_answer))
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "beats":
                answer_list = []
                total = 0
                for el in question_dict[2].flatten().notesAndRests.stream():
                    total += el.duration.quarterLength
                correct_answer = str(int(total))
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_difference = random.randrange(-2, 2)
                    wrong_answer = int(total) + random_difference
                    if str(int(wrong_answer)) not in answer_list:
                        answer_list.append(str(int(wrong_answer)))
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "note value duration":
                answer_list = []
                correct_answer = question_dict[2].measure(1)[0].duration.type + " note"
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    duration_list = ["whole", "half", "quarter", "eighth", "16th", "32nd", "dotted whole", "dotted half", "dotted quarter", "dotted eighth", "dotted sixteenth"]
                    random_duration = random.choice(duration_list)
                    wrong_answer = random_duration + " note"
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "arp quality":
                answer_list = []
                correct_answer = question_dict[2][2].pitchedCommonName
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = generate_chord().pitchedCommonName
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "arp inversion":
                answer_list = []
                correct_answer = question_dict[2][2].inversion()
                if correct_answer == 0:
                    correct_answer = "root"
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    inversion_list = ["root", "first", "second", "third", "fourth", "fifth", "sixth"]
                    wrong_answer = random.choice(inversion_list[:len(question_dict[2][2])])
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "note":
            if question_dict[0] == "identify pitch":
                answer_list = []
                note_string_form = question_dict[2].measure(1)[0].name
                answer_list.append(note_string_form)
                while len(answer_list) != 4:
                    wrong_answer = call_question_function("note", input_user_level=input_user_level).name
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(note_string_form) + 1)
            
            elif question_dict[0] == "identify duration":
                answer_list = []
                inversion_string_form = question_dict[2].measure(1)[0].duration.type
                answer_list.append(inversion_string_form)
                while len(answer_list) != 4:
                    duration_list = ["whole", "half", "quarter", "eighth", "16th", "32nd", "dotted whole", "dotted half", "dotted quarter", "dotted eighth", "dotted sixteenth"]
                    wrong_answer = random.choice(duration_list)
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(inversion_string_form) + 1)
        
        elif input_question_type == "chord":
            if question_dict[0] == "quality":
                answer_list = []
                correct_answer = harmony.chordSymbolFigureFromChord(question_dict[2].measure(1)[0], True)
                answer_list.append(correct_answer[1])
                while len(answer_list) != 4:
                    wrong_answer = harmony.chordSymbolFigureFromChord(generate_chord(), True)
                    if wrong_answer[1] not in answer_list:
                        answer_list.append(wrong_answer[1])
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(correct_answer[1]) + 1)

            elif question_dict[0] == "inversion":
                answer_list = []
                inversion_string_form = question_dict[2].measure(1)[0].inversion()
                inversion_map = {0: "root", 1: "first", 2: "second", 3: "third"}
                correct_answer = inversion_map[inversion_string_form]
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    inversion_list = ["root", "first", "second", "third", "fourth", "fifth", "sixth"]
                    wrong_answer = random.choice(inversion_list)
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "chord progression":
            if question_dict[0] == "determine key":
                answer_list = []
                correct_answer = question_dict[2].keySignature.asKey().name
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_key = key.KeySignature(random.randrange(-6, 6, 1)).asKey().name
                    if wrong_key not in answer_list:
                        answer_list.append(wrong_key)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "find common tone":
                answer_list = []
                chord_pitch_list = []
                for el in question_dict[2]:
                    if el.isChord == True:
                        chord_pitch_list.append(set(el.pitchNames))
                common_tones = list(set(chord_pitch_list[0]).intersection(*chord_pitch_list))
                if len(common_tones) == 0:
                    correct_answer = "None"
                    answer_list.append(correct_answer)
                else:
                    correct_answer = random.choice(common_tones)
                    answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_note = call_question_function("note", input_user_level=input_user_level).name
                    if wrong_note not in answer_list and wrong_note not in common_tones:
                        answer_list.append(wrong_note)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

            elif question_dict[0] == "find non diatonic":
                scale_pitches = question_dict[2].keySignature.getScale("major").pitches
                scale_string = [p.name for p in scale_pitches]
                answer_list = []
                chord_pitch_list = []
                for el in question_dict[2].flatten().notes.stream():
                    if el.isChord == True:
                        chord_pitch_list.append(set(el.pitchNames))
                correct_answer_list = []
                wrong_answer_list = []
                for c in chord_pitch_list:
                    if len(c.intersection(scale_string)) != len(c):
                        correct_answer_list.append(harmony.chordSymbolFromChord(chord.Chord(c)).figure)
                    else:
                        wrong_answer_list.append(harmony.chordSymbolFromChord(chord.Chord(c)).figure)
                correct_answer = random.choice(correct_answer_list)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    answer_list.append(random.choice(wrong_answer_list))
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

            elif question_dict[0] == "roman numerals":
                current_scale_pitches = question_dict[2].keySignature.getScale("major")
                answer_list = []
                chord_pitch_list = []
                correct_answer = []
                wrong_answer = []
                for el in question_dict[2].flatten().notes.stream():
                    correct_answer.append(convert_to_roman_numerals(el, question_dict[2].keySignature.asKey()))             
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_prog = call_question_function("chord progression", input_user_level=input_user_level)
                    for w in wrong_prog.flatten().notes.stream():
                        wrong_answer.append(convert_to_roman_numerals(w, wrong_prog.keySignature.asKey()))
                    answer_list.append(wrong_answer)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "interval":
            if question_dict[0] == "correct name":
                answer_list = []
                answer_string = str(question_dict[2][1].directedName)
                answer_string = answer_string.replace("-", "")
                answer_list.append(answer_string)
                while len(answer_list) != 4:
                    wrong_interval = call_question_function("interval", input_user_level=input_user_level)
                    wrong_string = str(wrong_interval[1].directedName)
                    wrong_string = wrong_string.replace("-", "")
                    if wrong_string not in answer_list:
                        answer_list.append(wrong_string)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(answer_string) + 1)

        elif input_question_type == "scale":
            if question_dict[0] == "mode name":
                scale_list_index = master_scale_dict.index(question_dict[2][1])
                answer_list = []
                if question_dict[2][1].type in ["Whole Tone", "Whole Half Diminished", "Half Whole Diminished"]:
                    correct_answer = question_dict[2][1].type
                    answer_list.append(correct_answer)
                else:
                    correct_answer = question_dict[2][1].mode
                    answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_mode = master_scale_dict[scale_list_index + random.choice([-3, -2, -1, 1, 2, 3])].mode
                    if wrong_mode not in answer_list:
                        answer_list.append(wrong_mode)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
                
            elif question_dict[0] == "relative minor":
                answer_list = []
                current_scale_pitches = scale.DiatonicScale(question_dict[2][2][0])
                correct_answer = list([str(p.name) for p in current_scale_pitches.getRelativeMinor().pitches])
                answer_list.append(correct_answer)
                parallel_minor = list([str(p.name) for p in current_scale_pitches.getParallelMinor().pitches])
                answer_list.append(parallel_minor)
                while len(answer_list) != 4:
                    mode_dict = {1: "ionian", 2: "dorian", 3: "phrygian", 4: "lydian", 5: "mixolydian", 7: "locrian"}
                    scale_degrees = list(mode_dict.keys())
                    random_scale_degree = random.choice(scale_degrees)
                    wrong_pitch = current_scale_pitches.pitchFromDegree(random_scale_degree)
                    wrong_answer = list([str(p.name) for p in scale.AbstractDiatonicScale(mode_dict[random_scale_degree]).getRealization(wrong_pitch, 1)])
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "diatonic chord":
                answer_list = []
                current_scale = question_dict[2][2]
                random_scale_degree = random.randrange(1, len(current_scale), 1)
                triad_degrees = []
                triad_degrees.append(random_scale_degree)
                degree_count = random_scale_degree
                for n in range(2):
                    degree_count += 2
                    next_degree = degree_count
                    if next_degree > 7:
                        next_degree = next_degree - 7
                    triad_degrees.append(next_degree)
                diatonic_chord = chord.Chord([current_scale[triad_degrees[0]].name, current_scale[triad_degrees[1]].name, current_scale[triad_degrees[2]].name])
                correct_answer = harmony.chordSymbolFromChord(diatonic_chord).figure
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_scale_degree = random.randrange(1, len(current_scale), 1)
                    random_quality = random.choice(["", "m", "+", "dim"])
                    wrong_answer = generate_chord(current_scale[random_scale_degree], random_quality)
                    if len(set(wrong_answer.pitchNames).intersection(set([p.name for p in current_scale]))) != len(wrong_answer.pitchNames):
                        if wrong_answer not in answer_list:
                            answer_list.append(harmony.chordSymbolFromChord(wrong_answer).figure)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

            elif question_dict[0] == "nondiatonic chord":
                answer_list = []
                current_scale = question_dict[2][2]
                random_scale_degree = random.randrange(1, len(current_scale), 1)
                random_quality = random.choice(["", "m", "+", "dim"])
                wrong_answer = generate_chord(current_scale[random_scale_degree], random_quality)
                if len(set(wrong_answer.pitchNames).intersection(set([p.name for p in current_scale]))) != len(wrong_answer.pitchNames):
                    correct_answer = harmony.chordSymbolFromChord(wrong_answer).figure
                    answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_scale_degree = random.randrange(1, len(current_scale), 1)
                    triad_degrees = []
                    triad_degrees.append(random_scale_degree)
                    degree_count = random_scale_degree
                    for n in range(2):
                        degree_count += 2
                        next_degree = degree_count
                        if next_degree > 7:
                            next_degree = next_degree - 7
                        triad_degrees.append(next_degree)
                    diatonic_chord = chord.Chord([current_scale[triad_degrees[0]].name, current_scale[triad_degrees[1]].name, current_scale[triad_degrees[2]].name])
                    if harmony.chordSymbolFromChord(diatonic_chord).figure not in answer_list:
                        answer_list.append(harmony.chordSymbolFromChord(diatonic_chord).figure)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
        elif input_question_type == "excerpt":
            if question_dict[0] == "determine key":
                answer_list = []
                correct_answer = question_dict[2].keySignature.asKey().name
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_key = key.KeySignature(random.randrange(-6, 6, 1)).asKey().name
                    if wrong_key not in answer_list:
                        answer_list.append(wrong_key)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
        elif input_question_type == "rhythm":
            if question_dict[0] == "subdivision":
                answer_list = []
                correct_answer = question_dict[3]
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_difference = random.randrange(-2, 2)
                    wrong_answer = int(correct_answer) + random_difference
                    if str(wrong_answer) not in answer_list:
                        answer_list.append(str(wrong_answer))
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "beats":
                answer_list = []
                total = 0
                for el in question_dict[2].flatten().notesAndRests.stream():
                    total += el.duration.quarterLength
                correct_answer = str(int(total))
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_difference = random.randrange(-2, 2)
                    wrong_answer = int(total) + random_difference
                    if str(int(wrong_answer)) not in answer_list:
                        answer_list.append(str(int(wrong_answer)))
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

            elif question_dict[0] == "duration":
                answer_list = []
                correct_answer = question_dict[2].measure(1)[0].duration.type + " note"
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    duration_list = ["whole", "half", "quarter", "eighth", "16th", "32nd", "dotted whole", "dotted half", "dotted quarter", "dotted eighth", "dotted sixteenth"]
                    random_duration = random.choice(duration_list)
                    wrong_answer = random_duration + " note"
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "note value duration":
                answer_list = []
                note_duration = int(question_dict[2][1].duration.quarterLength)
                if note_duration > 1:
                    correct_answer = str(note_duration) + " beats"
                else:
                    correct_answer = str(note_duration) + " beat"
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    duration_list = [0.25, 0.5, 1, 2, 3, 4]
                    random_duration = random.choice(duration_list)
                    if random_duration > 1:
                        wrong_answer = str(random_duration) + " beats"
                    else:
                        wrong_answer = str(random_duration) + " beat"
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "arpeggio":
            if question_dict[0] == "chord name":
                answer_list = []
                correct_answer = question_dict[2][2].pitchedCommonName
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = call_question_function("chord", input_user_level=input_user_level).pitchedCommonName
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "arp inversion":
                answer_list = []
                correct_answer = question_dict[2][2].inversion()
                if correct_answer == 0:
                    correct_answer = "root"
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    inversion_list = ["root", "first", "second", "third", "fourth", "fifth", "sixth"]
                    wrong_answer = random.choice(inversion_list[:len(question_dict[2][2])])
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
    def generate_mc_xml_answer(input_question_type, question_dict, input_user_level): #complete

        if input_question_type == "text":
            if question_dict[0] == "correct inversion":
                answer_list = []
                correct_answer = question_dict[2]
                correct_inversion = correct_answer.measure(1)[0].inversion(question_dict[3])
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_inversion = random.randrange(0, len(correct_answer.pitches), 1)
                    wrong_answer = correct_answer
                    wrong_answer.measure(1)[0].inversion(random_inversion)
                    if random_inversion != correct_inversion:
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index
            
            elif question_dict[0] == "possible mode":
                answer_list = []
                correct_scale = scale.ConcreteScale(pitches=question_dict[2][2])
                correct_duration = question_dict[2][0].measure(1)[0].duration.quarterLength
                random_scale_degree = correct_scale.pitches[random.randrange(2, 8)]
                octave_up = random_scale_degree.name + str(int(random_scale_degree.octave) + 1)
                correct_mode = correct_scale.getPitches(random_scale_degree, octave_up)
                correct_answer = stream.Stream()
                for c in correct_mode:
                    correct_note = note.Note(c)
                    correct_note.duration.quarterLength = correct_duration
                    correct_answer.append(correct_note)
                correct_answer.makeMeasures()
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = call_question_function("scale", input_user_level, {"0":[correct_mode[0]], "2": correct_duration})[0]
                    if wrong_answer.pitches != correct_mode:
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index
            
            elif question_dict[0] == "relative minor":
                return answer_relative_minor_scale(question_dict, input_user_level, "xml", mc=True)

            elif question_dict[0] == "diatonic chord":
                return answer_diatonic_chord(question_dict, input_user_level, "xml", mc=True)

            elif question_dict[0] == "nondiatonic chord":
                return answer_non_diatonic_chord(question_dict, input_user_level, "xml", mc=True)

        elif input_question_type == "audio":
            if question_dict[0] == "same duration":
                answer_list = []
                correct_rhythm_length = question_dict[2].highestTime
                correct_answer = stream.Stream()
                correct_note = note.Note("E4")
                correct_note.duration.quarterLength = correct_rhythm_length
                correct_answer.makeNotation()
                correct_answer.append(correct_note)
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = stream.Stream()
                    wrong_note = note.Note("E4")
                    wrong_note.duration.quarterLength = random.randrange(1, 5)
                    wrong_answer.append(wrong_note)
                    if wrong_note.duration.quarterLength != correct_rhythm_length:
                        wrong_answer.makeNotation()
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

        elif input_question_type == "note":
            if question_dict[0] == "match":
                answer_list = []
                correct_answer = question_dict[2]
                correct_note = question_dict[2].measure(1)[0].pitch
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = call_question_function("note", input_user_level=input_user_level)
                    wrong_note = wrong_answer.measure(1)[0].pitch
                    if wrong_note != correct_note:
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index
                  
        elif input_question_type == "chord":
            if question_dict[0] == "correct inversion":
                answer_list = []
                correct_answer = question_dict[2]
                correct_inversion = correct_answer.measure(1)[0].inversion(question_dict[3])
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_inversion = random.randrange(0, len(correct_answer.pitches), 1)
                    wrong_answer = correct_answer
                    wrong_answer.measure(1)[0].inversion(random_inversion)
                    if random_inversion != correct_inversion:
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

            elif question_dict[0] == "correct interval transposition":
                answer_list = []
                correct_answer = question_dict[2]
                correct_chord = correct_answer.measure(1)[0].transpose(question_dict[3])
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_transpo = random.randrange(-6, 6, 1)
                    wrong_answer = correct_answer
                    wrong_chord = wrong_answer.measure(1)[0].transpose(random_transpo)
                    if wrong_chord != correct_chord:
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

        elif input_question_type == "chord progression":
            if question_dict[0] == "is transposition":
                answer_list = []
                correct_answer = question_dict[2].transpose(random.randrange(-6, 6, 1))
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                major_scale = scale.DiatonicScale(question_dict[2].keySignature.asKey().getTonic())
                while len(answer_list) != 4:
                    wrong_stream = stream.Stream()
                    wrong_stream.keySignature = question_dict[2].keySignature
                    wrong_stream.timeSignature = question_dict[2].timeSignature
                    for temp_measure in question_dict[2]:
                        if "Measure" in temp_measure.classes:
                            wrong_stream.append(stream.Measure(number=temp_measure.measureNumber))
                            for chord_reharm in reversed(temp_measure):
                                if "Chord" in chord_reharm.classes:
                                    temp_chord = chord_reharm.simplifyEnharmonics()
                                    temp_chord.duration.quarterLength = chord_reharm.duration.quarterLength

                                for n in range(0, 2): #how many iterations
                                    reharm_choices = ["thirds", "quality"]
                                    random_choice = random.choice(reharm_choices)
                                    if random_choice == "thirds":
                                        temp_chord = move_in_thirds(temp_chord, major_scale, random.randrange(-1, 2, 1), random.randrange(1, 3, 1))
                                    elif random_choice == "quality":
                                        temp_chord = change_quality(temp_chord)

                                temp_chord = fix_chord_spelling(temp_chord)

                                wrong_stream.measure(temp_measure.measureNumber).insert(chord_reharm.offset, temp_chord)

                    wrong_stream = export_m21_to_xml(wrong_stream)
                    answer_list.append(wrong_stream)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index
            
            elif question_dict[0] == "specific transposition":
                answer_list = []
                correct_answer = question_dict[2].transpose(question_dict[3])
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_interval = random.randrange(-6, 6, 1)
                    if question_dict[3].semitones != random_interval:
                        wrong_answer = question_dict[2].transpose(random.randrange(-6, 6, 1))
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

        elif input_question_type == "interval":
            if question_dict[0] == "correct transposition":
                answer_list = []
                correct_answer = question_dict[2][0].transpose(question_dict[3])
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    random_interval = random.randrange(-6, 6, 1)
                    if question_dict[3].semitones != random_interval:
                        wrong_answer = question_dict[2][0].transpose(random_interval)
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

        elif input_question_type == "scale":
            if question_dict[0] == "possible mode":
                answer_list = []
                correct_scale = scale.ConcreteScale(pitches=question_dict[2][2])
                correct_duration = question_dict[2][0].measure(1)[0].duration.quarterLength
                random_scale_degree = correct_scale.pitches[random.randrange(2, 8)]
                octave_up = random_scale_degree.name + str(int(random_scale_degree.octave) + 1)
                correct_mode = correct_scale.getPitches(random_scale_degree, octave_up)
                correct_answer = stream.Stream()
                for c in correct_mode:
                    correct_note = note.Note(c)
                    correct_note.duration.quarterLength = correct_duration
                    correct_answer.append(correct_note)
                correct_answer.makeMeasures()
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = call_question_function("scale", input_user_level, {"0":[correct_mode[0]], "2":correct_duration})[0]
                    if wrong_answer.pitches != correct_mode:
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

            elif question_dict[0] == "relative minor":
                return answer_relative_minor_scale(question_dict, input_user_level, output="xml", mc=True)

            elif question_dict[0] == "diatonic chord":
                return answer_diatonic_chord(question_dict, input_user_level, output="xml", mc=True)

            elif question_dict[0] == "nondiatonic chord":
                return answer_non_diatonic_chord(question_dict, input_user_level, output="xml", mc=True)
            
        elif input_question_type == "excerpt":
            if question_dict[0] == "what measure":
                answer_list = []
                correct_answer = stream.Stream(question_dict[2].measure(question_dict[3]))
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = call_question_function("excerpt", input_user_level, {"2":1})
                    if wrong_answer.flatten().notesAndRests != correct_answer.flatten().notesAndRests:
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

            elif question_dict[0] == "what beat":
                answer_list = []
                correct_answer = stream.Stream(question_dict[3])
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = stream.Stream()
                    wrong_note = random.choice(question_dict[2].flatten().notesAndRests)
                    if wrong_note != question_dict[3]:
                        wrong_answer.append(wrong_note)
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

        elif input_question_type == "rhythm":
            if question_dict[0] == "same duration":
                answer_list = []
                correct_rhythm_length = question_dict[2].highestTime
                correct_answer = stream.Stream()
                correct_note = note.Note("E4")
                correct_note.duration.quarterLength = correct_rhythm_length
                correct_answer.makeNotation()
                correct_answer.append(correct_note)
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = stream.Stream()
                    wrong_note = note.Note("E4")
                    wrong_note.duration.quarterLength = random.randrange(1, 5)
                    wrong_answer.append(wrong_note)
                    if wrong_note.duration.quarterLength != correct_rhythm_length:
                        correct_answer.makeNotation()
                        wrong_answer = export_m21_to_xml(wrong_answer)
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

        elif input_question_type == "arpeggio":
            if question_dict[0] == "correct transposition":
                answer_list = []
                correct_answer = question_dict[2][0].transpose(random.randrange(-6, 6, 1))
                correct_answer = export_m21_to_xml(correct_answer)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_arp = call_question_function("arpeggio", input_user_level=input_user_level)[0]
                    if wrong_arp.pitches != correct_answer.pitches:
                        wrong_arp = export_m21_to_xml(wrong_arp)
                        answer_list.append(wrong_arp)
                random.shuffle(answer_list)
                correct_answer_index = answer_list.index(correct_answer)
                return answer_list, correct_answer_index

    def generate_mc_audio_answer(input_question_type, question_dict, input_user_level): #complete
    
        if input_question_type == "text": #need to convert all of these to midi!!!
            if question_dict[0] == "chord quality":
                answer_list = []
                correct_chord = question_dict[2].measure(1)[0]
                correct_midi = ([p.midi for p in correct_chord.pitches], 1, 4)
                answer_list.append(correct_midi)
                chord_quality_list = []
                chord_quality_list.append(correct_chord.quality)
                while len(answer_list) != 4:
                    wrong_chord = call_question_function("chord", input_user_level=input_user_level)
                    wrong_midi = ([p.midi for p in wrong_chord.pitches], 1, 4)
                    if wrong_chord.quality not in chord_quality_list and wrong_chord != correct_chord:
                        answer_list.append(wrong_midi)
                        chord_quality_list.append(wrong_chord.quality)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(correct_midi) + 1)
            
            elif question_dict[0] == "chord inversion":
                answer_list = []
                correct_chord = question_dict[2].measure(1)[0]
                correct_midi = ([p.midi for p in correct_chord.pitches], 1, 4)
                inversion_list = []
                inversion_list.append(correct_chord.inversion())
                answer_list.append(correct_midi)
                while len(answer_list) != 4:
                    random_inversion = random.randrange(0, len(correct_chord.pitches), 1)
                    wrong_chord = chord.Chord(correct_chord.pitches)
                    wrong_chord.inversion(random_inversion)
                    wrong_midi = ([p.midi for p in wrong_chord.pitches], 1, 4)
                    if random_inversion not in inversion_list:
                        answer_list.append(wrong_midi)
                        inversion_list.append(random_inversion)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(correct_midi) + 1)
            
            elif question_dict[0] == "correct interval audio":
                answer_list = []
                correct_answer = []
                interval_list = []
                correct_interval = question_dict[2][1].name
                interval_list.append(correct_interval)
                for el in question_dict[2][0].flatten().notesAndRests.stream():
                    correct_midi = (el.pitch.midi , 1, el.duration.quarterLength)
                    correct_answer.append(correct_midi)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_prog = call_question_function("interval", input_user_level=input_user_level)
                    if wrong_prog[1].name not in interval_list:
                        for w in wrong_prog[0].flatten().notesAndRests.stream():
                            wrong_midi = (w.pitch.midi, 1, w.duration.quarterLength)
                            wrong_answer.append(wrong_midi)
                    answer_list.append(wrong_answer)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "correct scale mode audio":
                answer_list = []
                correct_answer = []
                scale_string = question_dict[2][2]
                for el in scale_string:
                    correct_midi = (pitch.Pitch(el).midi, 1, 1)
                    correct_answer.append(correct_midi)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_scale = generate_scale([scale_string[0]])
                    if wrong_scale[2] != scale_string:
                        for w in wrong_scale[2]:
                            wrong_midi = (pitch.Pitch(w).midi, 1, 1)
                            wrong_answer.append(wrong_midi)
                    answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "correct arp quality":
                answer_list = []
                correct_answer = harmony.chordSymbolFigureFromChord(question_dict[2][2], includeChordType=True)[1]
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = harmony.chordSymbolFigureFromChord(generate_chord(), includeChordType=True)[1]
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "correct arp inversion":
                answer_list = []
                correct_answer = question_dict[2][2].inversion()
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    inversion_list = list(range(0, 7))
                    inversion_list.remove(correct_answer)
                    possible_inversions = inversion_list[:len(question_dict[2][2].pitches) - 1]
                    set_inversion_int = random.choice(possible_inversions)
                    inverted_chord = chord.Chord(question_dict[2][2].pitches)
                    inverted_chord.inversion(set_inversion_int)
                    answer_list.append(inverted_chord)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "audio":
            if question_dict[0] == "inversion":
                answer_list = []
                correct_chord = question_dict[2].measure(1)[0]
                correct_midi = ([p.midi for p in correct_chord.pitches], 1, 4)
                inversion_list = []
                inversion_list.append(correct_chord.inversion())
                answer_list.append(correct_midi)
                while len(answer_list) != 4:
                    random_inversion = random.randrange(0, len(correct_chord.pitches), 1)
                    wrong_chord = chord.Chord(correct_chord.pitches)
                    wrong_chord.inversion(random_inversion)
                    wrong_midi = ([p.midi for p in wrong_chord.pitches], 1, 4)
                    if random_inversion not in inversion_list:
                        answer_list.append(wrong_midi)
                        inversion_list.append(random_inversion)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(correct_midi) + 1)
            
            elif question_dict[0] == "correct audio":
                answer_list = []
                correct_answer = []
                interval_list = []
                correct_interval = question_dict[2][1].name
                interval_list.append(correct_interval)
                for el in question_dict[2][0].flatten().notesAndRests.stream():
                    correct_midi = (el.pitch.midi , 1, el.duration.quarterLength)
                    correct_answer.append(correct_midi)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_prog = call_question_function("interval", input_user_level=input_user_level)
                    if wrong_prog[1].name not in interval_list:
                        for w in wrong_prog[0].flatten().notesAndRests.stream():
                            wrong_midi = (w.pitch.midi, 1, w.duration.quarterLength)
                            wrong_answer.append(wrong_midi)
                    answer_list.append(wrong_answer)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "correct quality":
                pass
            elif question_dict[0] == "correct inversion":
                pass
      
        elif input_question_type == "chord":
            if question_dict[0] == "quality":
                answer_list = []
                correct_chord = question_dict[2].measure(1)[0]
                correct_midi = ([p.midi for p in correct_chord.pitches], 1, 4)
                answer_list.append(correct_midi)
                chord_quality_list = []
                chord_quality_list.append(correct_chord.quality)
                while len(answer_list) != 4:
                    wrong_chord = call_question_function("chord", input_user_level=input_user_level)
                    wrong_midi = ([p.midi for p in wrong_chord.pitches], 1, 4)
                    if wrong_chord.quality not in chord_quality_list and wrong_chord != correct_chord:
                        answer_list.append(wrong_midi)
                        chord_quality_list.append(wrong_chord.quality)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(correct_midi) + 1)

            elif question_dict[0] == "inversion":
                answer_list = []
                correct_chord = question_dict[2].measure(1)[0]
                correct_midi = ([p.midi for p in correct_chord.pitches], 1, 4)
                inversion_list = []
                inversion_list.append(correct_chord.inversion())
                answer_list.append(correct_midi)
                while len(answer_list) != 4:
                    random_inversion = random.randrange(0, len(correct_chord.pitches), 1)
                    wrong_chord = chord.Chord(correct_chord.pitches)
                    wrong_chord.inversion(random_inversion)
                    wrong_midi = ([p.midi for p in wrong_chord.pitches], 1, 4)
                    if random_inversion not in inversion_list:
                        answer_list.append(wrong_midi)
                        inversion_list.append(random_inversion)
                random.shuffle(answer_list)
                return answer_list, str(answer_list.index(correct_midi) + 1)

        elif input_question_type == "chord progression":
            if question_dict[0] == "correct qualities":
                answer_list = []
                correct_answer = []
                for el in question_dict[2].flatten().notesAndRests.stream():
                    if el.isRest == True:
                        correct_midi = ("rest", el.duration.quarterLength)
                    elif el.isChord == True:
                        correct_midi = ([p.midi for p in el.pitches], 1, el.duration.quarterLength)
                    correct_answer.append(correct_midi)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_prog = call_question_function("chord progression", input_user_level=input_user_level)
                    for w in wrong_prog.flatten().notesAndRests.stream():
                        if w.isRest == True:
                            wrong_midi = ("rest", w.duration.quarterLength)
                        elif w.isChord == True:
                            wrong_midi = ([p.midi for p in w.pitches], 1, w.duration.quarterLength)
                        wrong_answer.append(wrong_midi)
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "interval":
            if question_dict[0] == "correct audio":
                answer_list = []
                correct_answer = []
                interval_list = []
                correct_interval = question_dict[2][1].name
                interval_list.append(correct_interval)
                for el in question_dict[2][0].flatten().notesAndRests.stream():
                    correct_midi = (el.pitch.midi , 1, el.duration.quarterLength)
                    correct_answer.append(correct_midi)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_prog = call_question_function("interval", input_user_level=input_user_level)
                    if wrong_prog[1].name not in interval_list:
                        for w in wrong_prog[0].flatten().notesAndRests.stream():
                            wrong_midi = (w.pitch.midi, 1, w.duration.quarterLength)
                            wrong_answer.append(wrong_midi)
                    answer_list.append(wrong_answer)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "scale":
            if question_dict[0] == "correct mode audio":
                answer_list = []
                correct_answer = []
                scale_string = question_dict[2][2]
                for el in scale_string:
                    correct_midi = (pitch.Pitch(el).midi, 1, 1)
                    correct_answer.append(correct_midi)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_scale = call_question_function("scale", input_user_level, {"0":[scale_string[0]]})
                    if wrong_scale[2] != scale_string:
                        for w in wrong_scale[2]:
                            wrong_midi = (pitch.Pitch(w).midi, 1, 1)
                            wrong_answer.append(wrong_midi)
                    answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
        elif input_question_type == "excerpt":
            if question_dict[0] == "correct audio":
                answer_list = []
                correct_answer = []
                for el in question_dict[2].flatten().notesAndRests.stream():
                    if el.isRest == True:
                        correct_midi = ("rest", el.duration.quarterLength)
                    elif el.isChord == True:
                        correct_midi = ([p.midi for p in el.pitches], 1, el.duration.quarterLength)
                    elif el.isNote == True:
                        correct_midi = (el.pitch.midi , 1, el.duration.quarterLength)
                    correct_answer.append(correct_midi)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_prog = call_question_function("excerpt", input_user_level=input_user_level)
                    for w in wrong_prog.flatten().notesAndRests.stream():
                        if w.isRest == True:
                            wrong_midi = ("rest", w.duration.quarterLength)
                        elif w.isChord == True:
                            wrong_midi = ([p.midi for p in w.pitches], 1, w.duration.quarterLength)
                        elif el.isNote == True:
                            wrong_midi = (w.pitch.midi, 1, w.duration.quarterLength)
                        wrong_answer.append(wrong_midi)
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "rhythm":
            if question_dict[0] == "correct audio":
                answer_list = []
                correct_answer = []
                for el in question_dict[2].flatten().notesAndRests.stream():
                    if el.isRest == True:
                        correct_midi = ("rest", el.duration.quarterLength)
                    else:
                        correct_midi = (el.pitch.midi , 1, el.duration.quarterLength)
                    correct_answer.append(correct_midi)
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = []
                    wrong_prog = call_question_function("rhythm", input_user_level=input_user_level)
                    for w in wrong_prog.flatten().notesAndRests.stream():
                        if w.isRest == True:
                            wrong_midi = ("rest", w.duration.quarterLength)
                        else:
                            wrong_midi = (w.pitch.midi, 1, w.duration.quarterLength)
                        wrong_answer.append(wrong_midi)
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

        elif input_question_type == "arpeggio": #this one needs fixing
            if question_dict[0] == "correct quality":
                answer_list = []
                correct_answer = harmony.chordSymbolFigureFromChord(question_dict[2][2], includeChordType=True)[1]
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    wrong_answer = harmony.chordSymbolFigureFromChord(generate_chord(), includeChordType=True)[1]
                    if wrong_answer not in answer_list:
                        answer_list.append(wrong_answer)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1
            
            elif question_dict[0] == "correct inversion":
                answer_list = []
                correct_answer = question_dict[2][2].inversion()
                answer_list.append(correct_answer)
                while len(answer_list) != 4:
                    inversion_list = list(range(0, 7))
                    inversion_list.remove(correct_answer)
                    possible_inversions = inversion_list[:len(question_dict[2][2].pitches) - 1]
                    set_inversion_int = random.choice(possible_inversions)
                    inverted_chord = chord.Chord(question_dict[2][2].pitches)
                    inverted_chord.inversion(set_inversion_int)
                    answer_list.append(inverted_chord)
                random.shuffle(answer_list)
                return answer_list, answer_list.index(correct_answer) + 1

    answer_type_map = {
        "text": generate_text_answer,
        "piano": generate_piano_answer,
        "record": generate_record_answer,
        "mc text": generate_mc_text_answer,
        "mc xml": generate_mc_xml_answer,
        "mc audio": generate_mc_audio_answer,
    }

    if input_answer_type in answer_type_map:
        new_answer = answer_type_map[input_answer_type](input_question_type, question_dict, input_user_level)
    else:
        raise ValueError(f"Unknown input_answer_type: {input_answer_type}")

    return new_answer
    

### 0 = prompt text, 1 = question render (if included), 2 = question text, 3 = answer elements (if multiple choice, will be tuple)
def generate_screen(question_type, answer_type, user_level, user_language="en"):
    
    def translate_text(text, language):
        if language == "es":
            translator = Translator()
            translation = translator.translate(text, dest=language)
            return translation.text
        return text

    # Create prompt text
    prompt_text = generate_prompt_text(question_type, answer_type, user_language)

    # Generate question
    question_elements = generate_question(question_type, answer_type, user_level)

    # Export question to musicXML
    question_render = None
    if question_type not in ["text", "audio"]:
        finished_question = question_elements[2]
        question_render = export_m21_to_xml(finished_question[0] if isinstance(finished_question, tuple) else finished_question)

    # Export to mp3
    # TODO: Add code for exporting to mp3 if needed

    # Translate question text
    question_string = translate_text(question_elements[1], user_language)

    # Generate answer
    answer_elements = generate_answer(answer_type, question_type, question_elements, input_user_level=user_level)

    return prompt_text, question_render, question_string, answer_elements


