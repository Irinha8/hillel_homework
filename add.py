class Patient:
    next_id = 1

    def __init__(self, last_name, first_name, age, address):
        self.id = Patient.next_id
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.address = address
        Patient.next_id += 1


class PatientsDb:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        self.patients.update({patient.id: patient})

    def get_patients(self):
        return list(self.patients.values())

    def get_patient_by_id(self, patient_id):
        pass


def main():
    db = PatientsDb()

    while True:
        command = input("Enter command: ")
        if command == "stop":
            break

        if command == "add":
            """
            Спрашивать по отдельности фамилию, имя, возраст, адрес
            Печатать сообщение об успешности добавления пациента в БД
            """
            last_name = input("Enter patients' last name: ")
            first_name = input("Enter patients' first name: ")
            age = int(input("Enter patients' age: "))
            address = input("Enter patients' address: ")
            patient = Patient(last_name, first_name, age, address)
            db.add_patient(patient)
            print("Patient is successfully added to database")

        if command == "list":
            print("List of patients:")
            for patient in db.get_patients():
                print(patient.id, patient.last_name, patient.first_name, patient.age, patient.address)

        if command == "get_by_id":
            pass


if __name__ == '__main__':
   main()