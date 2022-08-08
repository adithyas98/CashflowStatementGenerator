import mintapi
import getpass
import keyring


class MintData:
    '''
    This class will pull all of the transactions from mint and export them as a 
    list of transaction objects (see transaction class)
    '''
    def __init__(self,email=None,password=None):
        '''
        Constructor
        Inputs:
            - email(string): email to use to log into mint account
            - password(string): password to use to long into mint account
                -These are None by default
        If the values above are None, then the user will be prompted to enter
        the username and password in the command line and store it in the user's
        keyring
        '''
        self.mint = None#Make a variable to ensure everything below worked
        #Prompt the user to pass in credentials if they are blank
        if email == None:
            #Then we want to prompt the user for an email
            email = input("Please Enter Your Email\n")
        #We can try to get the password using the keychain
        password = keyring.get_password("mint",email)
        #we can check to see if the password exists
        if password == None:
            #Then we need to prompt the user
            print("Seems like you don't have an account linked in your system")
            #We need a way to get the password, but not show it in cli
            password = getpass.getpass("Please Enter Your Password: ")
            #we can try to log in now
            try:
                self.mint = mintapi.Mint(email,password)
            except:
                #There was some sort of error so close the program
                print("Seems like there was an error with your credentials\n")
                print("Please try again, but re starting the program\n")
                quit()
            #If it does work, then we will store the password in the keyring
            print("Login successful!\n")
            print("Will store password in the keyring\n")
            keyring.set_password("mint",email,password)
        else:
            try:
                self.mint = mintapi.Mint(email,password)
            except:
                #There was some sort of error so close the program
                print("Seems like there was an error with your credentials\n")
                password = getpass.getpass("Please Enter Your Password: ")
                try:
                    self.mint = mintapi.Mint(email,password)
                except:
                    #There was some sort of error so close the program
                    print("Seems like there was an error with your credentials\n")
                    print("Please try again, but re starting the program\n")
                    quit()
                #If it does work, then we will store the password in the keyring
                print("Login successful!\n")
                print("Will store password in the keyring\n")
                keyring.set_password("mint",email,password)
        #Make sure mint isn't none
        assert self.mint != None
    def getTransactions(self,startDate=None,endDate=None):
        '''
        Method will return all transactions in a lsit of transaction objects
        Inputs:
            startDate: the start date to look for
            endDate: The end date to look for
        Outputs:
            Will output a list of transaction objects


 
             

