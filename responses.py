import random

responses = {
    "hi": [
        "Yo da, what’s good?",
        "Ayy macha, how you vibin’?",
        "Hey ra, namma Bengaluru welcomes you!",
        "Hi boss, what’s the scene?",
        "Hello la, you back in namma city?",
        "Sup da, how’s it rolling?",
        "Hey there, namma techie life calling!"
    ],
    "hello": [
        "Hello hello, what’s cooking, da?",
        "Ayy ra, you landed in Bengaluru or what?",
        "Hi macha, all set for the day?",
        "Hello boss, namma vibe strong today!",
        "Hey la, you chilling like a Koramangala hipster?"
    ],
    "how are you": [
        "All chill da, you howda?",
        "I’m solid ra, what’s your scene?",
        "Jhakaas here, you tell macha!",
        "Good la, you surviving Bengaluru traffic?",
        "I’m tops da, you holding up?",
        "Chill boss, how’s your day going?",
        "All good ra, you still kicking it?"
    ],
    "what’s up": [
        "Not much da, just namma Bengaluru vibes!",
        "Ayy, same old grind, you what’s up?",
        "Chilling ra, what’s the word on the street?",
        "Just here macha, you got any plans?",
        "Nothing big la, you stirring something up?"
    ],
    "what can you do": [
        "I can chat like a boss da, what you want?",
        "Slang gyaan, chill vibes, you name it ra!",
        "Talk Bengaluru style, help you out, simple da!",
        "I’m your namma chatbot, what’s your ask?",
        "Throw me a line, I’ll sling some slang back, macha!",
        "Chat, crack jokes, keep it real—your call, da!"
    ],
    "bye": [
        "Catch you later macha, stay cool!",
        "Hogappa ra, don’t forget namma vibe!",
        "See ya da, keep it real!",
        "Take it easy boss, I’ll be around!",
        "Later la, namma Bengaluru’s waiting!",
        "Ciao da, stay jhakaas!"
    ],
    "thanks": [
        "No probs da, anytime!",
        "Cool ra, glad to help!",
        "Welcome macha, namma style!",
        "Chill boss, it’s all good!",
        "Anytime la, you’re the real MVP!"
    ],
    "cool": [
        "Jhakaas da, right?",
        "Too cool ra, namma Bengaluru level!",
        "Solid macha, you liking it?",
        "Cool beans boss, what’s next?",
        "Proper chill la, innit?"
    ],
    "where are you": [
        "Right here da, in namma digital Bengaluru!",
        "Chilling in the cloud ra, where you at?",
        "I’m namma GPT, everywhere and nowhere, macha!",
        "Stuck in Docker la, you know the vibe!",
        "Around boss, just a POST away!"
    ],
    "weather": [
        "Bengaluru weather da, always a mood!",
        "Chill ra, probably raining in Whitefield!",
        "Nice and cool macha, typical namma climate!",
        "Bit cloudy la, you stepping out?",
        "Perfect coffee weather boss, innit?"
    ],
    "food": [
        "Dosa da, always a win!",
        "Biryani ra, namma Bengaluru special!",
        "Macha, you tried filter coffee yet?",
        "Vada pav la, street food vibes!",
        "Boss, namma city’s food game is strong!"
    ],
    "traffic": [
        "Ugh da, MG Road’s a mess!",
        "Traffic ra, same old Bengaluru story!",
        "Macha, you stuck in namma jams?",
        "Peak hour la, adjust maadi!",
        "Boss, it’s Bengaluru—traffic’s life!"
    ],
    "work": [
        "Grindin’ da, you know the tech life!",
        "Work ra, same old namma hustle!",
        "Macha, you coding or chilling?",
        "Office vibes la, how’s your gig?",
        "Boss, namma Bengaluru work mode on!"
    ],
    "default": [
        "No clue da, ask something else!",
        "Adjust maadi ra, I’ll figure it out!",
        "Chill bro, I’ll reply faster than MG Road traffic!",
        "Huh la, you lost me there!",
        "Boss, try again, I’m half-asleep!",
        "Macha, what you on about?",
        "Dunno da, hit me with something clear!"
    ]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])