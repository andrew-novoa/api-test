
### Just for reference -- 55 combinations ###
qa_dict = {
    "text": ["text", "piano", "record", "mc text", "mc xml", "mc audio"],
    "audio": ["text", "record", "mc text", "mc xml", "mc audio"],
    "note": ["text", "piano", "record", "mc text", "mc xml"], 
    "interval": ["text", "piano", "record", "mc text", "mc xml", "mc audio"],
    "scale": ["text", "piano", "record", "mc text", "mc xml", "mc audio"],
    "chord": ["text", "piano", "record", "mc text", "mc xml", "mc audio"],
    "chord progression": ["text", "record", "mc text", "mc xml", "mc audio"],
    "excerpt": ["text", "record", "mc text", "mc xml", "mc audio"],
    "rhythm": ["text", "record", "mc text", "mc xml", "mc audio"],
    "arpeggio": ["text", "piano", "record", "mc text", "mc xml", "mc audio"]
    }
question_type_list = list(qa_dict.keys())

### Dictionary of what questions can be asked per user level ###
question_levels = {
    "piano": {
        "theory":{
            1:{ ### Theory Chapter 1 ###
                "chapter name": "Getting Started",
                "lessons":{
                    1:{ #T1-1#
                        "lesson name": "Your First Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            }    
                        }
                    },
                    2:{ #T1-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            }
                        }
                    },
                    3:{ #T1-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            }
                        }
                    },
                    4:{ #T1-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    5:{ #T1-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    }
                }
            },
            2:{ ### Theory Chapter 2 ###
                "chapter name": "2nd Chapter",
                "lessons":{
                    1:{ #T2-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    2:{ #T2-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "text":{
                                "text":["scale degree"],
                                "piano":["play pitch", "play scale degree"],
                                "record":["play pitch", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    3:{ #T2-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            }
                        }
                    },
                    4:{ #T2-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    5:{ #T2-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    6:{ #T2-6#
                        "lesson name": "6th Lesson",
                        "question choices":{
                            "text":{
                                "piano":["play pitch"],
                                "record":["play pitch", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    7:{ #T2-7#
                        "lesson name": "7th Lesson",
                        "question choices":{
                                "text":{
                                    "text":["interval semitones"],
                                    "piano":["play pitch", "play interval"],
                                    "record":["play pitch", "play scale"] 
                                },
                                "note":{
                                    "text":["identify", "black or white"],
                                    "piano":["play pitch"],
                                    "record":["play pitch"]
                                },
                                "interval":{
                                    "text":["identify", "semitones"],
                                    "piano":["play interval"],
                                    "record":["play interval"],
                                    "mc text":["correct name"]
                                },
                                "scale":{
                                    "record":["play scale"]
                                }
                            }
                        }
                    }
                },
            3:{ ### Theory Chapter 3 ###
                "chapter name": "3rd Chapter",
                "lessons":{
                    1:{ #T3-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    2:{ #T3-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    3:{ #T3-2#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    4:{ #T3-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    5:{ #T3-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    6:{ #T3-6#
                        "lesson name": "6th Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"]
                            },
                            "scale":{
                                "record":["play scale"]
                            }
                        }
                    },
                    7:{ #T3-7#
                        "lesson name": "7th Lesson",
                        "question choices":{
                                "text":{
                                    "text":["chord intervals", "chord intervals half steps", "interval semitones"],
                                    "piano":["play pitch", "play chord tone", "play second note in interval", "play interval"],
                                    "record":["play pitch", "play chord", "play scale"] 
                                },
                                "note":{
                                    "text":["identify", "black or white"],
                                    "piano":["play pitch"],
                                    "record":["play pitch"]
                                },
                                "chord":{
                                    "text":["quality", "intervals", "intervals half steps"],
                                    "piano":["play chord tone"],
                                    "record":["play chord"],
                                    "mc text":["quality"]
                                },
                                "chord progression":{
                                    "record":["play progression"]
                                },
                                "interval":{
                                    "text":["identify", "semitones"],
                                    "piano":["play interval"],
                                    "record":["play interval"],
                                    "mc text":["correct name"]
                                },
                                "scale":{
                                    "record":["play scale"]
                                }
                            }
                        }
                    }
                },
            4:{ ### Theory Chapter 4 ###
                "chapter name": "4th Chapter",
                "lessons":{
                    1:{ #T4-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    2:{ #T4-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    3:{ #T4-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    4:{ #T4-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    5:{ #T4-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"],
                                "mc xml":["is transposition", "specific transposition"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    }
                }
            },
            5:{ ### Theory Chapter 5 ###
                "chapter name": "5th Chapter",
                "lessons":{
                    1:{ #T5-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"],
                                "mc text":["diatonic chord", "nondiatonic chord"],
                                "mc xml":["diatonic chord", "nondiatonic chord"]
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    2:{ #T5-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"],
                                "mc text":["diatonic chord", "nondiatonic chord"],
                                "mc xml":["diatonic chord", "nondiatonic chord"]
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    3:{ #T5-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"],
                                "mc text":["diatonic chord", "nondiatonic chord"],
                                "mc xml":["diatonic chord", "nondiatonic chord"]
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "text":["diatonic or not"],
                                "record":["play progression"],
                                "mc text":["find non diatonic"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    4:{ #T5-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"],
                                "mc text":["diatonic chord", "nondiatonic chord"],
                                "mc xml":["diatonic chord", "nondiatonic chord"]
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "text":["diatonic or not"],
                                "record":["play progression"],
                                "mc text":["find non diatonic"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    5:{ #T5-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"],
                                "mc xml":["is transposition", "specific transposition"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    },
                    6:{ #T5-6#
                        "lesson name": "6th Lesson",
                        "question choices":{
                            "text":{
                                "text":["chord intervals", "chord intervals half steps", "interval semitones", "scale degree"],
                                "piano":["play pitch", "play chord tone", "play second note in interval", "play interval", "play scale degree"],
                                "record":["play pitch", "play chord", "play scale"] 
                            },
                            "note":{
                                "text":["identify", "black or white"],
                                "piano":["play pitch"],
                                "record":["play pitch"]
                            },
                            "chord":{
                                "text":["quality", "intervals", "intervals half steps"],
                                "piano":["play chord tone"],
                                "record":["play chord"],
                                "mc text":["quality"]
                            },
                            "chord progression":{
                                "record":["play progression"],
                                "mc xml":["is transposition", "specific transposition"]
                            },
                            "interval":{
                                "text":["identify", "semitones"],
                                "piano":["play interval"],
                                "record":["play interval"],
                                "mc text":["correct name"],
                                "mc xml":["correct transposition"]
                            },
                            "scale":{
                                "piano":["play scale degree"],
                                "record":["play scale"]
                            }
                        }
                    }
                }
            }
        },

        "rhythm":{
            1:{ ### Rhythm Chapter 1 ###
                "chapter name": "1st Chapter",
                "lessons":{
                    1:{ #R1-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "audio":{
                                "text":["beats"]
                            }
                        }
                    },
                    2:{ #R1-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "audio":{
                                "text":["beats"]
                            }
                        }
                    },
                    3:{ #R1-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "audio":{
                                "text":["beats"]
                            }
                        }
                    },
                    4:{ #R1-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration"],
                                "mc text":["note value duration"]
                            },
                            "rhythm":{
                                "text":["note value duration"],
                                "mc text":["note value duration"]
                            }
                        }
                    },
                    5:{ #R1-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration"],
                                "mc text":["note value duration"]
                            },
                            "rhythm":{
                                "text":["note value duration"],
                                "mc text":["note value duration"]
                            }
                        }
                    },
                    6:{ #R1-6#
                        "lesson name": "6th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration"],
                                "mc text":["note value duration"]
                            },
                            "rhythm":{
                                "text":["note value duration"],
                                "mc text":["note value duration"]
                            }
                        }
                    }
                }
            },
            2:{ ### Rhythm Chapter 2 ###
                "chapter name": "2nd Chapter",
                "lessons":{
                    1:{ #R2-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    2:{ #R2-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    3:{ #R2-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    4:{ #R2-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    5:{ #R2-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    6:{ #R2-6#
                        "lesson name": "6th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    }
                }
            },
            3:{ ### Rhythm Chapter 3 ###
                "chapter name": "3rd Chapter",
                "lessons":{
                    1:{ #R3-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    2:{ #R3-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    3:{ #R3-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    4:{ #R3-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    5:{ #R3-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    6:{ #R3-6#
                        "lesson name": "6th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    }
                }
            },
            4:{ ### Rhythm Chapter 4 ###
                "chapter name": "4th Chapter",
                "lessons":{
                    1:{ #R4-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    2:{ #R4-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    }, 
                    3:{ #R4-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    4:{ #R4-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    },
                    5:{ #R4-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "text":{
                                "text":["note value duration", "note value subdivision"],
                                "mc text":["note value duration", "note value subdivision"]
                            },
                            "rhythm":{
                                "text":["subdivision", "beats", "note value duration"],
                                "record":["play rhythm"],
                                "mc text":["subdivision", "beats", "note value duration"]
                            }
                        }
                    }
                }
            }
        },

        "listen":{
            1:{ ### Listen Chapter 1 ###
                "chapter name": "1st Chapter",
                "lessons":{
                    1:{ #L1-1#
                        "lesson name": "1st Lesson",
                        "question choices":{
                            "audio":{
                                "text":["up or down"]
                            }
                        }
                    },
                    2:{ #L1-2#
                        "lesson name": "2nd Lesson",
                        "question choices":{
                            "audio":{
                                "text":["up or down"]
                            }
                        }
                    },
                    3:{ #L1-3#
                        "lesson name": "3rd Lesson",
                        "question choices":{
                            "audio":{
                                "text":["up or down"]
                            }
                        }
                    },
                    4:{ #L1-4#
                        "lesson name": "4th Lesson",
                        "question choices":{
                            "audio":{
                                "text":["up or down"],
                                "mc audio":["correct audio"]
                            }
                        }
                    },
                    5:{ #L1-5#
                        "lesson name": "5th Lesson",
                        "question choices":{
                            "audio":{
                                "mc audio":["correct audio"]
                            }
                        }
                    }
                }
            }
        }
    },

    "guitar":{
        "theory":{},
        "rhythm":{},
        "listen":{}
    },

    "bass":{
        "theory":{},
        "rhythm":{},
        "listen":{}
    },

    "ukulele":{
        "theory":{},
        "rhythm":{},
        "listen":{}
    }
}


