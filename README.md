# Getting Started

## docker from source

```bash
git clone
cd github-repo-lister
make build
make run MOUNT_DIRECTORY="directory_path_where_you_want_your_output_file"
```


## devcontainer
1. build the container
2. run `main.py`
3. this will create a `github_repos.csv` in your mounted directory. In my case it's a folder inside my Obsidian Vault (`$ONEDRIVE/docs/second-brain/2. Areas/Software`). The CSV is picked by a Dataview query. To update the mounted directory, just update `devcontainer.json`.

# Core Functionality

Compiling a list of Github repositories you own and putting them in a CSV file with some metadata.

# Deployment

No deployment required at the moment.

# Backup

The system is stateless.
The output is reproducible.


# Troubleshooting / FAQ

Nothing at the moment.


