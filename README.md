# Move Projects Between Snyk Organizations

This script retrieves all projects from a specified Snyk organization and moves them to another target organization.

## Prerequisites
- Python 3.x installed
- A valid [Snyk API Token](https://docs.snyk.io/snyk-api/rest-api/authentication-for-api#how-to-obtain-your-personal-token)
- `requests` library installed (if not, install using `pip install requests`)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/move-project-to-another-org.git
   cd move-project-to-another-org
   ```
2. Ensure the script `move_projects.py` is inside the repository directory.

## Usage
1. Set your Snyk API token as an environment variable:
   ```sh
   export SNYK_TOKEN=your-snyk-api-token
   ```
2. Run the script:
   ```sh
   python move_projects.py
   ```
3. Enter the required details when prompted:
   - Current Organization ID (where projects are currently located)
   - Target Organization ID (where projects will be moved)

## Expected Output
- The script retrieves and displays all projects from the current organization.
- It then attempts to move each project to the new organization.
- Success or failure messages are printed for each project.

## Notes
- Ensure that the authenticated user has permissions to move projects between organizations.
- If you encounter a `409 Conflict` error, it may be due to project constraints (e.g., already existing in the target org).

## License
This project is open-source and available under the [MIT License](LICENSE).

