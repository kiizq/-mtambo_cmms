# -mtambo_cmms
our portifolio project
M-TAMBO MAINTENANCE TRACKING AND DOCUMENTATION SOFTWARE
NB: Mtambo is a kiswahili word that refers to a mechanical system

Background
With the rapid growth of high-rise developments across Africa, the need for efficient management of critical building systems like HVAC, elevators, and power backup is increasing. Developers and maintenance companies require a simple CMMS to track and maintain these systems effectively. A tailored CMMS would help streamline maintenance operations.

Targeted users:
The CMMS will basically have 3 user groups:

Developers/Building owners
These the building owners, they can either be individual owners who own just own one building or large development companies who own multiple buildings.
The system will help this group of users to do the following:
Track all the 3 systems in all their facilities(buildings)
Monitor all the maintenance companies associated with the 3 systems
Real time tracking of the maintenance schedule of all systems in all their facilities
Be able to download the electronic maintenance log of any equipment as soon as its logged into the system by the relevant technician
Should be able to view the maintenance calendar of every single piece of equipment within any of his facilities
Should be able to view all the Maintenance companies associated with any of the 3 systems within any of his facilities.
Be able to automatically generate the maintenance history of any piece of equipment. 
 
Maintenance companies
In Kenya and across Africa, most of the maintenance companies for these 3 systems are small companies. With their core business being offering of maintenance operations, this CMMS will help this group of users to achieve the following:
Maintain an integrated calendar of all their maintenance jobs
Track all their technicians and their assigned jobs
View a list of all the buildings(facilities) where they have been contracted
Track all the maintenance jobs done by each of their technicians within a specified period
View a list of all their technicians
Generate and download the electronic maintenance logs for purposes of invoicing  
Technicians.
Technicians are the qualified individuals that every maintenance company uses to run their maintenance operations.
The CMMS should be able to help them to do the following:
Maintain a maintenance calendar on which buildings they should be attending to at any particular date
Generate electronic logs by just feeding the required data into the system
  

SYSTEM DESIGN

