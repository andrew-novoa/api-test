import math
from scamp import *
import random
from theory import *
from music21 import chord, clef, harmony, interval, key, meter, note, roman, scale, stream

### Set Clef ###
user_instrument = "piano"
if user_instrument == "bass":
    user_clef = clef.BassClef()
else:
    user_clef = clef.TrebleClef()

function_defaults = {
    "note":[None, None, False],
    "chord":[[], [], True],
    "chord progression":[None, False, None, "written"],
    "interval":[None, [], None, True],
    "scale":[[], [], None],
    "excerpt":[None, False, None],
    "rhythm":[[], [], None, 0.25],
    "arpeggio":[None, None, None],
    "note value":[[], None],
    "time elements":[[], []]
    }

### Main Functions ###

def generate_tone():
    pass

def generate_note(specific_note = None, specific_duration = None, stand_alone = False):
    new_note = note.Note()
    if specific_note != None:
        if type(specific_note) == list:
            new_note.pitch = random.choice(specific_note)
        else:
            new_note.pitch = specific_note
    else:
        new_note.pitch.midi = random.randrange(57, 73, 1) #range will depend on clef and user level

    if stand_alone == True:
        if specific_duration != None:
            new_note.duration.quarterLength = specific_duration
        else:
            duration_choices = [1, 2, 4]
            new_note.duration.quarterLength = random.choice(duration_choices)
        new_measure = stream.Measure(new_note)
        new_stream = stream.Stream()

        new_stream.append(user_clef)
        new_stream.append(new_measure)

        return new_stream
    
    else:
        return new_note

def generate_chord(chord_root_list = [], chord_quality_list = [], stand_alone = False): #figure out voicings and inversions, also create method to create certain type of chord (use this as an actual function)
    
    if len(chord_root_list) != 0:
        root_note = note.Note(random.choice(chord_root_list))
    else:
        root_note = note.Note()
        root_note.pitch.midi = random.randrange(57, 73, 1)
    new_chord = chord.Chord()
    new_chord.add(root_note)

    if len(chord_quality_list) != 0:
        chord_quality = random.choice(chord_quality_list)
        for i in chord_by_interval_dict[chord_quality]:
            temp_interval = interval.Interval(i)
            temp_interval.pitchStart = root_note.pitch
            new_chord.add(temp_interval.pitchEnd)
    else:
        for i in chord_by_interval_dict[chord_interval_list[random.randrange(0, len(chord_interval_list), 1)]]:
            temp_interval = interval.Interval(i)
            temp_interval.pitchStart = root_note.pitch
            new_chord.add(temp_interval.pitchEnd)

    new_chord = fix_chord_spelling(new_chord)

    if stand_alone == True:
        duration_choices = [1, 2, 4]
        new_chord.duration.quarterLength = random.choice(duration_choices)
        new_stream = stream.Stream()
        new_measure = stream.Measure(new_chord)
        new_stream.append(new_measure)
        new_stream.timeSignature = None
        return new_stream
    else:
        return new_chord

