import csv
import sys

def main():
    # Read in CSV file for projects
    projects = list(csv.DictReader(open("projects.csv", "r"), delimiter=","))

    # Read in README header
    with open('header.md') as f:
        header = f.read().splitlines()

    # Write to README.md
    with open('../README.md', 'w') as f:
        ################################
        # Printing out old README header
        ################################
        for line in header:
            print(line, file=f)

        ################################
        # Printing out projects
        ################################
        print("\n| Project Title     | Author   | Link                               | Description                    |", file=f)
        print(  "|-------------------|----------|------------------------------------|--------------------------------|", file=f)
        for x in projects:
            print(f"| {x['Project Title']} | {x['Author']} | {x['Link']} | {x['Description']} |", file=f)

if __name__ == '__main__':
    main()
