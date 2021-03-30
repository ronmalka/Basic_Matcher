import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matcher.settings')

import django 
django.setup()

from basic_matcher.models import Candidate, Job, Skill

candidates = ['Teacher', 'Software Developer','Android developer', 'Full stack developer' ]
jobs = ['Teacher', 'Software Developer','Android developer', 'Full stack developer', 'Software engineer','Moblie Developer']

def populate():
    # populate skill
    math = Skill(title = 'Math')
    math.save()
    java = Skill(title = 'Java')
    java.save()
    android = Skill(title = 'Android')
    android.save()
    python = Skill(title = 'Python')
    python.save()
    django = Skill(title = 'Django')
    django.save()
    react = Skill(title = 'React')
    react.save()

    # populate candidate
    for i,title in enumerate(candidates):
        c = Candidate(title = title)
        c.save()

        if(i == 0):
            math.candidates.add(c)
        elif(i == 1):
            java.candidates.add(c)
            python.candidates.add(c)
        elif(i == 2):
            java.candidates.add(c)
            android.candidates.add(c)
        elif(i == 3):
            python.candidates.add(c)
            django.candidates.add(c)
            react.candidates.add(c)    
            
    # poplate jobs
    for i,title in enumerate(jobs):
            j = Job(title = title)
            j.save()

            if(i == 0):
                math.jobs.add(j)
            elif(i == 1):
                java.jobs.add(j)
                python.jobs.add(j)
            elif(i == 2):
                java.jobs.add(j)
                android.jobs.add(j)
            elif(i == 3):
                python.jobs.add(j)
                django.jobs.add(j)
                react.jobs.add(j)
            elif(i == 4): 
                java.jobs.add(j)
                android.jobs.add(j)       
                python.jobs.add(j)
                django.jobs.add(j)
                react.jobs.add(j)
            elif(i == 5):
                python.jobs.add(j)
                android.jobs.add(j)
                java.jobs.add(j)       

def main():
   populate()

if __name__ == '__main__':
    main()
        

