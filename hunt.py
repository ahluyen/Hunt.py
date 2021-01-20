'''
Author: Anh Pouliquen

'''

def get_input ():
    '''
    Description:
    The first function was created to get information from parents. The required information are:
    first name, last name, and their DNA sequence. We returned a tuple of 3 strings for further
    use in the main body. 
    '''
    
    firstname = raw_input ("Enter your first name here: ")
    lastname = raw_input ("Enter your last name here: ")
    dna = raw_input ("Enter your DNA sequence here: ")
    return firstname, lastname, dna


def countCAG (dna):
    """
    Description:
    This function was created to count the total of repeats CAG in user's DNA sequence. The parameters
    of this function is dna (which we get from get_input()). The precondition of this functions is that
    if the first index to the third index of dna is CAG is will count as one repeat. Index will keep being
    updated by an increment of three. The loop will continues to count number of repeat CAG until it hit
    the end of the sequence, or when it finds an sequence that is not CAG.The total number of repeats CAG
    is being returned for further use in the main body. And the type is Integer.
    
    >>> countCAG("C")
    0
    >>> countCAG("CAGCA")
    1
    >>> countCAG("CAGCATCAGCAGCAG")
    1
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCA")
    41
    >>> countCAG("")
    0
    >>> countCAG("CA")
    0
    >>> countCAG("CAGCAGCATCAGCAGCAGCAGCAGCGAAGCGAC")
    2
    >>> countCAG("CATCAGCAGCAT")
    0
    """
    count = 0
    i = 0
    while i < len(dna):
        if dna[i:i+3] == 'CAG':
            count += 1
        else:
            break
        i = i + 3
    return count


def prediction(numCAG):
    """
    Description:
    This function was created to take the number of repeats CAG in countCAG() and give a prediction of
    classification and disease status for parents.The parameter of this function is numCAG (which we
    get from countCAG(). A tuple of 2 strings are being returned for further use in main body. 
    
      >>> prediction(27)
      ('Normal', 'Unaffected')
      >>> prediction(35)
      ('Intermediate', 'Unaffected')
      >>> prediction(42)
      ('Reduced Penetrance', 'Somewhat Affected')
      >>> prediction(45)
      ('Full Penetrance', 'Affected')
      >>> prediction(28)
      ('Intermediate', 'Unaffected')
      >>> prediction(41)
      ('Reduced Penetrance', 'Somewhat Affected')
      >>> prediction(36)
      ('Intermediate', 'Unaffected')
      >>> prediction(38)
      ('Reduced Penetrance', 'Somewhat Affected')
    """
    
    if numCAG < 28:
        Classification = 'Normal'
        Status = 'Unaffected'
    elif numCAG >= 28 and numCAG <= 36:
        Classification = 'Intermediate'
        Status = 'Unaffected'
    elif numCAG >= 37 and numCAG <= 42:
        Classification = 'Reduced Penetrance'
        Status = 'Somewhat Affected'
    elif numCAG > 42:
        Classification = 'Full Penetrance'
        Status = 'Affected'
    return Classification, Status


def main ():
    first_name, last_name, DNA = get_input()
    total = countCAG(DNA)
    predict = prediction(total)
    Cla, Sta = prediction(total)
    print "Your last name is: ", last_name
    print "Your first name is: ", first_name
    print "Your DNA sequence is: ", DNA
    print "Your total of repeats of CAG is: ", total
    print "Your Classification is: ", Cla, "and your Disease Status is: ", Sta


if __name__ == '__main__': 
    import doctest
    doctest.testmod()
    
    main ()
    


    
