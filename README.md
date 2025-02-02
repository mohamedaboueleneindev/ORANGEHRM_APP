Test Scenarios:
1. Checking login functionality using diffrent Credentials from an excel file.

    Steps:

     1.open login page.

     2.load from excell diffrent credintials.

     3.check if the user is logged in or not and compare it to the expected result in the excell sheet.

     4.repeat steps 2 and 3 until all rows are covered.

     5.assert if all test passed as expected or not.
           
3. Checking adding employee functionality using randomly generated names.
   
     Steps:
   
   1.open login page

   2.login using the correct Credentials from config.ini.

   3.open the pm menu and clicking on add employee.

   4.generate random employee firstname ,lastname and id and click on save.

   5.assert if the name added is matching with the randomly generated firstname and lastname.

5. Checking adding candidate functionality using randomly selected vacancies from dynamic list
   
    Steps:

   1.open login page

   2.login using the correct Credentials from config.ini.

   3.open the recruitment menu and click on tha add candidate.

   4.generate random firstname ,lastname ,email.

   5.check all available vacancies and randomly select one.

   6.enter a contact no and tha date of application and click on save.

   7.assert if the name added is matching with the randomly generated firstname and lastname.
   
