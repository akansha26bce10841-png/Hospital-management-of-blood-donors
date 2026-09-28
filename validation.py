def check_age(age):
    if age >=18 and age <=65:
        return True
    else:
        return False
def check_blood_group(blood_group):
    valid_groups = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
    if blood_group in valid_groups:
        return True
    else:
        return False
def check_phone(phone):
    if len(phone)==10 and phone.isdigit():
        return True
    else:
        return False