def generate_chord_progression(input_key_sig = None, non_diatonic = False, specified_length=None, output_type = "written"):

    time_elements = generate_time_elements()
    time_sig = time_elements[0]
    meter_division_count = time_elements[1]
    meter_sequence = time_elements[2]
    prime_numbers = [3, 5, 7, 11, 13]

    #create key signature
    if input_key_sig != None:
        key_sig = key.KeySignature(input_key_sig)
    else:
        key_sig = key.KeySignature(random.randrange(-7, 7, 1))
    
    major_scale = scale.MajorScale(key_sig.asKey("major").tonic)
    tonic_chord = generate_chord([major_scale.getTonic().name], [""])
    dom_chord = generate_chord([major_scale.getDominant().name], [""])

    ### generate random measures with tonic and dominant chords ###
    original_progression = stream.Stream()
    original_progression.keySignature = key_sig
    original_progression.timeSignature = time_sig

    reharmed_progression = stream.Stream()
    reharmed_progression.keySignature = key_sig
    reharmed_progression.timeSignature = time_sig

    if specified_length != None:
        if type(specified_length) == list:
            number_of_measures = random.choice(specified_length)
        else:
            number_of_measures = specified_length
    else:
        number_of_measures = random.randrange(1, 4)

    for m in range(1, number_of_measures + 1):
        original_progression.append(stream.Measure(number = m))
        reharmed_progression.append(stream.Measure(number = m))

    #distribute chords throughout measures
    two_div_list = []
    three_div_list = []
    four_div_list = []
    if meter_division_count == 2:
        full_measure_duration = ((int(str(meter_sequence)[1]) / int(str(meter_sequence)[3])) + (int(str(meter_sequence)[5]) / int(str(meter_sequence)[7]))) * 4
        first_half_duration = ((int(str(meter_sequence)[1]) / int(str(meter_sequence)[3]))) * 4
        second_half_duration = ((int(str(meter_sequence)[5]) / int(str(meter_sequence)[7]))) * 4
        two_div_list.append(full_measure_duration)
        two_div_list.append([first_half_duration, second_half_duration])
        if int(str(meter_sequence)[1]) in prime_numbers or int(str(meter_sequence)[5]) in prime_numbers:
            first_quarter_duration = math.ceil(int(str(meter_sequence)[1]) / 2)
            one_qd_quarter_length = (first_quarter_duration / int(str(meter_sequence)[3])) * 4
            second_quarter_duration = int(str(meter_sequence)[1]) - first_quarter_duration
            two_qd_quarter_length = (second_quarter_duration / int(str(meter_sequence)[3])) * 4
            third_quarter_duration = math.ceil(int(str(meter_sequence)[5]) / 2)
            three_qd_quarter_length = (third_quarter_duration / int(str(meter_sequence)[3])) * 4
            fourth_quarter_duration = int(str(meter_sequence)[5]) - third_quarter_duration
            four_qd_quarter_length = (fourth_quarter_duration / int(str(meter_sequence)[3])) * 4
            two_div_list.append([one_qd_quarter_length, two_qd_quarter_length, second_half_duration])
            two_div_list.append([first_half_duration, three_qd_quarter_length, four_qd_quarter_length])
            two_div_list.append([one_qd_quarter_length, two_qd_quarter_length, three_qd_quarter_length, four_qd_quarter_length])

    elif meter_division_count == 3:
        full_measure_duration = ((int(str(meter_sequence)[1]) / int(str(meter_sequence)[3])) + (int(str(meter_sequence)[5]) / int(str(meter_sequence)[7])) + (int(str(meter_sequence)[9]) / int(str(meter_sequence)[11]))) * 4
        first_half_duration = ((int(str(meter_sequence)[1]) / int(str(meter_sequence)[3])) + (int(str(meter_sequence)[5]) / int(str(meter_sequence)[7]))) * 4
        second_half_duration = ((int(str(meter_sequence)[5]) / int(str(meter_sequence)[7])) + (int(str(meter_sequence)[9]) / int(str(meter_sequence)[11]))) * 4
        first_third_duration = ((int(str(meter_sequence)[1]) / int(str(meter_sequence)[3]))) * 4
        second_third_duration = ((int(str(meter_sequence)[5]) / int(str(meter_sequence)[7]))) * 4
        third_third_duration = ((int(str(meter_sequence)[9]) / int(str(meter_sequence)[11]))) * 4
        three_div_list.append(full_measure_duration)
        three_div_list.append([first_half_duration, second_half_duration])
        three_div_list.append([first_third_duration, second_half_duration])
        three_div_list.append([first_half_duration, third_third_duration])
        three_div_list.append([first_third_duration, second_third_duration, third_third_duration])

    elif meter_division_count == 4:
        full_measure_duration = ((int(str(meter_sequence)[1]) / int(str(meter_sequence)[3])) + (int(str(meter_sequence)[5]) / int(str(meter_sequence)[7])) + (int(str(meter_sequence)[9]) / int(str(meter_sequence)[11])) + (int(str(meter_sequence)[13]) / int(str(meter_sequence)[15]))) * 4
        first_half_duration = ((int(str(meter_sequence)[1]) / int(str(meter_sequence)[3])) + (int(str(meter_sequence)[5]) / int(str(meter_sequence)[7]))) * 4
        second_half_duration = ((int(str(meter_sequence)[9]) / int(str(meter_sequence)[11])) + (int(str(meter_sequence)[13]) / int(str(meter_sequence)[15]))) * 4
        one_qd_quarter_length = (int(str(meter_sequence)[1]) / int(str(meter_sequence)[3])) * 4
        two_qd_quarter_length = (int(str(meter_sequence)[5]) / int(str(meter_sequence)[7])) * 4
        three_qd_quarter_length = (int(str(meter_sequence)[9]) / int(str(meter_sequence)[11])) * 4
        four_qd_quarter_length = (int(str(meter_sequence)[13]) / int(str(meter_sequence)[15])) * 4
        four_div_list.append(full_measure_duration)
        four_div_list.append([first_half_duration, second_half_duration])
        four_div_list.append([one_qd_quarter_length, two_qd_quarter_length, second_half_duration])
        four_div_list.append([first_half_duration, three_qd_quarter_length, four_qd_quarter_length])
        four_div_list.append([one_qd_quarter_length, two_qd_quarter_length, three_qd_quarter_length, four_qd_quarter_length])


    tonic_or_dom = [tonic_chord, dom_chord]
    for c in range(number_of_measures, 0, -1):
        if meter_division_count == 2:
            list_select = two_div_list
        elif meter_division_count == 3:
            list_select = three_div_list
        elif meter_division_count == 4:
            list_select = four_div_list

        offset_count = 0
        random_division = random.choice(list_select)
        if type(random_division) != float:
            for div in random_division:
                random_function_choice = chord.Chord(random.choice(tonic_or_dom).pitches)
                random_function_choice.duration.quarterLength = div
                original_progression.measure(c).insert(offset_count, random_function_choice)
                offset_count += random_function_choice.duration.quarterLength
        else:
            random_function_choice = chord.Chord(random.choice(tonic_or_dom).pitches)
            random_function_choice.duration.quarterLength = random_division               
            original_progression.measure(c).insert(offset_count, random_function_choice)
            offset_count += random_function_choice.duration.quarterLength

    ### iterate through original progression and reharm ###
    for temp_measure in original_progression:
        if temp_measure.measureNumber != None:
            for chord_reharm in reversed(temp_measure):
                temp_chord = chord_reharm.simplifyEnharmonics()
                temp_chord.duration.quarterLength = chord_reharm.duration.quarterLength
                new_dom = None

                for n in range(0, 4): #how many iterations

                    reharm_choices = ["thirds", "thirds", "quality", "tritone", "add extensions", "retroactive dominant", "retroactive dominant"]
                    if non_diatonic == False:
                        reharm_choices.remove("quality")
                        reharm_choices.remove("tritone")
                    random_choice = random.choice(reharm_choices)

                    if random_choice == "thirds":
                        temp_chord = move_in_thirds(temp_chord, major_scale, random.randrange(-1, 2, 1), random.randrange(1, 3, 1))
                    elif random_choice == "quality":
                        temp_chord = change_quality(temp_chord)
                    elif random_choice == "add extensions":
                        temp_chord = add_extensions(temp_chord, major_scale, non_diatonic)
                    elif random_choice == "tritone":
                        if chord_reharm == dom_chord:
                            temp_chord = tritone_sub(temp_chord)
                    elif random_choice == "retroactive dominant":
                        if chord_reharm.duration.quarterLength >= 2:
                            two_chords = retroactive_dom(temp_chord, chord_reharm.duration.quarterLength, major_scale, non_diatonic)
                            temp_chord = two_chords[1]
                            new_dom = two_chords[0]

                temp_chord = fix_chord_spelling(temp_chord)

                ### three outputs: written chords, chord slashes, chord symbols ###
                if output_type != "written": #add chord symbols
                    chord_symbol = harmony.chordSymbolFromChord(temp_chord)
                    if new_dom != None:
                        new_dom_chord_symbol = harmony.chordSymbolFromChord(new_dom)
                        reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset + temp_chord.duration.quarterLength, chord_symbol)
                        reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset, new_dom_chord_symbol)
                    else:
                        reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset, chord_symbol)

                    if output_type == "slashes": #add slash notes
                        slash_note = note.Note("B4") #will need to check clef
                        slash_note.notehead = "slash"
                        slash_note.duration.quarterLength = temp_chord.duration.quarterLength
                        if new_dom != None:
                            extra_slash_note = note.Note("B4")
                            extra_slash_note.notehead = "slash"
                            extra_slash_note.duration.quarterLength = new_dom.duration.quarterLength
                            reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset + temp_chord.duration.quarterLength, slash_note)
                            reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset, extra_slash_note)
                        else:
                            reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset, slash_note)

                else:
                    if new_dom == None: #write out full chords
                        reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset, temp_chord)
                    else:
                        reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset + temp_chord.duration.quarterLength, temp_chord)
                        reharmed_progression.measure(temp_measure.measureNumber).insert(chord_reharm.offset, new_dom)

    return reharmed_progression

