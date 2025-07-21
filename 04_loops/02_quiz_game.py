"""
Interactive Quiz Game
A practical program creating a quiz game with multiple categories and difficulty levels.
Demonstrates: For loops, while loops, nested loops, break/continue, range() function
"""

import random

def main():
    print("=" * 60)
    print("              INTERACTIVE QUIZ GAME")
    print("=" * 60)
    
    # Player information
    player_name = input("Enter your name: ")
    print(f"\n🎯 Welcome to the Quiz Game, {player_name}!")
    print("Test your knowledge across different categories!")
    
    # Quiz categories with questions
    quiz_categories = {
        "Science": {
            "easy": [
                {"question": "What planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": 0},
                {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": 2},
                {"question": "How many bones are in the adult human body?", "options": ["206", "208", "210", "215"], "answer": 0},
                {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "NaCl", "O2"], "answer": 0},
                {"question": "Which organ pumps blood through the human body?", "options": ["Brain", "Heart", "Lungs", "Liver"], "answer": 1}
            ],
            "medium": [
                {"question": "What is the speed of light in vacuum?", "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "200,000 km/s"], "answer": 0},
                {"question": "Which element has the atomic number 1?", "options": ["Helium", "Hydrogen", "Lithium", "Carbon"], "answer": 1},
                {"question": "What type of animal is a Komodo dragon?", "options": ["Snake", "Crocodile", "Lizard", "Turtle"], "answer": 2},
                {"question": "How many chambers does a human heart have?", "options": ["2", "3", "4", "5"], "answer": 2},
                {"question": "What is the hardest natural substance?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "answer": 2}
            ],
            "hard": [
                {"question": "What is the name of the theoretical boundary around a black hole?", "options": ["Event Horizon", "Photon Sphere", "Ergosphere", "Singularity"], "answer": 0},
                {"question": "Which scientist developed the theory of relativity?", "options": ["Newton", "Einstein", "Hawking", "Bohr"], "answer": 1},
                {"question": "What is the most abundant gas in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"], "answer": 2}
            ]
        },
        "History": {
            "easy": [
                {"question": "In which year did World War II end?", "options": ["1944", "1945", "1946", "1947"], "answer": 1},
                {"question": "Who was the first President of the United States?", "options": ["Thomas Jefferson", "George Washington", "John Adams", "Benjamin Franklin"], "answer": 1},
                {"question": "Which country gifted the Statue of Liberty to the USA?", "options": ["Britain", "Spain", "France", "Italy"], "answer": 2},
                {"question": "In which city was President Kennedy assassinated?", "options": ["Dallas", "Miami", "New York", "Washington"], "answer": 0},
                {"question": "What year did the Berlin Wall fall?", "options": ["1987", "1988", "1989", "1990"], "answer": 2}
            ],
            "medium": [
                {"question": "Who was known as the Iron Lady?", "options": ["Margaret Thatcher", "Queen Elizabeth", "Indira Gandhi", "Golda Meir"], "answer": 0},
                {"question": "Which empire was ruled by Julius Caesar?", "options": ["Greek", "Roman", "Byzantine", "Ottoman"], "answer": 1},
                {"question": "The Magna Carta was signed in which year?", "options": ["1215", "1225", "1235", "1245"], "answer": 0},
                {"question": "Who painted the ceiling of the Sistine Chapel?", "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"], "answer": 1}
            ],
            "hard": [
                {"question": "The Treaty of Westphalia ended which war?", "options": ["Thirty Years War", "Hundred Years War", "Seven Years War", "War of Spanish Succession"], "answer": 0},
                {"question": "Which dynasty ruled China for the longest period?", "options": ["Ming", "Qing", "Zhou", "Han"], "answer": 2}
            ]
        },
        "Geography": {
            "easy": [
                {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "answer": 2},
                {"question": "Which is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": 3},
                {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": 2},
                {"question": "Which country has the most natural lakes?", "options": ["Canada", "Russia", "USA", "Finland"], "answer": 0},
                {"question": "What is the longest river in the world?", "options": ["Amazon", "Nile", "Mississippi", "Yangtze"], "answer": 1}
            ],
            "medium": [
                {"question": "Which country has the most time zones?", "options": ["Russia", "USA", "China", "France"], "answer": 3},
                {"question": "What is the smallest country in the world?", "options": ["Monaco", "Nauru", "Vatican City", "San Marino"], "answer": 2},
                {"question": "Which mountain range contains Mount Everest?", "options": ["Alps", "Andes", "Himalayas", "Rockies"], "answer": 2},
                {"question": "What is the deepest point in Earth's oceans?", "options": ["Mariana Trench", "Puerto Rico Trench", "Japan Trench", "Peru-Chile Trench"], "answer": 0}
            ],
            "hard": [
                {"question": "Which country is completely landlocked by South Africa?", "options": ["Lesotho", "Swaziland", "Botswana", "Zimbabwe"], "answer": 0},
                {"question": "What is the capital of Bhutan?", "options": ["Thimphu", "Paro", "Punakha", "Jakar"], "answer": 0}
            ]
        },
        "Sports": {
            "easy": [
                {"question": "How many players are on a basketball team on court?", "options": ["4", "5", "6", "7"], "answer": 1},
                {"question": "In which sport would you perform a slam dunk?", "options": ["Football", "Basketball", "Tennis", "Volleyball"], "answer": 1},
                {"question": "How often are the Summer Olympics held?", "options": ["Every 2 years", "Every 3 years", "Every 4 years", "Every 5 years"], "answer": 2},
                {"question": "What does FIFA stand for?", "options": ["International Football Association", "Federation of International Football", "Fédération Internationale de Football Association", "Football International Federation Association"], "answer": 2}
            ],
            "medium": [
                {"question": "Which country won the 2018 FIFA World Cup?", "options": ["Brazil", "Germany", "France", "Argentina"], "answer": 2},
                {"question": "In tennis, what score comes after deuce?", "options": ["Game", "Advantage", "40-Love", "Set"], "answer": 1},
                {"question": "How many holes are played in a standard round of golf?", "options": ["16", "18", "20", "22"], "answer": 1}
            ],
            "hard": [
                {"question": "Which swimmer has won the most Olympic gold medals?", "options": ["Mark Spitz", "Michael Phelps", "Ryan Lochte", "Caeleb Dressel"], "answer": 1},
                {"question": "In cricket, what is the maximum number of overs in a Test match innings?", "options": ["Unlimited", "100", "150", "200"], "answer": 0}
            ]
        }
    }
    
    # Player statistics
    total_score = 0
    total_questions = 0
    category_scores = {}
    game_history = []
    
    # Main game loop
    while True:
        print("\n" + "=" * 60)
        print("                QUIZ GAME MENU")
        print("=" * 60)
        print("1. Play Quiz")
        print("2. View Statistics")
        print("3. Practice Mode")
        print("4. Challenge Mode")
        print("5. Leaderboard")
        print("6. Exit")
        print("-" * 60)
        
        choice = input("Select an option (1-6): ")
        
        if choice == "1":
            # Play Quiz
            print("\n📚 QUIZ CATEGORIES")
            print("-" * 30)
            
            categories = list(quiz_categories.keys())
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            
            # Category selection loop
            while True:
                try:
                    cat_choice = int(input(f"Choose category (1-{len(categories)}): ")) - 1
                    if 0 <= cat_choice < len(categories):
                        selected_category = categories[cat_choice]
                        break
                    else:
                        print(f"Please choose between 1-{len(categories)}")
                except ValueError:
                    print("Please enter a valid number!")
            
            # Difficulty selection
            print(f"\n🎚️ DIFFICULTY LEVELS for {selected_category}")
            print("-" * 40)
            print("1. Easy (5 questions)")
            print("2. Medium (4 questions)")
            print("3. Hard (2-3 questions)")
            print("4. Mixed (Random from all levels)")
            
            while True:
                try:
                    diff_choice = int(input("Choose difficulty (1-4): "))
                    if 1 <= diff_choice <= 4:
                        break
                    else:
                        print("Please choose between 1-4")
                except ValueError:
                    print("Please enter a valid number!")
            
            # Prepare questions based on difficulty
            if diff_choice == 1:
                questions = quiz_categories[selected_category]["easy"]
                difficulty = "Easy"
            elif diff_choice == 2:
                questions = quiz_categories[selected_category]["medium"]
                difficulty = "Medium"
            elif diff_choice == 3:
                questions = quiz_categories[selected_category]["hard"]
                difficulty = "Hard"
            else:  # Mixed mode
                all_questions = []
                for level in quiz_categories[selected_category].values():
                    all_questions.extend(level)
                questions = random.sample(all_questions, min(8, len(all_questions)))
                difficulty = "Mixed"
            
            # Start the quiz
            print(f"\n🚀 Starting {selected_category} Quiz - {difficulty} Level")
            print(f"Number of questions: {len(questions)}")
            print("=" * 50)
            
            correct_answers = 0
            quiz_questions = questions.copy()
            
            # Question loop
            for i, question_data in enumerate(quiz_questions, 1):
                print(f"\nQuestion {i}/{len(quiz_questions)}")
                print("-" * 30)
                print(f"❓ {question_data['question']}")
                
                # Display options
                for j, option in enumerate(question_data['options']):
                    print(f"{j + 1}. {option}")
                
                # Get user answer with validation
                while True:
                    try:
                        user_answer = int(input(f"Your answer (1-{len(question_data['options'])}): ")) - 1
                        if 0 <= user_answer < len(question_data['options']):
                            break
                        else:
                            print(f"Please choose between 1-{len(question_data['options'])}")
                    except ValueError:
                        print("Please enter a valid number!")
                
                # Check answer
                if user_answer == question_data['answer']:
                    print("✅ Correct!")
                    correct_answers += 1
                else:
                    correct_option = question_data['options'][question_data['answer']]
                    print(f"❌ Wrong! The correct answer is: {correct_option}")
                
                # Show current score
                print(f"Score: {correct_answers}/{i}")
            
            # Quiz completed
            quiz_score = (correct_answers / len(quiz_questions)) * 100
            total_score += correct_answers
            total_questions += len(quiz_questions)
            
            # Update category scores
            if selected_category not in category_scores:
                category_scores[selected_category] = {"correct": 0, "total": 0}
            category_scores[selected_category]["correct"] += correct_answers
            category_scores[selected_category]["total"] += len(quiz_questions)
            
            # Store game history
            game_result = {
                "category": selected_category,
                "difficulty": difficulty,
                "score": correct_answers,
                "total": len(quiz_questions),
                "percentage": quiz_score
            }
            game_history.append(game_result)
            
            # Display results
            print("\n" + "🎉" * 20)
            print("           QUIZ COMPLETED!")
            print("🎉" * 20)
            print(f"Category: {selected_category}")
            print(f"Difficulty: {difficulty}")
            print(f"Score: {correct_answers}/{len(quiz_questions)}")
            print(f"Percentage: {quiz_score:.1f}%")
            
            # Performance evaluation
            if quiz_score >= 90:
                print("🏆 Outstanding! You're a genius!")
            elif quiz_score >= 80:
                print("🥇 Excellent work!")
            elif quiz_score >= 70:
                print("🥈 Good job!")
            elif quiz_score >= 60:
                print("🥉 Not bad, keep practicing!")
            else:
                print("📚 Keep studying and try again!")
        
        elif choice == "2":
            # View Statistics
            if total_questions == 0:
                print("\n📊 No games played yet!")
                continue
            
            print("\n📊 YOUR QUIZ STATISTICS")
            print("=" * 50)
            
            overall_percentage = (total_score / total_questions) * 100
            print(f"Overall Performance:")
            print(f"Total Questions Answered: {total_questions}")
            print(f"Total Correct Answers: {total_score}")
            print(f"Overall Accuracy: {overall_percentage:.1f}%")
            
            # Category-wise performance
            print(f"\n📚 Category-wise Performance:")
            print("-" * 40)
            for category, scores in category_scores.items():
                cat_percentage = (scores["correct"] / scores["total"]) * 100
                print(f"{category}: {scores['correct']}/{scores['total']} ({cat_percentage:.1f}%)")
            
            # Recent game history
            if game_history:
                print(f"\n🕐 Recent Games:")
                print("-" * 40)
                recent_games = game_history[-5:]  # Last 5 games
                for i, game in enumerate(recent_games, 1):
                    print(f"{i}. {game['category']} ({game['difficulty']}) - {game['score']}/{game['total']} ({game['percentage']:.1f}%)")
        
        elif choice == "3":
            # Practice Mode
            print("\n💪 PRACTICE MODE")
            print("-" * 25)
            print("Practice specific topics with unlimited attempts!")
            
            # Category selection for practice
            categories = list(quiz_categories.keys())
            print("\nSelect category to practice:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            
            try:
                cat_choice = int(input(f"Choose category (1-{len(categories)}): ")) - 1
                if 0 <= cat_choice < len(categories):
                    practice_category = categories[cat_choice]
                else:
                    print("Invalid choice!")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            # Collect all questions from the category
            practice_questions = []
            for level_questions in quiz_categories[practice_category].values():
                practice_questions.extend(level_questions)
            
            print(f"\n📖 Practicing {practice_category}")
            print(f"Available questions: {len(practice_questions)}")
            
            # Practice session loop
            practice_score = 0
            practice_count = 0
            
            while True:
                # Random question selection
                if not practice_questions:
                    print("No more questions available!")
                    break
                
                current_question = random.choice(practice_questions)
                practice_count += 1
                
                print(f"\nPractice Question {practice_count}")
                print("-" * 30)
                print(f"❓ {current_question['question']}")
                
                for j, option in enumerate(current_question['options']):
                    print(f"{j + 1}. {option}")
                
                try:
                    user_answer = int(input(f"Your answer (1-{len(current_question['options'])}): ")) - 1
                    
                    if user_answer == current_question['answer']:
                        print("✅ Correct! Well done!")
                        practice_score += 1
                    else:
                        correct_option = current_question['options'][current_question['answer']]
                        print(f"❌ Wrong! The correct answer is: {correct_option}")
                    
                    print(f"Practice Score: {practice_score}/{practice_count}")
                    
                    continue_practice = input("\nContinue practicing? (y/n): ").lower()
                    if continue_practice != 'y':
                        break
                        
                except ValueError:
                    print("Invalid input! Please enter a number.")
                except (KeyboardInterrupt, EOFError):
                    break
            
            if practice_count > 0:
                practice_percentage = (practice_score / practice_count) * 100
                print(f"\n📊 Practice Session Complete!")
                print(f"Questions Attempted: {practice_count}")
                print(f"Correct Answers: {practice_score}")
                print(f"Accuracy: {practice_percentage:.1f}%")
        
        elif choice == "4":
            # Challenge Mode
            print("\n🏆 CHALLENGE MODE")
            print("-" * 25)
            print("Take on special challenges!")
            
            challenges = {
                1: {"name": "Speed Challenge", "desc": "Answer 10 questions in 2 minutes", "time_limit": 120},
                2: {"name": "Perfect Score", "desc": "Get 100% in any category", "target": 100},
                3: {"name": "Knowledge Master", "desc": "Score 80%+ in all categories", "target": 80},
                4: {"name": "Marathon", "desc": "Answer 25 questions consecutively", "count": 25}
            }
            
            print("\nAvailable Challenges:")
            for key, challenge in challenges.items():
                print(f"{key}. {challenge['name']} - {challenge['desc']}")
            
            try:
                challenge_choice = int(input("Select challenge (1-4): "))
                if challenge_choice not in challenges:
                    print("Invalid choice!")
                    continue
                    
                selected_challenge = challenges[challenge_choice]
                print(f"\n🎯 Challenge: {selected_challenge['name']}")
                print(f"Description: {selected_challenge['desc']}")
                
                if challenge_choice == 1:  # Speed Challenge
                    # Implementation for speed challenge
                    print("⏱️ You have 2 minutes to answer 10 questions!")
                    input("Press Enter when ready to start...")
                    
                    # This would need actual timer implementation
                    print("⚠️ Timer-based challenges require advanced implementation")
                    print("This is a basic version - try to answer quickly!")
                    
                elif challenge_choice == 3:  # Knowledge Master
                    print("\n📊 Knowledge Master Challenge Progress:")
                    if not category_scores:
                        print("❌ No quiz data available. Play some quizzes first!")
                        continue
                    
                    master_status = True
                    for category, scores in category_scores.items():
                        percentage = (scores["correct"] / scores["total"]) * 100
                        status = "✅" if percentage >= 80 else "❌"
                        print(f"{status} {category}: {percentage:.1f}%")
                        if percentage < 80:
                            master_status = False
                    
                    if master_status:
                        print("🏆 CHALLENGE COMPLETED! You are a Knowledge Master!")
                    else:
                        print("Keep practicing to achieve 80%+ in all categories!")
                
                else:
                    print("🚧 This challenge is under development!")
                    
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "5":
            # Leaderboard (simulated)
            print("\n🏆 LEADERBOARD")
            print("-" * 30)
            
            if total_questions == 0:
                print("Play some quizzes to see your ranking!")
                continue
            
            # Simulated leaderboard data
            leaderboard = [
                {"name": "QuizMaster", "score": 95.2},
                {"name": "BrainBox", "score": 92.8},
                {"name": "SmartCookie", "score": 89.5},
                {"name": player_name, "score": (total_score / total_questions) * 100},
                {"name": "StudyBuddy", "score": 85.1},
                {"name": "Bookworm", "score": 82.3}
            ]
            
            # Sort by score
            leaderboard.sort(key=lambda x: x["score"], reverse=True)
            
            print("Rank | Player        | Score")
            print("-" * 30)
            for i, player in enumerate(leaderboard, 1):
                if player["name"] == player_name:
                    print(f"{i:>4} | {player['name']:<12} | {player['score']:>5.1f}% ⭐")
                else:
                    print(f"{i:>4} | {player['name']:<12} | {player['score']:>5.1f}%")
        
        elif choice == "6":
            # Exit
            print(f"\n🎓 QUIZ GAME SUMMARY")
            print("=" * 40)
            print(f"Thanks for playing, {player_name}!")
            
            if total_questions > 0:
                final_percentage = (total_score / total_questions) * 100
                print(f"Final Statistics:")
                print(f"Questions Answered: {total_questions}")
                print(f"Correct Answers: {total_score}")
                print(f"Overall Accuracy: {final_percentage:.1f}%")
                print(f"Games Played: {len(game_history)}")
                
                # Best performance
                if game_history:
                    best_game = max(game_history, key=lambda x: x["percentage"])
                    print(f"Best Performance: {best_game['percentage']:.1f}% in {best_game['category']}")
            
            print("\nKeep learning and come back for more challenges! 🚀")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main() 