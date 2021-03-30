from basic_matcher.models import Candidate, Skill, Job
from django.http import Http404
from django.shortcuts import get_object_or_404

# assuming that the best fit 
# is first by the title matching 
# and if the title does not match, 
# the best fit will be the candidate with the max skills that match.

# assuming that it's possible to get more than one candidates 
# with the same title or the same number of skills



class Candidate_Finder():

    def find_match_by_title(job_title):
        try:
            candidates = Candidate.objects.filter(title=job_title)
        except Candidate.DoesNotExist:
            return []
        else:
            return candidates    
            
    def find_match_by_max_skills(job):
        skills = job.skill_set.all()
        max_skill = 0
        all_candidates = []

        for c in Candidate.objects.all():
            counter = 0
            for s in c.skill_set.all():
                if s in skills:
                    counter = counter+1

            if max_skill == counter:
                all_candidates.append(c)
            elif max_skill < counter:
                all_candidates.clear()
                all_candidates.append(c)
                max_skill = counter    

        return all_candidates

    def candidate_finder(job_id):
        try:
            job = Job.objects.get(pk=job_id)
        except Job.DoesNotExist:
            raise Http404("Job does not exist")
        
        matches = Candidate_Finder.find_match_by_title (job.title)

        if not matches:
            matches = Candidate_Finder.find_match_by_max_skills(job)

        return matches
