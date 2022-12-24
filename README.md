# git-with(out)

Simple CLI to add `Co-Authored-by` to your git commits.

## Usage

### Introducing new people to the program

```shell
git-with introduce bilbo.baggings "Bilbo Baggins" bilbo.baggins@shire.org
git-with introduce gandalf.thegray "Ganfalf The Gray" gandalf.thegray@wizard.com
```

### Coding with people

```shell
git-with bilbo.baggins ganfalf.thegray
```

### Stop coding with a specific person

```shell
git-without bilbo.baggins
```

### Coding alone again

```shell
git-without everyone
```