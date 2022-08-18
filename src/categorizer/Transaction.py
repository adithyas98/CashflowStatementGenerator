#Created by Adithya Shastry


class Transaction:
    '''
    A class that will serve as the primary method to holding information 
    regarding a transaction
    '''

    def __init__(self,amount,name,category=None,description=None):
        '''
        Constructor
        Inputs:
            - amount(float): the amount of money that this charge transaction is
                -for negative values, input a negative number
            - name(string): the name of the transaction
            - category(string): the category this transaction is placed in
                -by default it is None
        '''
        #We just want to set the values to the inputs we are getting
        self.amount = amount
        self.name = name
        self.category = category
        self.description = self.description

