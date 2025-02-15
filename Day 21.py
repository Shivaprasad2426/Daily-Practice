import os
import requests

def upload_file(repo, path, token, file_path, commit_message="Add new file"):
    # Read the file content
    with open(file_path, 'rb') as file:
        content = file.read()

    # Encode the file content to base64
    content_base64 = content.encode('base64')

    # Create the API URL for uploading
    url = f"https://api.github.com/repos/{repo}/contents/{path}"

    # Create the payload for the API request
    payload = {
        "message": commit_message,
        "committer": {
            "name": "Shivaprasad2426",
            "email": "shivaprasad2426@example.com"
        },
        "content": content_base64
    }

    # Create the headers for the API request
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Make the API request to upload the file
    response = requests.put(url, json=payload, headers=headers)

    # Check the response status
    if response.status_code == 201:
        print("File uploaded successfully!")
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    # Example usage
    repo = "Shivaprasad2426/Daily-Practice"
    path = "new_directory/new_file.txt"
    token = os.getenv("GITHUB_TOKEN")  # Ensure you set your GitHub token as an environment variable
    file_path = "path/to/your/local/file.txt"
    upload_file(repo, path, token, file_path)
