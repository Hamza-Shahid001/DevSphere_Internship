# Basic AI Logic System

A small, rule-based "AI" console application written in Python. It offers a movie recommender, an activity recommender, a weather advisor, and a keyword-based chatbot, all driven by `if`/`else` logic and lookup tables. It was built as a Week 1 exercise for the DevSphere Internship to demonstrate AI basics and core Python concepts.

## Features

| Option | Module | What it does |
|--------|--------|--------------|
| 1 | Movie Recommender | Asks for a genre and your mood, then suggests a matching movie. |
| 2 | Activity Recommender | Asks for a setting and energy level, then suggests an activity. |
| 3 | Weather Advisor | Asks for the temperature and sky conditions, then gives decision-tree advice. |
| 4 | Simple Chatbot | Matches keywords in your messages to canned replies. Type `quit`, `exit`, or `back` to return. |
| 5 | Exit | Closes the program. |

### Options per module

- **Movie Recommender**
  - Genre: `action`, `comedy`, `drama`, `horror`, `sci-fi`
  - Mood: `happy`, `sad`, `bored`
- **Activity Recommender**
  - Setting: `outdoor`, `indoor`, `creative`
  - Energy: `energetic`, `relaxed`, `social`
- **Weather Advisor**
  - Temperature: `hot`, `warm`, `cool`, `cold`
  - Sky: `sunny`, `cloudy`, `rainy`

Invalid input is rejected with a message, and the program asks again until a valid option is entered.

## How It Works

The program has three parts:

1. **Knowledge base**: two dictionaries, `MOVIES` and `ACTIVITIES`, keyed by tuples such as `("action", "happy")`. Each key maps to a recommendation string.
2. **Helper functions**: `get_valid_input()` keeps prompting until the answer is one of the allowed options, and `separator()` prints divider lines.
3. **AI modules**: `movie_recommender()`, `activity_recommender()`, `weather_advisor()`, and `simple_chatbot()`, each called from the main menu in `main()`.

The "intelligence" is entirely rule-based. There is no machine learning model and no external API calls. Recommendations come from exact lookups, the weather advice comes from nested `if`/`elif`/`else` branches, and the chatbot checks whether any known keyword appears in the input.

## Requirements

- Python 3.9 or newer (the code uses the built-in `list[str]` type hint).
- No third-party packages are needed.

## Getting Started

1. Clone or download this folder.
2. Open a terminal in the folder that contains `main.py`.
3. Run the program:

   ```bash
   python main.py
   ```

   On Windows you can also use `py main.py`.

4. Enter a menu number from 1 to 5 and follow the prompts.

### Example session

```
  What would you like to do?
  ...
  Enter your choice (1-5): 1

🎥  MOVIE RECOMMENDER
What genre do you feel like?
  Options: action | comedy | drama | horror | sci-fi
> horror

How are you feeling right now?
  Options: happy | sad | bored
> bored

  ✅  Based on your mood & taste, I recommend:
  🎬 Hereditary          — will keep you on edge.
```

## Project Structure

```
Week_1/
├── main.py      # The entire application
└── README.md    # This file
```

## Customising

- **Add a movie or activity**: add a new entry to the `MOVIES` or `ACTIVITIES` dictionary using a `(category, mood/energy)` tuple as the key. Make sure the category and mood values also appear in the lists passed to `get_valid_input()` in the matching module, or the new entry can never be reached.
- **Add chatbot replies**: add a keyword and reply to the `responses` dictionary inside `simple_chatbot()`. Keywords are matched as substrings of the lowercased input, so order matters; the first match wins.
- **Change weather advice**: edit the branches in `weather_advisor()`.

## Concepts Demonstrated

- Conditional logic (`if` / `elif` / `else`) and rule-based decision making
- Dictionaries and tuple keys for lookups
- Input validation with loops
- Functions and docstrings
- Basic string formatting and console output
- The `if __name__ == "__main__":` entry-point pattern

## Limitations

- Recommendations are limited to the entries hard-coded in `main.py`.
- The chatbot only recognises exact keywords. It does not understand context or grammar.
- The weather advice is generic. Its one location-specific message (hot rain) refers to Karachi.
- There are no automated tests.

## Author

DevSphere Internship, Week 1.
