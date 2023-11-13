from datetime import datetime


def validation_check(self, value_format, user_input, error_message):
    if not user_input:
        print(error_message)
        return None

    if value_format == "int":
        if not user_input.isdigit():
            print(error_message)
            return None
        return int(user_input)

    if value_format == "str":
        return user_input

class Patient:
    def __init__(self, patient_id, name, dob, medical_history, diagnoses, treatments):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.medical_history = medical_history
        self.diagnoses = diagnoses
        self.treatments = treatments

    def get_patient_info(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, DOB: {self.dob}"


class Doctor:
    def __init__(self, doctor_id, name, specialization, experience):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.experience = experience

    def get_doctor_info(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}, Experience: {self.experience} years"


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = status

    def get_appointment_info(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}, Time: {self.time}, Status: {self.status}"

    def book_appointment(self):
        self.status = "Booked"

    def reschedule_appointment(self, new_date, new_time):
        self.date = new_date
        self.time = new_time
        self.status = "Rescheduled"

    def cancel_appointment(self):
        self.status = "Cancelled"


class Billing:
    def __init__(self, patient, services, payments):
        self.patient = patient
        self.services = services
        self.payments = payments

    # def generate_bill(self):
    #     bill_amount = sum(service.cost for service in self.services)
    #     return bill_amount

    def generate_bill(self):
        bill_amount = 0
        # for service in self.services:
        #     bill_amount += service.cost
        return bill_amount

    def process_payment(self, payment_amount):
        self.payments.append(payment_amount)


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.billing = []


    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def book_appointment(self, patient, doctor, date, time):
        appointment = Appointment(len(self.appointments) + 1, patient, doctor, date, time, 1)
        self.appointments.append(appointment)
        print(f"Appointment booked for {patient.name} with {doctor.name} on {date} at {time}")

    def add_billing(self, bill):
        self.billing.append(bill)

    def display_patient_info(self, patient_id):
        patient = self.patients[patient_id - 1]
        print(patient.get_patient_info())

    def display_doctor_info(self, doctor_id):
        doctor = self.doctors[doctor_id - 1]
        print(doctor.get_doctor_info())

    def display_appointment_info(self, appointment_id):
        appointment = self.appointments[appointment_id - 1]
        print(appointment.get_appointment_info())

    def reschedule_appointment(self, appointment_id, new_date, new_time):
        appointment = self.appointments[appointment_id - 1]
        appointment.reschedule_appointment(new_date, new_time)

    def cancel_appointment(self, appointment_id):
        appointment = self.appointments[appointment_id - 1]
        appointment.cancel_appointment()
        print("Appointment cancelled")


def display_menu():
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Book Appointment")
    print("4. Generate Bill")
    print("5. Process Payment")
    print("6. Display Patient Info")
    print("7. Display Doctor Info")
    print("8. Display Appointment Info")
    print("9. Reschedule Appointment")
    print("10. Cancel Appointment")
    print("11. Exit")


def main():
    hospital = Hospital()
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        validation_check("int", choice, "Please enter integer value")
        if choice == 11:
            break
        elif choice == 1:
            name = input("Enter patient name: ")
            dob = input("Enter patient DOB (YYYY-MM-DD): ")
            medical_history = input("Enter patient medical history: ")
            diagnoses = input("Enter patient diagnoses (comma separated): ").split(',')
            treatments = input("Enter patient treatments (comma separated): ").split(',')
            patient = Patient(len(hospital.patients) + 1, name, dob, medical_history, diagnoses, treatments)
            hospital.add_patient(patient)
        elif choice == 2:
            name = input("Enter doctor name: ")
            specialization = input("Enter doctor specialization: ")
            experience = int(input("Enter doctor experience (years): "))
            doctor = Doctor(len(hospital.doctors) + 1, name, specialization, experience)
            hospital.add_doctor(doctor)
        elif choice == 3:
            patient_id = int(input("Enter patient ID: "))
            patient = hospital.patients[patient_id - 1]
            doctor_id = int(input("Enter doctor ID: "))
            doctor = hospital.doctors[doctor_id - 1]
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            try:
                appointment_time = datetime.strptime(time, "%H:%M").time()
            except ValueError:
                print("Invalid time format. Please enter the time in HH:MM format.")
                return

            if appointment_time.hour > 23 or appointment_time.minute > 59:
                print("Invalid time. Please enter a valid time within the 24-hour format.")
                return
            hospital.book_appointment(patient, doctor, date, time)
        elif choice == 4:
            patient_id = int(input("Enter patient ID: "))
            patient = hospital.patients[patient_id - 1]
            services = input("Enter services (comma separated): ").split(',')
            bill = Billing(patient, services, [])
            hospital.add_billing(bill)
            bill_amount = bill.generate_bill()
            print(f"Bill amount: Rs.{bill_amount}")
        elif choice == 5:
            patient_id = int(input("Enter patient ID: "))
            patient = hospital.patients[patient_id - 1]
            payment_amount = float(input("Enter payment amount: "))
            bill = hospital.billing[patient_id - 1]
            bill.process_payment(payment_amount)
            print(f"Payment of Rs.{payment_amount} processed.")
        elif choice == 6:
            patient_id = int(input("Enter patient ID: "))
            patient = hospital.patients[patient_id - 1]
            print(patient.get_patient_info())
        elif choice == 7:
            doctor_id = int(input("Enter doctor ID: "))
            doctor = hospital.doctors[doctor_id - 1]
            print(doctor.get_doctor_info())
        elif choice == 8:
            appointment_id = int(input("Enter appointment ID: "))
            appointment = hospital.appointments[appointment_id - 1]
            print(appointment.get_appointment_info())
        elif choice == 9:
            appointment_id = int(input("Enter appointment ID: "))
            appointment = hospital.appointments[appointment_id - 1]
            new_date = input("Enter new appointment date (YYYY-MM-DD): ")
            new_time = input("Enter new appointment time (HH:MM): ")
            hospital.reschedule_appointment(appointment_id, new_date, new_time)
        elif choice == 10:
            appointment_id = int(input("Enter appointment ID: "))
            hospital.cancel_appointment(appointment_id)


if __name__ == "__main__":
    main()
