import sqlite3
import unittest
import unittest.mock
import os
from DAOs import ContactDAO

#added
from models import Contact

# To complete...
class TestContactDAO(unittest.TestCase):

    def setUp(self):
        self.db_file = 'temp.db'
        self.contactDAO = ContactDAO(self.db_file)
        self.contactDAO.init_db()

    def tearDown(self):
        os.remove(self.db_file)

    def isSameContact(self, contact1, contact2):
        return(
            contact1.id           == contact2.id           and
            contact1.first_name   == contact2.first_name   and
            contact1.last_name    == contact2.last_name    and
            contact1.phone        == contact2.phone        and
            contact1.mail         == contact2.mail         and
            contact1.updated      == contact2.updated      and
            contact1.updated_date == contact2.updated_date )

    def test_when_init_db_is_called_it_should_create_table(self):
        try:
            with sqlite3.connect(self.db_file) as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM contact')
        except sqlite3.OperationalError:
            self.fail("Should not have raised sqlite3.OperationalError")

    def test_when_add_is_called_it_should_return_an_autoincremented_id(self):
        firstId = None
        contact1 = Contact(firstId, "testFirstName1", "testLastName1", "911", "testMail1", True, "testTime1")
        firstId = self.contactDAO.add(contact1)

        SecondId = None
        contact2 = Contact(SecondId, "testFirstName2", "testLastName2", "911", "testMail2", True, "testTime2")
        SecondId = self.contactDAO.add(contact2)

        self.assertTrue(SecondId == firstId + 1)

    def test_get_by_id_after_add_should_return_inserted_value(self):
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", True, "testTime")
        contact.id = self.contactDAO.add(contact)

        contactReturned = self.contactDAO.get_by_id(id = contact.id)

        self.assertTrue(self.isSameContact(contact, contactReturned))

    def test_get_by_names_after_add_should_return_inserted_value(self):
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", True, "testTime")
        contact.id = self.contactDAO.add(contact)

        contactReturned = self.contactDAO.get_by_names(first_name = contact.first_name, last_name = contact.last_name)

        self.assertTrue(self.isSameContact(contact, contactReturned))

    def test_get_by_id_with_undefined_rowid_should_return_None(self):
        self.assertTrue(self.contactDAO.get_by_id(None) == None)

    def test_get_by_names_with_notexisted_contact_should_return_None(self):
        self.assertTrue(self.contactDAO.get_by_names("", "") == None)

    def test_deactivate_contact_then_get_it_with_id_should_be_not_updated(self):
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", True, "testTime")
        contact.id = self.contactDAO.add(contact)
        self.contactDAO.deactivate(contact.id)
        self.assertTrue(not self.contactDAO.get_by_id(contact.id).updated)

    def test_deactivate_contact_on_undefined_id_should_return_zero(self):
        self.assertTrue(self.contactDAO.deactivate(None) == 0)

    def test_after_deleting_contact_by_id_get_it_with_id_should_return_None(self):
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", True, "testTime")
        contact.id = self.contactDAO.add(contact)
        self.contactDAO.delete_by_id(contact.id)
        self.assertTrue(self.contactDAO.get_by_id(contact.id) == None)

    def test_deleting_undefined_id_should_return_zero(self):
        self.assertTrue(self.contactDAO.delete_by_id(None) == 0)

    def test_after_deleting_contact_by_id_get_item_with_id_should_return_None(self):
        # FX: tested two times?
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", True, "testTime")
        contact.id = self.contactDAO.add(contact)
        self.contactDAO.delete_by_id(contact.id)
        self.assertTrue(self.contactDAO.get_by_id(contact.id) == None)

    def test_deleting_not_existed_contact_should_return_zero(self):
        self.assertTrue(self.contactDAO.delete_by_id(0) == 0)
        self.assertTrue(self.contactDAO.delete_by_names("", "") == 0)

    def test_update_contact_should_set_the_provided_values(self):
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", True, "testTime")
        contact.id = self.contactDAO.add(contact)

        newFirstName = "newFirstName"
        newLastName = "newLastName"
        newNumber = "newNumber"
        newMail = "newMail"

        contact.first_name = newFirstName
        contact.last_name = newLastName
        contact.phone = newNumber
        contact.mail = newMail

        self.contactDAO.update(contact)

        updatedContact = self.contactDAO.get_by_id(contact.id)

        self.assertTrue(self.isSameContact(contact, updatedContact))

    def test_update_contact_should_return_zero_if_id_does_not_exist(self):
        contact = Contact(None, "testName", "testName", "514", "testMail", True, "testTime")
        self.assertTrue( self.contactDAO.update(contact) == 0 )

    def test_list_contacts_with_no_contacts_added_returns_empty_list(self):
        self.assertTrue( self.contactDAO.list(None) == [] )

    def test_list_contacts_with_one_contact_should_return_list_with_contact(self):
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", True, "testTime")
        contact.id = self.contactDAO.add(contact)

        contactList = self.contactDAO.list(True)

        self.assertTrue(len(contactList) == 1 and self.isSameContact(contact, contactList[0]))

    def test_list_contacts_with_updated_False_and_all_items_updated_should_return_empty_list(self):
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", True, "testTime")
        contact.id = self.contactDAO.add(contact)
        contactList = self.contactDAO.list(False)
        self.assertTrue(len(contactList) == 0)

    def test_list_contacts_with_updated_True_and_all_items_not_updated_should_return_empty_list(self):
        contact = Contact(None, "testFirstName", "testLastName", "911", "testMail", False, "testTime")
        contact.id = self.contactDAO.add(contact)
        contactList = self.contactDAO.list(True)
        self.assertTrue(len(contactList) == 0)

    def test_list_contacts_with_all_not_updated_items_and_updated_False_should_return_all_contacts(self):
        contact1 = Contact(None, "testFirstName1", "testLastName1", "testNum1", "testMail1", False, "testTime1")
        contact1.id = self.contactDAO.add(contact1)
        contact2 = Contact(None, "testFirstName2", "testLastName2", "testNum2", "testMail2", False, "testTime2")
        contact2.id = self.contactDAO.add(contact2)

        contactList = self.contactDAO.list(False)
        self.assertTrue(len(contactList) == 2 and self.isSameContact(contact1, contactList[0]) and self.isSameContact(contact2, contactList[1]))

    def test_list_contacts_with_all_updated_items_and_updated_True_should_return_all_contacts(self):
        contact1 = Contact(None, "testFirstName1", "testLastName1", "testNum1", "testMail1", True, "testTime1")
        contact1.id = self.contactDAO.add(contact1)
        contact2 = Contact(None, "testFirstName2", "testLastName2", "testNum2", "testMail2", True, "testTime2")
        contact2.id = self.contactDAO.add(contact2)

        contactList = self.contactDAO.list(True)
        self.assertTrue(len(contactList) == 2 and self.isSameContact(contact1, contactList[0]) and self.isSameContact(contact2, contactList[1]))

if __name__ == '__main__':
    unittest.main()
