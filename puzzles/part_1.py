#GIVEN:
guest_name = "   aLExAnDeR   "
event_name = "bIrThDAy baSH"
location = "  suNnyvaLE city hall  "
time = "  5:00Pm   "

#EXPECTED OUTPUT:
"""
Dear Alexander,

You are invited to the Birthday Bash!
Location: Sunnyvale City Hall
Time: 05:00PM

Sincerely,
Party Committee
"""

print(f"Dear {guest_name.strip().lower().capitalize()},\nYou are invited to the {event_name.lower().title()}!\nLocation: {location.strip().lower().title()}\nTime: {time.upper().strip()}\n\nSincerely,\nParty Committee")