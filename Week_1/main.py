"""
Basic AI Logic System: Recommendation Chatbot
Topic: AI Basics + Python
Demonstrates: if-else decision-making, rule-based AI
"""

# ─────────────────────────────────────────────
#  KNOWLEDGE BASE  (the AI's "brain")
# ─────────────────────────────────────────────

MOVIES = {
    ("action", "happy"):    "🎬 Mad Max: Fury Road  — high-octane thrills!",
    ("action", "sad"):      "🎬 John Wick           — lose yourself in the action.",
    ("action", "bored"):    "🎬 Top Gun: Maverick   — pure adrenaline.",
    ("comedy", "happy"):    "🎬 The Grand Budapest Hotel — witty & whimsical.",
    ("comedy", "sad"):      "🎬 Superbad            — guaranteed laughs.",
    ("comedy", "bored"):    "🎬 Game Night          — light & fun.",
    ("drama", "happy"):     "🎬 The Pursuit of Happyness — inspiring story.",
    ("drama", "sad"):       "🎬 Good Will Hunting   — deeply moving.",
    ("drama", "bored"):     "🎬 Parasite            — gripping from start to end.",
    ("horror", "happy"):    "🎬 Get Out             — smart & chilling.",
    ("horror", "sad"):      "🎬 A Quiet Place       — tense & emotional.",
    ("horror", "bored"):    "🎬 Hereditary          — will keep you on edge.",
    ("sci-fi", "happy"):    "🎬 Interstellar        — awe-inspiring adventure.",
    ("sci-fi", "sad"):      "🎬 Arrival             — beautifully melancholic.",
    ("sci-fi", "bored"):    "🎬 The Martian         — smart, fun survival story.",
}

ACTIVITIES = {
    ("outdoor", "energetic"):  "🏃 Go for a trail run or hike nearby.",
    ("outdoor", "relaxed"):    "🌿 Take a slow walk in a park or by the sea.",
    ("outdoor", "social"):     "🏏 Organise a cricket or football match with friends.",
    ("indoor", "energetic"):   "💪 Do a home HIIT workout (YouTube has great free ones).",
    ("indoor", "relaxed"):     "📚 Curl up with a good book and some chai.",
    ("indoor", "social"):      "🎮 Host a board-game or video-game evening.",
    ("creative", "energetic"): "🎨 Start a DIY project or redecorate a corner of your room.",
    ("creative", "relaxed"):   "✏️  Sketch, journal, or try digital art.",
    ("creative", "social"):    "🎵 Jam session or collaborate on a creative project with friends.",
}


# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def get_valid_input(prompt: str, options: list[str]) -> str:
    """Keep asking until the user enters a valid option."""
    options_lower = [o.lower() for o in options]
    while True:
        raw = input(prompt).strip().lower()
        if raw in options_lower:
            return raw
        print(f"  ⚠  Please choose one of: {', '.join(options)}\n")


def separator(char="─", width=50):
    print(char * width)


# ─────────────────────────────────────────────
#  AI MODULES
# ─────────────────────────────────────────────

def movie_recommender():
    """Rule-based movie recommendation engine."""
    separator()
    print("🎥  MOVIE RECOMMENDER")
    separator()

    genre = get_valid_input(
        "What genre do you feel like?\n"
        "  Options: action | comedy | drama | horror | sci-fi\n"
        "> ",
        ["action", "comedy", "drama", "horror", "sci-fi"]
    )

    mood = get_valid_input(
        "\nHow are you feeling right now?\n"
        "  Options: happy | sad | bored\n"
        "> ",
        ["happy", "sad", "bored"]
    )

    key = (genre, mood)
    recommendation = MOVIES.get(key)

    print()
    if recommendation:
        print(f"  ✅  Based on your mood & taste, I recommend:\n  {recommendation}")
    else:
        print("  🤔  Hmm, I don't have a match — try exploring IMDb for that combo!")


def activity_recommender():
    """Rule-based activity suggestion engine."""
    separator()
    print("🏄  ACTIVITY RECOMMENDER")
    separator()

    setting = get_valid_input(
        "What kind of setting do you prefer?\n"
        "  Options: outdoor | indoor | creative\n"
        "> ",
        ["outdoor", "indoor", "creative"]
    )

    energy = get_valid_input(
        "\nWhat's your energy level?\n"
        "  Options: energetic | relaxed | social\n"
        "> ",
        ["energetic", "relaxed", "social"]
    )

    key = (setting, energy)
    recommendation = ACTIVITIES.get(key)

    print()
    if recommendation:
        print(f"  ✅  Here's what I suggest:\n  {recommendation}")
    else:
        print("  🤔  No match found — try a new hobby you've been putting off!")


