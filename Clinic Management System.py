import datetime

class Patient:
    def __init__(self, pid, name, age, doctor, appointment_date):
        self.pid = pid
        self.name = name
        self.age = age
        self.doctor = doctor
        self.appointment_date = appointment_date

class ClinicManagement:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        pid = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        doctor = input("Enter doctor's name: ")
        date_input = input("Enter appointment date (YYYY-MM-DD): ")
        try:
            appointment_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.\n")
            return
        self.patients.append(Patient(pid, name, age, doctor, appointment_date))
        print("Patient added successfully!\n")

    def view_appointments(self):
        if not self.patients:
            print("No appointments scheduled yet.\n")
            return
        print("\nScheduled Appointments:")
        for p in self.patients:
            print(f"ID: {p.pid}, Name: {p.name}, Age: {p.age}, Doctor: {p.doctor}, Date: {p.appointment_date}")
        print()

    def search_patient(self):
        pid = input("Enter patient ID to search: ")
        for p in self.patients:
            if p.pid == pid:
                print(f"Found - Name: {p.name}, Age: {p.age}, Doctor: {p.doctor}, Date: {p.appointment_date}\n")
                return
        print("Patient not found.\n")

    def delete_patient(self):
        pid = input("Enter patient ID to delete record: ")
        for p in self.patients:
            if p.pid == pid:
                self.patients.remove(p)
                print("Patient record deleted.\n")
                return
        print("Patient not found.\n")

    def run(self):
        while True:
            print("===== Clinic Management Menu =====")
            print("1. Add Patient")
            print("2. View Appointments")
            print("3. Search Patient")
            print("4. Delete Patient Record")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_patient()
            elif choice == '2':
                self.view_appointments()
            elif choice == '3':
                self.search_patient()
            elif choice == '4':
                self.delete_patient()
            elif choice == '5':
                print("Exiting Clinic Management System.")
                break
            else:
                print("Invalid choice. Try again.\n")

# Run the system
if __name__ == "__main__":
    system = ClinicManagement()
    system.run()
