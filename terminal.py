import sqlite3

from functions import (
    add_client,
    update_client,
    delete_client,
    get_clients,
    add_trainer,
    update_trainer,
    delete_trainer,
    get_trainers,
    add_group_class,
    update_group_class,
    delete_group_class,
    get_group_classes,
    add_membership,
    update_membership,
    delete_membership,
    get_memberships,
    add_schedule,
    update_schedule,
    delete_schedule,
    get_schedules,
    add_booking,
    update_booking,
    delete_booking,
    get_bookings,
    add_payment,
    update_payment,
    delete_payment,
    get_payments,
    add_equipment,
    update_equipment,
    delete_equipment,
    get_equipment
)

while True:
    print("\n=== SPORT CLUB MANAGER ===")
    print("1 - Add client")
    print("2 - Update client")
    print("3 - Delete client")
    print("4 - Show clients")
    print("5 - Add trainer")
    print("6 - Update trainer")
    print("7 - Delete trainer")
    print("8 - Show trainers")
    print("9 - Add group class")
    print("10 - Update group class")
    print("11 - Delete group class")
    print("12 - Show group classes")
    print("13 - Add membership")
    print("14 - Update membership")
    print("15 - Delete membership")
    print("16 - Show memberships")
    print("17 - Add schedule entry")
    print("18 - Update schedule entry")
    print("19 - Delete schedule entry")
    print("20 - Show schedule")
    print("21 - Add booking")
    print("22 - Update booking")
    print("23 - Delete booking")
    print("24 - Show bookings")
    print("25 - Add payment")
    print("26 - Update payment")
    print("27 - Delete payment")
    print("28 - Show payments")
    print("29 - Add equipment")
    print("30 - Update equipment")
    print("31 - Delete equipment")
    print("32 - Show equipment")
    print("0 - Exit")

    choice = input("Choice: ")

    try:
        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            registration_date = input("Registration date (YYYY-MM-DD): ")
            client_id = add_client(first_name, last_name, phone, email, registration_date)
            print("Client added, ID:", client_id)

        elif choice == "2":
            print("\nClients:")
            for client in get_clients():
                print(client)

            client_id = int(input("Client ID: "))
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            registration_date = input("Registration date (YYYY-MM-DD): ")
            if update_client(client_id, first_name, last_name, phone, email, registration_date) > 0:
                print("Client updated.")
            else:
                print("Client with this ID was not found.")

        elif choice == "3":
            print("\nClients:")
            for client in get_clients():
                print(client)

            client_id = int(input("Enter the ID of the client to delete: "))
            if delete_client(client_id) > 0:
                print("Client deleted.")
            else:
                print("Client with this ID was not found.")

        elif choice == "4":
            print("\nClients:")
            for client in get_clients():
                print(client)

        elif choice == "5":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone = input("Phone: ")
            specialization = input("Specialization: ")
            hire_date = input("Hire date (YYYY-MM-DD): ")
            trainer_id = add_trainer(first_name, last_name, phone, specialization, hire_date)
            print("Trainer added, ID:", trainer_id)

        elif choice == "6":
            print("\nTrainers:")
            for trainer in get_trainers():
                print(trainer)

            trainer_id = int(input("Trainer ID: "))
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone = input("Phone: ")
            specialization = input("Specialization: ")
            hire_date = input("Hire date (YYYY-MM-DD): ")
            if update_trainer(trainer_id, first_name, last_name, phone, specialization, hire_date) > 0:
                print("Trainer updated.")
            else:
                print("Trainer with this ID was not found.")

        elif choice == "7":
            print("\nTrainers:")
            for trainer in get_trainers():
                print(trainer)

            trainer_id = int(input("Enter the ID of the trainer to delete: "))
            if delete_trainer(trainer_id) > 0:
                print("Trainer deleted.")
            else:
                print("Trainer with this ID was not found.")

        elif choice == "8":
            print("\nTrainers:")
            for trainer in get_trainers():
                print(trainer)

        elif choice == "9":
            name = input("Class name: ")
            description = input("Description: ")
            duration = int(input("Duration in minutes: "))
            class_id = add_group_class(name, description, duration)
            print("Group class added, ID:", class_id)

        elif choice == "10":
            print("\nGroup classes:")
            for group_class in get_group_classes():
                print(group_class)

            class_id = int(input("Class ID: "))
            name = input("Class name: ")
            description = input("Description: ")
            duration = int(input("Duration in minutes: "))
            if update_group_class(class_id, name, description, duration) > 0:
                print("Group class updated.")
            else:
                print("Group class with this ID was not found.")

        elif choice == "11":
            print("\nGroup classes:")
            for group_class in get_group_classes():
                print(group_class)

            class_id = int(input("Enter the ID of the class to delete: "))
            if delete_group_class(class_id) > 0:
                print("Group class deleted.")
            else:
                print("Group class with this ID was not found.")

        elif choice == "12":
            print("\nGroup classes:")
            for group_class in get_group_classes():
                print(group_class)

        elif choice == "13":
            print("\nClients:")
            for client in get_clients():
                print(client)

            client_id = int(input("Client ID: "))
            membership_type = input("Membership type: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            membership_id = add_membership(client_id, membership_type, start_date, end_date)
            print("Membership added, ID:", membership_id)

        elif choice == "14":
            print("\nMemberships:")
            for membership in get_memberships():
                print(membership)

            membership_id = int(input("Membership ID: "))
            client_id = int(input("Client ID: "))
            membership_type = input("Membership type: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            if update_membership(membership_id, client_id, membership_type, start_date, end_date) > 0:
                print("Membership updated.")
            else:
                print("Membership with this ID was not found.")

        elif choice == "15":
            print("\nMemberships:")
            for membership in get_memberships():
                print(membership)

            membership_id = int(input("Enter the ID of the membership to delete: "))
            if delete_membership(membership_id) > 0:
                print("Membership deleted.")
            else:
                print("Membership with this ID was not found.")

        elif choice == "16":
            print("\nMemberships:")
            for membership in get_memberships():
                print(membership)

        elif choice == "17":
            print("\nGroup classes:")
            for group_class in get_group_classes():
                print(group_class)

            print("\nTrainers:")
            for trainer in get_trainers():
                print(trainer)

            class_id = int(input("Class ID: "))
            trainer_id = int(input("Trainer ID: "))
            date_time = input("Date & time (YYYY-MM-DD HH:MM:SS): ")
            room = input("Room: ")
            schedule_id = add_schedule(class_id, trainer_id, date_time, room)
            print("Schedule entry added, ID:", schedule_id)

        elif choice == "18":
            print("\nSchedule:")
            for schedule in get_schedules():
                print(schedule)

            schedule_id = int(input("Schedule ID: "))
            class_id = int(input("Class ID: "))
            trainer_id = int(input("Trainer ID: "))
            date_time = input("Date & time (YYYY-MM-DD HH:MM:SS): ")
            room = input("Room: ")
            if update_schedule(schedule_id, class_id, trainer_id, date_time, room) > 0:
                print("Schedule entry updated.")
            else:
                print("Schedule entry with this ID was not found.")

        elif choice == "19":
            print("\nSchedule:")
            for schedule in get_schedules():
                print(schedule)

            schedule_id = int(input("Enter the ID of the schedule entry to delete: "))
            if delete_schedule(schedule_id) > 0:
                print("Schedule entry deleted.")
            else:
                print("Schedule entry with this ID was not found.")

        elif choice == "20":
            print("\nSchedule:")
            for schedule in get_schedules():
                print(schedule)

        elif choice == "21":
            print("\nClients:")
            for client in get_clients():
                print(client)

            print("\nSchedule:")
            for schedule in get_schedules():
                print(schedule)

            client_id = int(input("Client ID: "))
            schedule_id = int(input("Schedule ID: "))
            booking_date = input("Booking date (YYYY-MM-DD): ")
            booking_id = add_booking(client_id, schedule_id, booking_date)
            print("Booking added, ID:", booking_id)

        elif choice == "22":
            print("\nBookings:")
            for booking in get_bookings():
                print(booking)

            booking_id = int(input("Booking ID: "))
            client_id = int(input("Client ID: "))
            schedule_id = int(input("Schedule ID: "))
            booking_date = input("Booking date (YYYY-MM-DD): ")
            if update_booking(booking_id, client_id, schedule_id, booking_date) > 0:
                print("Booking updated.")
            else:
                print("Booking with this ID was not found.")

        elif choice == "23":
            print("\nBookings:")
            for booking in get_bookings():
                print(booking)

            booking_id = int(input("Enter the ID of the booking to delete: "))
            if delete_booking(booking_id) > 0:
                print("Booking deleted.")
            else:
                print("Booking with this ID was not found.")

        elif choice == "24":
            print("\nBookings:")
            for booking in get_bookings():
                print(booking)

        elif choice == "25":
            print("\nClients:")
            for client in get_clients():
                print(client)

            client_id = int(input("Client ID: "))
            amount = float(input("Amount: "))
            payment_date = input("Payment date (YYYY-MM-DD): ")
            payment_method = input("Payment method: ")
            payment_id = add_payment(client_id, amount, payment_date, payment_method)
            print("Payment added, ID:", payment_id)

        elif choice == "26":
            print("\nPayments:")
            for payment in get_payments():
                print(payment)

            payment_id = int(input("Payment ID: "))
            client_id = int(input("Client ID: "))
            amount = float(input("Amount: "))
            payment_date = input("Payment date (YYYY-MM-DD): ")
            payment_method = input("Payment method: ")
            if update_payment(payment_id, client_id, amount, payment_date, payment_method) > 0:
                print("Payment updated.")
            else:
                print("Payment with this ID was not found.")

        elif choice == "27":
            print("\nPayments:")
            for payment in get_payments():
                print(payment)

            payment_id = int(input("Enter the ID of the payment to delete: "))
            if delete_payment(payment_id) > 0:
                print("Payment deleted.")
            else:
                print("Payment with this ID was not found.")

        elif choice == "28":
            print("\nPayments:")
            for payment in get_payments():
                print(payment)

        elif choice == "29":
            name = input("Equipment name: ")
            quantity = int(input("Quantity: "))
            condition = input("Condition: ")
            purchase_date = input("Purchase date (YYYY-MM-DD): ")
            equipment_id = add_equipment(name, quantity, condition, purchase_date)
            print("Equipment added, ID:", equipment_id)

        elif choice == "30":
            print("\nEquipment:")
            for equipment in get_equipment():
                print(equipment)

            equipment_id = int(input("Equipment ID: "))
            name = input("Equipment name: ")
            quantity = int(input("Quantity: "))
            condition = input("Condition: ")
            purchase_date = input("Purchase date (YYYY-MM-DD): ")
            if update_equipment(equipment_id, name, quantity, condition, purchase_date) > 0:
                print("Equipment updated.")
            else:
                print("Equipment with this ID was not found.")

        elif choice == "31":
            print("\nEquipment:")
            for equipment in get_equipment():
                print(equipment)

            equipment_id = int(input("Enter the ID of the equipment to delete: "))
            if delete_equipment(equipment_id) > 0:
                print("Equipment deleted.")
            else:
                print("Equipment with this ID was not found.")

        elif choice == "32":
            print("\nEquipment:")
            for equipment in get_equipment():
                print(equipment)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

    except ValueError:
        print("Error: please enter a number where a number is required.")
    except sqlite3.Error as error:
        print("Database error:", error)
