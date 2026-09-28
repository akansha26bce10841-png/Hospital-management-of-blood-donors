from donor_data import donors
from validation import check_blood_group
def search_by_blood_group():
    print("\n----- SEARCH DONOR -----")
    blood_group = input("Enter required blood group: ").upper()
    if not check_blood_group(blood_group):
        print("Invalid blood group.")
        return
    found = False
    print("\nMatching Donors:")
    for donor in donors:
        if donor[4] == blood_group:
            found = True
            print("ID:", donor[0]," Name:", donor[1], "| Phone:", donor[5],"| City:", donor[6])
    if found == False:
        print("No donor found for blood group", blood_group)
