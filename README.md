# Basic Matcher

please note:
  - The database is clean before the run
  - I'm using Django with version 3.1.7 and Python with version 3.8.2


Running Instructions:
--------------------
from the main folder Basic_Matcher/
1. Create the database :
  1a. run 'python manage.py makemigrations basic_matcher'
  
  1b. run 'python manage.py migrate'
  
  1c. run 'python populate.py'
  
2. Run the server by 'python manage.py runserver' 
3. Enter to <your_localhost_address>/basic_matcher
4. For looking candidates that fit into the required job, enter the job's id and click search



Site:
--------------------

![1](https://user-images.githubusercontent.com/43497130/112990892-39ad7b00-916f-11eb-9790-5167b5074531.png)

Running Example:
--------------------

Case One: Job does not exist
-
Enter wrong job's Id

![jobnotexist](https://user-images.githubusercontent.com/43497130/112991017-5c3f9400-916f-11eb-8916-20958d7a1498.png)

results

![jobnotexist404](https://user-images.githubusercontent.com/43497130/112991044-62ce0b80-916f-11eb-8be6-36f78bf5d7b7.png)



Case Two: Found candidate by the titles matching
-
Enter job's Id

![jobbyname](https://user-images.githubusercontent.com/43497130/112991263-9741c780-916f-11eb-8811-9607fc009bff.png)

![jobbynamesearch](https://user-images.githubusercontent.com/43497130/112991272-99a42180-916f-11eb-8c22-208d6510a9f8.png)

results

![jobbynameresults](https://user-images.githubusercontent.com/43497130/112991286-9e68d580-916f-11eb-9321-da2b39d28b8f.png)



Case Three: Found candidate by the skills matching
-
Enter job's Id

![jobbyskill](https://user-images.githubusercontent.com/43497130/112991473-d243fb00-916f-11eb-8d37-a0489e65db98.png)

![jobbyskillsearch](https://user-images.githubusercontent.com/43497130/112991499-dbcd6300-916f-11eb-808f-85d762634650.png)

results

![jobbyskillresults](https://user-images.githubusercontent.com/43497130/112991516-e1c34400-916f-11eb-9489-a0bd107ff5bd.png)



Case Four: Found more than one candidates by the skills matching
-
Enter job's Id

![jobbyskillmulty](https://user-images.githubusercontent.com/43497130/112991542-e982e880-916f-11eb-86f1-cf4f27fa2d14.png)

![jobbyskillmultysearch](https://user-images.githubusercontent.com/43497130/112991574-f1428d00-916f-11eb-85ae-35c087aa8bab.png)

results

![jobbyskillmultyresults](https://user-images.githubusercontent.com/43497130/112992138-95c4cf00-9170-11eb-8bcf-95bcbd716c46.png)








