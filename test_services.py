import sqlite3
import unittest
from unittest.mock import Mock
import os
from services import ContactService, AlreadyExistedItem, UndefinedID, NotExistedItem
from models import Contact
from DAOs import ContactDAO
from random import randint
from services import ContactService

#added (FX)
from datetime import datetime

# To complete...
class TestContactService(unittest.TestCase):

    def setUp(self):
        self.contactDAO = Mock()
        self.contactService = ContactService(self.contactDAO)

    def test_when_contact_is_created_updated_should_be_True(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        contact = self.contactService.create_contact('Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.assertTrue(contact.updated)

    def test_when_contact_is_created_updated_date_should_be_now(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        contact = self.contactService.create_contact('Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')

            #timestamps equals, plus or minus 0.5 seconds
        self.assertTrue(
            contact.updated_date >= datetime.now().timestamp() - 0.5 and
            contact.updated_date <= datetime.now().timestamp() + 0.5)

    def test_when_contact_is_created_and_DAO_get_by_names_returns_contact_it_should_raise_AlreadyExistedItem(self):
        pass

    def test_when_contact_is_changed_updated_should_be_True(self):
        self.contactDAO.update.return_value = 1
        contact = self.contactService.update_contact(1, 'Houssem','Ben Braiek','987-654-3210','houssem.bb@gmail.com')
        self.assertTrue(contact.updated)

    def test_when_contact_is_changed_updated_date_should_be_now(self):
        self.contactDAO.update.return_value = 1
        contact = self.contactService.update_contact(1, 'Houssem','Ben Braiek','987-654-3210','houssem.bb@gmail.com')
        self.assertEqual(contact.updated_date, datetime.now().timestamp())


    def test_when_contact_is_changed_and_DAO_update_returns_zero_it_should_raise_UndefinedID(self):
        pass
        
    def test_when_retrieve_contact_is_called_with_id_and_DAO_get_by_id_should_be_called(self):
        contact = Contact(0, "LOG", "3430", '012-345-6789', "mail@gmail.com", True, "2019-09-14")
        self.contactDAO.get_by_id.return_value = contact
        self.assertEquals(self.contactService.retrieve_contact(1), contact)
        self.assertTrue(self.contactDAO.get_by_id.called)

    def test_when_retrieve_contact_is_called_with_names_and_DAO_get_by_names_should_be_called(self):
        contact = Contact(0, "LOG", "3430", '012-345-6789', "mail@gmail.com", True, "2019-09-14")
        self.contactDAO.get_by_names.return_value = contact
        self.assertEquals(self.contactService.retrieve_contact(None, 'LOG', '3430'), contact)
        self.assertTrue(self.contactDAO.get_by_names.called)

    def test_when_retrieve_contact_is_called_with_id_and_DAO_returns_None_it_should_raise_UndefinedID(self):
        pass

    def test_when_retrieve_contact_is_called_with_names_and_DAO_returns_None_it_should_raise_NotExistedItem(self):
        pass

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_should_be_called(self):
        self.contactDAO.delete_by_id.return_value = 1
        self.contactService.delete_contact(1)
        self.assertTrue(self.contactDAO.delete_by_id.called)

    def test_when_delete_contact_is_called_with_names_and_DAO_delete_by_names_should_be_called(self):
        self.contactDAO.delete_by_names.return_value = 1
        self.contactService.delete_contact(None, "LOG", "3430")
        self.assertTrue(self.contactDAO.delete_by_names.called)

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_returns_zero_it_should_raise_UndefinedID(self):
        pass

    def test_when_retrieve_contact_is_called_with_names_and_DAO_delete_by_names_returns_zero_it_should_raise_NotExistedItem(self):
        pass

    
    def test_when_valid_phone_then_return_true(self):
        first_three = randint(100, 999)
        second_three = randint(100, 999)
        last_four = randint(1000,9999)
        
        self.assertTrue(self.contactService.check_phone(str(first_three) + "-" + str(second_three) + "-" + str(last_four)))    
    
        
        
    def test_when_phone_without_hyphen_then_return_false(self):
        first_three = randint(100, 999)
        second_three = randint(100, 999)
        last_four = randint(1000,9999)
        
        self.assertFalse(self.contactService.check_phone(str(first_three) + str(second_three) + "-" + str(last_four)))
        
        
        
    def test_when_phone_with_character_then_return_false(self):
        three_digits = randint(100, 999)
        last_four = randint(1000,9999)        
        
        self.assertFalse(self.contactService.check_phone("aaaaa" + "-" + str(three_digits) + "-" + str(last_four))) 
        self.assertFalse(self.contactService.check_phone(str(three_digits) + "-" + "aaaaa" + "-" + str(last_four))) 
        self.assertFalse(self.contactService.check_phone(str(three_digits) + "-" + str(three_digits) + "-" + "aaaa")) 
       
        
    
    def test_when_phone_with_different_number_of_digits_then_return_false(self):
        first_three = randint(1000, 9999)
        second_three = randint(100, 999)
        last_four = randint(1000,9999)        
        self.assertFalse(self.contactService.check_phone(str(first_three) + "-" + str(second_three) + "-" + str(last_four)))    
              
        first_three = randint(100, 999)
        second_three = randint(1000, 9999)
        last_four = randint(1000,9999)        
        self.assertFalse(self.contactService.check_phone(str(first_three) + "-" + str(second_three) + "-" + str(last_four)))    

        first_three = randint(100, 999)
        second_three = randint(100, 999)
        last_four = randint(100,999)        
        self.assertFalse(self.contactService.check_phone(str(first_three) + "-" + str(second_three) + "-" + str(last_four)))    
        

    def test_when_valid_email_with_then_return_true(self):
        self.assertTrue(self.contactService.check_mail("hello@gmail.com"))   

    def test_when_email_without_at_symbol_return_false(self):
        self.assertFalse(self.contactService.check_mail("hellogmail.com"))  
        
    def test_when_email_without_domain_return_false(self):            
        self.assertFalse(self.contactService.check_mail("LOG.3430..bar@"))          
        
    def test_when_email_without_username_return_false(self):
        self.assertFalse(self.contactService.check_mail("@gmail.com"))  
 
        
if __name__ == '__main__':
    unittest.main()
