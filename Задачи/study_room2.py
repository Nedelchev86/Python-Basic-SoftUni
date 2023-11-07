# # meter to  cm
#
# h = float(input()) * 100
# w = float(input()) * 100
#
# passageway = 100 # cm
# door= 1 # place
# rostrum = 2 # place
#
# one_desk = 70 * 120
#
# places = (((w - passageway) * h) - door - rostrum) / one_desk
# print(places)

# convert m -> cm
w = float(input()) * 100  # length in meters
h = float(input()) * 100  # width in meters

h -= 100  # corridor -> (-100cm)

places_not_present = 3  # missing workplaces

# working place: measures
workplace_h = 70
workplace_w = 120

# distributed desks
desks_in_row = h / workplace_h  # desks on a row
desk_rows = w / workplace_w  # shows how much rows with desks

Total_places = desk_rows * desks_in_row - places_not_present

print(int(Total_places))
