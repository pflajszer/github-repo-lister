from dotenv import load_dotenv
import requests
import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    
    load_dotenv()

    # Replace with your GitHub username and token
    USERNAME = os.getenv("GITHUB_USERNAME", "your_username")
    TOKEN = os.getenv("GITHUB_TOKEN", "your_token")

    # GitHub API URL
    BASE_URL = "https://api.github.com"

    def get_repos():
        logger.info("Fetching repositories...")
        repos = []
        page = 1
        while True:
            url = f"{BASE_URL}/user/repos?per_page=100&page={page}"
            logger.debug(f"Requesting URL: {url}")
            r = requests.get(url, auth=(USERNAME, TOKEN))
            if r.status_code != 200:
                logger.error(f"Failed to fetch repositories: {r.status_code} - {r.text}")
                break
            data = r.json()
            if not data:
                logger.info("No more repositories found.")
                break
            repos.extend(data)
            logger.info(f"Fetched {len(data)} repositories from page {page}.")
            page += 1
        logger.info(f"Total repositories fetched: {len(repos)}")
        return repos

    def get_repo_info(repo):
        logger.debug(f"Processing repository: {repo.get('name', 'Unknown')}")
        if repo['fork']:
            logger.info(f"Skipping forked repository: {repo['name']}")
            return {}

        if repo['owner']['login'] != USERNAME:
            logger.info(f"Skipping repository not owned by user: {repo['name']}")
            return {}
        
        name = repo['name']
        full_name = repo['full_name']
        link = f"[{name}]({repo['html_url']})"
        archived = repo['archived']
        
        # Get topics
        topics_url = f"{BASE_URL}/repos/{full_name}/topics"
        logger.debug(f"Fetching topics for repository: {name}")
        topics_response = requests.get(topics_url, auth=(USERNAME, TOKEN), headers={"Accept": "application/vnd.github.mercy-preview+json"})
        topics = topics_response.json().get("names", [])
        topics_str = ", ".join(topics)
        
        # Get latest tag
        tags_url = f"{BASE_URL}/repos/{full_name}/tags"
        logger.debug(f"Fetching tags for repository: {name}")
        tags = requests.get(tags_url, auth=(USERNAME, TOKEN)).json()
        
        latest_stable_tag = None
        latest_beta_tag = None

        if tags:
            for tag in tags:
                tag_name = tag['name']
                if "-beta" in tag_name:
                    if latest_beta_tag is None or tag_name > latest_beta_tag:
                        latest_beta_tag = tag_name
                else:
                    if latest_stable_tag is None or tag_name > latest_stable_tag:
                        latest_stable_tag = tag_name

        # Get milestones
        milestones_url = f"{BASE_URL}/repos/{full_name}/milestones"
        logger.debug(f"Fetching milestones for repository: {name}")
        milestones = requests.get(milestones_url, auth=(USERNAME, TOKEN)).json()
        milestone_titles = [m['title'] for m in milestones] if milestones else []
        
        # Get branches
        branches_url = f"{BASE_URL}/repos/{full_name}/branches"
        logger.debug(f"Fetching branches for repository: {name}")
        branches = requests.get(branches_url, auth=(USERNAME, TOKEN)).json()
        branch_names = [branch['name'] for branch in branches] if branches else []

        logger.info(f"Processed repository: {name}")
        return {
            "MarkdownHyperlink": link,
            "Repo": name,
            "LatestBetaTag": latest_beta_tag,
            "LatestStableTag": latest_stable_tag,
            "Archived": archived,
            "Milestones": ", ".join(milestone_titles),
            "Branches": ", ".join(branch_names),
            "Topics": topics_str
        }

    # Fetch all repos and gather info
    logger.info("Starting repository information gathering...")
    all_repos = get_repos()
    data = [get_repo_info(repo) for repo in all_repos]

    # Create DataFrame
    logger.info("Creating DataFrame from repository data...")
    df = pd.DataFrame(data)
    df = df.dropna(subset=["Repo"])
    df = df.sort_values(by=["Archived", "Repo"])
    logger.info("DataFrame created successfully.")

    # Save to CSV
    output_path = "output/github_repos"
    logger.info(f"Saving repository data to CSV: {output_path}.csv")
    df.to_csv(output_path + ".csv", index=False)
    logger.info(f"Saving repository data to Markdown: {output_path}.md")
    df.to_markdown(output_path + ".md", index=False)
    logger.info("Repository data saved successfully.")