DASHBOARD
Given the requirements and the three distinct user groups, the system should have three primary dashboards, each tailored to the specific needs of the different users:
Developer/Building Owner Dashboard:
Track and monitor all systems (HVAC, elevators, power backup) across multiple facilities.
View maintenance schedules, history, and calendars.
Access and download electronic maintenance logs.
Monitor associated maintenance companies and technicians.
Maintenance Company Dashboard:
Manage and track all maintenance jobs and associated technicians.
View contracted buildings and their maintenance status.
Maintain an integrated maintenance calendar.
Generate and download electronic maintenance logs for invoicing.
Technician Dashboard:
Access personal maintenance calendar and job assignments.
Log maintenance activities into the system.
Generate electronic maintenance logs with relevant data entry.
These three dashboards will ensure that each user group can efficiently manage their specific tasks while maintaining an integrated approach to building system maintenance.
1. Developer/Building Owner Dashboard
Purpose: To provide building owners and developers with comprehensive tools for tracking and managing their buildings, equipment, and maintenance activities.
Dashboard Layout:
Header:
Logo: Company or system logo.
Profile Icon: Dropdown for user settings, account management, and logout.
Navigation Menu:
Home: Return to the main dashboard view.
Buildings: Access a list of all buildings.
Equipment: View and manage equipment across buildings.
Maintenance Companies: View and manage associated maintenance companies.
Maintenance History: Access historical maintenance records.
Calendar: View a calendar of upcoming maintenance activities.
Reports: Generate and view various reports (e.g., maintenance summaries, equipment status).
Main Dashboard Area:
Overview Widgets:
Total Buildings: Display the number of buildings.
Total Equipment: Display the number of equipment units.
Upcoming Maintenance: Quick view of upcoming maintenance tasks.
Recent Activity: Display recent maintenance activities or updates.
Buttons and Features:
Add Building: Button to open a form for registering new buildings.
Add Equipment: Button to register new equipment in a building.
View Building Details: Button to view detailed information about a selected building.
View Equipment Details: Button to view detailed information about a selected piece of equipment.
Download Logs: Button to download maintenance logs for specific equipment.
View Maintenance Schedule: Button to access and view detailed maintenance schedules.
Generate Report: Button to create reports on maintenance history, equipment status, etc.
Contact Support: Button for help or support queries.
Settings: Button to access user settings and preferences.
2. Maintenance Company Dashboard
Purpose: To help maintenance companies manage their maintenance jobs, technicians, and client buildings efficiently.
Dashboard Layout:
Header:
Logo: Company or system logo.
Profile Icon: Dropdown for user settings, account management, and logout.
Navigation Menu:
Home: Return to the main dashboard view.
Jobs: View and manage maintenance jobs.
Technicians: Manage technician details and assignments.
Buildings: View buildings they are contracted to maintain.
Calendar: Access a calendar of scheduled maintenance tasks.
Reports: Generate reports on technician performance, job status, etc.
Main Dashboard Area:
Overview Widgets:
Total Jobs: Display the number of active and completed jobs.
Technician Status: Overview of technician availability and workload.
Upcoming Jobs: Quick view of upcoming maintenance jobs.
Recent Activity: Display recent job updates or technician activities.
Buttons and Features:
Add Job: Button to create a new maintenance job.
View Job Details: Button to view detailed information about a selected job.
Assign Technician: Button to assign a technician to a maintenance job.
Add Technician: Button to register new technicians.
View Technician Details: Button to view details of a selected technician.
View Building List: Button to see the list of all buildings the company is contracted with.
Generate Report: Button to create reports on job status, technician performance, etc.
Download Logs: Button to download electronic maintenance logs for invoicing.
Contact Support: Button for help or support queries.
Settings: Button to access user settings and preferences.
3. Technician Dashboard
Purpose: To allow technicians to manage their job assignments, view schedules, and log maintenance activities efficiently.
Dashboard Layout:
Header:
Logo: Company or system logo.
Profile Icon: Dropdown for user settings, account management, and logout.
Navigation Menu:
Home: Return to the main dashboard view.
My Jobs: View and manage assigned jobs.
Calendar: Access a calendar with job assignments and schedules.
Logs: View and manage maintenance logs.
Support: Access support and help resources.
Main Dashboard Area:
Overview Widgets:
Upcoming Jobs: Display a list of upcoming job assignments.
Job Status: Overview of job statuses (e.g., pending, in progress, completed).
Recent Logs: Display recent maintenance logs or activities.
Buttons and Features:
View Job Details: Button to view details of a selected job.
Log Maintenance Activity: Button to enter and submit maintenance activities for a job.
Update Job Status: Button to update the status of a job (e.g., from "In Progress" to "Completed").
View Calendar: Button to access the calendar view of job assignments.
Generate Log Report: Button to generate and download maintenance logs.
Contact Support: Button for help or support queries.
Settings: Button to access user settings and preferences.
SIGN-UP
1. Developer/Building Owner Sign-Up Page
Purpose: To create accounts for individual building owners or large development companies.
Fields:
Company Name/Individual Name: The name of the company or individual.
Contact Person: The primary contact person’s name.
Email Address: For account creation and notifications.
Phone Number: For contact and verification purposes.
Password: To secure the account.
Confirm Password: To ensure the password was entered correctly.
Address: Optional but useful for physical location verification.
Facilities Information: Optional initial field to enter details about buildings or facilities they own. This can be filled out later if preferred.
Design Notes:
A dropdown or radio button to select whether the user is an individual owner or a development company.
Provide a brief explanation of what they can expect after signing up (e.g., verification process, next steps).
2. Maintenance Company Sign-Up Page
Purpose: To register maintenance companies and their details.
Fields:
Company Name: The name of the maintenance company.
Contact Person: Name of the primary contact person at the company.
Email Address: For communication and account-related updates.
Phone Number: Contact number for verification and communication.
Password: To secure the account.
Confirm Password: To ensure password accuracy.
Equipment the company specializes in: A drop down menu to select whether the company deals in HVAC,Elevators or Power back-up generators
Company Address: Physical address of the company.
Service Areas: Optional field to specify geographical areas covered.
Company Registration Number: For verification purposes, if applicable.(I think we can make this optional though)
Design Notes:
Provide information on the verification process and how it will affect their ability to access certain features.
3. Technician Sign-Up Page
Purpose: To register individual technicians who will be performing maintenance tasks.
Fields:
Full Name: The technician’s full name.
Email Address: For account creation and updates.
Phone Number: For direct communication and verification.
Password: To secure their account.
Confirm Password: To ensure the password was entered correctly.
Company Affiliation: A dropdown or input field to select or enter the company they work for.
Specializations: Optional field to indicate their areas of expertise or certification levels.
Design Notes:
Since technicians are affiliated with maintenance companies, ensure there is a field to select their associated company from a dropdown list populated by the maintenance companies already registered.