def generate_interval(start_pitch = None, specific_interval = [], specific_duration = None, stand_alone = True):
    if len(specific_interval) != 0:
        new_interval = interval.Interval(random.choice(specific_interval))
    else:
        new_interval = interval.Interval(random.randrange(-15, 15, 1))
    
    if stand_alone == False:
        return new_interval

    else:
        start_note = note.Note()
        if start_pitch != None:
            start_note.pitch = start_pitch
        else:
            start_note.pitch.midi = random.randrange(57, 73, 1)

        new_interval.pitchStart = start_note.pitch
        end_note = note.Note(new_interval.pitchEnd)

        if specific_duration != None:
            start_note.duration.quarterLength = specific_duration
        else:
            duration_choices = [1, 2]
            start_note.duration.quarterLength = random.choice(duration_choices)
        end_note.duration.quarterLength = start_note.duration.quarterLength

        new_measure = stream.Measure(start_note)
        new_measure.append(end_note)
        new_stream = stream.Stream()
        new_stream.append(new_measure)

        return new_stream.makeNotation(), new_interval

def generate_scale(scale_tonic_list = [], mode_list = [], specified_duration=None):
    new_stream = stream.Stream()
    if len(scale_tonic_list) != 0: #scale_tonic should be in form of list
        tonic_list_choice = random.choice(scale_tonic_list)
        root_note = note.Note(tonic_list_choice)
    else:
        root_note = note.Note()
        root_note.pitch.midi = random.randrange(57, 73, 1)

    if specified_duration != None:
        duration_select = specified_duration
    else:
        duration_choices = [0.5, 1]
        duration_select = random.choice(duration_choices)

    if len(mode_list) != 0:
        mode_select = master_scale_dict[random.choice(mode_list)]
    else:
        mode_select = master_scale_dict[random.choice(scale_key_list)]

    new_scale = mode_select.getRealization(root_note.pitch, 1)
    new_scale_string_form = [str(scale_note) for scale_note in new_scale]
    if sum(s.count('-') for s in new_scale_string_form) >= len(new_scale) or sum(s.count('#')  for s in new_scale_string_form) >= len(new_scale):
        note_respell = True
    else:
        if new_scale[0].name == "F#" and random.choice([0, 1]) == 1:
            note_respell = True
        else:
            note_respell = False

    for n in new_scale:
        if note_respell == True:
            temp_note = note.Note(n.getEnharmonic())
        else:
            temp_note = note.Note(n)
        temp_note.duration.quarterLength = duration_select
        new_stream.append(temp_note)

    return new_stream.makeMeasures(), mode_select, new_scale

