# Introduction
This is the Github repository for the BP coding challenge administered by George Chandler. In this README, I will outline the details of the project, along with my workflow. As this was my first experience with the initialization of CI/CD pipelines within Azure DevOps, I ran into many problems during the process of creating the pipeline. However, I believe I was able to successfully perform the tasks of the project, which involved deploying a "Hello World!" Python application to Azure Functions via CI/CD pipelines. As requested, I have shared this repo with Lewis.Treacy@bp.com & Jacob.Pollack@bp.com. Created by Divyansh Prasad.

**The function URL endpoint:** https://dpfunc01.azurewebsites.net/api/HelloWorld

# Step 1 - "Hello World" Python App
This step involved the creation of the Python app to output "Hello World!" from an HTTP endpoint, while structuring it to make it compatible for Azure Functions. Following Microsoft's documentation and the Azure library, I created the Python app, the requirements.txt file that contains necessary dependencies, and the supplementary JSON files required for deployment.

# Step 2 - Generate Azure Function
After coding, I generated an Azure Function known as "dpfunc01", which would be the location at which the Function app would inevitably be connected to via the CI/CD pipeline. 

# Step 3 - Creation of Build Pipeline
Next, I created a project within Azure DevOps and connected this repository to a Build pipeline. DevOps then generated the YAML file that allowed the Build pipeline to be created. One possible issue encountered here is that, while the project gets built successfully, it proceeds to deploying it to the stated Azure Function without the need of a Release pipeline (I used the "Python Function App to Linux on Azure" option). I figured it may be there for the purpose of deploying it to a test Function app before making a Release, which would actually deploy it to an in-production Function app. Regardless, it does not affect the runnability of the pipeline.

# Step 4 - Creation of Release Pipeline (SonarQube Quality Scanning)
Arguably the toughest section of this project was the creation of the Release pipeline. It involved learning much in-depth knowledege about Azure applications, project properties, service connections, etc. As developing the stages were the more robust processes, I have listed them here:

1. I first began by setting up the Artifact as the Build pipeline I created in the earlier step - originally, I tried connecting the Github repository as an artifact, but later realized using the Build pipeline was a better approach. 
2. In the next stage of the pipeline, I created a SonarQube quality test - I tried utilizing truffleHog at first, but ran into numerous issues. Thus, I deployed a SonarQube server from the given repository and created credentials, generated required keys, and made a service connection to the server. This proved to be the most difficult segment of this project due to confusing exceptions being thrown and, in general, not having enough knowledge on SonarQube. After much research and deliberation, I noticed that my SonarQube test stage itself needed to be ran using different parameters, as it was attempting to analyze a .NET project. After much trial and error, I was able to get SonarQube to successfully analyze the given code. 
3. The final stage I left for deployment of the Function app. This simply involved using my Azure subscription and uploading the Function app to the same one I had previously conceived: dpfunc01.

Regarding pre- and post-deployment conditions, I put a post-deployment approval requirement after the SonarQube stage, and both pre- and post-deployment approval requirements on the deployment stage, all addressed to myself. I felt that these were the most logical locations to insert these conditions from a testing standpoint. Finally, for ease-of-use I enabled Continuous Deployment in the Artifact to initialize the creation of a Release whenever a Build is made.

# Conclusion
This project provided me with hands-on experience with the designing of CI/CD pipelines. From it, I have learned just how powerful pipelines can be, along with the immensity of functions and applications available inside Azure DevOps which were previously unknown to me.  
