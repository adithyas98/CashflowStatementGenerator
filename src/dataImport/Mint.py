import mintapi
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

