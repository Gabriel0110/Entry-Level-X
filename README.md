# Entry-Level-X
-WORK IN PROGRESS-

A Django web development project to aggregate entry-level jobs making it easier for people to find them with a one-stop shop rather than digging around on LinkedIn, Indeed, etc. seeing jobs that aren't entry-level but are still incorrectly listed as such.  This is a personal hassle for myself and others, and it's a solvable problem if companies put in the effort.

The idea for this project was from my friend Christian Iannone and myself as we both struggle with finding legitimately entry-level jobs in tech.  I'm currently learning Django on my own, and I thought this was a great project to learn via hands-on experience.

The jobs are aggregated from public job aggregation APIs (Indeed, TheMuse, GitHub Jobs, etc).  It has currently been tested with jobs pulled from TheMuse via their API.  The Python scripts located in the 'utility_scripts' folder make the API calls, load the jobs into a CSV file for review and approval, and push them into the SQLite database linked to the Django server.

Until better filtering algorithms and methods are instrumented to sort out the non-entry-level jobs, it is essential to have a human-in-the-loop step in the process to review the jobs pulled by the APIs to ensure jobs being pushed to the database are legitimately "entry-level."  One of the hardest problems with this project so far, and likely in the continued future, is the filtering aspect.  I would argue that precise and accurate filtering is one of the most crucial pieces to this project, and I would be hesitant to launch with anything greater than a 3-5% false positive rate.  Otherwise, this project is just another aggregation site that fails to solve the same problem that others have.

Next Steps in Development:
- Design better filtering of jobs pulled from the APIs to reduce false positives before pushing into database
- Design a better search function to eliminate false positives for searching (unrelated jobs being populated because a search term was found in the description, etc)
- Add actual URLs to the "Apply on Company Site" button that point to the actual job posting on the company sites
- Implement checking for duplicate pulls from the APIs and prevent duplicate job postings being pushed to the database
- More appealing UI
- Account registration to allow for saving/favoriting job postings
  

Home Page  
![](/image1.PNG)  

Job Detail Page  
![](/image2.PNG)  

Search Result Example  
![](/image3.PNG)