DATABASE
Database Design Overview
Entities and Their Relationships
Developers/Building Owners
Maintenance Companies
Technicians
Buildings
Equipment
Maintenance Jobs
Maintenance Logs
Core Tables and Relationships
1. Developers/Building Owners Table
Table Name: BuildingOwners
Primary Key: OwnerID (Unique Identifier)
Fields:
OwnerID (INT, PK)
Name (VARCHAR)
Email (VARCHAR, Unique)
PhoneNumber (VARCHAR, Unique)
Address (VARCHAR)
PasswordHash (VARCHAR) — Securely store hashed passwords
CreatedAt (DATETIME)
UpdatedAt (DATETIME)
2. Maintenance Companies Table
Table Name: MaintenanceCompanies
Primary Key: CompanyID (Unique Identifier)
Fields:
CompanyID (INT, PK)
Name (VARCHAR)
ContactPerson (VARCHAR)
Email (VARCHAR, Unique)
PhoneNumber (VARCHAR, Unique)
Address (VARCHAR)
RegistrationNumber (VARCHAR, Unique)
PasswordHash (VARCHAR) — Securely store hashed passwords
CreatedAt (DATETIME)
UpdatedAt (DATETIME)
3. Technicians Table
Table Name: Technicians
Primary Key: TechnicianID (Unique Identifier)
Fields:
TechnicianID (INT, PK)
Name (VARCHAR)
Email (VARCHAR, Unique)
PhoneNumber (VARCHAR, Unique)
CompanyID (INT, FK) — Foreign Key referencing MaintenanceCompanies.CompanyID
Specializations (VARCHAR) — Areas of expertise
PasswordHash (VARCHAR) — Securely store hashed passwords
CreatedAt (DATETIME)
UpdatedAt (DATETIME)
4. Buildings Table
Table Name: Buildings
Primary Key: BuildingID (Unique Identifier)
Fields:
BuildingID (INT, PK)
Name (VARCHAR)
Address (VARCHAR)
OwnerID (INT, FK) — Foreign Key referencing BuildingOwners.OwnerID
BuildingType (VARCHAR) — Type of the building (e.g., residential, commercial)
CreatedAt (DATETIME)
UpdatedAt (DATETIME)
5. Equipment Table
Table Name: Equipment
Primary Key: EquipmentID (Unique Identifier)
Fields:
EquipmentID (INT, PK)
Name (VARCHAR)
SerialNumber (VARCHAR, Unique)
InstallationDate (DATE)
BuildingID (INT, FK) — Foreign Key referencing Buildings.BuildingID
EquipmentType (VARCHAR) — Type of equipment (e.g., HVAC, elevator)
CreatedAt (DATETIME)
UpdatedAt (DATETIME)
6. Maintenance Jobs Table
Table Name: MaintenanceJobs
Primary Key: JobID (Unique Identifier)
Fields:
JobID (INT, PK)
EquipmentID (INT, FK) — Foreign Key referencing Equipment.EquipmentID
TechnicianID (INT, FK) — Foreign Key referencing Technicians.TechnicianID
ScheduledDate (DATETIME)
CompletionDate (DATETIME, Nullable)
Status (VARCHAR) — Status of the job (e.g., scheduled, in-progress, completed)
Description (TEXT)
CreatedAt (DATETIME)
UpdatedAt (DATETIME)
7. Maintenance Logs Table
Table Name: MaintenanceLogs
Primary Key: LogID (Unique Identifier)
Fields:
LogID (INT, PK)
JobID (INT, FK) — Foreign Key referencing MaintenanceJobs.JobID
TechnicianID (INT, FK) — Foreign Key referencing Technicians.TechnicianID
LogDate (DATETIME)
Details (TEXT)
CreatedAt (DATETIME)
UpdatedAt (DATETIME)
Relationships and Constraints
One-to-Many Relationships:
BuildingOwners to Buildings: A building owner can own multiple buildings. (OwnerID in Buildings table is a Foreign Key to BuildingOwners)
MaintenanceCompanies to Technicians: A maintenance company can have multiple technicians. (CompanyID in Technicians table is a Foreign Key to MaintenanceCompanies)
Buildings to Equipment: A building can have multiple pieces of equipment. (BuildingID in Equipment table is a Foreign Key to Buildings)
Equipment to MaintenanceJobs: Each piece of equipment can have multiple maintenance jobs. (EquipmentID in MaintenanceJobs table is a Foreign Key to Equipment)
Technicians to MaintenanceJobs: A technician can handle multiple jobs. (TechnicianID in MaintenanceJobs table is a Foreign Key to Technicians)
MaintenanceJobs to MaintenanceLogs: Each maintenance job can have multiple logs. (JobID in MaintenanceLogs table is a Foreign Key to MaintenanceJobs)
Indexing and Optimization
Indexes:
Create indexes on foreign keys to improve join performance (e.g., OwnerID, CompanyID, BuildingID, EquipmentID, TechnicianID, JobID).
Index commonly queried fields such as Email in the BuildingOwners, MaintenanceCompanies, and Technicians tables.
Normalization:
Ensure the database schema is normalized to reduce redundancy and improve data integrity.
Use normalization techniques up to the third normal form (3NF) to organize data efficiently.
Security Considerations:
Store passwords using secure hashing algorithms (e.g., bcrypt, Argon2).
Implement access control measures to ensure that users can only access and modify data they are authorized to handle.

