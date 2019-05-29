from CrayCrayDrugStoreFinal import CrayCrayDrugStore
running = True
myLegalDrugz = CrayCrayDrugStore()
while running is True:

    sectiondivider = ('\n--------------------------------------------')
    print(sectiondivider)
    print('Welcome to Andii and Cobbie\'s CrayCray DrugStore.\nPlease select an action.')
    print('1 Find Customer\n2 Lineup\n3 Serve\n4 Rotate\n5 Display\n6 Exit')
    a = input('\nWhat would you like to do? (Select a command and hit enter/RET)\n')

    if a == '1':
        print(sectiondivider)
        nameofcust = input('Enter the name of the customer you are searching for: ')
        fixedname = myLegalDrugz.stringFixer(nameofcust)
        toPrint = myLegalDrugz.FindCustomer(fixedname)
        print(toPrint)

    elif a == '2':
        nameofnewcust = input('Name of new customer: ')
        ageofnewcust = int(input('Age of new customer: '))
        myLegalDrugz.Lineup(nameofnewcust, ageofnewcust)

    elif a == '3':
        print(sectiondivider)
        myLegalDrugz.Serve()

    elif a == '4':
        print(sectiondivider)
        myLegalDrugz.Rotate()

    elif a == '5':
        print(sectiondivider)
        myLegalDrugz.Display()

    elif a == '6':
        print(sectiondivider)
        myLegalDrugz.Exit()
        running = False

    else:
        print('You did not input a valid command.')
