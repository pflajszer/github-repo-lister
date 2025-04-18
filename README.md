# Getting Started

## docker from source

```bash
git clone
cd github-repo-lister
make build
make run MOUNT_DIRECTORY="directory_path_where_you_want_your_output_file"
```


## devcontainer
1. update the "directory_path_where_you_want_your_output_file" value in `devcontainer.json`
1. build the devcontainer
1. run `main.py`

# Core Functionality

Compiling a list of Github repositories you own and putting them in a CSV file with some metadata. The script automatically ignores Forked repos and the ones you have access via other Organizations.

Running the script will create a `github_repos` in `csv` and `md` formats in your mounted directory.

In my case it's a folder inside my Obsidian Vault (`"directory_path_where_you_want_your_output_file"`). The CSV is picked by a Dataview query.

Example output:

| MarkdownHyperlink                                                                                                         | Repo                                         | LatestBetaTag   | LatestStableTag   | Archived   | Milestones   | Branches                                  | Topics      |
|:--------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------|:----------------|:------------------|:-----------|:-------------|:------------------------------------------|:------------|
| [AzureTablesLifecycleManager](https://github.com/pflajszer/AzureTablesLifecycleManager)                                   | AzureTablesLifecycleManager                  | v2.2.0-beta     | v2.2.0            | False      |              | master, test                              | active      |
| [Paving](https://github.com/pflajszer/Paving)                                                                             | Paving                                       | v4.0.10-beta    | v4.0.10           | False      |              | dev, master                               | active      |
| [budget-interface](https://github.com/pflajszer/budget-interface)                                                         | budget-interface                             | v0.1.0-beta     | v0.1.0            | False      | v0.2.0       | dev, master                               | active      |
| [dotfiles-macos](https://github.com/pflajszer/dotfiles-macos)                                                             | dotfiles-macos                               |                 |                   | False      |              | main                                      | dotfiles    |
| [dotfiles-ubuntu-desktop](https://github.com/pflajszer/dotfiles-ubuntu-desktop)                                           | dotfiles-ubuntu-desktop                      |                 |                   | False      |              | master                                    | dotfiles    |
| [dotfiles-wsl](https://github.com/pflajszer/dotfiles-wsl)                                                                 | dotfiles-wsl                                 |                 |                   | False      |              | main, master                              | dotfiles    |
| [fifa-stat-extractor](https://github.com/pflajszer/fifa-stat-extractor)                                                   | fifa-stat-extractor                          |                 |                   | False      | v0.3.0       | dev, main, v0.3.0                         | active      |
| [github-repo-lister](https://github.com/pflajszer/github-repo-lister)                                                     | github-repo-lister                           |                 |                   | False      |              | main                                      | active      |
| [kaggle](https://github.com/pflajszer/kaggle)                                                                             | kaggle                                       |                 |                   | False      |              | main                                      | experiments |
| [resume](https://github.com/pflajszer/resume)                                                                             | resume                                       |                 |                   | False      |              | main                                      | maintenance |
| [ticktick-exporter](https://github.com/pflajszer/ticktick-exporter)                                                       | ticktick-exporter                            | v0.1.0-beta     | v0.1.0            | False      |              | dev, master                               | maintenance |

# Deployment

No deployment required at the moment.

# Backup

The system is stateless.
The output is reproducible.


# Troubleshooting / FAQ

Nothing at the moment.


