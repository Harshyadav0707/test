from machine import Pin
import time

# --- GPIO Configuration ---
green_led = Pin(4, Pin.OUT)
yellow_led = Pin(5, Pin.OUT)
red_led = Pin(2, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)

# --- Global Variables ---
emergency_flag = False
cycle_count = 0

# --- Interrupt Service Routine (ISR) for Emergency Button ---
def button_pressed_handler(pin):
    global emergency_flag
    emergency_flag = True

# Attach interrupt to the button
button.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed_handler)

# --- Helper Function to Turn All LEDs Off ---
def all_off():
    green_led.value(0)
    yellow_led.value(0)
    red_led.value(0)

# --- Startup State (All LEDs Off initially) ---
all_off()
print("System Started: All LEDs OFF")
time.sleep(1)

# --- Main Loop ---
while True:
    # 1. EMERGENCY CHECK & HANDLING (Bonus Included)
    if emergency_flag:
        print("\n[STATE: EMERGENCY] Override Activated!")
        all_off()
        
        # Immediately GREEN for 5 seconds
        green_led.value(1)
        print("[STATE: GREEN] Emergency Passage - 5s")
        time.sleep(5)
        green_led.value(0)
        
        # Bonus: Intersection Clear (RED for 2 seconds)
        red_led.value(1)
        print("[STATE: RED] Intersection Clearing - 2s")
        time.sleep(2)
        red_led.value(0)
        
        # Reset flag after handling emergency
        emergency_flag = False
        print("Emergency Handled. Resuming Normal Cycle...\n")
        continue

    # 2. NORMAL TRAFFIC CYCLE (Bonus Included)
    
    # Bonus: 'ALL OFF' state for 1 second before GREEN
    all_off()
    print("\n[STATE: ALL OFF] Preparing for Green - 1s")
    time.sleep(1)
    if emergency_flag: continue

    # GREEN State (5 seconds)
    green_led.value(1)
    print("[STATE: GREEN] Go - 5s")
    for _ in range(50):
        time.sleep(0.1)
        if emergency_flag: break
    green_led.value(0)
    if emergency_flag: continue

    # YELLOW State (2 seconds)
    yellow_led.value(1)
    print("[STATE: YELLOW] Slow Down - 2s")
    for _ in range(20):
        time.sleep(0.1)
        if emergency_flag: break
    yellow_led.value(0)
    if emergency_flag: continue

    # RED State (5 seconds)
    red_led.value(1)
    print("[STATE: RED] Stop - 5s")
    for _ in range(50):
        time.sleep(0.1)
        if emergency_flag: break
    red_led.value(0)
    if emergency_flag: continue

    # Bonus: Cycle Counter Increment & Print
    cycle_count += 1
    print("####################################")
    print(f"SUCCESS: Traffic Cycle {cycle_count} Completed!")
    print("####################################")