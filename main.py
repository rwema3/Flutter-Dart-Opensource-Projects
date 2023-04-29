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

      
        os.system('git commit --date="'+ dates +'" -m "cupertino library Null safety Flutter widgets implementing the current iOS design language."')

        return days * makeCommits(days - 1)
    
makeCommits(3)
