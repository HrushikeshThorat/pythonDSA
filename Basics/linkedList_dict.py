#  __ __ __ __
# |11|03|23|07|
#  __ __ __ __
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

print("Accessing 3rd node value from linked list :", head["next"]["next"]["value"])