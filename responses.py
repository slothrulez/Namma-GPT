import random

responses = {
    "hi": [
        "Yo da, what’s good?",
        "Ayy macha, how you vibin’?",
        "Hey ra, namma Bengaluru welcomes you!"
    ],
    "how are you": [
        "All chill da, you howda?",
        "I’m solid ra, what’s your scene?",
        "Jhakaas here, you tell macha!"
    ],
    "what can you do": [
        "I can chat like a boss da, what you want?",
        "Slang gyaan, chill vibes, you name it ra!",
        "Talk Bengaluru style, help you out, simple da!"
    ],
    "bye": [
        "Catch you later macha, stay cool!",
        "Hogappa ra, don’t forget namma vibe!",
        "See ya da, keep it real!"
    ],
    "default": [
        "No clue da, ask something else!",
        "Adjust maadi ra, I’ll figure it out!",
        "Chill bro, I’ll reply faster than MG Road traffic!"
    ]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])