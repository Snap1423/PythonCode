"""
Weather Advisory System
A practical program providing weather advisories based on multiple conditions.
Demonstrates: Complex conditional statements, logical operators, nested conditions
"""

def main():
    print("=" * 60)
    print("           WEATHER ADVISORY SYSTEM")
    print("=" * 60)
    
    print("🌤️  Welcome to Smart Weather Advisory System")
    print("Get personalized weather alerts and recommendations")
    print("-" * 60)
    
    # Get location information
    city = input("Enter your city: ")
    
    # Get current weather conditions
    print("\nEnter current weather conditions:")
    
    try:
        temperature = float(input("Temperature (°C): "))
        humidity = float(input("Humidity (%): "))
        wind_speed = float(input("Wind speed (km/h): "))
        
        if not (0 <= humidity <= 100):
            print("Humidity must be between 0-100%")
            return
        if wind_speed < 0:
            print("Wind speed cannot be negative")
            return
            
    except ValueError:
        print("Please enter valid numeric values!")
        return
    
    # Weather conditions
    print("\nCurrent Weather Conditions:")
    print("1. Clear/Sunny")
    print("2. Partly Cloudy")
    print("3. Cloudy")
    print("4. Rainy")
    print("5. Heavy Rain/Storm")
    print("6. Snowy")
    print("7. Foggy")
    
    while True:
        try:
            weather_choice = int(input("Select weather condition (1-7): "))
            if 1 <= weather_choice <= 7:
                break
            else:
                print("Please select 1-7")
        except ValueError:
            print("Please enter a valid number")
    
    weather_conditions = {
        1: "Clear/Sunny",
        2: "Partly Cloudy", 
        3: "Cloudy",
        4: "Rainy",
        5: "Heavy Rain/Storm",
        6: "Snowy",
        7: "Foggy"
    }
    current_weather = weather_conditions[weather_choice]
    
    # Additional conditions
    print("\nAdditional Information:")
    air_quality = input("Air quality (Good/Moderate/Poor/Very Poor): ").title()
    if air_quality not in ["Good", "Moderate", "Poor", "Very Poor"]:
        air_quality = "Unknown"
    
    uv_index = None
    if weather_choice in [1, 2]:  # Clear or partly cloudy
        while True:
            try:
                uv_index = int(input("UV Index (0-11): "))
                if 0 <= uv_index <= 11:
                    break
                else:
                    print("UV Index must be between 0-11")
            except ValueError:
                print("Please enter a valid number")
    
    time_of_day = input("Time period (Morning/Afternoon/Evening/Night): ").title()
    if time_of_day not in ["Morning", "Afternoon", "Evening", "Night"]:
        time_of_day = "Unknown"
    
    # Activity planning
    print("\nPlanned Activities (select all that apply):")
    print("1. Outdoor sports")
    print("2. Walking/Jogging")
    print("3. Driving")
    print("4. Cycling")
    print("5. Outdoor event")
    print("6. Gardening")
    print("7. None of the above")
    
    activities = []
    activity_names = {
        1: "Outdoor sports",
        2: "Walking/Jogging", 
        3: "Driving",
        4: "Cycling",
        5: "Outdoor event",
        6: "Gardening"
    }
    
    activity_input = input("Enter activity numbers separated by commas (e.g., 1,2,3): ")
    try:
        for num in activity_input.split(','):
            activity_num = int(num.strip())
            if activity_num in activity_names:
                activities.append(activity_names[activity_num])
            elif activity_num == 7:
                activities = []
                break
    except ValueError:
        activities = []
    
    # Generate weather advisory
    print("\n" + "=" * 60)
    print("              WEATHER ADVISORY")
    print("=" * 60)
    print(f"📍 Location: {city}")
    print(f"🌤️  Current Weather: {current_weather}")
    print(f"🌡️  Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} km/h")
    print(f"🌬️  Air Quality: {air_quality}")
    if uv_index is not None:
        print(f"☀️  UV Index: {uv_index}")
    print(f"🕐 Time: {time_of_day}")
    print("-" * 60)
    
    # Temperature analysis
    print("🌡️  TEMPERATURE ADVISORY:")
    if temperature < 0:
        temp_advisory = "🥶 Freezing conditions - Risk of hypothermia"
        clothing = "Heavy winter clothing, gloves, hat essential"
    elif temperature < 10:
        temp_advisory = "🧊 Very cold - Dress warmly"
        clothing = "Winter jacket, warm layers recommended"
    elif temperature < 20:
        temp_advisory = "❄️  Cool temperature"
        clothing = "Light jacket or sweater recommended"
    elif temperature < 30:
        temp_advisory = "🌤️  Pleasant temperature"
        clothing = "Comfortable clothing, no special precautions"
    elif temperature < 35:
        temp_advisory = "🌞 Warm temperature"
        clothing = "Light, breathable clothing recommended"
    elif temperature < 40:
        temp_advisory = "🔥 Hot temperature - Stay hydrated"
        clothing = "Minimal, light-colored clothing"
    else:
        temp_advisory = "🌡️  Extreme heat - Health risk"
        clothing = "Avoid outdoor activities, stay indoors"
    
    print(f"   {temp_advisory}")
    print(f"   👕 Clothing: {clothing}")
    
    # Humidity analysis
    print("\n💧 HUMIDITY ADVISORY:")
    if humidity < 30:
        humidity_advisory = "🏜️  Low humidity - Dry conditions"
        humidity_tips = "Use moisturizer, stay hydrated"
    elif humidity < 60:
        humidity_advisory = "✅ Comfortable humidity levels"
        humidity_tips = "No special precautions needed"
    elif humidity < 80:
        humidity_advisory = "💦 High humidity - May feel muggy"
        humidity_tips = "Wear breathable fabrics, stay cool"
    else:
        humidity_advisory = "🌊 Very high humidity - Uncomfortable"
        humidity_tips = "Limit outdoor activities, use AC/fans"
    
    print(f"   {humidity_advisory}")
    print(f"   💡 Tips: {humidity_tips}")
    
    # Wind analysis
    print("\n💨 WIND ADVISORY:")
    if wind_speed < 5:
        wind_advisory = "🍃 Calm conditions"
    elif wind_speed < 15:
        wind_advisory = "🌬️  Light breeze"
    elif wind_speed < 25:
        wind_advisory = "💨 Moderate wind"
    elif wind_speed < 40:
        wind_advisory = "🌪️  Strong wind - Secure loose objects"
    elif wind_speed < 60:
        wind_advisory = "⚠️  Very strong wind - Avoid outdoor activities"
    else:
        wind_advisory = "🌀 Extreme wind - Stay indoors"
    
    print(f"   {wind_advisory}")
    
    # Weather-specific advisories
    print(f"\n🌤️  WEATHER-SPECIFIC ADVISORY:")
    if current_weather == "Clear/Sunny":
        if uv_index is not None:
            if uv_index <= 2:
                uv_risk = "Low UV risk"
            elif uv_index <= 5:
                uv_risk = "Moderate UV risk - Use sunscreen"
            elif uv_index <= 7:
                uv_risk = "High UV risk - Sunscreen and hat recommended"
            elif uv_index <= 10:
                uv_risk = "Very high UV risk - Limit sun exposure"
            else:
                uv_risk = "Extreme UV risk - Avoid sun exposure"
            print(f"   ☀️  {uv_risk}")
        print("   👀 Wear sunglasses, apply sunscreen")
        
    elif current_weather == "Rainy":
        print("   ☔ Carry umbrella/raincoat")
        print("   🚗 Drive carefully - wet roads")
        print("   ⚡ Watch for lightning if thunderstorm")
        
    elif current_weather == "Heavy Rain/Storm":
        print("   🌩️  SEVERE WEATHER WARNING")
        print("   🏠 Stay indoors if possible")
        print("   🚗 Avoid driving unless absolutely necessary")
        print("   ⚡ Unplug electrical devices")
        
    elif current_weather == "Snowy":
        print("   ❄️  Snow conditions")
        print("   🚗 Use snow tires/chains")
        print("   👟 Wear appropriate footwear")
        print("   🧊 Watch for icy conditions")
        
    elif current_weather == "Foggy":
        print("   🌫️  Reduced visibility")
        print("   🚗 Use fog lights, drive slowly")
        print("   🚶 Be extra cautious when walking")
    
    # Air quality advisory
    print(f"\n🌬️  AIR QUALITY ADVISORY:")
    if air_quality == "Good":
        print("   ✅ Safe for all outdoor activities")
    elif air_quality == "Moderate":
        print("   ⚠️  Sensitive individuals may experience discomfort")
    elif air_quality == "Poor":
        print("   🔴 Limit outdoor activities, especially exercise")
        print("   😷 Consider wearing a mask outdoors")
    elif air_quality == "Very Poor":
        print("   ☠️  HEALTH ALERT - Avoid outdoor activities")
        print("   🏠 Stay indoors, close windows")
        print("   😷 Wear N95 mask if must go outside")
    
    # Activity-specific recommendations
    if activities:
        print(f"\n🏃 ACTIVITY RECOMMENDATIONS:")
        
        for activity in activities:
            print(f"\n   📋 {activity}:")
            
            # Determine safety for each activity
            safety_score = 100
            warnings = []
            
            # Temperature impacts
            if temperature < 5 or temperature > 35:
                safety_score -= 30
                warnings.append("Extreme temperature")
            
            # Weather impacts
            if current_weather in ["Heavy Rain/Storm", "Snowy"]:
                safety_score -= 50
                warnings.append("Severe weather")
            elif current_weather in ["Rainy", "Foggy"]:
                safety_score -= 25
                warnings.append("Poor weather conditions")
            
            # Wind impacts
            if wind_speed > 30:
                safety_score -= 30
                warnings.append("Strong winds")
            
            # Air quality impacts
            if air_quality in ["Poor", "Very Poor"]:
                safety_score -= 40
                warnings.append("Poor air quality")
            
            # Activity-specific conditions
            if activity in ["Outdoor sports", "Cycling"] and wind_speed > 25:
                safety_score -= 20
                warnings.append("Wind affects performance")
            
            if activity == "Driving" and current_weather in ["Foggy", "Heavy Rain/Storm"]:
                safety_score -= 30
                warnings.append("Reduced visibility")
            
            # Determine recommendation
            if safety_score >= 80:
                recommendation = "✅ RECOMMENDED - Good conditions"
            elif safety_score >= 60:
                recommendation = "⚠️  CAUTION - Take precautions"
            elif safety_score >= 40:
                recommendation = "🔴 NOT RECOMMENDED - Consider postponing"
            else:
                recommendation = "❌ AVOID - Unsafe conditions"
            
            print(f"      {recommendation}")
            if warnings:
                print(f"      ⚠️  Warnings: {', '.join(warnings)}")
    
    # General recommendations
    print(f"\n💡 GENERAL RECOMMENDATIONS:")
    general_tips = []
    
    if temperature > 30 or humidity > 70:
        general_tips.append("Stay hydrated - drink plenty of water")
    
    if current_weather in ["Rainy", "Heavy Rain/Storm"]:
        general_tips.append("Check weather updates frequently")
    
    if wind_speed > 20:
        general_tips.append("Secure outdoor furniture and objects")
    
    if air_quality in ["Poor", "Very Poor"]:
        general_tips.append("Keep windows closed, use air purifier")
    
    if uv_index and uv_index > 6:
        general_tips.append("Limit sun exposure between 10 AM - 4 PM")
    
    if not general_tips:
        general_tips.append("Enjoy the pleasant weather conditions!")
    
    for tip in general_tips:
        print(f"   • {tip}")
    
    print(f"\n📱 Stay updated with latest weather forecasts")
    print(f"🚨 Emergency contact: 108 (India) or local emergency number")
    print("=" * 60)

if __name__ == "__main__":
    main() 