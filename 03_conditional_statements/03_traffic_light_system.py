"""
Smart Traffic Light Management System
A practical program simulating traffic light control with various conditions.
Demonstrates: Conditional statements, time-based logic, priority handling
"""

import time
import random

def main():
    print("=" * 65)
    print("        SMART TRAFFIC LIGHT MANAGEMENT SYSTEM")
    print("=" * 65)
    
    # Initialize traffic light states
    directions = ["North", "South", "East", "West"]
    current_light = "Red"
    current_direction = 0
    
    # Traffic parameters
    emergency_mode = False
    rush_hour = False
    pedestrian_request = False
    vehicle_count = {"North": 0, "South": 0, "East": 0, "West": 0}
    
    print("🚦 Smart Traffic Control System Initialized")
    print("📍 Location: Main Street & City Avenue Intersection")
    print("-" * 65)
    
    while True:
        print("\n" + "=" * 65)
        print("              TRAFFIC CONTROL PANEL")
        print("=" * 65)
        print("1. Check Current Status")
        print("2. Manual Traffic Count Input")
        print("3. Pedestrian Crossing Request")
        print("4. Emergency Vehicle Priority")
        print("5. Toggle Rush Hour Mode")
        print("6. Simulate Automatic Cycle")
        print("7. View Traffic Statistics")
        print("8. Exit System")
        print("-" * 65)
        
        choice = input("Select option (1-8): ")
        
        if choice == "1":
            # Check Current Status
            print("\n" + "🚦" * 20)
            print("           CURRENT TRAFFIC STATUS")
            print("🚦" * 20)
            
            # Simulate current light state
            light_states = ["Red", "Yellow", "Green"]
            current_light = random.choice(light_states)
            active_direction = directions[current_direction]
            
            print(f"Active Direction: {active_direction}")
            print(f"Current Light: {get_light_emoji(current_light)} {current_light}")
            
            # Display all directions
            for i, direction in enumerate(directions):
                if i == current_direction:
                    status = f"{get_light_emoji(current_light)} {current_light}"
                else:
                    status = f"🔴 Red"
                
                count = vehicle_count[direction]
                waiting_status = get_traffic_density(count)
                print(f"{direction:>6}: {status} | Vehicles: {count:>2} | {waiting_status}")
            
            # Special conditions
            if emergency_mode:
                print("🚨 EMERGENCY MODE ACTIVE")
            if rush_hour:
                print("⏰ RUSH HOUR MODE ACTIVE")
            if pedestrian_request:
                print("🚶 PEDESTRIAN CROSSING REQUESTED")
                
        elif choice == "2":
            # Manual Traffic Count Input
            print("\n" + "-" * 40)
            print("        MANUAL TRAFFIC COUNT")
            print("-" * 40)
            
            for direction in directions:
                while True:
                    try:
                        count = int(input(f"Enter vehicle count for {direction}: "))
                        if 0 <= count <= 50:
                            vehicle_count[direction] = count
                            break
                        else:
                            print("Count must be between 0-50")
                    except ValueError:
                        print("Please enter a valid number")
            
            print("✅ Traffic counts updated successfully!")
            
        elif choice == "3":
            # Pedestrian Crossing Request
            print("\n" + "-" * 40)
            print("      PEDESTRIAN CROSSING")
            print("-" * 40)
            
            if pedestrian_request:
                print("🚶 Pedestrian crossing already requested")
                print("Estimated wait time: 30-60 seconds")
            else:
                pedestrian_request = True
                print("🚶 Pedestrian crossing request registered")
                
                # Determine wait time based on current conditions
                if emergency_mode:
                    wait_time = "Emergency vehicles have priority - Wait extended"
                elif current_light == "Green":
                    wait_time = "15-30 seconds (current cycle ending)"
                elif vehicle_count[directions[current_direction]] > 20:
                    wait_time = "45-90 seconds (heavy traffic)"
                else:
                    wait_time = "30-45 seconds (normal wait)"
                
                print(f"Estimated wait time: {wait_time}")
                
                # Process pedestrian crossing
                print("\nProcessing pedestrian request...")
                if current_light == "Red":
                    print("✅ Safe to cross NOW - All vehicles stopped")
                    pedestrian_request = False
                elif vehicle_count[directions[current_direction]] < 5:
                    print("⚠️  Light changing to accommodate pedestrians")
                    current_light = "Yellow"
                    print("🟡 Yellow light activated")
                    print("⏱️  3 seconds until Red")
                    print("✅ Pedestrian crossing will be available shortly")
                    pedestrian_request = False
                else:
                    print("⏰ Request queued - will be processed at next cycle")
        
        elif choice == "4":
            # Emergency Vehicle Priority
            print("\n" + "-" * 40)
            print("      EMERGENCY VEHICLE PRIORITY")
            print("-" * 40)
            
            if emergency_mode:
                emergency_mode = False
                print("🚨 Emergency mode DEACTIVATED")
                print("Returning to normal traffic flow")
            else:
                print("Emergency vehicle detected!")
                print("1. Ambulance")
                print("2. Fire Truck") 
                print("3. Police Vehicle")
                print("4. VIP Convoy")
                
                try:
                    emergency_type = int(input("Select emergency type (1-4): "))
                    types = {1: "Ambulance", 2: "Fire Truck", 3: "Police Vehicle", 4: "VIP Convoy"}
                    
                    if emergency_type in types:
                        emergency_mode = True
                        vehicle_type = types[emergency_type]
                        
                        print(f"🚨 EMERGENCY PRIORITY ACTIVATED")
                        print(f"Vehicle Type: {vehicle_type}")
                        
                        # Determine emergency direction
                        print("Emergency vehicle direction:")
                        for i, direction in enumerate(directions):
                            print(f"{i+1}. {direction}")
                        
                        direction_choice = int(input("Select direction (1-4): ")) - 1
                        emergency_direction = directions[direction_choice]
                        
                        print(f"\n🚨 CLEARING PATH FOR {vehicle_type.upper()}")
                        print(f"Direction: {emergency_direction}")
                        
                        # Override normal traffic flow
                        current_direction = direction_choice
                        current_light = "Green"
                        
                        print(f"🟢 {emergency_direction} direction: GREEN light")
                        for direction in directions:
                            if direction != emergency_direction:
                                print(f"🔴 {direction} direction: RED light")
                        
                        print("⚠️  All other traffic must stop immediately")
                        print("⏱️  Emergency mode will auto-deactivate after passage")
                        
                    else:
                        print("Invalid emergency type")
                except ValueError:
                    print("Please enter a valid number")
                    
        elif choice == "5":
            # Toggle Rush Hour Mode
            print("\n" + "-" * 40)
            print("        RUSH HOUR MODE")
            print("-" * 40)
            
            if rush_hour:
                rush_hour = False
                print("⏰ Rush hour mode DEACTIVATED")
                print("Returning to normal timing cycles")
            else:
                rush_hour = True
                print("⏰ Rush hour mode ACTIVATED")
                print("Extended green times for busy directions")
                
                # Simulate rush hour traffic increase
                for direction in directions:
                    vehicle_count[direction] = min(50, vehicle_count[direction] + random.randint(10, 20))
                
                print("📈 Traffic volume increased automatically")
                
        elif choice == "6":
            # Simulate Automatic Cycle
            print("\n" + "-" * 50)
            print("         AUTOMATIC TRAFFIC CYCLE")
            print("-" * 50)
            
            print("🔄 Starting automatic traffic light cycle...")
            
            for cycle in range(4):  # One complete cycle for all directions
                direction = directions[cycle]
                current_direction = cycle
                
                # Determine timing based on traffic and conditions
                if emergency_mode:
                    timing = get_emergency_timing()
                elif rush_hour:
                    timing = get_rush_hour_timing(vehicle_count[direction])
                else:
                    timing = get_normal_timing(vehicle_count[direction])
                
                print(f"\n🔄 Cycle {cycle + 1}/4: {direction} Direction")
                print("-" * 30)
                
                # Red to Green transition
                if pedestrian_request and cycle == 0:
                    print("🚶 Processing pedestrian crossing...")
                    print("🔴 All directions: RED (Pedestrian crossing)")
                    simulate_wait(3)
                    pedestrian_request = False
                    print("✅ Pedestrian crossing complete")
                
                # Green phase
                current_light = "Green"
                print(f"🟢 {direction}: GREEN for {timing['green']} seconds")
                
                for other_dir in directions:
                    if other_dir != direction:
                        print(f"🔴 {other_dir}: RED")
                
                simulate_wait(timing['green'])
                
                # Yellow phase
                current_light = "Yellow"
                print(f"🟡 {direction}: YELLOW for {timing['yellow']} seconds")
                simulate_wait(timing['yellow'])
                
                # Red phase
                current_light = "Red"
                print(f"🔴 {direction}: RED")
                
                # Update vehicle count (vehicles pass through)
                vehicles_passed = min(vehicle_count[direction], timing['green'] // 2)
                vehicle_count[direction] = max(0, vehicle_count[direction] - vehicles_passed)
                print(f"✅ {vehicles_passed} vehicles passed through")
                
                if emergency_mode and cycle == 0:
                    print("🚨 Emergency vehicle passed - Deactivating emergency mode")
                    emergency_mode = False
                    break
            
            print("\n✅ Complete traffic cycle finished!")
            
        elif choice == "7":
            # View Traffic Statistics
            print("\n" + "-" * 50)
            print("           TRAFFIC STATISTICS")
            print("-" * 50)
            
            total_vehicles = sum(vehicle_count.values())
            
            print(f"📊 Current Traffic Summary:")
            print(f"Total Vehicles Waiting: {total_vehicles}")
            
            if total_vehicles > 0:
                for direction in directions:
                    count = vehicle_count[direction]
                    percentage = (count / total_vehicles) * 100
                    density = get_traffic_density(count)
                    print(f"{direction:>6}: {count:>2} vehicles ({percentage:>5.1f}%) - {density}")
            
            # Traffic recommendations
            print(f"\n📋 System Recommendations:")
            
            if total_vehicles > 80:
                print("🔴 CRITICAL: Consider activating rush hour mode")
            elif total_vehicles > 50:
                print("🟡 HIGH: Monitor traffic closely")
            elif total_vehicles > 20:
                print("🟢 MODERATE: Normal monitoring")
            else:
                print("🟢 LOW: Minimal traffic")
            
            # Find busiest direction
            busiest_direction = max(vehicle_count, key=vehicle_count.get)
            if vehicle_count[busiest_direction] > 15:
                print(f"⚠️  Busiest direction: {busiest_direction} ({vehicle_count[busiest_direction]} vehicles)")
                print(f"   Consider extending green time for {busiest_direction}")
            
        elif choice == "8":
            # Exit System
            print("\n" + "=" * 65)
            print("      SHUTTING DOWN TRAFFIC CONTROL SYSTEM")
            print("=" * 65)
            print("🔴 Setting all lights to FLASHING RED")
            print("⚠️  Manual traffic control recommended")
            print("📞 Contact traffic control center if needed")
            print("👋 System shutdown complete")
            break
            
        else:
            print("❌ Invalid choice! Please select 1-8.")

def get_light_emoji(light):
    if light == "Red":
        return "🔴"
    elif light == "Yellow":
        return "🟡"
    elif light == "Green":
        return "🟢"
    return "⚫"

def get_traffic_density(count):
    if count >= 30:
        return "🔴 Heavy Traffic"
    elif count >= 15:
        return "🟡 Moderate Traffic"
    elif count >= 5:
        return "🟢 Light Traffic"
    else:
        return "⚪ Minimal Traffic"

def get_normal_timing(vehicle_count):
    base_green = 30
    if vehicle_count > 20:
        green_time = base_green + 15
    elif vehicle_count > 10:
        green_time = base_green + 10
    else:
        green_time = base_green
    
    return {"green": green_time, "yellow": 5}

def get_rush_hour_timing(vehicle_count):
    base_green = 45
    if vehicle_count > 25:
        green_time = base_green + 20
    elif vehicle_count > 15:
        green_time = base_green + 15
    else:
        green_time = base_green
    
    return {"green": green_time, "yellow": 5}

def get_emergency_timing():
    return {"green": 60, "yellow": 3}

def simulate_wait(seconds):
    print(f"⏱️  [{seconds}s]", end="", flush=True)
    for i in range(seconds):
        time.sleep(0.1)  # Shortened for demo
        print(".", end="", flush=True)
    print(" ✓")

if __name__ == "__main__":
    main() 