def generate_excerpt(input_key_sig = None, non_diatonic = False, input_length=None):
    
    starter_progression = generate_chord_progression(input_key_sig, non_diatonic, specified_length=input_length, output_type="symbols")

    new_stream = stream.Stream()

    new_stream.timeSignature = starter_progression.timeSignature
    new_stream.keySignature = starter_progression.keySignature

    for excerpt_measure in starter_progression:
        measure_count = 0
        if excerpt_measure.measureNumber != None:
            measure_count += 1
            new_measure = stream.Measure(number=measure_count)
            new_stream.append(new_measure)
            for excerpt_chord in excerpt_measure:
                new_stream.measure(measure_count).insert(excerpt_chord.offset, note.Note(random.choice(excerpt_chord.pitches)))

    return new_stream

def generate_rhythm(denominator_list = [], numerator_list = [], number_of_measures=None, smallest_value=0.25):
    new_stream = stream.Stream()
    time_elements = generate_time_elements(denominator_list, numerator_list)
    time_sig = time_elements[0]
    new_stream.timeSignature = time_sig
    new_stream.staffLines = 1

    #create measures
    if number_of_measures != None:
        random_number_of_measures = number_of_measures
    else:
        random_number_of_measures = random.choice([1, 2, 3])
    for m in range(1, random_number_of_measures + 1):
        new_stream.append(stream.Measure(number = m))

    #create rhythms and rests
    beat_value = 1
    rhythm_list = []
    for m in range(random_number_of_measures):
        temp_measure_list = []
        temp_ql_list = []
        if time_sig.denominator == 4:
            for n in range(time_sig.numerator):
                beat_value = 1
                temp_measure_list.append(1)
                temp_ql_list.append(1)
        elif time_sig.denominator == 8:
            for n in range(int(time_sig.numerator / 3)):
                beat_value = 1.5
                temp_measure_list.append(1.5)
                temp_ql_list.append(1.5)

        edit_options = ["none", "split", "merge"]
        for r in range(3): #number of iterations
            random_index = random.randrange(0, len(temp_measure_list), 1) #choose random note in measure

            edit_choice = random.choice(edit_options)

            if edit_choice == "split" and float(temp_measure_list[random_index]) > smallest_value:
                if temp_measure_list[random_index] == 1.5: #we need to take into consideration meter
                    div = 3
                else:
                    div = 2
                split_value = round(float(temp_measure_list[random_index]) / div, 2)
                temp_measure_list[random_index] = split_value
                for d in range(div - 1):
                    temp_measure_list.insert(random_index + 1, split_value)

            elif edit_choice == "merge":
                if len(temp_measure_list) > 1:
                    if random_index == len(temp_measure_list) - 1:
                        merge_direction = -1
                    elif random_index == 0:
                        merge_direction = 1
                    else:
                        merge_direction = random.choice([-1, 1]) 
        
                    merge_note = float(temp_measure_list[random_index]) + float(temp_measure_list[random_index + merge_direction])
                    temp_measure_list[random_index] = merge_note
                    if random_index + merge_direction >= 0:
                        temp_measure_list.pop(random_index + merge_direction)

        rhythm_list.append(temp_measure_list)


    for measure_number, temp_measure in enumerate(rhythm_list):
        for ind, note_duration in enumerate(temp_measure):
            if random.choice(["note", "note", "rest"]) == "rest" and sum(temp_measure[:ind]) % beat_value == 0:
                new_note = note.Rest(note_duration)
            else:
                new_note = note.Note("E4")
                new_note.duration.quarterLength = note_duration
            new_stream.measure(measure_number + 1).append(new_note)
    
    new_stream.makeTies()
    new_stream.makeNotation()

    return new_stream

