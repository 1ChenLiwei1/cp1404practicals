
from operator import attrgetter
from datetime import datetime
from project_management import Project

def main():
    projects = load_projects('projects.txt')
    print(f"Loaded {len(projects)} projects from projects.txt")
    while True:
        display_menu()
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save to projects.txt? (y/n) ").lower() == 'y':
                save_projects('projects.txt', projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_index = int(input("Project choice: "))
    project = projects[project_index]
    print(project)
    new_percent_complete = input("New Percentage: ")
    if new_percent_complete:
        project.percent_complete = int(new_percent_complete)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)

def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    percent_complete = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))

def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%Y")
    filtered_projects = [p for p in projects if p.start_date > date]
    for project in sorted(filtered_projects, key=attrgetter('start_date')):
        print(project)

def display_projects(projects):
    print("Incomplete projects:")
    for project in sorted([p for p in projects if not p.is_complete()]):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted([p for p in projects if p.is_complete()]):
        print(f"  {project}")

def save_projects(filename, projects):
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")
def display_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        file.readline()
        for line in file:
            row = line.strip().split("\t")
            projects.append(Project(row[0], row[1], row[2], row[3], row[4]))
    return projects


if __name__ == '__main__':
    main()