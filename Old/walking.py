#Jake is testing github/git commands
def walk():
    right_foot = None
    left_foot = None
    step = right_foot
    while True:
        if step == right_foot:
            step = left_foot
            print("Left step.")

        if step == left_foot:
            step = right_foot
            print("Right step.")


walk()