### Dictionary of what content the questions can ask ###
content_levels = {
    "piano": {
        "theory":{
            ### Theory Chapter 1 ###
            "T1-1":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T1-2":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T1-3":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T1-4":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T1-5":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },

            ### Theory Chapter 2 ###
            "T2-1":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T2-2":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T2-3":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T2-4":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T2-5":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T2-6":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T2-7":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },

            ### Theory Chapter 3 ###
            "T3-1":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T3-2":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T3-3":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T3-4":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T3-5":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T3-6":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T3-7":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },

            ### Theory Chapter 4 ###
            "T4-1":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T4-2":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T4-3":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T4-4":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T4-5":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },

            ### Theory Chapter 5 ###
            "T5-1":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{"1": True},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T5-2":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{"1": True},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F", "B-", "E-"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T5-3":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{"1": True},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F", "B-", "E-"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T5-4":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{"1": True},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F", "B-", "E-", "A-", "D-"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T5-5":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{"1": True},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F", "B-", "E-", "A-", "D-"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "T5-6":{
                "generate note":{"2": True},
                "generate chord":{"1":["", "m", "+", "dim"], "2": True},
                "generate chord progression":{"1": True},
                "generate interval":{},
                "generate scale":{"0":["C", "G", "D", "A", "E", "B", "F", "B-", "E-", "A-", "D-", "G-", "F#"], "1":["ionian"]},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            }
        },
        "rhythm":{
            ### Rhythm Chapter 1 ###
            "R1-1":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R1-2":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R1-3":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R1-4":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R1-5":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R1-6":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            ### Rhythm Chapter 2 ###
            "R2-1":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R2-2":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R2-3":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R2-4":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R2-5":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R2-6":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            ### Rhythm Chapter 3 ###
            "R3-1":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R3-2":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R3-3":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R3-4":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R3-5":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5]},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "R3-6":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5]},
                "generate time elements":{"0":[4, 8], "1":[4]}
            },
            ### Rhythm Chapter 4 ###
            "R4-1":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5, 0.25]},
                "generate time elements":{"0":[4, 8], "1":[4]}
            },
            "R4-2":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5, 0.25]},
                "generate time elements":{"0":[4, 8], "1":[4]}
            },
            "R4-3":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5, 0.25]},
                "generate time elements":{"0":[4, 8], "1":[4]}
            },
            "R4-4":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5, 0.25]},
                "generate time elements":{"0":[4, 8], "1":[4]}
            },
            "R4-5":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"0":[4], "1":[4], "3": 1},
                "generate arpeggio":{},
                "generate note value":{"0":[1, 2, 4, 1.5, 3, 0.5, 0.25]},
                "generate time elements":{"0":[4, 8], "1":[4]}
            }
        },
        "listen":{
                ### Listen Chapter 1 ###
            "L1-1":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "L1-2":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "L1-3":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "L1-4":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            },
            "L1-5":{
                "generate note":{"2": True},
                "generate chord":{},
                "generate chord progression":{},
                "generate interval":{},
                "generate scale":{},
                "generate excerpt":{},
                "generate rhythm":{"3": 1},
                "generate arpeggio":{},
                "generate note value":{},
                "generate time elements":{"0":[4], "1":[4]}
            }
        }
    },

    "guitar":{
        "theory":{},
        "rhythm":{},
        "listen":{}
    },

    "bass":{
        "theory":{},
        "rhythm":{},
        "listen":{}
    },

    "ukulele":{
        "theory":{},
        "rhythm":{},
        "listen":{}
    }
}


