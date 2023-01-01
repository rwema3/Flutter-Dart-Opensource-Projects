import os

        # staging 
        os.system('git add data.txt')

        # commits
        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

        return days * makeCommits(days - 1)
makeCommits(3)