from donor_data import donors
from validation import check_age, check_blood_group, check_phone
def add_donor():
    print("\n- - - - - ADD NEW DONOR - - - - -")
    donor_id = input(" Enter Donor ID: ")
    name = input(" Enter Name: ")
    age = int(input(" Enter Age: "))
    if not check_age(age):
        print( "Donor must be between 18 and 65 years old.")
        return 
    gender = input(" Enter Gender: ")
    blood_group = input(" Enter Blood Group: ").upper()
    if not check_blood_group(blood_group):
        print(" Invalid blood group.")
        return
    phone = input(" Enter Phone Number: ")
    if not check_phone(phone):
        print(" Invalid phone number.")
        return
    city = input(" Enter City: ")
    donor = [donor_id,name,age,gender,blood_group,phone,city]
    donors.append(donor)
    print("Donor added successfully!")
def view_donors():
    print("\n----- ALL DONORS -----")
    if len(donors) == 0:
        print("No donor records found.")
        return
    for donor in donors:
        print("\nDonor ID: ", donor[0])
        print("Name: ", donor[1])
        print("Age: ", donor[2])
        print("Gender: ", donor[3])
        print("Blood Group: ", donor[4])
        print("Phone: ", donor[5])
        print("City: ", donor[6])
def update_donor():
    print("\n----- UPDATE DONOR -----")
    donor_id = input("Enter Donor ID to update: ")
    found = False
    for donor in donors:
        if donor[0] == donor_id:
            found = True
            print("Current phone:", donor[5])
            new_phone = input("Enter new phone number: ")
            if check_phone(new_phone):
                donor[5] = new_phone
            else:
                print("Invalid phone number.")
                return
            new_city = input("Enter new city: ")
            donor[6] = new_city
            print("Donor details updated successfully!")
    if found == False:
        print("Donor not found.")
def delete_donor():
    print("\n- - - - - DELETE DONOR - - - - -")
    donor_id= input("Enter Donor ID to delete: ")
    found= False
    for donor in donors:
        if donor[0]== donor_id:
            donors.remove(donor)
            found = True
            print("Donor deleted successfully!")
            break
    if found== False:
        print("Donor not found.")
