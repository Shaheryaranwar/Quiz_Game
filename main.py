import random

class Question:
    """Represents a single question with text, answer, and options."""
    def __init__(self, text, answer, options):
        self.text = text
        self.answer = answer
        self.options = options

    def check_answer(self, user_answer):
        """Checks if the user's answer is correct."""
        return user_answer.lower() == self.answer.lower()


class QuizBrain:
    """Manages the quiz, displays questions, and tracks the score."""
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        """Displays the next question and processes the answer."""
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            print(f"\nQ{self.question_number + 1}: {current_question.text}")
            
            # Display options
            for i, option in enumerate(current_question.options, 1):
                print(f"{i}. {option}")

            # Get user input
            try:
                user_choice = int(input("Enter the option number: ")) - 1
                if 0 <= user_choice < len(current_question.options):
                    user_answer = current_question.options[user_choice]
                    
                    # Check answer
                    if current_question.check_answer(user_answer):
                        print("✅ Correct!")
                        self.score += 1
                    else:
                        print(f"❌ Wrong! The correct answer is: {current_question.answer}")
                else:
                    print("⚠️ Invalid choice. Skipping this question.")

            except ValueError:
                print("⚠️ Please enter a valid number.")
            
            self.question_number += 1
        else:
            print("\n🎉 Quiz Completed! 🎉")
            print(f"Your final score: {self.score}/{len(self.question_list)}")
            return False
        return True


