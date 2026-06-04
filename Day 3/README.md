# Git Commands Cheatsheet

```git version```   
```
Displays the version of git that has been installed
```
```git config --global user.name "Name"```
```
Sets your identity (Git username) for all your commits
```
```git config --global user.email "Mail"```
```
Sets your email address (has to match your GitHub)
```
```git init```
```
Initialises a new GitHub repository in the current folder
```
```git clone <url>```
```
Downloads an existing repository from a remote server (e.g. GitHub) to your local machine
```
```git status```
```
Shows the current state of the repository, including untracked, modified or staged files
```
```git add <file>```
```
Adds a specific file to the staging area for the next commit
```
```git add.```
```
Adds all the files in the current directory to the staging area
```
```git rm <file>```
```
Deletes a file from the working directory and repository
```
```git commit -m "Message"```
```
Creates a commit with a message 
```
```git commit -am "Message"```
```
One command to perform git add. and git commit -m "Message" for tracked files
```
```git branch```
```
Lists all the local branches in the repository
```
```git branch <name>```
```
Creates a new branch
```
```git checkout <name>```
```
Switches to the specified existing branch 
```
```git checkout -b <name>```
```
Creates a new branch and switches to it 
```
```git merge <branch>```
```
Merges the specified branch into the current branch
```
```git pull```
```
Downloads and merges the latest changes (Fetch and Merge)
```
```git push -u origin <branch>```
```
Uploads commits to a remote branch
```
```git log```
```
Shows the full history of commits
```
```git remote -v```
```
Displays all the remote repositories conected to your local repository
```
```git remote add origin <url>```
```
Connects your local repository to a remote repository
```
```git remote remove <name>```
```
Removes a remote repository connection
```

