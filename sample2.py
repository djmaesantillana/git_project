# By Dr. Fuentes 2020
import nltk
from nltk.chat.util import Chat, reflections
print(Chat)

reflections = {"i am":'you are',
"i was": 'you were', 
"i":'you',
"i'm":'you are',
"i'd":'you would',
"i've": 'you have',
"i'll": 'you will',
"my": 'your',
"you are": 'I am',
"you were": 'I was',
"you've": 'I have',
"you'll": 'I will',
"your's": 'my',
"yours": 'mine',
"you": 'me',
"me": 'you'}

set_pairs = [
    [
        r"my name is(.*)",
        ["Hello %1, How are you doing today?",]
    ],
    [
        r"hi|hey|hello"
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["You can call me a Dr. F ChatBot?",]
    ],
    [
        r"How are you?",
        ["I am fine, thank you! How can I help you?",]
    ],
    [
        r"sana all",
        ["great to hear that, how can I help you?",]
    ],
    [
        r"How can I help you?",
        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can check their website",]
    ],
    [
        r"thanks for suggestion. Do they have great authors and instructors?",
        ["Yes, they have the world class best authors, that is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["I am happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. See you soon:)"]
    ],
]

def chatbot(): print("Hi, I'm the chatbot!! you can try me!!")

chatbot()
print("chatter")
chat = Chat(set_pairs, reflections)
print(chat)
chat.converse()
if__name__=="__main__":
    chatbot()