"""
road_simulation.py
Full Self Driving Simulation mode in Kigali: ALU Rwanda -> Convention Center
"""

SEGMENT_M = 100
ZEBRA_WAIT = 15
ACCELERATION = 5
BRAKING = 20
START_NAME = "ALU Rwanda"
END_NAME = "Convention Center"

road = [
    "60", "road", "road", "road", "zebra", "road", "road", "80", "road", "road",
    "road", "road", "road", "road", "bus", "road", "road", "bus", "road", "road",
    "road", "60", "road", "road", "road", "road", "80", "road", "road", "zebra",
    "road", "road", "road", "road",
]


# ==================== PART 1: CHECK THE SIGN ====================

def is_valid_sign(sign):
    if not isinstance(sign, str):
        return False
    clean_sign = sign.strip().lower()
    if clean_sign in ["bus", "zebra"]:
        return True
    if clean_sign.isdigit():
        val = int(clean_sign)
        if 20 <= val <= 100:
            return True
    return False


def get_sign_type(sign):
    if not isinstance(sign, str):
        return "road"
    clean_sign = sign.strip().lower()
    if clean_sign == "bus":
        return "bus"
    elif clean_sign == "zebra":
        return "zebra"
    elif clean_sign.isdigit() and 20 <= int(clean_sign) <= 100:
        return "speed"
    else:
        return "road"


# ==================== PART 2: TAKE ACTION ====================

def get_speed_limit(sign, current_limit):
    if get_sign_type(sign) == "speed":
        return int(str(sign).strip())
    return current_limit


def get_target_speed(limit, stop_timer):
    if stop_timer > 0:
        return 0
    return limit


def adjust_speed(speed, target):
    if speed < target:
        speed += ACCELERATION
        if speed > target:
            speed = target
    elif speed > target:
        speed -= BRAKING
        if speed < target:
            speed = target
    return speed


def count_signs(road_list):
    speed_signs = 0
    zebras = 0
    buses = 0
    if isinstance(road_list, list):
        for sign in road_list:
            stype = get_sign_type(sign)
            if stype == "speed":
                speed_signs += 1
            elif stype == "zebra":
                zebras += 1
            elif stype == "bus":
                buses += 1
    return (speed_signs, zebras, buses)


# ==================== PART 3: SAFE INPUT AND JOURNEY SUMMARY ====================

def ask_for_number(question, low, high):
    while True:
        try:
            raw_input = input(question)
            value = int(raw_input.strip())
            if low <= value <= high:
                return value
            print(f"Please enter a number between {low} and {high}.")
        except (ValueError, TypeError, AttributeError):
            print("Invalid input! Please enter a valid whole number.")


def insert_sign(road_list, sign, position):
    if not isinstance(road_list, list):
        return False
    if not isinstance(position, int) or isinstance(position, bool):
        return False
    if 0 <= position <= len(road_list):
        road_list.insert(position, sign)
        return True
    return False


def replace_sign(road_list, sign, index):
    if not isinstance(road_list, list):
        return False
    if not isinstance(index, int) or isinstance(index, bool):
        return False
    if 0 <= index <= len(road_list) - 1:
        road_list[index] = sign
        return True
    return False


def get_journey_summary(road_list):
    signs_passed = 0
    if isinstance(road_list, list):
        for sign in road_list:
            if get_sign_type(sign) != "road":
                signs_passed += 1
        length_m = len(road_list) * SEGMENT_M
    else:
        length_m = 0
    return (signs_passed, length_m, START_NAME, END_NAME)


if __name__ == "__main__":
    import sys
    import transit_program
    transit_program.run(sys.modules[__name__])