def generate_arpeggio(arp_root=None, arp_quality=None, arp_duration=None):

    new_stream = stream.Stream()
    new_chord = generate_chord(chord_root_list=arp_root, chord_quality_list=arp_quality)
    back_down_pitches = list(reversed(new_chord.pitches[:-1]))
    arp_pitches = list(new_chord.pitches) + back_down_pitches

    if arp_duration != None:
        random_duration = arp_duration
    else:
        duration_choices = [0.5, 1]
        random_duration = random.choice(duration_choices)

    for p in arp_pitches:
        new_note = note.Note(p)
        new_note.duration.quarterLength = random_duration
        new_stream.append(new_note)

    return new_stream.makeMeasures(), [p.nameWithOctave for p in new_stream.pitches], new_chord

def generate_note_value(specific_note_values=[], rest_or_note=None):
    new_stream = stream.Stream()
    new_stream.staffLines = 1
    if rest_or_note == None:
        rest_or_note = random.choice(["note", "rest"])
        
    if rest_or_note == "note":
        new_note = note.Note("E4")
    elif rest_or_note == "rest":
        new_note = note.Rest()

    if len(specific_note_values) != 0:
        new_note.duration.quarterLength = random.choice(specific_note_values)
    else:
        new_note.duration.quarterLength = random.choice([0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6])

    new_stream.append(new_note)

    return new_stream, new_note


### Secondary Functions ###

def move_in_thirds(input_chord, input_scale, direction, iterate):
    # will have to figure out which mode is closest to original key
    input_scale = scale.DiatonicScale(input_chord[0])
    if direction == -1:
        new_root = input_scale.nextPitch(input_chord[0].nameWithOctave, scale.Direction.DESCENDING, stepSize = 2 * iterate)
    elif direction == 1:
        new_root = input_scale.nextPitch(input_chord[0].nameWithOctave, scale.Direction.ASCENDING, stepSize = 2 * iterate)
    elif direction == 0:
        return input_chord

    new_root_scale_degree = input_scale.getScaleDegreeFromPitch(new_root)

    diatonic_majors = [1, 4, 5]
    diatonic_minors = [2, 3, 6]

    if new_root_scale_degree in diatonic_majors:
        return generate_chord([new_root], [""])
    elif new_root_scale_degree in diatonic_minors:
        return generate_chord([new_root], ["m"])
    elif new_root_scale_degree == 7: #will have to check if non-diatonic is allowed then change it to flat 7
        return generate_chord([new_root], ["dim"])

