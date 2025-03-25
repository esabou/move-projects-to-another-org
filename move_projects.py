import requests
import os

# Ask for user input
current_org = input("Enter the org ID where your current projects are: ")
move_org = input("Enter the org ID where you would like to move your projects: ")
auth_token = os.getenv("SNYK_TOKEN")

headers = {
"Authorization": f"token {auth_token}",
"Content-Type": "application/vnd.api+json",
"Accept": "application/vnd.api+json"
}

# Get all projects enpoint for an Organisation
def get_all_projects():
    url = f"https://api.snyk.io/rest/orgs/{current_org}/projects?&version=2024-10-15"
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", [])

        project_info = [{"id": project["id"], "name": project["attributes"]["name"]} for project in data]
        return project_info
    else:
        print(f"❌ Failed to get projects: {response.status_code} - {response.text}")
        return []



# Move projects endpoint
def move_project(project_id):
    url = f"https://api.snyk.io/v1/org/{current_org}/project/{project_id}/move"    
    
    response = requests.put(
        url,
        headers={"Content-Type":"application/json", "Authorization": f"token {auth_token}"},
        json={"targetOrgId": move_org}
    )

    if response.status_code == 200:
        print(f"✅ Successfully moved project ID: {project_id}")
        return response.json()
    else:
        print(f"❌ Failed to move project ID: {project_id}. Status Code: {response.status_code}")
        return None

# Get projects and move them to the new organization
projects = get_all_projects()


# Print the retrieved projects
print()
print(f"🎯 Retrieved {len(projects)} projects.")
for project in projects:
    print(f"{project['name']}: {project['id']}")



for project in projects:
    print()
    print(f"⏳ Moving Project - ID: {project['id']}, Name: {project['name']}")
    move_project(project['id'])