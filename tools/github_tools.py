import requests

class GithubClient:
    def __init__(self):
        self.base_url = "https://api.github.com/repos/"
        self.api_token = "YOUR_GITHUB_ACCESS_TOKEN" # Replace with your token for higher rate limits
        self.headers = {'Authorization': f'token {self.api_token}'} if self.api_token else {}
        self.search_url = "https://api.github.com/search/"

    def get_repo_info(self, repo_path):
        url = f"{self.base_url}{repo_path}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_repo_contents(self, repo_path):
        url = f"{self.base_url}{repo_path}/contents"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return []

    def file_exists(self, repo_path, filename):
        url = f"{self.base_url}{repo_path}/contents/{filename}"
        response = requests.head(url, headers=self.headers)
        return response.status_code == 200
        
    def get_issues_count(self, repo_path):
        query = f'q=repo:{repo_path}+is:issue'
        url = f"{self.search_url}issues?{query}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('total_count', 0)
        return 0

    def get_pulls_count(self, repo_path):
        query = f'q=repo:{repo_path}+is:pr'
        url = f"{self.search_url}issues?{query}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('total_count', 0)
        return 0