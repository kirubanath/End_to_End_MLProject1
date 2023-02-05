# End_to_End_MLProject1

This is an End to End ML project created on boston housing price dataset. The aim of this is to understand the life cycle of an ML project.

## [The Webapp](https://ml-project-housingprice.herokuapp.com/)
(The app looks very basic but the objective here is understanding MLOPS)

### Software and Tools requirements:

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Heroku Account](https://www.heroku.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

### Steps: 

**Create a new repository:**
1. .gitignore
2. licence
3. readme

**Create a new environment for the project:**

```
conda create -p environment_name python==3.7 -y
```

**Activate the environment:**

```
conda activate environment_path/
```

**Create the requirements.txt file and install them**

```
pip install -r requirements.txt
```

**Configure Git username and email:**

```
git config --global user.name "user-name"
```

```
git config --global user.email "user-emailid"
```

**Adding files to push to github:**

```
git status : to see the status
```

```
git add file_name

git add . : to add everything except the ones in gitignore
```

**Committing the local files to the github repo:**

```
git commit -m "Commit message" :creates a snapshot in the local directory
```

**Pushing to the repo:**
```
git push origin main : from current env to main branch
```

**Create the home.html file for the webapp**

**Create the app using Flask with various funcitonalities defined**

**Use Postman to verify the API request**

**Create the docker file**

**setup github actions**

1. .github folder
2. workflows subfolder
3. main.yaml file
4. add the secret keys in github repo








