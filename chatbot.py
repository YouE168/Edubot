import re
import random

class SchoolChatbot:
    def __init__(self):
        self.name = "EduBot"
        self.responses = {
            # Greetings
            'greeting': [
                "Hello! I'm EduBot, your school helpdesk assistant. How can I help you today?",
                "Hi there! Welcome to the school helpdesk. What can I assist you with?",
                "Greetings! I'm here to help with your school-related questions."
            ],
            
            # Schedule/Classes
            'schedule': [
                "For class schedules, please check your student portal or contact the registrar's office at ext. 1234.",
                "You can find your class schedule in the student portal. If you need help accessing it, contact IT support.",
                "Class schedules are available online. Would you like me to help you with anything else?"
            ],
            
            # Library
            'library': [
                "The library is open Monday-Friday 8AM-8PM, weekends 10AM-6PM.",
                "You can access library resources online 24/7. For physical books, visit during operating hours.",
            ],
            
            # Cafeteria/Food
            'food': [
                "Today's cafeteria menu is available on the school website under 'Student Life'.",
                "The cafeteria serves breakfast 7-9AM and lunch 11AM-2PM.",
                "For dietary restrictions or special meals, contact food services at ext. 5678."
            ],
            
            # IT Support
            'tech': [
                "For technical issues, contact IT support at ithelp@school.edu or ext. 9999.",
                "Having trouble with WiFi? Try reconnecting or contact IT support for assistance.",
                "IT support offers walk-in help at the tech center, room 101, weekdays 9AM-5PM."
            ],
            
            # Financial Aid
            'financial': [
                "For financial aid questions, visit the financial aid office or call ext. 3456.",
                "Financial aid applications are due by February 1st for the following academic year.",
                "Need help with FAFSA? The financial aid office offers workshops every Friday."
            ],
            
            # Default responses
            'default': [
                "I'm sorry, I don't understand that question. Can you try rephrasing it?",
                "I'm not sure about that. Would you like me to connect you with a human advisor?",
                "That's outside my knowledge. Please contact the main office at ext. 1000 for assistance."
            ],
            
            # Goodbye
            'goodbye': [
                "Goodbye! Have a great day at school!",
                "Thanks for using the school helpdesk. See you later!",
                "Take care! Don't hesitate to ask if you need more help."
            ]
        }
        
        # Keywords for pattern matching
        self.patterns = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'greetings'],
            'schedule': ['schedule', 'class', 'classes', 'timetable', 'time'],
            'library': ['library', 'books', 'study', 'reading'],
            'food': ['food', 'cafeteria', 'lunch', 'breakfast', 'eat', 'menu', 'dining'],
            'tech': ['computer', 'wifi', 'internet', 'password', 'login', 'technical', 'it'],
            'financial': ['financial aid', 'money', 'tuition', 'scholarship', 'fafsa', 'payment'],
            'goodbye': ['bye', 'goodbye', 'see you', 'thanks', 'thank you', 'exit', 'quit']
        }
    
    def get_response_type(self, user_input):
        """Determine the type of response needed based on user input"""
        user_input = user_input.lower()
        
        # Check each pattern category
        for response_type, keywords in self.patterns.items():
            for keyword in keywords:
                if keyword in user_input:
                    return response_type
        
        # If no pattern matches, return default
        return 'default'
    
    def get_response(self, user_input):
        """Get a response based on user input"""
        response_type = self.get_response_type(user_input)
        return random.choice(self.responses[response_type])
    
    def chat(self):
        """Main chat loop"""
        print(f"🤖 {self.get_response('hello')}")
        print("(Type 'quit' or 'exit' to end the conversation)")
        print("-" * 50)
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                print("🤖 Please type something!")
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"🤖 {self.get_response('goodbye')}")
                break
            
            response = self.get_response(user_input)
            print(f"🤖 {response}")
            print()

# Run the chatbot
if __name__ == "__main__":
    bot = SchoolChatbot()
    bot.chat()