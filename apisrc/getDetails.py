from github import Github
from github.Organization import Organization

from Keys import SECRET_KEY
import json

USER_NAME = "0b01"

g = Github(SECRET_KEY)

user = g.get_user(USER_NAME)


print(user.name)


repoData = []

for repo in g.get_user(USER_NAME).get_repos():

    commits = repo.get_commits()
    name = repo.name
    totalCommits = commits.totalCount
    personalCommits = 0

    for commit in commits:
        if commit.commit is not None:

            if ((commit.commit.author.name == USER_NAME) or (commit.commit.author.name.casefold() == user.name.casefold())):
                personalCommits = personalCommits + 1
            
    #ignore repositories where zero contribution was made, this implies those repos are copied from external sources.
    if personalCommits != 0:

        data = {"repoName": name, "totalCommits": totalCommits, "personalCommits": personalCommits}
        repoData.append(data)
        print (repoData)

Data = {"repoData":repoData}

with open("simpleData.json", "w") as fp:
       json.dump(Data, fp, indent=4)