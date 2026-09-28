donors =[]
def add_donor():
    print("\n- - -   ADD DONOR    - - -")
    donor_id = input("Enter Donor ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    blood_group = input("Enter Blood Group: ").upper()
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")
    donor = [donor_id,name,age,gender,blood_group,phone,city]
    donors.append(donor)
    print("\nDonor added successfully!")
def view_donors():
    print("\n- - -   ADD DONOR    - - -")
    if len(donors) == 0:
        print("No donor records found.")
        return
    for donor in donors:
        print("\nDonor ID    :", donor[0])
        print("Name        :", donor[1])
        print("Age         :", donor[2])
        print("Gender      :", donor[3])
        print("Blood Group :", donor[4])
        print("Phone       :", donor[5])
        print("City        :", donor[6])
def search_donor():
    print("\n- - - SEARCH DONOR - - -")
    blood_group = input("Enter Blood Group: ").upper()
    found = False
    for donor in donors:
        if donor[4] == blood_group:
            print("\nDonor Found")
            print("ID    :", donor[0])
            print("Name  :", donor[1])
            print("Phone :", donor[5])
            print("City  :", donor[6])
            found = True
    if found == False:
        print("No donor found for", blood_group)
def update_donor():
    print("\n- - - UPDATE DONOR - - -")
    donor_id = input("Enter Donor ID: ")
    found = False
    for donor in donors:
        if donor[0] == donor_id:
            new_phone = input("Enter New Phone Number: ")
            new_city = input("Enter New City: ")
            donor[5] = new_phone
            donor[6] = new_city
            print("Donor details updated successfully!")
            found = True
    if found == False:
        print("Donor not found.")
def delete_donor():
    print("\n - - -  DELETE DONOR - - -")
    donor_id = input("Enter Donor ID: ")
    found = False
    for donor in donors:
        if donor[0] == donor_id:
            donors.remove(donor)
            print("Donor deleted successfully!")
            found = True
            break
    if found == False:
        print("Donor not found.")
def blood_group_report():
    print("\n - - -  BLOOD GROUP REPORT - - -")
    groups = ["A+", "A-", "B+", "B-",
              "AB+", "AB-", "O+", "O-"]
    for group in groups:
        count = 0
        for donor in donors:
            if donor[4] == group:
                count = count + 1
        print(group, ":", count, "donor(s)")
def main():
    while True:
        print("="*35)
        print(" HOSPITAL BLOOD DONOR MANAGEMENT")
        print("="*35)
        print("1. Add Donor")
        print("2. View Donors")
        print("3. Search Donor")
        print("4. Update Donor")
        print("5. Delete Donor")
        print("6. Blood Group Report")
        print("7. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_donor()
        elif choice == "2":
            view_donors()
        elif choice == "3":
            search_donor()
        elif choice == "4":
            update_donor()
        elif choice == "5":
            delete_donor()
        elif choice == "6":
            blood_group_report()
        elif choice == "7":
            print("\nThank you for using the system!")
            break
        else:
            print("Invalid choice!")
main()
