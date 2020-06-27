{
    "interactionModel": {
        "languageModel": {
            "invocationName": "yana",
            "intents": [
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": [
                        "what should i tell now",
                        "please help",
                        "what",
                        "what to do next",
                        "i ama unable to understand",
                        "help"
                    ]
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "citycall_intent",
                    "slots": [
                        {
                            "name": "city",
                            "type": "city"
                        },
                        {
                            "name": "area",
                            "type": "area"
                        },
                        {
                            "name": "book",
                            "type": "book"
                        }
                    ],
                    "samples": [
                        "i want to place my",
                        "my place is",
                        "i live in",
                        "i live in {city} city {area}",
                        "{city} city {area}",
                        "i live in {area} {city}",
                        "i want to place {book} at {city} {area}",
                        "{city} {area} is my place",
                        "i want to place my {book} at {city} city {area} area",
                        "{city} city {area} is my place",
                        "my place is {city} {area}",
                        "my place is {city} city {area}",
                        "i want to place my {book} in {city} {area}",
                        "i want to place my {book} at {city} city {area} ",
                        "{city}",
                        "{area} {city}",
                        "{area}",
                        "place my {book} at {city} {area}",
                        "{area} {city} is my",
                        "{area} {city} is my place",
                        "my place is {area} {city}",
                        "i want to place my {book} at {area} {city} ",
                        "{city} {area}"
                    ]
                },
                {
                    "name": "hotelcall_intent",
                    "slots": [
                        {
                            "name": "hotels",
                            "type": "hotel"
                        }
                    ],
                    "samples": [
                        "i want to order from {hotels} restaurant",
                        "i will order from {hotels} hotel",
                        "select {hotels} restaurant",
                        "select {hotels} hotel",
                        "restaurant {hotels}",
                        "{hotels} restaurant",
                        "hotel {hotels}",
                        "{hotels} hotel",
                        "{hotels}"
                    ]
                },
                {
                    "name": "menuselect_intent",
                    "slots": [],
                    "samples": []
                },
                {
                    "name": "additem_intent",
                    "slots": [
                        {
                            "name": "number",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "item",
                            "type": "item"
                        }
                    ],
                    "samples": [
                        "{item} {number}",
                        "another {number} {item}",
                        "another {item}",
                        "add another {item}",
                        "add another {number} {item}",
                        "we want {item}",
                        "we want {number} {item}",
                        "i want {item}",
                        "i want {number} {item}",
                        "add {item} and quantity is {number}",
                        "select {number} {item}",
                        "add {item}",
                        "select {item}",
                        "{item}",
                        "{number} {item}",
                        "add {number} {item}"
                    ]
                },
                {
                    "name": "billing_intent",
                    "slots": [],
                    "samples": [
                        "proceed with the order",
                        "proceed with this order",
                        "proceed for billing",
                        "place this order",
                        "place the order",
                        "order this much",
                        "order it",
                        "bring it",
                        "this is my order",
                        "place it",
                        "finish",
                        "that's it",
                        "done"
                    ]
                },
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.YesIntent",
                    "samples": [
                        "yes yes confirm yes",
                        "yes yes",
                        "yes confirm",
                        "confirmed",
                        "confirm",
                        "confirm it",
                        "yes baby",
                        "do it",
                        "okay do it",
                        "okay",
                        "yo baby",
                        "yes",
                        "ya",
                        "sure",
                        "yup"
                    ]
                },
                {
                    "name": "AMAZON.NoIntent",
                    "samples": [
                        "nana karte pyar kisi se kar bete",
                        "no baba",
                        "naaa",
                        "naa",
                        "na",
                        "no wait",
                        "nope wait",
                        "nope",
                        "no"
                    ]
                }
            ],
            "types": [
                {
                    "name": "city",
                    "values": [
                        {
                            "name": {
                                "value": "mumbai",
                                "synonyms": [
                                    "mumbe",
                                    "mumba",
                                    "amchi mumbai",
                                    "sapno ki nagari",
                                    "bambay",
                                    "bombay"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "hyderabad",
                                "synonyms": [
                                    "hydarebad",
                                    "hydarabad",
                                    "hydera"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "bangalore",
                                "synonyms": [
                                    "bangaluru",
                                    "bengaluru",
                                    "bengalore"
                                ]
                            }
                        }
                    ]
                },
                {
                    "name": "area",
                    "values": [
                        {
                            "name": {
                                "value": "mubarakpet",
                                "synonyms": [
                                    "moobarak",
                                    "moobarakpet",
                                    "mobarakpet",
                                    "mubarakpat",
                                    "mubarkpat"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "baba ali road",
                                "synonyms": [
                                    "babaali",
                                    "baba ali",
                                    "baba aliroad",
                                    "babaali road",
                                    "babaaliroad"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "cantonment",
                                "synonyms": [
                                    "mumbai cant",
                                    "mumbaicant",
                                    "canton",
                                    "cant"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "south bandra",
                                "synonyms": [
                                    "southbendra",
                                    "south bendra",
                                    "bendra",
                                    "southbandra"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "channasandra",
                                "synonyms": [
                                    "chennasandra",
                                    "chnsndra",
                                    "chnsndra",
                                    "chanasandra"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "whitefield",
                                "synonyms": [
                                    "wt fld",
                                    "white field"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "jayanagar",
                                "synonyms": [
                                    "jayngra",
                                    "jngra",
                                    "jaynagar",
                                    "jayanagara",
                                    "jaynagara"
                                ]
                            }
                        }
                    ]
                },
                {
                    "name": "book",
                    "values": [
                        {
                            "name": {
                                "value": "order"
                            }
                        },
                        {
                            "name": {
                                "value": "book"
                            }
                        }
                    ]
                },
                {
                    "name": "hotel",
                    "values": [
                        {
                            "name": {
                                "value": "hot spot",
                                "synonyms": [
                                    "hotspot"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "green dot",
                                "synonyms": [
                                    "gendot",
                                    "geendot",
                                    "grendot",
                                    "greendot"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "socials",
                                "synonyms": [
                                    "social"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "tfc"
                            }
                        },
                        {
                            "name": {
                                "value": "euki",
                                "synonyms": [
                                    "ukki",
                                    "euuki",
                                    "euuke",
                                    "euukee",
                                    "uuki",
                                    "uki"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "oberoi",
                                "synonyms": [
                                    "oboroi"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "taj",
                                "synonyms": [
                                    "va taj"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "sri krishna sagar",
                                "synonyms": [
                                    "sri krishnasagar",
                                    "srikrishnasagar",
                                    "sks"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "atri",
                                "synonyms": [
                                    "atheri",
                                    "athri"
                                ]
                            }
                        }
                    ]
                },
                {
                    "name": "item",
                    "values": [
                        {
                            "name": {
                                "value": "virgin mojito"
                            }
                        },
                        {
                            "name": {
                                "value": "masala papad"
                            }
                        },
                        {
                            "name": {
                                "value": "pizza"
                            }
                        },
                        {
                            "name": {
                                "value": "sushi"
                            }
                        },
                        {
                            "name": {
                                "value": "momos"
                            }
                        },
                        {
                            "name": {
                                "value": "macroni"
                            }
                        },
                        {
                            "name": {
                                "value": "gobi crispy"
                            }
                        },
                        {
                            "name": {
                                "value": "baby corn crispy"
                            }
                        },
                        {
                            "name": {
                                "value": "paneer tikka"
                            }
                        },
                        {
                            "name": {
                                "value": "red sauce pasta"
                            }
                        },
                        {
                            "name": {
                                "value": "white sauce pasta"
                            }
                        },
                        {
                            "name": {
                                "value": "roti"
                            }
                        },
                        {
                            "name": {
                                "value": "aloo paratha"
                            }
                        }
                    ]
                },
                {
                    "name": "no",
                    "values": [
                        {
                            "name": {
                                "value": "nope"
                            }
                        },
                        {
                            "name": {
                                "value": "no pe"
                            }
                        },
                        {
                            "name": {
                                "value": "no i want to add more"
                            }
                        },
                        {
                            "name": {
                                "value": "no i will add something"
                            }
                        },
                        {
                            "name": {
                                "value": "wait"
                            }
                        },
                        {
                            "name": {
                                "value": "wait no"
                            }
                        },
                        {
                            "name": {
                                "value": "naa"
                            }
                        },
                        {
                            "name": {
                                "value": "no"
                            }
                        }
                    ]
                }
            ]
        },
        "dialog": {
            "intents": [
                {
                    "name": "citycall_intent",
                    "confirmationRequired": true,
                    "prompts": {
                        "confirmation": "Confirm.Intent.1229135580381"
                    },
                    "slots": [
                        {
                            "name": "city",
                            "type": "city",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        },
                        {
                            "name": "area",
                            "type": "area",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        },
                        {
                            "name": "book",
                            "type": "book",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        }
                    ]
                },
                {
                    "name": "hotelcall_intent",
                    "confirmationRequired": true,
                    "prompts": {
                        "confirmation": "Confirm.Intent.449214418612"
                    },
                    "slots": [
                        {
                            "name": "hotels",
                            "type": "hotel",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        }
                    ]
                },
                {
                    "name": "additem_intent",
                    "confirmationRequired": true,
                    "prompts": {
                        "confirmation": "Confirm.Intent.1105558479325"
                    },
                    "slots": [
                        {
                            "name": "number",
                            "type": "AMAZON.NUMBER",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        },
                        {
                            "name": "item",
                            "type": "item",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        }
                    ]
                },
                {
                    "name": "billing_intent",
                    "confirmationRequired": true,
                    "prompts": {
                        "confirmation": "Confirm.Intent.149428573918"
                    },
                    "slots": []
                }
            ]
        },
        "prompts": [
            {
                "id": "Confirm.Intent.934016994318",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "are you sure about the {city} city {area} area?"
                    }
                ]
            },
            {
                "id": "Confirm.Intent.449214418612",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "{hotels} restaurant. is this right?"
                    }
                ]
            },
            {
                "id": "Confirm.Intent.1229135580381",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "is {area} in {city} city correct?"
                    }
                ]
            },
            {
                "id": "Confirm.Intent.1105558479325",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "please provide the quantity?"
                    }
                ]
            },
            {
                "id": "Confirm.Intent.149428573918",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "are you sure to place the order?"
                    }
                ]
            }
        ]
    }
}
