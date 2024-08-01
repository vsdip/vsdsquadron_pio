import csv

def main():
    # Read in CSV file for projects
    with open("projects.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=",")
        projects = list(reader)

    # Read in README header
    with open('header.md') as f:
        header = f.read().splitlines()

    # Write to the README.md file located in the parent directory
    with open('../README.md', 'w') as f:
        ################################
        # Printing out old README header
        ################################
        for line in header:
            print(line, file=f)

        ################################
        # Printing out projects
        ################################
        print("\n| Project Title     | Author   | Description                    |", file=f)
        print(  "|-------------------|----------|--------------------------------|", file=f)
        for x in projects:
            try:
                # Create the link for the project title
                project_title = f"[{x['Project Title']}]({x['Link']})"
                print(f"| {project_title} | {x['Author']} | {x['Description']} |", file=f)
            except KeyError as e:
                print(f"Error: Missing key in row: {e}")
                print(f"Row content: {x}")
                continue

if __name__ == '__main__':
    main()
