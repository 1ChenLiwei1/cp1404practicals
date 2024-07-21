
from operator import attrgetter
from datetime import datetime
from project_management import Project

def main():
    projects = load_projects('projects.txt')
    print(f"Loaded {len(projects)} projects from projects.txt")




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