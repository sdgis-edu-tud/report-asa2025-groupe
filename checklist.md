The following checklist can be used to assess the level of reproducibility of your project.

## Documentation
- [x] Is there a README file that indicates
  - [x] the purpose of the project, 
  - [x] who to contact with questions, 
  - [x] a map of the directory structure, and 
  - [x] a description of what software and hardware is needed to reproduce your workflow?
- [ ] Are there README files in each folder describing the contents of the folder, how they were acquired/generated? -> No, seems excessive.
- [x] Is there a CITATION file that tells users how to site the project, data, and code?
- [x] Does the project have a LICENSE file?
- [ ] Is the project's repository publicly available? -> No, can/should we change that?

## Data
- [x] Is the data included or linked, with instructions on how to obtain the data?
- [ ] If data is not included, is this because it is not necessary or generated as part of the project? -> N/A
- [ ] Are your raw data (if any) and processed data files separated? -> No raw data files, we directly use WFS endpoint data
- [ ] If data is not open: -> N/A
  - [ ] Is it accessible via a protocol? -> N/A
  - [ ] Is there synthetic data provided so the project can be run? -> N/A
- [ ] Is citation information available for the data? -> Yes, on the 4TU Research Data site, link to be received.
- [x] Does the data use open formats, such as CSV and TXT? -> Yes, both GPKG and GeoJSON

## Software
- [x] Is there a list of dependencies? 
- [ ] Is a container available to run the project? -> N/A, .rproj/.qmd doesn't require Dockers/Containers
- [ ] Are version number of every external application used in the process? -> N/A
- [x] Does your project use only open software?

## Workflow and automation
- [x] Is the workflow clearly documented (with or without code)?
- [x] Is your workflow scripted, i.e., using code? 
- [x] Is your code well documented?
- [x] Is your code modular, i.e., does it use functions?
- [ ] Are unit tests available for the code? -> No, seems excessive.
- [ ] Does your repository make use of continuous integration tools to insure internal reproduciblity? -> No, seems excessive.

## Organization
- [x] Are all data, code, results, and documentation housed within a monophyletic folder structure?
- [ ] Is your project folder structured to separate your data, code, documentation, and results? -> N/A
- [x] Can the project be run from the project's root folder?
- [x] Is the project under version control?
- [x] Do files use a consistent naming scheme that indicates what they contain? -> More or less, also explained in README/ Report.

## Publication
- [x] Are papers and reports from the project generated using literate programming tools so that results are not hard-coded?
- [ ] Does the project have a persistent identifier? -> ? 

This list was inspired by the more extensive [Checklist Questions to stimulate thought about a Project's Reproducibility](https://github.com/datacarpentry/rr-intro/blob/gh-pages/checklist.md) 
which we recommend you consider for making your work reproducible.
