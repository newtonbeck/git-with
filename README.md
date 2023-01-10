# git-with(out)

Simple CLI to add `Co-Authored-by` to your git commits.

## Requirements

- python >= 3.10
- pip3

## Setup

Clone this project:

```shell
git clone https://github.com/newtonbeck/git-with.git
cd git-with
pip3 install -r requirements.txt
```

Still inside the `git-with` project, add it to your `PATH` in order to run `git-with` and `git-without` from any other directory:

```shell
echo "export GIT_WITH_HOME=$(pwd)" >> ~/.zshrc
echo "export PATH=\$PATH:\$GIT_WITH_HOME" >> ~/.zshrc
source ~/.zshrc
```

## Usage

### Help

To see the command help docs run:

```
shell
git-with help
```

### Adding git-with(out) to a repository

To add the git hooks to a repository:

```shell
cd path/to/your/repo
git-with init
```

> :warning: this project does not work with mulitple `prepare-commit-msg` hooks, it is a known issue, PRs are welcome.

### Introducing new people to the program

To introduce a new person to the program:

```shell
git-with introduce bilbo "Bilbo Baggins" bilbo.baggins@shire.org
git-with introduce gandalf "Ganfalf The Gray" gandalf.thegray@wizard.com
```

### Coding with people

To add an introduced person as a co-author in your next git commits, run:

```shell
git-with bilbo ganfalf
```

### Stop coding with a specific person

To remove an introduced person as a co-author from your next git commits, run:

```shell
git-without bilbo
```

### Coding alone again

To remove everyone as co-authors from your next git commits, run:

```shell
git-without everyone
```
