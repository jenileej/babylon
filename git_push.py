from git import Repo
import datetime

today = str(datetime.datetime.now())

repo = Repo('')
repo.git.add('--all')
repo.git.commit('-m', 'commit message ' + today)
origin = repo.remote(name='origin')
origin.push()