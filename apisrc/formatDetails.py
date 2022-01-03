import json

with open('simpleData.json') as json_file:
    data = json.load(json_file)


#gets Contribution percentages

repoData = []
sum = 0

for entry in data["repoData"]:
    repoName = entry["repoName"]
    totalCommits = entry["totalCommits"]
    personalCommits = entry["personalCommits"]

    percentContribution = round(((personalCommits / totalCommits) * 100),2)
    sum = sum + percentContribution

    jsonEntry = {"repoName":repoName, "totalCommits":totalCommits, "personalCommits":personalCommits, "percContribution":percentContribution}
    repoData.append(jsonEntry)
    
averageContribution = round(sum / len(data["repoData"]),2)   #average contribution over all repositories

finalDict = {"AvgCont":averageContribution, "repoData":repoData}

with open("graphData.json", "w") as fp:
       json.dump(finalDict, fp, indent=4)

print(averageContribution)

