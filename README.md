# git-with(out)

Simple CLI to add `Co-Authored-by` to your git commits.

## Setup

Clone this project:

```
git clone git@github.com:newtonbeck/git-with.git
cd git-with
```

Configure a global git templates directory, this directory will contain your global git hooks:

```
mkdir -p ~/.git-templates/hooks
git config --global init.templatedir '~/.git-templates'
```

> Initially, I planned to use a symlink there, but as the global hook is imported to the projects as a symlink, I ended up with two symlinks and it did not work as expected (MRs are welcome here).

Finally, copy the `prepare-commit-msg` and `users.py` files to the hooks directory:

```
cp prepare-commit-msg ~/.git-templates/hooks/prepare-commit-msg
cp users.py ~/.git-templates/hooks/users.py
```

## Usage

### Introducing new people to the program

```shell
git-with introduce bilbo "Bilbo Baggins" bilbo.baggins@shire.org
git-with introduce gandalf "Ganfalf The Gray" gandalf.thegray@wizard.com
```

### Coding with people

```shell
git-with bilbo ganfalf
```

### Stop coding with a specific person

```shell
git-without bilbo
```

### Coding alone again

```shell
git-without everyone
```