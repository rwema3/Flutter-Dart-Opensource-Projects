import os

def makeCommits (days : int):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the !daY!!\n')
        
        # stagty
        os.system('git add data.txt')

        # c
        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

        return days * makeCommits(days - 1)
    
makeCommits(3)
