# ABDUL-KAREEM, Ibrahim
import os

def create_student_folders():
    """Creates folders for each student with an empty README.md file."""
    students = [
        "ABDUL-KAREEM, Ibrahim",
        "ADUBA, Emmanuel",
        "ANAMAN-GILLAN, Eric",
        "BEUGRE, Corneille",
        "DAO, Martin",
        "FOSUHENE, Solomon",
        "GONCALVES, Joao Paulo",
        "KING, Jonathan",
        "LEGISTER, Tia",
        "NZIOKA, Josh",
        "OLUIGBO, Chibuike",
        "PECKUS, Marijus",
        "Quartey, Richard",
        "RODGERS, Ciaran",
        "WOJNA, Kacper"
    ]

    for student in students:
        # Extract surname and name
        surname, name = student.split(", ")
        folder_name = f"{surname} {name}"

        # Create the folder
        os.makedirs(folder_name, exist_ok=True)

        # Create the README.md file
        with open(os.path.join(folder_name, "README.md"), "w") as f:
            f.write("")

create_student_folders()
