
def clean_phonenumber(phonenumber):
    to_remove = ["-", " "]
    for c in to_remove:
        phonenumber = phonenumber.replace(c, "")
    return phonenumber
