from donor_data import donors
def blood_group_report():
    print("\n----- BLOOD GROUP REPORT -----")
    blood_groups = ["A+", "A-","B+", "B-","AB+", "AB-","O+", "O-"]
    for group in blood_groups:
        count = 0
        for donor in donors:
            if donor[4] == group:
                count = count + 1
        print(group, ":", count, "donor(s)")
def total_donors():
    print("\nTotal Registered Donors:", len(donors))
