![[Pasted image 20231105142119.png]]

Requirements engineering is an iterative process, with two main aspects:
1. User requirements
2. System requirements

![[Pasted image 20231105142944.png]]
# Requirements Specification
Documenting the understanding of people’s needs
-  The “instructions” to the development team
-  The “acceptance criteria” for the final software/system
-  Into a document called Requirement Specification (one or more)
	-  Shared, agreed description for everyone

Is used to evaluate the final system
![[Pasted image 20231105143217.png]]
## User Requirements
Describes what the user does with the system, often referred to as the **user needs**.

What activities the user might be able to perform
The services that the system should provide and the constrains under which it must operate
***Should be understandable by users who don’t have technical knowledge*** -> avoid details

Primary input for creating:
## System Requirements
A more detailed description of the ***system services*** and ***operational constraints*** such as how it will be used, and developmental constraints such as programming languages.

They add detail and explain how the user requirements should be provided by the system. ***They shouldn’t be concerned with how the system should be implemented or designed.***

| User Requirements   | System Requirements |
| ------------------- | ------------------- |
| Client managers     | System end users                    |
| System End users    | Client engineers                    |
| Client engineers    | System architects                    |
| Contractor managers | Software developers                    |
| System architects                    |                     |

***User requirements:*** The user is the subject and the program is an object
***System requirements:*** The program being developed is a subject

e.g.
> The *user* **should** get monthly management reports showing the cost of drugs prescribed by each clinic during that month. (User requirements)
> The *system* **shall** automatically generate the report for printing after 17.30 on the last working day of the month (System requirements)

`Note:` The subject (italicised) of each point
`     ` Neither concerns implementation

## Functional VS Non-functional
### Functional
A ***functional requirement*** specifies a function that a system (or its component) must be capable of performing that can support the user to perform their work (e.g., visibility)
*a system may be required to enter and print cost estimates*
### Non-functional
A ***non-functional requirement*** specify all the remaining requirements not covered by the functional requirements i.e., not what the software will do, but how the software will do it.
*Quality requirements: Accessibility, concurrency, performance efficiency, price, privacy, interoperability, usability, security, etc*
# What Makes Good Requirements
1. **Verifiable** *(it can be tested)*
2. **Clear** *(easy to read and understand by non-technical people)**
	1. Leaves no one guessing (e.g., for how long? Central point?)
3. **Concise** *(no more than 30-50 words in length)*
4. **Coherent** *(logical and consistent)* 
5. **Unambiguous** *(can't be interpreted in multiple ways)*
	1. Avoid vague words (e.g., some)
6. **Implementation-free** *(must not contain software or technology design decisions)*
	1. DO NOT describe the user interface in words
7. **Traceable** *(unique identity or number)*
	1. Cannot be broken into smaller requirements
	2. Can easily be traced
# Prioritisation
## MoSCoW

![[Pasted image 20231105145800.png]]