def change_quality(input_chord, input_quality = None, non_diatonic = False): #add condition for diatonicism

    chord_intervals = input_chord.annotateIntervals(inPlace=False)
    chord_intervals = [ly.text for ly in reversed(chord_intervals.lyrics)]

    if input_quality != None:
        return generate_chord([input_chord[0].nameWithOctave], [input_quality])
    
    else:
        if bool(set([9, 11, 13]) & set(chord_intervals)) == True:
            quality_choices = list(range(37, 58))
        elif bool(set([7]) & set(chord_intervals)) == True:
            quality_choices = list(range(9, 37))
        else:
            quality_choices = list(range(0, 9))
            quality_choices.remove(3)

        if chord_intervals in list(chord_by_interval_dict.values()):
            quality_choices.remove(list(chord_by_interval_dict.values()).index(chord_intervals)) #remove original quality from choices
    
        new_chord = generate_chord([input_chord[0].nameWithOctave], [chord_interval_list[random.choice(quality_choices)]])
        
        return new_chord

def add_extensions(input_chord, input_scale, non_diatonic = False): #maybe instead of adding a bunch of extensions, we only add the non-diatonic ones
    new_chord = chord.Chord(input_chord.pitches)
    iterate_number = random.choice([1, 1, 1, 1, 2, 2, 2, 3, 4])
    new_mode = None

    if input_chord.quality == "major":
        new_mode = scale.LydianScale(input_chord[0])
    elif input_chord.quality == "minor":
        new_mode = scale.DorianScale(input_chord[0])
    elif input_chord.quality == "augmented":
        new_mode = scale.WholeToneScale(input_chord[0])
    elif input_chord.quality == "diminished": 
        if input_chord.isHalfDiminishedSeventh == True:
            new_mode = dorian_flat5_scale._net.realizePitch(input_chord[0])
        elif input_chord.isDiminishedSeventh == True:
            new_mode = whole_half_diminished_scale._net.realizePitch(input_chord[0])
        elif input_chord.isTriad == True:
            new_mode = dorian_flat5_scale._net.realizePitch(input_chord[0])
    else:
        new_mode = scale.DiatonicScale(input_chord[0])

    if non_diatonic == True:
        ref_scale = new_mode
    else:
        ref_scale = input_scale

    if len(new_chord) < 7 and ref_scale != None:
        for i in range(iterate_number + 1):
            new_extension = ref_scale.nextPitch(new_chord[-1].nameWithOctave, scale.Direction.ASCENDING, stepSize = 2)
            if new_extension.simplifyEnharmonic().name not in new_chord.pitchNames:
                new_chord.add(new_extension.simplifyEnharmonic())
            if len(new_chord) == 7:
                break

    return new_chord.simplifyEnharmonics()

def tritone_sub(input_chord):
    trione_chord = input_chord.transpose("d5")
    return trione_chord.simplifyEnharmonics()

def retroactive_dom(input_chord, chord_duration, input_scale, non_diatonic = False): #add condition for diatonicism
    ref_scale = scale.DiatonicScale(input_chord[0])
    dom_chord = generate_chord([ref_scale.getDominant().nameWithOctave], [""])
    new_chord = chord.Chord(input_chord.pitches)
    new_chord.duration.quarterLength = chord_duration / 2
    dom_chord.duration.quarterLength = chord_duration / 2
    return dom_chord.simplifyEnharmonics(), new_chord.simplifyEnharmonics()

