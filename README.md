# CS109 Group Project Fall 2016 

## ***Predicting Rossmann Sales***

#### Where to find things:

If you are a student and want to see our project summary visit [Predict Rossmann Sales](https://weiyialanchen.github.io/rossman_sales_analysis/)

If you want to learn how the site was built, visit [GitHub using gh-pages](https://pages.github.com/), we use automate page generator to create a static page.

#### Project Dependencies and non-standard libraries

##### Visualization

Tableau/Matplotlib was used to prepare some of the visualizations. The results were then imported into iPython via embedding into `%%html` cells.

##### Libraries Used
We use a number of different libraries besides the typical ones from class (pandas, numpy, sklearn, statsmodels)

Xgboost was used for main models/experiments with parallel programming.

## ***File Organizations***

- /data/: used to contain Kaggle raw data, removed due to memory usage
- /docs/: website contents
- /images/: images generated from IPython Notebook and used in website
- /kaggle_submission/: predictions of Kaggle test data
- /scripts/: utility functions
- /styles/: website style
- EDA.ipynb and EDA_summary.doc: Milestone 3, exporatory data analysis
- Model_summary.doc and model.ipynb: Milestone 4 and 5, baseline models and future works

## ***Git Notes***

In the CS109, we have using `git` in a non-traditional role. 
Usually branches live only to deliver some well defined piece of
functionality and then are merged back into the master branch.

Since we will be working concurrently on multiple parts of this 
project, `git` will be very useful tool to ensure that we can 
work in parallel, even on the same code, without interference.

Here are some notes to get you started. 

#### Copy this repository to your machine

`git clone git@github.com:weiyialanchen/rossmann_sales_analysis.git`

### Creating a branch 

This will create a new branch in the code. You can do anything you
want in this branch and it will not affect anything in master, 
until a merge is done (see below).

```
cd rossmann_sales_analysis
git checkout -b newbranch
git push origin newbranch
git push --set-upstream origin newbranch
```
The `push origin` is needed to send the branch to github, which you
will need to do before pushing the branch so everyone else can see
it.

From this point do whatever edits you want. Create a subdirectory,
add files, make changes.

### Commit early and regularly

Do not leave your code unbackedup on your machine. I commit every
time I add something new and useful that works. It could be as little
as 2-3 lines of code. 

This is the same as in class, although now you will be committing just
to your branch.

Assuming you are in the cs109-groupproj-college directory

```
git add .
git commit -m "<one line summary of what changed>"
git push
```

### See what others have done

To grab a fresh local copy of everything in the github repository, use
`git fetch`. Any new branches anyone else has created will be moved
down.

To switch to their branch, while leaving yours untouched use 
`git checkout otherbranch`. To get back to your branch `git checkout mybranch`.

### Merging - Step 1

The first step in merging is to merge the latest master branch into
your branch

```
git fetch
git merge origin/master
```
If there are any conflicts, like two people having written to the same
file in the same place, it will let you know. It is pretty smart
about merging different pieces of code or file that do not impact each
other. This is one of git's most amazing features.

After you have reconciled any merge conflicts, you can commit
the merged master into your branch, which are the same commands as 
before

```
git add .  
git commit -m "I merged in master"  
git push  
```
Now your branch has all of master and all of your new stuff

### Merging - Step 2

Now that you are fully up to date in your branch, you can update master:

```
git checkout master  
git merge newbranch    
git status    
git push  
```
Now your code has been integrated into master. Your work is done.

Create a new branch to start on another unit of work (or keep 
working on the same branch if it isn't done yet).

It is a good idea to not wait too long to merge into master. Once it is
in a stable state, ready to use by others if not feature complete, do
the merge into master.

### When Two People Work on the Same Branch

If two of you are working on the same branch (which I don't 
particularly advise), you have to do a few extra steps to
keep each other in sync. Otherwise one of you will make a 
change, push the change, while another person makes a change.
Then git complains about not being able to reconcile the two
changes and the commits are out of sync.

So before pushing your code, merge in the latest copy of the
origin branch from github:

```
git fetch
git merge origin/mybranch
```
If there are no conflicts, you can proceed. Otherwise, you have
to manually fix the conflicts first.

Then, as before:

```
git add .
git commit -m "added cool gizmo 45"
git push
```

Bottom line: fetch and merge from the origin branch before making
your commits and pushes.

### That's It

`git` has many powerful features like pull requests and code reviews,
but I don't think we need them for this project.

