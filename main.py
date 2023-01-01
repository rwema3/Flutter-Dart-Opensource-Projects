import os

    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the !dai!!\n')
        
        # staging 
        os.system('git add data.txt')

        # commits
        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

        return days * makeCommits(days - 1)
makeCommits(3)