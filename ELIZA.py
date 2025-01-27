import re
import random

def question3_eliza():
    print("\n--- Question 3: ELIZA-Like Chatbot ---")

    # Fallback responses to add variety when no rule matches
    fallbacks = [
        "Could you elaborate on that?",
        "Please, go on.",
        "I see. Tell me more about that.",
    ]

    # Rules: a list of regex–response pairs
    rules = [
        (re.compile(r"\bI need help with\b\s*(.*)", re.IGNORECASE),       # "I need help with _____"
         "What part about {0} do you need help?"),
        
        (re.compile(r"(?:Academic\s*)", re.IGNORECASE),       # "Academic"
         "I am sorry to hear that, which subject do you need help?"),
        
        (re.compile(r"\bI\s*(?:am\s*)?feeling\b\s*(.*)", re.IGNORECASE),  # "I am feeling ___"
         "Why do you think you're feeling{0}?"),

        (re.compile(r"\bI\s*feel\s+(.*)", re.IGNORECASE),                 # "I feel ___"
         "Why do you feel {0}?"),

        (re.compile(r"\bI\s*want\s+(.*)", re.IGNORECASE),                # "I want ___"
         "What would having {0} mean to you?"),

        (re.compile(r"\bmy name is (.*)", re.IGNORECASE),                # "My name is ___"
         "Hello {0}, lovely to meet you. How are you feeling today?"),

        (re.compile(r"\byou are (.*)", re.IGNORECASE),                   # "You are ___"
         "Why do you think I am {0}?"),

        (re.compile(r"\bI'?m not sure about (.*)", re.IGNORECASE),       # "I'm not sure about ___"
         "What makes you uncertain about {0}?"),

        (re.compile(r"\bI can'?t (.*)", re.IGNORECASE),                  # "I can't ___"
         "What do you suppose might happen if you could {0}?"),

        (re.compile(r"\bI cannot (.*)", re.IGNORECASE),                  # "I cannot ___"
         "What leads you to believe you cannot {0}?"),

        (re.compile(r"\bI wonder (.*)", re.IGNORECASE),                  # "I wonder ___"
         "That's quite interesting. Have you tried to explore {0} further?"),

        (re.compile(r"\bI remember (.*)", re.IGNORECASE),                # "I remember ___"
         "What significance does {0} hold for you?"),

        (re.compile(r"\bI used to (.*)", re.IGNORECASE),                 # "I used to ___"
         "How do you feel now, looking back on {0}?"),

        (re.compile(r"\bI wish (.*)", re.IGNORECASE),                    # "I wish ___"
         "Why do you wish {0}?"),

        (re.compile(r"\bI love (.*)", re.IGNORECASE),                    # "I love ___"
         "What makes you love {0} so much?"),

        (re.compile(r"\bI hate (.*)", re.IGNORECASE),                    # "I hate ___"
         "Why does {0} bother you so greatly?"),

        (re.compile(r"\bIt hurts when (.*)", re.IGNORECASE),             # "It hurts when ___"
         "Have you discussed how it hurts when {0} with anyone else?"),

        (re.compile(r"\bI dream about (.*)", re.IGNORECASE),             # "I dream about ___"
         "What do you think your dream about {0} might mean?"),

        (re.compile(r"\bMy (father|mother) is (.*)", re.IGNORECASE),     # "My father/mother is ___"
         "How do you feel about your {0} being {1}?"),

        (re.compile(r"\bPeople (.*)", re.IGNORECASE),                    # "People ___"
         "What do you think causes people to {0}?"),

        (re.compile(r"\bNobody (.*)", re.IGNORECASE),                    # "Nobody ___"
         "How does it make you feel that nobody {0}?"),

        (re.compile(r"\bI often think about (.*)", re.IGNORECASE),       # "I often think about ___"
         "What sorts of thoughts do you have about {0}?"),

        (re.compile(r"\bI don'?t know (.*)", re.IGNORECASE),             # "I don't know ___"
         "What do you think might happen if you did know {0}?"),

        (re.compile(r"\bI feel (guilty|ashamed) about (.*)", re.IGNORECASE),  # "I feel guilty/ashamed about ___"
         "Why do you suppose you feel {0} about {1}?"),

        (re.compile(r"\bI can'?t decide whether (.*)", re.IGNORECASE),   # "I can't decide whether ___"
         "What might help you make a decision about {0}?"),

        (re.compile(r"\bI'?m confused about (.*)", re.IGNORECASE),       # "I'm confused about ___"
         "What do you think is the main source of your confusion about {0}?"),
    ]

    # Pronoun reflection function
    def reflect_pronouns(text):
        reflections = {
            r"\byou\b": "I",
            r"\byour\b": "my",
            r"\bare\b": "am",
            r"\bmy\b": "your",
            r"\bme\b": "you",
            r"\bI\b": "you",
            r"\bI'm\b": "you're",
        }
        for pattern, replacement in reflections.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        return text

    # Main response function
    def eliza_respond(user_input):
        user_input = user_input.strip()
        for pattern, response_template in rules:
            match = pattern.search(user_input)
            if match:
                groups = match.groups()  # Capture all groups
                reflected_groups = [reflect_pronouns(g) for g in groups]  # Reflect pronouns in each group
                return response_template.format(*reflected_groups)
        return random.choice(fallbacks)

    # Demonstration
    sample_inputs = [
        "I am feeling nervous",
        "I feel sad about my exams",
        "I want a new house",
        "My name is Cassiopeia",
        "You are ignoring me",
        "I'm not sure about the future",
        "I feel guilty about everything",
        "I can't decide whether to stay or leave",
    ]

    print("\nDemonstration of ELIZA-like responses:\n")
    for sample in sample_inputs:
        print(f"User: {sample}")
        print(f"Bot:  {eliza_respond(sample)}\n")

    # Interactive loop
    print(f"  Type 'quit' or 'exit' to leave. \n Bot: Welcome to UOB helpline, how may I help you\n")
    while True:
        user_input = input(">> ")
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!\n")
            break
        print(f"User: {user_input}")
        print(f"Bot:  {eliza_respond(user_input)}\n")

    print("--- End Question 3 ---\n")

# -------------------------------------------------------------------------
# Main section to demonstrate each function in turn.
# -------------------------------------------------------------------------

if __name__ == "__main__":
    question3_eliza()