def generate_time_elements(denominators = [], numerators = []):
    #create time signature
    if len(denominators) != 0:
        denominator_select = random.choice(denominators)
    else:
        denominator_choices = [4, 8] #we will have to vary complexity
        denominator_select = random.choice(denominator_choices)
    
    if len(numerators) != 0:
        numerator_select = random.choice(numerators)
    else:
        if denominator_select == 4:
            numerator_choices = [2, 3, 4, 5, 6, 7]
        elif denominator_select == 8:
            numerator_choices = [5, 6, 7, 9, 10, 12]
        numerator_select = random.choice(numerator_choices)

    time_sig_string = str(numerator_select) + "/" + str(denominator_select)
    time_sig = meter.TimeSignature(time_sig_string)
    
    #create meter sequence
    prime_numbers = [3, 5, 7, 11, 13]
    meter_sequence = meter.MeterSequence(time_sig_string)
    if meter_sequence.numerator in prime_numbers and meter_sequence.numerator > 4:
        meter_seq_options = meter_sequence.getPartitionOptions()[:math.floor(meter_sequence.numerator / 2)]
        meter_sequence = meter.MeterSequence(random.choice(meter_seq_options))
    else:
        meter_sequence = meter.MeterSequence(meter_sequence.getPartitionOptions()[0])
    meter_division_count = str(meter_sequence).count("+") + 1
    time_sig.beamSequence = meter_sequence
    time_sig.beatSequence = meter_sequence

    return time_sig, meter_division_count, meter_sequence


### Auxillary Functions ###

def fix_chord_spelling(chord_item):
        chord_item.root(chord_item.bass())
        chord_item.sortAscending()
        pitch_list = list(chord_item.pitches)
        fixed_chord = chord.Chord()
        for num, p in enumerate(pitch_list):
            if num == 0:
                fixed_chord.add(p)
            else:
                interval_check = interval.Interval(pitchStart=pitch_list[0], pitchEnd=p).name
                if interval_check in ["d4", "A6", "d8", "A8", "A12", "dd10", "d9", "dd11"]:
                    respell = pitch.Pitch(p.getEnharmonic())
                elif interval_check in ["A5", "A4"] and num > 2:
                    respell = pitch.Pitch(p.getEnharmonic()) 
                elif interval_check in ["m6", "dd6"] and num < 3:
                    respell = pitch.Pitch(p.getEnharmonic())
                elif interval_check in ["m10", "m3",] and num > 2:
                    sharp_nine = interval.Interval("A9")
                    sharp_nine.pitchStart = pitch_list[0]
                    respell = sharp_nine.pitchEnd
                elif interval_check in ["dd7"] == 2:
                    respell = pitch.Pitch(p.getEnharmonic())
                else:
                    respell = p
                if "--" not in respell.nameWithOctave:
                    fixed_chord.add(respell)
                else:
                    fixed_chord.add(pitch.Pitch(respell.getEnharmonic()))
        fixed_chord.root(fixed_chord.bass())
        fixed_chord.sortAscending()

        fixed_chord_intervals = fixed_chord.annotateIntervals(inPlace=False, stripSpecifiers=False)
        fixed_chord_intervals = [ly.text for ly in reversed(fixed_chord_intervals.lyrics)]

        # print(fixed_chord)
        # print(fixed_chord_intervals)
        return fixed_chord

def convert_to_roman_numerals(chord_item, input_key):
    fixed_chord = fix_chord_spelling(chord_item)
    chord_symbol = harmony.chordSymbolFromChord(fixed_chord).figure
    extensions = chord_symbol.replace(fixed_chord.root().name, "")
    roman_numeral = roman.romanNumeralFromChord(fixed_chord, input_key)
    base_roman = roman_numeral.romanNumeral
    if base_roman.islower() == True and extensions[0] == "m":
        extensions = extensions[1:]
    # print(chord_symbol, base_roman)
    completed_roman_numeral = base_roman + extensions
    # print(completed_roman_numeral)
    return completed_roman_numeral

def generate_prompt_text(question_type, answer_type, language="en"):
    if language == "en":
        if question_type == "audio":
            prompt_text1 = "Listen"
        else:
            prompt_text1 = "Read"

        if answer_type in ["piano", "record"]:
            prompt_text2 = "play"
        elif "mc" in answer_type:
            prompt_text2 = "select"
        else:
            prompt_text2 = "type"

    elif language == "es":
        if question_type == "audio":
            prompt_text1 = "Escuche"
        else:
            prompt_text1 = "Lea"

        if answer_type in ["piano", "record"]:
            prompt_text2 = "toque"
        elif "mc" in answer_type:
            prompt_text2 = "seleccione"
        else:
            prompt_text2 = "escriba"

    prompt_text_full = prompt_text1 + " and " + prompt_text2
    return prompt_text_full

