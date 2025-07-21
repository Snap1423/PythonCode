# Chapter 3: Conditional Statements

This chapter contains practical Python programs demonstrating if-else statements, nested conditions, multiway branching, and complex conditional logic.

## Programs in this Chapter:

### 1. ATM Machine Simulator (`01_atm_machine_simulator.py`)
**Concepts Demonstrated:** If-else statements, nested conditions, multiway branching, input validation
**Description:** A complete ATM simulation with PIN verification, balance checking, cash withdrawal, deposit, and account management.

**Key Features:**
- PIN verification with attempt limits
- Multiple transaction types (balance, withdraw, deposit, statement)
- Complex withdrawal validation (amount limits, daily limits)
- Nested menu system
- Security features (PIN change, validation)

---

### 2. Student Admission System (`02_student_admission_system.py`)
**Concepts Demonstrated:** Complex conditional statements, logical operators, nested if-else, score calculations
**Description:** A college admission system that evaluates students based on multiple criteria and provides detailed results.

**Key Features:**
- Multi-criteria evaluation (10th, 12th, entrance scores)
- Category-based cutoffs (General, OBC, SC/ST, EWS)
- Bonus points for sports and NCC
- Scholarship eligibility determination
- Fee calculation with discounts

---

### 3. Smart Traffic Light System (`03_traffic_light_system.py`)
**Concepts Demonstrated:** Conditional statements, time-based logic, priority handling, state management
**Description:** An intelligent traffic management system with emergency vehicle priority, pedestrian crossings, and adaptive timing.

**Key Features:**
- Multi-directional traffic control
- Emergency vehicle priority override
- Pedestrian crossing requests
- Rush hour mode with adaptive timing
- Traffic density monitoring and recommendations

---

### 4. Weather Advisory System (`04_weather_advisory_system.py`)
**Concepts Demonstrated:** Complex conditional statements, logical operators, nested conditions, risk assessment
**Description:** A comprehensive weather advisory system providing personalized recommendations based on multiple weather parameters.

**Key Features:**
- Multi-parameter weather analysis (temperature, humidity, wind, air quality)
- Activity-specific safety recommendations
- Weather condition categorization
- Health and safety advisories
- UV index analysis for sunny conditions

---

### 5. Movie Ticket Booking System (`05_movie_ticket_booking.py`)
**Concepts Demonstrated:** Complex conditional statements, pricing logic, validation, business rules
**Description:** A complete movie ticket booking system with dynamic pricing, seat selection, and discount calculations.

**Key Features:**
- Movie and showtime selection
- Dynamic pricing based on time slots
- Age-based ticket pricing (Child, Adult, Senior)
- Multiple discount types (group, student, weekend)
- Payment method selection and processing

---

## Learning Objectives:
By working through these programs, students will learn:
- Basic if-else statement structure and syntax
- Nested conditional statements
- Multiway branching with elif statements
- Logical operators (and, or, not)
- Comparison operators in conditions
- Complex business logic implementation
- Input validation using conditions
- State management in interactive programs

## Conditional Statement Patterns Covered:

### 1. Simple If-Else
```python
if condition:
    # action
else:
    # alternative action
```

### 2. Multiway Branching
```python
if condition1:
    # action1
elif condition2:
    # action2
elif condition3:
    # action3
else:
    # default action
```

### 3. Nested Conditions
```python
if outer_condition:
    if inner_condition:
        # nested action
    else:
        # nested alternative
else:
    # outer alternative
```

### 4. Complex Logical Conditions
```python
if (condition1 and condition2) or (condition3 and not condition4):
    # complex logic action
```

## How to Run:
```bash
python 01_atm_machine_simulator.py
python 02_student_admission_system.py
python 03_traffic_light_system.py
python 04_weather_advisory_system.py
python 05_movie_ticket_booking.py
```

## Real-world Applications:
These programs demonstrate conditional statements in:
- Banking and financial systems
- Educational institutions
- Traffic management systems
- Weather forecasting services
- Entertainment booking platforms

## Extensions and Improvements:
Students can enhance these programs by:
- Adding database connectivity for persistent data
- Implementing user authentication systems
- Creating web interfaces
- Adding more sophisticated validation rules
- Implementing logging and audit trails 