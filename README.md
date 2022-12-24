# With

Simple CLI to add `Co-Authored-by` to your git commits.

## Usage

### Configuring people

```shell
with add bilbo.baggings "Bilbo Baggins" bilbo.baggins@shire.org
with add gandalf.thegray "Ganfalf The Gray" gandalf.thegray@wizard.com
```

### Adding people to your commits

```shell
with bilbo.baggins ganfalf.thegray
```

### Removing one person from your commits

```shell
with remove bilbo.baggins
```

### Removing everyone from your commits

```shell
with alone
```