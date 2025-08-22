
# GitHub Environments Setup

1. Go to your repository on GitHub -> Settings -> Environments.
2. Create environment `staging` and `production`.
3. For `production`, add **Required reviewers** (team members who must approve) and optionally a **Wait timer**.
4. You can restrict deployment branches as well.

When a workflow job declares `environment: production`, GitHub will pause the job and require approval(s) before continuing.
