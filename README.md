# SwengVisualisation
Visualisation of github api data.

Goal of Visualisation:

    In the file getDetails.py, the field USER_NAME can be changed to any specific github username. 
    Given so, the api data received is the amount of committs for each repository that the user contributed to, and also the amount of those committs that were done by the user themselves.

    This allows me to see what percentage of the commit total the user contributed to, allowing me to create a metric I call 
    "Contribution Amount", that can be a measure for how much work the user contributes for each repository. I can also create an
    average contribution figure that represents the average amount of contribution over all the repositories the user is involved in.

    Repositories with 0 personal committs are ignored, since many people clone other repositories onto their github accounts. This is done to avoid skewing their contribution metric.


Method Taken Towards Goal:

    I decided to retrieve the API data using PyGithub, this data is compiled directly into python dicts and stored as a JSON in a local file. I chose this method as Github API polling takes a long time for some reason, so storing it somewhere means once we do it once, we can reuse the data without having to poll again. However, the first time can take a while. I had a big problem with exceeding the API rate limit after running the code 5 or 6 times, so ensure you don't run it too often

    Next I am using Chart js, a simple charting tool, to visualise the data in a useful way on a localhost web server using html and javascript.

    
Tools Needed:

Please let me know if it does not work, this was all that I needed to run it

1. install the latest Python version

2. install Pip

3. pip install PyGithub


Running the Application:

    !WARNING! you must clear the python server cache otherwise it won't update graphData.json

    There are two main ways to run my program, one is the full functionality, and the other runs the visualisation immediately using pre-created files to avoid the long wait for the api polling.
    If you want to run the visualisation first, skip to the "Visualisation" section below. This will use my pre-created Json files from a microsoft employee by the username "0b01". Otherwise, you can input another github user which will rewrite the Json files in the "API-Polling" section below.

    All necessary files are in the apisrc folder

    API-Polling:

    1. In the file getDetails.py you must delete the line "from Keys import SECRET_KEY" and set "g = Github(SECRET_KEY)" where 
       SECRET_KEY is your github access token. Mine is stored in a hidden Keys file.

    2. Set the USER_NAME field to a username of a github account (note not their actual name, but the login name shown just below it)

    3. run ./run.sh, this gets github API data from the user specified in part 2. This may take a while as github API calls are very slow.
        The necessary basic details will be put in a file called simpleData.json. They will be immediately reformatted for visualisation purposes and stored in graphData.json


    Visualisation:

    1. Assuming the graphData.json file has been filled through API calls, we can run ./run-server.sh, which should start a python web server on localhost:8000

    2. Once we are on the site, open Visualisation.html

    3. Here we will see a button labelled "Create/Update Graphs", click on that and it will load in the JSON files and create the graphs using them

    The top graph is a double barchart where the left bar shows the total commits in the named repository on the x-axis. the right bar shows the amount of commits the specified user contributed to the repository.

    The bottom graph shows the percentage contributions of the data in the first graph, and in the title states the average contribution percentage for the user



By Pascal Raos
