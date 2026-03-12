# Git Basics

## Overview

Git is a distributed version control system that tracks changes in source code during software development.

## Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Essential Commands

### Initialize a repository

```bash
git init
```

### Clone a repository

```bash
git clone <url>
```

### Check status

```bash
git status
```

### Stage and commit

```bash
git add <file>        # stage a specific file
git add .             # stage all changes
git commit -m "message"
```

### View history

```bash
git log --oneline
```

### Branches

```bash
git branch              # list branches
git checkout -b feature # create and switch to new branch
git merge feature       # merge branch into current
```

### Remote

```bash
git push origin main
git pull origin main
```

## References

- https://git-scm.com/doc
