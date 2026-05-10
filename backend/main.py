from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS fix (frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str




@app.post("/generate")
def generate_quiz(data: TextInput):
    text = data.text.lower()

    # 1
    if "water boils" in text:
        return {"question": "At what temperature does water boil?", "answer": "100 degree"}

    # 2
    elif "capital of bangladesh" in text:
        return {"question": "What is the capital of Bangladesh?", "answer": "Dhaka"}

    # 3
    elif "sun rises" in text:
        return {"question": "Where does the sun rise?", "answer": "East"}

    # 4
    elif "photosynthesis" in text:
        return {"question": "Where does photosynthesis occur?", "answer": "In plants"}

    # 5
    elif "triangle" in text:
        return {"question": "How many sides does a triangle have?", "answer": "Three"}

    # 6
    elif "square" in text:
        return {"question": "How many sides does a square have?", "answer": "Four"}

    # 7
    elif "earth revolves" in text:
        return {"question": "What does the Earth revolve around?", "answer": "The Sun"}

    # 8
    elif "moon" in text:
        return {"question": "What does the Moon revolve around?", "answer": "Earth"}

    # 9
    elif "oxygen" in text:
        return {"question": "Which gas do humans need to survive?", "answer": "Oxygen"}

    # 10
    elif "plants" in text:
        return {"question": "What do plants produce?", "answer": "Oxygen"}

    # 11
    elif "bangladesh independence" in text:
        return {"question": "When did Bangladesh become independent?", "answer": "1971"}

    # 12
    elif "river padma" in text:
        return {"question": "What is Padma?", "answer": "A river"}

    # 13
    elif "capital of india" in text:
        return {"question": "What is the capital of India?", "answer": "New Delhi"}

    # 14
    elif "largest ocean" in text:
        return {"question": "Which is the largest ocean?", "answer": "Pacific Ocean"}

    # 15
    elif "largest continent" in text:
        return {"question": "Which is the largest continent?", "answer": "Asia"}

    # 16
    elif "human heart" in text:
        return {"question": "What does the heart do?", "answer": "Pumps blood"}

    # 17
    elif "blood" in text:
        return {"question": "What carries oxygen in the body?", "answer": "Blood"}

    # 18
    elif "computer" in text:
        return {"question": "What is a computer used for?", "answer": "Processing data"}

    # 19
    elif "keyboard" in text:
        return {"question": "What is a keyboard used for?", "answer": "Typing input"}

    # 20
    elif "mouse" in text:
        return {"question": "What is a mouse used for?", "answer": "Controlling cursor"}

    # 21
    elif "python" in text:
        return {"question": "What is Python?", "answer": "A programming language"}

    # 22
    elif "internet" in text:
        return {"question": "What is the Internet?", "answer": "A global network"}

    # 23
    elif "school" in text:
        return {"question": "Where do students study?", "answer": "School"}

    # 24
    elif "teacher" in text:
        return {"question": "Who teaches students?", "answer": "Teacher"}

    # 25
    elif "doctor" in text:
        return {"question": "Who treats patients?", "answer": "Doctor"}

    # 26
    elif "hospital" in text:
        return {"question": "Where do sick people go?", "answer": "Hospital"}

    # 27
    elif "car" in text:
        return {"question": "What is a car used for?", "answer": "Transport"}

    # 28
    elif "train" in text:
        return {"question": "What is a train used for?", "answer": "Transport"}

    # 29
    elif "rain" in text:
        return {"question": "What falls from clouds?", "answer": "Rain"}

    # 30
    elif "air" in text:
        return {"question": "What do we breathe?", "answer": "Air"}

    else:
        return {
            "question": "What is the main idea of the text?",
            "answer": "Not defined"
        }

