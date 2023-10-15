## #Contents 

[[Git]]
## What is version control?
Version control is a system designed to allow multiple people to work concurrently on the same project.

`NOTE:` Revision control systems are useful even when only one developer is working on a project: when, for example, she uses multiple computers to contribute to the project, or when she wants to be able to roll back changes made to the project etc.

> When several people work on the same project concurrently, they need to somehow coordinate their joint efforts, as well as organise and control revisions they make to the shared code in a methodical and logical way. This is what revision control (or version control) systems are for1. There are several conceptual models for organising concurrent development of code. Here, we will consider the simplest one, the centralised model:
 [[CM1101_Lab_Exercise5.pdf]]
![[Pasted image 20231012145621.png]]

**Repository:** *The centralised copy of the code stored on the server, considered the main version*
**Working copy** *The version of the code that is stored on the programmers computer*

When a developer makes a change to their working copy the ***commit[^1]*** them to the central repo, making it available to the other developers. Similarly developers can retrieve the changes from the centralised system. One ***updates*** their code from the central repo.

[^1]: In Git, as opposed to, say, SVN, each developer also has a full local copy of the repository. Performing a commit in Git means committing changes to the local repository; to make the changes available to other developers, they need to be pushed to a remote (central) repository.

The job of the version control system is to keep track of all the changes that have been made, currently getting made, and will be made.