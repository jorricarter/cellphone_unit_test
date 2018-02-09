import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(2, 'Bill')
        employee3 = Employee(3, 'Ted')

        testEmployees = [ employee1, employee2, employee3 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_employee(employee2)
        testAssignmentMgr.add_employee(employee3)

        self.assertCountEqual(testEmployees, testAssignmentMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(1, 'Bill')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(employee2)


    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments
        assignments = PhoneAssignments()

        phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')

        assignments.add_phone(phone1)

        employee2 = Employee(2, 'Bill')

        assignments.add_employee(employee2)

        assignments.assign(phone1.id, employee2)
        self.assertEqual(phone1, assignments.phone_info(employee2))


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.
        assignments = PhoneAssignments()

        phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')
        phone2 = Phone(2, 'Samsung', 'Galaxy S III')

        assignments.add_phone(phone1)

        employee2 = Employee(2, 'Bill')
        employee3 = Employee(3, 'Ted')

        assignments.add_employee(employee2)
        assignments.add_employee(employee3)

        assignments.assign(phone1.id, employee2)
        with self.assertRaises(PhoneError):
            assignments.assign(phone1.id, employee3)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.
        assignments = PhoneAssignments()

        phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')
        phone2 = Phone(2, 'Samsung', 'Galaxy S III')

        assignments.add_phone(phone1)
        assignments.add_phone(phone2)

        employee2 = Employee(2, 'Bill')

        assignments.add_employee(employee2)

        assignments.assign(phone1.id, employee2)
        with self.assertRaises(PhoneError):
            assignments.assign(phone2.id, employee2)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        assignments = PhoneAssignments()

        phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')
        assignments.add_phone(phone1)

        employee2 = Employee(2, 'Bill')
        assignments.add_employee(employee2)

        assignments.assign(phone1.id, employee2)
        self.assertIsNone(assignments.assign(phone1.id, employee2))


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        assignments = PhoneAssignments()

        phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')
        assignments.add_phone(phone1)

        employee2 = Employee(2, 'Bill')
        assignments.add_employee(employee2)

        assignments.assign(phone1.id, employee2)
        assignments.un_assign(phone1.id)
        self.assertIsNone(assignments.phone_info(employee2))


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist
        assignments = PhoneAssignments()

        phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')
        phone2 = Phone(2, 'Samsung', 'Galaxy S III')
        phone3 = Phone(3, 'Samsung', 'Galaxy A7')

        assignments.add_phone(phone1)
        assignments.add_phone(phone2)
        assignments.add_phone(phone3)

        employee1 = Employee(1, 'Alice')
        employee2 = Employee(2, 'Bill')
        employee3 = Employee(3, 'Ted')
        employee4 = Employee(4, 'Fred')

        assignments.add_employee(employee1)
        assignments.add_employee(employee2)
        assignments.add_employee(employee3)

        assignments.assign(phone1.id, employee2)  # Assign phone 1 to employee 2
        assignments.assign(phone2.id, employee3)  # Assign phone 2 to employee 3

        self.assertEqual(phone1, assignments.phone_info(employee2))
        self.assertIsNone(assignments.phone_info(employee1))
        with self.assertRaises(PhoneError):
            assignments.phone_info(employee4)
