1.	Setup GitHub repository of the ml/dl project for other developers to collaborate simultaneously.

2.	Create folder of the project in local system & create virtual environment and activate

virtualenv venv
venv\Scripts\activate

3.	Clone github repository & sync with github to commit all our code using below codes in command line:

git init  initialize an empty repo on git
git add README.md  create a description file in local system & add in git repo
git commit -m "first commit"  commit the README.md file
git branch -M main  change branch to main before pushing what you’ve commited
git remote add origin https://github.com/iamprashantjain/ml-ops_laptop-price-predictor.git --> add the address of the repo where its needed to be pushed
git push -u origin main  push the changes to git

4. 

