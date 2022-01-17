from git import Repo

repo = Repo('')
repo.git.add('--all')
repo.git.commit('-m', 'commit message')
origin = repo.remote(name='origin')
origin.push()