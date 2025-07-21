# Chapter 4: Loops

This chapter contains practical Python programs demonstrating while loops, for loops, nested loops, and loop control statements (break, continue, pass).

## Programs in this Chapter:

### 1. Fitness Tracker Application (`01_fitness_tracker.py`)
**Concepts Demonstrated:** While loops, for loops, nested loops, break/continue statements, data tracking
**Description:** A comprehensive fitness tracking application that monitors daily activities, workouts, and progress towards health goals.

**Key Features:**
- Daily activity logging with step counting
- Multiple workout types with calorie calculations
- Goal setting and progress tracking
- Weekly progress reports and statistics
- Challenge mode for motivation
- Achievement badges system

---

### 2. Interactive Quiz Game (`02_quiz_game.py`)
**Concepts Demonstrated:** For loops, while loops, nested loops, break/continue, range() function, data processing
**Description:** A multi-category quiz game with different difficulty levels and comprehensive scoring system.

**Key Features:**
- Multiple categories (Science, History, Geography, Sports)
- Three difficulty levels (Easy, Medium, Hard)
- Practice mode with unlimited attempts
- Challenge mode with special objectives
- Leaderboard and statistics tracking
- Mixed difficulty mode for varied experience

---

### 3. Number Pattern Generator (`03_number_pattern_generator.py`)
**Concepts Demonstrated:** Nested loops, for loops with range(), pattern logic, mathematical calculations
**Description:** An advanced pattern generator that creates various geometric and mathematical patterns using nested loops.

**Key Features:**
- Triangle patterns (Pascal's triangle, multiplication tables)
- Square patterns (spiral, chess board, diagonal)
- Diamond patterns (hollow, filled, centered)
- Special mathematical patterns (Fibonacci, primes, factorials)
- Pyramid patterns with numbers and letters
- Custom pattern builder for user creativity

---

### 4. Banking Transaction System (`04_banking_transaction_system.py`)
**Concepts Demonstrated:** While loops, for loops, data processing, transaction management, nested conditions
**Description:** A complete banking system with multiple account management and detailed transaction history.

**Key Features:**
- Multiple account creation and management
- Various transaction types (deposit, withdrawal, transfer)
- Interest calculations for different account types
- Admin panel for account administration
- Comprehensive transaction logging
- Account statements and balance reporting

---

### 5. Inventory Management System (`05_inventory_management.py`)
**Concepts Demonstrated:** While loops, for loops, data manipulation, search algorithms, sorting
**Description:** A comprehensive inventory management system for retail stores with advanced reporting capabilities.

**Key Features:**
- Product catalog management (add, update, delete)
- Stock level monitoring and alerts
- Category-based organization
- Search and filter functionality
- Low stock alerts and restock suggestions
- Comprehensive reports and analytics

---

## Learning Objectives:
By working through these programs, students will learn:
- While loop syntax and usage patterns
- For loop with range() function variations
- Nested loops for complex data processing
- Loop control statements (break, continue, pass)
- Iterator patterns and data traversal
- Performance considerations in loop design
- Real-world applications of looping constructs

## Loop Patterns Covered:

### 1. Basic While Loop
```python
while condition:
    # loop body
    # update condition
```

### 2. For Loop with Range
```python
for i in range(start, stop, step):
    # loop body
```

### 3. Nested Loops
```python
for i in range(rows):
    for j in range(cols):
        # nested processing
```

### 4. Loop Control
```python
for item in collection:
    if skip_condition:
        continue
    if exit_condition:
        break
    # process item
```

### 5. Loop with Else
```python
for item in collection:
    if found_condition:
        break
else:
    # executed if loop completed without break
```

## How to Run:
```bash
python 01_fitness_tracker.py
python 02_quiz_game.py
python 03_number_pattern_generator.py
python 04_banking_transaction_system.py
python 05_inventory_management.py
```

## Real-world Applications:
These programs demonstrate loops in:
- Health and fitness tracking systems
- Educational and assessment platforms
- Graphics and pattern generation
- Financial transaction processing
- Inventory and retail management

## Extensions and Improvements:
Students can enhance these programs by:
- Adding data persistence with file I/O
- Implementing GUI interfaces
- Adding network connectivity for multi-user features
- Optimizing loop performance for large datasets
- Adding more sophisticated algorithms and data structures 