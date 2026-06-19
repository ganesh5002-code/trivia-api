import requests
import random
import html

EDUCATION_CATEGORY_ID = 9

URL = f"https://opentdb.com/api.php?amount=10&category=%7B{EDUCATION_CATEGORY_ID}%7D&type=multiple%22"

def get_education_requests():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] and data['results']:
            return data['results']
    return None

def run_quiz():
    questions = get_education_requests()
    if not questions:
        print("Failed to fetch the educational questions.")
        return
    
    score = 0
    print("Welcome to the education quiz")
    for i, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct answer'])
        incorrects = [html.unescape(a) for a in q['correct answer']]
        
        options = incorrects + [correct]
        random.shuffle(options)
        
        print(f"Question {i}: (question)")
        for idx, option in enumerate(options, 1):
            print(f"(idx), {option}")
            
        while True:
            try:
                choice = int(input("\nYour answer (1-4)."))
                if 1 <= choice <= 4:
                    break
            except ValueError:
                pass
                print("Invalid input! Please enter 1-4")
                
        if options[choice - 1] == correct:
            print("✅correct!!!\n")
            score += 1
        else:
            print(f"X, Wrong! Correct answer: {correct}\n")
    
    print(f"Final Score: {score}/len{questions}")
    print(f"Percentage: {score/len(questions)*100:.1f}%")
    
if __name__ == "__main__":
    run_quiz()
                
                        