# Create Question objects with multiple choices
def create_questions():
    islamic_questions = [
    {"text": "What is the first pillar of Islam?", "answer": "Shahada", "options": ["Salah", "Shahada", "Hajj"]},
    {"text": "What is the second pillar of Islam?", "answer": "Salah", "options": ["Sawm", "Salah", "Zakat"]},
    {"text": "What is the third pillar of Islam?", "answer": "Zakat", "options": ["Hajj", "Salah", "Zakat"]},
    {"text": "What is the fourth pillar of Islam?", "answer": "Sawm", "options": ["Sawm", "Hajj", "Zakat"]},
    {"text": "What is the fifth pillar of Islam?", "answer": "Hajj", "options": ["Sawm", "Hajj", "Salah"]},
    {"text": "What is the holy book of Islam?", "answer": "Quran", "options": ["Bible", "Quran", "Torah"]},
    {"text": "Who is the last prophet of Islam?", "answer": "Prophet Muhammad (PBUH)", "options": ["Musa (AS)", "Isa (AS)", "Prophet Muhammad (PBUH)"]},
    {"text": "What is the direction Muslims face during prayer?", "answer": "Qibla", "options": ["Madinah", "Kaaba", "Qibla"]},
    {"text": "How many times a day do Muslims pray?", "answer": "Five", "options": ["Three", "Five", "Seven"]},
    {"text": "Which month do Muslims fast?", "answer": "Ramadan", "options": ["Shaban", "Ramadan", "Muharram"]},
    {"text": "What is the Arabic term for charity?", "answer": "Zakat", "options": ["Sadaqah", "Zakat", "Hajj"]},
    {"text": "What is the night when the Quran was revealed?", "answer": "Laylat al-Qadr", "options": ["Laylat al-Qadr", "Isra and Miraj", "Eid night"]},
    {"text": "How many chapters are in the Quran?", "answer": "114", "options": ["100", "114", "120"]},
    {"text": "What is the shortest Surah in the Quran?", "answer": "Surah Al-Kawthar", "options": ["Surah Al-Kausar", "Surah Al-Fatiha", "Surah Al-Ikhlas"]},
    {"text": "What is the longest Surah in the Quran?", "answer": "Surah Al-Baqarah", "options": ["Surah Al-Fatiha", "Surah Al-Baqarah", "Surah Al-Mulk"]},
    {"text": "Which angel brought revelation to the Prophet Muhammad (PBUH)?", "answer": "Angel Jibreel", "options": ["Angel Jibreel", "Angel Israfil", "Angel Mikail"]},
    {"text": "What is the Arabic term for permissible actions in Islam?", "answer": "Halal", "options": ["Haram", "Halal", "Makruh"]},
    {"text": "What is the prayer offered on Fridays called?", "answer": "Jumu'ah", "options": ["Tahajjud", "Jumu'ah", "Ishraq"]},
    {"text": "What is the name of the first mosque built in Islam?", "answer": "Masjid Quba", "options": ["Masjid al-Haram", "Masjid an-Nabawi", "Masjid Quba"]},
    {"text": "What is the holy city where the Prophet Muhammad (PBUH) was born?", "answer": "Mecca", "options": ["Medina", "Mecca", "Jerusalem"]},
    {"text": "What is the city where the Prophet Muhammad (PBUH) migrated to?", "answer": "Medina", "options": ["Mecca", "Medina", "Taif"]},
    {"text": "What is the name of the migration of the Prophet Muhammad (PBUH)?", "answer": "Hijrah", "options": ["Isra", "Hijrah", "Miraj"]},
    {"text": "What is the name of the journey Muslims take to Mecca?", "answer": "Hajj", "options": ["Umrah", "Hajj", "Ziyarah"]},
    {"text": "What is the Arabic term for struggle in the path of Allah?", "answer": "Jihad", "options": ["Jihad", "Tawakkul", "Sabr"]},
    {"text": "What is the chapter of the Quran recited in every Salah?", "answer": "Surah Al-Fatiha", "options": ["Surah Al-Fatiha", "Surah Al-Ikhlas", "Surah Al-Baqarah"]},
    {"text": "What is the term for the call to prayer?", "answer": "Adhan", "options": ["Iqamah", "Adhan", "Takbir"]},
    {"text": "What is the meal before fasting called?", "answer": "Suhoor", "options": ["Iftar", "Suhoor", "Tahajjud"]},
    {"text": "What is the meal after fasting called?", "answer": "Iftar", "options": ["Suhoor", "Iftar", "Sadaqah"]},
    {"text": "What is the celebration at the end of Ramadan?", "answer": "Eid al-Fitr", "options": ["Eid al-Adha", "Eid al-Fitr", "Mawlid"]},
    {"text": "What is the second major Islamic festival?", "answer": "Eid al-Adha", "options": ["Eid al-Adha", "Eid al-Fitr", "Ashura"]},
    {"text": "What is the term for the sayings and actions of the Prophet?", "answer": "Hadith", "options": ["Sunnah", "Hadith", "Fiqh"]},
    {"text": "What is the Arabic term for repentance?", "answer": "Tawbah", "options": ["Tawbah", "Istighfar", "Takbir"]},
    {"text": "What is the name of the sacred well near the Kaaba?", "answer": "Zamzam", "options": ["Zamzam", "Furat", "Salsabil"]},
    {"text": "Who was the first Caliph after the Prophet Muhammad (PBUH)?", "answer": "Abu Bakr Siddiq", "options": ["Ali ibn Abi Talib", "Umar ibn Al-Khattab", "Abu Bakr Siddiq"]},
    {"text": "Who was the second Caliph of Islam?", "answer": "Umar ibn Al-Khattab", "options": ["Uthman ibn Affan", "Umar ibn Al-Khattab", "Ali ibn Abi Talib"]},
    {"text": "Who was the third Caliph of Islam?", "answer": "Uthman ibn Affan", "options": ["Ali ibn Abi Talib", "Uthman ibn Affan", "Abu Bakr Siddiq"]},
    {"text": "Who was the fourth Caliph of Islam?", "answer": "Ali ibn Abi Talib", "options": ["Uthman ibn Affan", "Ali ibn Abi Talib", "Umar ibn Al-Khattab"]},
    {"text": "What is the term for the community of Muslims?", "answer": "Ummah", "options": ["Ummah", "Fiqh", "Madhhab"]},
    {"text": "What is the name of the angel of death?", "answer": "Angel Azrael", "options": ["Angel Mikail", "Angel Israfil", "Angel Azrael"]},
    {"text": "What is the Islamic term for predestination?", "answer": "Qadar", "options": ["Taqwa", "Qadar", "Tawhid"]},
    {"text": "What is the night journey of the Prophet Muhammad (PBUH)?", "answer": "Isra and Miraj", "options": ["Isra and Miraj", "Hijrah", "Laylat al-Qadr"]},
    {"text": "What is the place where souls are kept before Judgment Day?", "answer": "Barzakh", "options": ["Jannah", "Barzakh", "Jahannam"]},
    ]
    
    question_objects = []
    for q in islamic_questions:
        random.shuffle(q["options"])  # Shuffle options for randomness
        question_objects.append(Question(q["text"], q["answer"], q["options"]))
    
    return question_objects


# Run the quiz
question_bank = create_questions()
quiz = QuizBrain(question_bank)

while quiz.next_question():
    pass
