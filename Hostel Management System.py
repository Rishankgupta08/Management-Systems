class Student:
    def __init__(self, sid, name, room_type):
        self.sid = sid
        self.name = name
        self.room_type = room_type  # 'Single' or 'Double'
        self.rent_paid = False

class HostelManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        sid = input("Enter student ID: ")
        name = input("Enter student name: ")
        room = input("Enter room type (Single/Double): ")
        self.students.append(Student(sid, name, room))
        print("Student added successfully!\n")

    def view_students(self):
        if not self.students:
            print("No students added yet.\n")
            return
        print("\nList of Students:")
        for s in self.students:
            print(f"ID: {s.sid}, Name: {s.name}, Room: {s.room_type}, Rent Paid: {'Yes' if s.rent_paid else 'No'}")
        print()

    def mark_rent_paid(self):
        sid = input("Enter student ID to mark rent paid: ")
        for s in self.students:
            if s.sid == sid:
                s.rent_paid = True
                print("Rent marked as paid.\n")
                return
        print("Student not found.\n")

    def search_student(self):
        sid = input("Enter student ID to search: ")
        for s in self.students:
            if s.sid == sid:
                print(f"Found - Name: {s.name}, Room: {s.room_type}, Rent Paid: {'Yes' if s.rent_paid else 'No'}\n")
                return
        print("Student not found.\n")

    def run(self):
        while True:
            print("===== Hostel Management Menu =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Mark Rent Paid")
            print("4. Search Student")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.mark_rent_paid()
            elif choice == '4':
                self.search_student()
            elif choice == '5':
                print("Exiting Hostel Management System.")
                break
            else:
                print("Invalid choice. Try again.\n")

# Run the system
if __name__ == "__main__":
    system = HostelManagement()
    system.run()
