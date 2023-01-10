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

Add the project's directory to your `PATH` in order to run `git-with` and `git-without` from any other directory:

```shell
echo "export PATH=\$PATH:$(pwd)" >> ~/.zshrc
source ~/.zshrc
```

Go to the repository in which you want to use the `git-with` and `git-without` commands and run the command below. It will add the git hooks to the repository.

```shell
cd path/to/your/repo
git-with init
```

> :warning: this project does not work with mulitple `prepare-commit-msg` hooks, it is a known issue, PRs are welcome.

## Usage

### Help

To see the command help docs run:

```
shell
git-with help
```

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
