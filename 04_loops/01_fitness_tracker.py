"""
Fitness Tracker Application
A practical program for tracking daily fitness activities using loops.
Demonstrates: While loops, for loops, nested loops, break/continue statements
"""

def main():
    print("=" * 60)
    print("              FITNESS TRACKER APP")
    print("=" * 60)
    
    # User profile setup
    user_name = input("Enter your name: ")
    print(f"\n👋 Welcome to Fitness Tracker, {user_name}!")
    
    # Get user goals
    try:
        daily_steps_goal = int(input("Enter your daily steps goal: "))
        weekly_workout_goal = int(input("Enter your weekly workout goal (minutes): "))
        daily_calorie_goal = int(input("Enter your daily calorie burn goal: "))
    except ValueError:
        print("Please enter valid numbers for goals!")
        return
    
    # Initialize tracking variables
    total_steps = 0
    total_calories = 0
    total_workout_time = 0
    day_count = 0
    weekly_data = []
    
    print(f"\n🎯 Goals Set:")
    print(f"   Daily Steps: {daily_steps_goal:,}")
    print(f"   Weekly Workout: {weekly_workout_goal} minutes")
    print(f"   Daily Calories: {daily_calorie_goal}")
    
    # Main tracking loop
    while True:
        print("\n" + "=" * 60)
        print("              FITNESS TRACKER MENU")
        print("=" * 60)
        print("1. Log Daily Activity")
        print("2. Log Workout Session")
        print("3. View Daily Summary")
        print("4. View Weekly Progress")
        print("5. Challenge Mode")
        print("6. Set New Goals")
        print("7. Exit")
        print("-" * 60)
        
        choice = input("Select an option (1-7): ")
        
        if choice == "1":
            # Log Daily Activity
            print("\n📱 DAILY ACTIVITY LOGGING")
            print("-" * 40)
            
            day_count += 1
            daily_steps = 0
            daily_calories = 0
            
            # Input validation loop
            while True:
                try:
                    steps = int(input("Enter steps taken today: "))
                    if steps >= 0:
                        daily_steps = steps
                        break
                    else:
                        print("Steps cannot be negative!")
                except ValueError:
                    print("Please enter a valid number!")
            
            # Calculate calories from steps (approximate)
            calories_from_steps = daily_steps * 0.04  # ~0.04 calories per step
            daily_calories += calories_from_steps
            
            # Add to totals
            total_steps += daily_steps
            total_calories += daily_calories
            
            # Daily activity breakdown
            activities = {
                "Walking": {"met": 3.5, "icon": "🚶"},
                "Running": {"met": 8.0, "icon": "🏃"},
                "Cycling": {"met": 6.0, "icon": "🚴"},
                "Swimming": {"met": 7.0, "icon": "🏊"},
                "Yoga": {"met": 2.5, "icon": "🧘"},
                "Dancing": {"met": 5.0, "icon": "💃"}
            }
            
            print(f"\nOptional: Log specific activities (enter 0 to skip)")
            daily_activity_calories = 0
            
            for activity, data in activities.items():
                while True:
                    try:
                        minutes = int(input(f"{data['icon']} {activity} (minutes): "))
                        if minutes >= 0:
                            if minutes > 0:
                                # MET calculation: calories = MET × weight(kg) × time(hours)
                                # Using average weight of 70kg
                                activity_calories = data["met"] * 70 * (minutes / 60)
                                daily_activity_calories += activity_calories
                                print(f"   Calories burned: {activity_calories:.1f}")
                            break
                        else:
                            print("Minutes cannot be negative!")
                    except ValueError:
                        print("Please enter a valid number!")
            
            daily_calories += daily_activity_calories
            total_calories += daily_activity_calories
            
            # Store daily data
            daily_data = {
                "day": day_count,
                "steps": daily_steps,
                "calories": daily_calories,
                "activities": daily_activity_calories
            }
            weekly_data.append(daily_data)
            
            # Daily achievement check
            print(f"\n🎯 Daily Goals Progress:")
            steps_percentage = (daily_steps / daily_steps_goal) * 100
            calories_percentage = (daily_calories / daily_calorie_goal) * 100
            
            print(f"Steps: {daily_steps:,}/{daily_steps_goal:,} ({steps_percentage:.1f}%)")
            print(f"Calories: {daily_calories:.0f}/{daily_calorie_goal} ({calories_percentage:.1f}%)")
            
            if daily_steps >= daily_steps_goal:
                print("🎉 Steps goal achieved!")
            if daily_calories >= daily_calorie_goal:
                print("🔥 Calorie goal achieved!")
        
        elif choice == "2":
            # Log Workout Session
            print("\n💪 WORKOUT SESSION LOGGING")
            print("-" * 40)
            
            workout_types = {
                1: {"name": "Cardio", "intensity": "High", "calories_per_min": 10},
                2: {"name": "Strength Training", "intensity": "Medium", "calories_per_min": 6},
                3: {"name": "Yoga/Stretching", "intensity": "Low", "calories_per_min": 3},
                4: {"name": "HIIT", "intensity": "Very High", "calories_per_min": 15},
                5: {"name": "Sports", "intensity": "High", "calories_per_min": 12}
            }
            
            print("Available Workout Types:")
            for key, workout in workout_types.items():
                print(f"{key}. {workout['name']} ({workout['intensity']} intensity)")
            
            while True:
                try:
                    workout_choice = int(input("Select workout type (1-5): "))
                    if workout_choice in workout_types:
                        selected_workout = workout_types[workout_choice]
                        break
                    else:
                        print("Please select a valid workout type (1-5)")
                except ValueError:
                    print("Please enter a valid number!")
            
            while True:
                try:
                    duration = int(input("Enter workout duration (minutes): "))
                    if duration > 0:
                        break
                    else:
                        print("Duration must be positive!")
                except ValueError:
                    print("Please enter a valid number!")
            
            # Calculate workout calories
            workout_calories = selected_workout["calories_per_min"] * duration
            total_workout_time += duration
            total_calories += workout_calories
            
            print(f"\n✅ Workout Logged:")
            print(f"   Type: {selected_workout['name']}")
            print(f"   Duration: {duration} minutes")
            print(f"   Intensity: {selected_workout['intensity']}")
            print(f"   Calories Burned: {workout_calories}")
            
            # Weekly workout progress
            weekly_percentage = (total_workout_time / weekly_workout_goal) * 100
            print(f"\n📊 Weekly Workout Progress: {total_workout_time}/{weekly_workout_goal} minutes ({weekly_percentage:.1f}%)")
            
            if total_workout_time >= weekly_workout_goal:
                print("🏆 Weekly workout goal achieved!")
        
        elif choice == "3":
            # View Daily Summary
            if not weekly_data:
                print("\n📋 No daily data logged yet!")
                continue
                
            print("\n📊 DAILY SUMMARY")
            print("-" * 50)
            
            latest_day = weekly_data[-1]
            avg_steps = total_steps / len(weekly_data) if weekly_data else 0
            avg_calories = total_calories / len(weekly_data) if weekly_data else 0
            
            print(f"Current Day: Day {latest_day['day']}")
            print(f"Today's Steps: {latest_day['steps']:,}")
            print(f"Today's Calories: {latest_day['calories']:.0f}")
            print(f"Today's Activity Calories: {latest_day['activities']:.0f}")
            print("-" * 50)
            print(f"Average Steps/Day: {avg_steps:,.0f}")
            print(f"Average Calories/Day: {avg_calories:.0f}")
            print(f"Total Workout Time: {total_workout_time} minutes")
            
            # Achievement badges
            print(f"\n🏆 ACHIEVEMENT BADGES:")
            badges = []
            
            if latest_day['steps'] >= daily_steps_goal:
                badges.append("🦶 Step Master")
            if latest_day['calories'] >= daily_calorie_goal:
                badges.append("🔥 Calorie Crusher")
            if total_workout_time >= weekly_workout_goal:
                badges.append("💪 Workout Warrior")
            if len(weekly_data) >= 7:
                badges.append("📅 Week Warrior")
            
            if badges:
                for badge in badges:
                    print(f"   {badge}")
            else:
                print("   No badges earned yet - keep going!")
        
        elif choice == "4":
            # View Weekly Progress
            if not weekly_data:
                print("\n📋 No weekly data available yet!")
                continue
                
            print("\n📈 WEEKLY PROGRESS REPORT")
            print("-" * 60)
            
            # Daily breakdown
            print("Day-by-Day Breakdown:")
            print(f"{'Day':<5} {'Steps':<10} {'Calories':<10} {'Goal Met':<10}")
            print("-" * 60)
            
            for day_data in weekly_data:
                steps_met = "✅" if day_data['steps'] >= daily_steps_goal else "❌"
                calories_met = "✅" if day_data['calories'] >= daily_calorie_goal else "❌"
                goal_status = f"{steps_met} {calories_met}"
                
                print(f"{day_data['day']:<5} {day_data['steps']:<10,} {day_data['calories']:<10.0f} {goal_status:<10}")
            
            # Weekly statistics
            if len(weekly_data) >= 7:
                week_data = weekly_data[-7:]  # Last 7 days
                
                total_week_steps = sum(day['steps'] for day in week_data)
                total_week_calories = sum(day['calories'] for day in week_data)
                days_steps_met = sum(1 for day in week_data if day['steps'] >= daily_steps_goal)
                days_calories_met = sum(1 for day in week_data if day['calories'] >= daily_calorie_goal)
                
                print("\n📊 This Week's Summary:")
                print(f"Total Steps: {total_week_steps:,}")
                print(f"Total Calories: {total_week_calories:.0f}")
                print(f"Days Steps Goal Met: {days_steps_met}/7")
                print(f"Days Calorie Goal Met: {days_calories_met}/7")
                print(f"Workout Minutes: {total_workout_time}")
                
                # Trend analysis
                if len(weekly_data) >= 14:
                    prev_week = weekly_data[-14:-7]
                    prev_week_steps = sum(day['steps'] for day in prev_week)
                    
                    if total_week_steps > prev_week_steps:
                        print("📈 Trending up - Great improvement!")
                    elif total_week_steps < prev_week_steps:
                        print("📉 Trending down - Let's get back on track!")
                    else:
                        print("➡️ Steady performance")
        
        elif choice == "5":
            # Challenge Mode
            print("\n🏃 FITNESS CHALLENGE MODE")
            print("-" * 40)
            
            challenges = {
                1: {"name": "Step Challenge", "target": daily_steps_goal * 1.5, "unit": "steps"},
                2: {"name": "Calorie Burn Challenge", "target": daily_calorie_goal * 1.2, "unit": "calories"},
                3: {"name": "Workout Streak", "target": 30, "unit": "minutes"},
                4: {"name": "Distance Challenge", "target": 10000, "unit": "steps (10K club)"}
            }
            
            print("Available Challenges:")
            for key, challenge in challenges.items():
                print(f"{key}. {challenge['name']} - Target: {challenge['target']:.0f} {challenge['unit']}")
            
            try:
                challenge_choice = int(input("Select a challenge (1-4): "))
                if challenge_choice not in challenges:
                    print("Invalid challenge selection!")
                    continue
                    
                selected_challenge = challenges[challenge_choice]
                target = selected_challenge["target"]
                
                print(f"\n🎯 Challenge Selected: {selected_challenge['name']}")
                print(f"Target: {target:.0f} {selected_challenge['unit']}")
                
                if challenge_choice in [1, 4]:  # Step challenges
                    current_progress = total_steps if weekly_data else 0
                    progress_percent = (current_progress / target) * 100
                    print(f"Current Progress: {current_progress:,}/{target:.0f} ({progress_percent:.1f}%)")
                    
                elif challenge_choice == 2:  # Calorie challenge
                    current_progress = total_calories
                    progress_percent = (current_progress / target) * 100
                    print(f"Current Progress: {current_progress:.0f}/{target:.0f} ({progress_percent:.1f}%)")
                    
                elif challenge_choice == 3:  # Workout challenge
                    current_progress = total_workout_time
                    progress_percent = (current_progress / target) * 100
                    print(f"Current Progress: {current_progress}/{target:.0f} minutes ({progress_percent:.1f}%)")
                
                if progress_percent >= 100:
                    print("🏆 CHALLENGE COMPLETED! Congratulations!")
                else:
                    remaining = target - current_progress
                    print(f"Keep going! You need {remaining:.0f} more {selected_challenge['unit']} to complete this challenge!")
                    
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "6":
            # Set New Goals
            print("\n🎯 SET NEW GOALS")
            print("-" * 30)
            
            print("Current Goals:")
            print(f"Daily Steps: {daily_steps_goal:,}")
            print(f"Weekly Workout: {weekly_workout_goal} minutes")
            print(f"Daily Calories: {daily_calorie_goal}")
            
            update_goals = input("\nUpdate goals? (y/n): ").lower()
            if update_goals == 'y':
                try:
                    new_steps = int(input("New daily steps goal: "))
                    new_workout = int(input("New weekly workout goal (minutes): "))
                    new_calories = int(input("New daily calorie goal: "))
                    
                    daily_steps_goal = new_steps
                    weekly_workout_goal = new_workout
                    daily_calorie_goal = new_calories
                    
                    print("✅ Goals updated successfully!")
                    
                except ValueError:
                    print("Please enter valid numbers!")
        
        elif choice == "7":
            # Exit
            print("\n🏃 FITNESS TRACKER SUMMARY")
            print("=" * 50)
            print(f"Total Days Tracked: {len(weekly_data)}")
            print(f"Total Steps: {total_steps:,}")
            print(f"Total Calories Burned: {total_calories:.0f}")
            print(f"Total Workout Time: {total_workout_time} minutes")
            
            if weekly_data:
                avg_daily_steps = total_steps / len(weekly_data)
                avg_daily_calories = total_calories / len(weekly_data)
                print(f"Average Daily Steps: {avg_daily_steps:,.0f}")
                print(f"Average Daily Calories: {avg_daily_calories:.0f}")
            
            print(f"\n🎯 Keep up the great work, {user_name}!")
            print("Stay healthy and active! 💪")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main() 