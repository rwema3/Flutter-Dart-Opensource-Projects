import os

def makeCommits (days : int):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- This was the commit for the !daY!!\n')
        
        # staging 
        os.system('git add data.txt')

        # commi
        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

makeCommits(3)
