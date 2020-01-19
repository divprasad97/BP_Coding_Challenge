# Introduction
This is the Github repository for the BP coding challenge administered by George Chandler. In this README, I will outline the details of the project, along with my workflow. As this was my first experience with the initialization of CI/CD pipelines within Azure DevOps, I ran into many problems during the process of creating the pipeline. However, I believe I was able to successfully perform the tasks of the project, which involved deploying a "Hello World!" Python application to Azure Functions via CI/CD pipelines. As requested, I have shared this repo with Lewis.Treacy@bp.com & Jacob.Pollack@bp.com. Created by Divyansh Prasad.

**The function URL endpoint:** https://dpfunc01.azurewebsites.net/api/HelloWorld

# Step 1 - "Hello World" Python App
This step involved the creation of the Python app to output "Hello World!" from an HTTP endpoint, while structuring it to make it compatible for Azure Functions. Following Microsoft's documentation and the Azure library, I created the Python app, the requirements.txt file that contains necessary dependencies, and the supplementary JSON files required for deployment.

# Step 2 - Generate Azure Function
After coding, I generated an Azure Function known as "dpfunc01", which would be the location at which the Function app would inevitably be connected to via the CI/CD pipeline. 

# Step 3 - Creation of Build Pipeline
Next, I created a project within Azure DevOps and connected this repository to a Build pipeline. DevOps then generated the YAML file that allowed the Build pipeline to be created. One possible issue encountered here is that, while the project gets built successfully, it proceeds to deploying it to the stated Azure Function without the need of a Release pipeline (I used the "Python Function App to Linux on Azure" option). I figured it may be there for the purpose of deploying it to a test Function app before making a Release, which would actually deploy it to an in-production Function app. Regardless, it does not affect the runnability of the pipeline.

Edit: I noticed the reason for deployment during Build stage, as it was included automatically within the YAML file. I went ahead and removed this section of code.

# Step 4 - Creation of Release Pipeline (SonarQube Quality Scanning)
Arguably the toughest section of this project was the creation of the Release pipeline. It involved learning much in-depth knowledege about Azure applications, project properties, service connections, etc. As developing the stages were the more robust processes, I have listed them here:

1. I first began by setting up the Artifact as the Build pipeline I created in the earlier step - originally, I tried connecting the Github repository as an artifact, but later realized using the Build pipeline was a better approach. 
2. In the next stage of the pipeline, I created a SonarQube quality test - I tried utilizing truffleHog at first, but ran into numerous issues. Thus, I deployed a SonarQube server from the given repository and created credentials, generated required keys, and made a service connection to the server. This proved to be the most difficult segment of this project due to confusing exceptions being thrown and, in general, not having enough knowledge on SonarQube. After much research and deliberation, I noticed that my SonarQube test stage itself needed to be ran using different parameters, as it was attempting to analyze a .NET project. After much trial and error, I was able to get SonarQube to successfully analyze the given code. 
3. The final stage I left for deployment of the Function app. This simply involved using my Azure subscription and uploading the Function app to the same one I had previously conceived: dpfunc01.

Regarding pre- and post-deployment conditions, I only used two post-deployment approval requirements: one on the SonarQube stage and another on the deployment stage, all addressed to myself. I felt that these were the most logical locations to insert these conditions from a self-testing standpoint. Finally, for ease-of-use I enabled Continuous Deployment in the Artifact to initialize the creation of a Release whenever a Build is made.

# Step 5 - Final Project Edits
After ensuring all the steps above worked properly, the last step of the project was to change the structure of the pipelines to meet project tasks and illustrate how the CI/CD pipeline would look in the real world. I have numbered these steps below:

1. Firstly, the SonarQube Scan step was included in the Release pipeline, when it should be included in the Build pipeline. Therefore, I first deleted the SonarQube stage from the Release pipeline and then inserted SonarQube tasks inside the YAML file of the Build pipeline.
2. Next, I needed to change the pipeline to demonstrate a realistic route-to-live. Thus, I created four separate deployment stages (for the purpose of this project, I have set the deployment to the same Azure Function, dpfunc01): 
- The first stage represents Development cycle in which the developer ensures their program works properly
- Next, the program would be sent to the QA team, who would perform their own checks to rectify the program
- In the case that a customer is involved in the production of the application, there would  be another stage between QA and Production to allow the customer to check the program
- Ultimately, after the program passes QA, all checks should be good and the program is ready to be sent into Production. 

In a practical environment, pre and post deployment conditions would include multiple users representing each part of the dev cycle. But in this case, I have put myself as the approver. 

# Conclusion
This project provided me with hands-on experience with the designing of CI/CD pipelines. From it, I have learned just how powerful pipelines can be, along with the immensity of functions and applications available inside Azure DevOps which were previously unknown to me.  
