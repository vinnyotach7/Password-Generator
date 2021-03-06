import unittest # Importing the unittest module
import Account from account  # Importing the account class


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account("Vinny","Otach","32180321","vinnyotach7@gmail.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Vinny")
        self.assertEqual(self.new_account.user_name,"Otach")
        self.assertEqual(self.new_account.password,"32180321")
        self.assertEqual(self.new_account.email,"vinnyotach7@gmail.com")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),1)  


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []    


    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0722731751","test@user.com") 
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0746058500","test@user.com") 
            test_account.save_account()

            self.new_account.delete_account()# Deleting an account object
            self.assertEqual(len(Account.account_list),1)        
     
    def test_find_account_by_account_name(self):
        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0746819636","test@user.com") 
        test_account.save_account()

        found_account = Account.find_by_name("Test")

        self.assertEqual(found_account.email,test_account.email)    
    def test_account_exists(self):
        '''
        test to check if we can return a true/false  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0742819636","test@user.com") 
        test_account.save_account()

        account_exists = Account.account_exist("0742819636")

        self.assertTrue(account_exists)
    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''
        displayed = Account.display_accounts()
        self.assertEqual(displayed,Account.account_list)    

if __name__ == '__main__':
    unittest.main()