Database Schema Diagram
A simplified entity-relationship diagram for the database design:
BuildingOwners
| OwnerID | Name | Email | PhoneNumber | Address | PasswordHash | CreatedAt | UpdatedAt |

MaintenanceCompanies
| CompanyID | Name | ContactPerson | Email | PhoneNumber | Address | RegistrationNumber | PasswordHash | CreatedAt | UpdatedAt |

Technicians
| TechnicianID | Name | Email | PhoneNumber | CompanyID | Specializations | PasswordHash | CreatedAt | UpdatedAt |

Buildings
| BuildingID | Name | Address | OwnerID | BuildingType | CreatedAt | UpdatedAt |

Equipment
| EquipmentID | Name | SerialNumber | InstallationDate | BuildingID | EquipmentType | CreatedAt | UpdatedAt |

MaintenanceJobs
| JobID | EquipmentID | TechnicianID | ScheduledDate | CompletionDate | Status | Description | CreatedAt | UpdatedAt |

MaintenanceLogs
| LogID | JobID | TechnicianID | LogDate | Details | CreatedAt | UpdatedAt |

10 Day Plan to deliver the MTAMBO CMMS project
Day 1: Project Setup and Initial Configuration
Set Up the Development Environment:
Install Django and other necessary packages.
Create a new Django project and apps for users, maintenance, and equipment.
Initialize Version Control:
Set up a Git repository for the project.
Create a .gitignore file and requirements.txt for dependencies.
Basic Django Configuration:
Configure settings.py with database settings and installed apps.
Day 2: UI/UX Design
Kelvin:
Create Wireframes and Mockups:
Design wireframes and mockups for all user dashboards (Building Owners, Maintenance Companies, Technicians) using tools like Figma or Adobe XD.
Design User Interface Elements:
Design components such as navigation bars, buttons, and forms that will be used in the dashboards.
Winston:
Define Models for Users and Authentication:
Create CustomUser model and custom user manager in users/models.py.
Implement user authentication features.
Define Models for Maintenance Companies, Technicians, and Jobs:
Implement MaintenanceCompany, Technician, MaintenanceJob, and MaintenanceLog models in maintenance/models.py.
Day 3: UI/UX Design and Model Implementation
Kelvin:
Develop Static HTML/CSS Templates:
Create static versions of the dashboard pages based on wireframes (without dynamic data).
Winston:
Define Models for Equipment and Buildings:
Implement Building and Equipment models in equipment/models.py.
Create and Apply Migrations:
Generate and apply migrations to create the database schema.
Day 4: Backend Development
Kelvin:
Continue Developing Static Templates:
Refine and finalize static templates for different user roles.
Winston:
Create User Authentication Views:
Implement login, logout, and registration views in users/views.py.
Set Up User Permissions and Access Control:
Define permissions and groups in users/models.py.
Day 5: Backend Development and UI Integration
Kelvin:
Begin Integrating Templates with Django Views:
Start integrating static templates with Django views for Building Owners.
Winston:
Configure URLs for Authentication:
Set up URL routing for authentication views in users/urls.py.
Create User Registration and Login Forms:
Implement forms for user registration and login in users/forms.py.
Day 6: Backend Development
Kelvin:
Continue UI Integration:
Integrate static templates with Django views for Maintenance Companies.
Winston:
Create Views for Building Owners:
Implement dashboard and management views for building owners in maintenance/views.py.
Create Forms for Building Management:
Create forms for adding and editing buildings and equipment.
Day 7: Backend Development and UI Integration
Kelvin:
Complete UI Integration for Technicians:
Integrate static templates with Django views for Technicians.
Winston:
Create Views for Maintenance Companies:
Implement dashboard and management views for maintenance companies in maintenance/views.py.
Create Forms for Maintenance Management:
Create forms for managing maintenance jobs, technicians, and logs.
Day 8: Advanced Features and Testing
Kelvin:
Finalize UI/UX Design:
Make final adjustments to the user interface and user experience based on feedback.
Winston:
Add Calendar Integration:
Implement features to display and manage maintenance schedules using Django packages or custom code.
Enable File Uploads and Downloads:
Implement functionality for uploading and downloading maintenance logs.
Day 9: Testing and Documentation
Kelvin:
Assist with Testing and Debugging:
Collaborate on testing the UI and fixing any frontend issues.
Winston:
Write Unit Tests:
Develop unit tests for models, views, and forms using Django’s testing framework.
Conduct Manual Testing:
Test all functionalities manually to identify and fix bugs.
Review and Refactor Code:
Refactor code to improve readability and maintainability based on testing feedback.
Day 10: Deployment and Handoff
Kelvin:
Assist with Deployment Preparation:
Help with deployment tasks, including preparing final UI elements for production.
Winston:
Deploy the Application:
Deploy the Django application to a production server using a web server like Gunicorn and Nginx.
Conduct Final Testing in Production:
Perform final testing to ensure the application works correctly in the production environment.
Handoff and Training:
Provide the final deliverable to the client, including training if necessary.
Update Documentation and Version Control:
Update documentation and ensure all code is committed to version control.
