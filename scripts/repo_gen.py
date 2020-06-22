import os
import csv
import yaml

PROJECTS_FILE = "projects2020.csv"
PROJECTS_FOLDER = "projects"
PROJECT_YAML = "projects.yml"
PROJECTS_REPOSITORY = "https://github.com/elixir-europe/BioHackathon-projects-2020/tree/master/projects/{number}"

# ACEPTED PROJECTS COLUMN NAMES
ACPT_PROJECT_NUMBER = "number"
ACPT_PROJECT_MERGED = "merged_from"
ACPT_PROJECT_TITLE = "title"
ACPT_PROJECT_SUBMITTER = "submitter"

# EASY CHAIR DUMP PROJECT COLUMNS
PROJECT_NUMBER = "#"
PROJECT_AUTHORS = "Authors"
PROJECT_TITLE = "Title"
PROJECT_ABSTRACT = "Abstract"

PROJECT_LEADS = "Leads for Project"
PROJECT_NOMINATED_PARTICIPANT = "Nominated participant"
PROJECT_EXPECTED_OUTCOMES = "Expected outcomes"
PROJECT_EXPECTED_AUDIENCE = "Expected participants"
PROJECT_NUMBER_OF_EXPECTED_HACKING_DAYS = "Number of days for project"
PROJECT_HACKING_TOPIC = "Topics"
PROJECT_DECISION = "Decision"

PROJECT_PAPER = "paper"


def load_all_projects():
    projects = []

    with open(PROJECTS_FILE) as pro_file:
        reader = csv.DictReader(pro_file, delimiter=',')
        line_count = 0
        for row in reader:

            if line_count == 0:
                print(f'Projects column names are {", ".join(row)}')

            project_link = PROJECTS_REPOSITORY.format(
                number=row.get(PROJECT_NUMBER))

            project = dict(
                number=row.get(PROJECT_NUMBER),
                authors=row.get(PROJECT_AUTHORS),                
                title=row.get(PROJECT_TITLE),
                leads=row.get(PROJECT_LEADS),
                expected_outcomes=row.get(PROJECT_EXPECTED_OUTCOMES),
                expected_audience=row.get(PROJECT_EXPECTED_AUDIENCE),        
                nominated_participant=row.get(PROJECT_NOMINATED_PARTICIPANT),
                number_of_expected_hacking_days=row.get(
                    PROJECT_NUMBER_OF_EXPECTED_HACKING_DAYS),                
                hacking_topic=row.get(PROJECT_HACKING_TOPIC),
                decision=row.get(PROJECT_DECISION),
                abstract=row.get(PROJECT_ABSTRACT),
                link=project_link
            )
            if row.get(PROJECT_DECISION) == "Accepted":
                projects.append(project)
            
            line_count += 1

    return projects


def to_file(project):

    path = "{}/{}".format(PROJECTS_FOLDER, project.get("number"))
    os.makedirs(path)

    file_name = "{}/{}/README.md".format(PROJECTS_FOLDER,
                                         project.get("number"))
    print("Creating file {}".format(file_name))

    with open(file_name, "w+") as output_file:
        output_file.write("# {}\n\n".format(project.get("title")))

        output_file.write("## Abstract\n\n")
        output_file.write(project.get("abstract"))

        output_file.write("\n\n## Topics\n\n")
        output_file.write(project.get("hacking_topic"))

        output_file.write(
            "\n\n**Project Number:** {}\n\n".format(project.get("number")))

        output_file.write("## Team\n\n")

        output_file.write("### Lead(s)\n\n")
        output_file.write(project.get("leads"))

        output_file.write("\n\n### Nominated participant(s)\n\n")
        output_file.write(project.get("nominated_participant"))

        output_file.write("\n\n## Expected outcomes\n\n")
        output_file.write(project.get("expected_outcomes"))

        output_file.write("\n\n## Expected audience\n\n")
        output_file.write(project.get("expected_audience"))

        output_file.write(
            "\n\n**Number of expected hacking days**: {}\n\n".format(project.get("number_of_expected_hacking_days")))


def main():
    projects = load_all_projects()

    projects_yaml = []

    for xls_project in projects:
        to_file(xls_project)

    yaml_projects = dict(
        project_list=projects
    )
    with open(PROJECTS_FILE) as pro_file, open(PROJECT_YAML, "w+") as yaml_output_file:
        yaml_output_file.write(
            yaml.dump(yaml_projects, default_flow_style=False))


if __name__ == '__main__':
    main()