def weather_advisor():
    """Simple rule-based weather advice system."""
    separator()
    print("🌤   WEATHER ADVISOR")
    separator()

    temp = get_valid_input(
        "What's the temperature like outside?\n"
        "  Options: hot | warm | cool | cold\n"
        "> ",
        ["hot", "warm", "cool", "cold"]
    )

    sky = get_valid_input(
        "\nWhat's the sky like?\n"
        "  Options: sunny | cloudy | rainy\n"
        "> ",
        ["sunny", "cloudy", "rainy"]
    )

    # Decision tree
    if temp == "hot":
        if sky == "sunny":
            advice = "🌞 Very hot & sunny — stay hydrated, wear sunscreen, avoid peak hours outdoors."
        elif sky == "cloudy":
            advice = "⛅ Hot but overcast — still warm, light cotton clothing recommended."
        else:  # rainy
            advice = "🌧  Hot rain — classic Karachi weather! Carry an umbrella & watch for flooding."

    elif temp == "warm":
        if sky == "sunny":
            advice = "😊 Perfect weather! Great time for a walk or outdoor activity."
        elif sky == "cloudy":
            advice = "🌤  Comfortable & mild — ideal for a relaxed outing."
        else:
            advice = "🌦  Light rain + warm = refreshing. A light jacket should do."

    elif temp == "cool":
        if sky == "sunny":
            advice = "🍂 Cool & sunny — lovely! Layer up and enjoy the outdoors."
        elif sky == "cloudy":
            advice = "🌥  Cool and grey — cosy indoors day or a brisk walk."
        else:
            advice = "🌧  Cool rain — a hot cup of chai and a book sounds ideal!"

    else:  # cold
        if sky == "sunny":
            advice = "❄️  Cold but bright — bundle up and enjoy the crisp air."
        elif sky == "cloudy":
            advice = "🧥 Cold & overcast — heavy layers, stay warm!"
        else:
            advice = "🌨  Cold rain — stay indoors if you can. Hot soup recommended!"

    print(f"\n  ✅  My advice:\n  {advice}")


def simple_chatbot():
    """Keyword-based conversational chatbot."""
    separator()
    print("💬  SIMPLE CHATBOT  (type 'quit' to exit)")
    separator()

    responses = {
        # Greetings
        "hello":    "Hey there! 👋 How can I help you today?",
        "hi":       "Hi! 😊 What's on your mind?",
        "hey":      "Hey! What can I do for you?",
        # Farewells
        "bye":      "Goodbye! Take care! 👋",
        "goodbye":  "See you later! 😊",
        # State
        "how are you":   "I'm just a program, but I'm running great! 🤖",
        "what are you":  "I'm a simple rule-based AI chatbot built with Python!",
        # Topics
        "help":     "I can help with recommendations! Try asking about movies or activities.",
        "weather":  "I have a weather advisor! Go back and choose option 3.",
        "movie":    "I love movies! Use option 1 in the main menu for a personalised pick.",
        "bored":    "Feeling bored? Try option 2 for activity ideas! 🎯",
        "thanks":   "You're welcome! 😊",
        "thank you":"Happy to help! 😊",
    }

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input in ("quit", "exit", "back"):
            print("Bot: Returning to main menu...\n")
            break

        # Check for keyword matches
        matched = False
        for keyword, reply in responses.items():
            if keyword in user_input:
                print(f"Bot: {reply}")
                matched = True
                break

        if not matched:
            # Fallback response
            if "?" in user_input:
                print("Bot: That's a great question! I'm still learning. 🤔")
            elif len(user_input) < 3:
                print("Bot: Could you say a bit more? I want to understand you better.")
            else:
                print("Bot: I'm not sure about that yet, but I'm always learning! 🤖")


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def main():
    print()
    separator("═")
    print("        🤖  BASIC AI LOGIC SYSTEM")
    print("     Rule-Based Decision Making in Python")
    separator("═")

    while True:
        print("""
  What would you like to do?
  ┌───────────────────────────────────────┐
  │  1 → Movie Recommender               │
  │  2 → Activity Recommender            │
  │  3 → Weather Advisor                 │
  │  4 → Simple Chatbot                  │
  │  5 → Exit                            │
  └───────────────────────────────────────┘""")

        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            movie_recommender()
        elif choice == "2":
            activity_recommender()
        elif choice == "3":
            weather_advisor()
        elif choice == "4":
            simple_chatbot()
        elif choice == "5":
            separator("═")
            print("  👋  Goodbye! Thanks for using the AI Logic System.")
            separator("═")
            break
        else:
            print("  ⚠  Invalid choice. Please enter a number between 1 and 5.")

        print()  # breathing room between modules


if __name__ == "__main__":
    main()