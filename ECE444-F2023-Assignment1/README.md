Harry Jiawei Hu

Activity 1 (screenshots showing the commit of README.md):
![Alt text](image.png)
![Alt text](image-1.png)

Activity 2 (screenshot showing the output of the merge command on main branch):
![Alt text](image-2.png)

Activity 3 (screenshot showing the successful merge between Main and Develop with prior conflicts - now resolved):
![Alt text](image-3.png)

Activity 4 (screenshot showing the commits of two python files containing class, functions and tests):
![Alt text](image-4.png)

Activity 5 (screenshot showing the commands (along with outputs) used for rebase from 'develop' branch onto 'rebase' branch):
![Alt text](image-5.png)
Shows the initial order of commits after rebasing the develop branch with the rebase branch
The results were c1->c2->c3->c4

Since the instructions wanted c4->c3->c2->c1, reordering was done using the interactive editor
![Alt text](image-6.png)
The outcome after reordering commits via git rebase -i HEAD~4 on VScode: 
![Alt text](image-7.png)