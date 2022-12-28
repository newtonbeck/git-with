# git-with(out)

Simple CLI to add `Co-Authored-by` to your git commits.

## Setup

Clone this project:

```shell
git clone git@github.com:newtonbeck/git-with.git
cd git-with
```

Configure a global git templates directory, this directory will contain your global git hooks:

```shell
mkdir -p ~/.git-templates/hooks
git config --global init.templatedir '~/.git-templates'
```

> Initially, I planned to use a symlink there, but as the global hook is imported to the projects as a symlink, I ended up with two symlinks and it did not work as expected (MRs are welcome here).

Copy the `prepare-commit-msg` and `users.py` files to the hooks directory:

```shell
cp prepare-commit-msg ~/.git-templates/hooks/prepare-commit-msg
cp users.py ~/.git-templates/hooks/users.py
```

Add the project's directory to your `PATH` in order to run `git-with` and `git-without` from any other directory:

```shell
echo "export PATH=PATH:$(pwd)" >> ~/.zshrc
source ~/.zshrc
```

Finally, re-initialize git in the repositories where you want to use the `git-with` hook:

```shell
cd <your repository>
git init
```

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
