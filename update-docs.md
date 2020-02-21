# Updating NMDC Documentation on GitHub Pages

The NDMC Documentation site is deployed on GitHub Pages.

The site itself is driven by Jekyll and the content is written in markdown.

To update the documentation to reflect any change and/or updates to the schema,

#### Merge latest changes from master

First, make sure you are on `gh-pages` branch.

Then, merge all the latest changes from `master` to `gh-pages`:

```
git merge master
```

You should not run into any merge conflicts. In the rare case that you do, resolve these conflicts via `git mergetool`.

#### Build markdown documentation

Now, build the new Markdown documentation from the updated schema YAML.

```
make docs
```

#### Commit the changes

Once you build the Markdown documentation, the contents of `docs` folder will have many of the files modified, depending on how extensive the update was.

Stage these files:

```
git add docs/
```

Commit the changes:

```
git commit -m "Update docs"
```

## Push the changes to GitHub

Now push the changes to GitHub. This push will trigger GitHub Pages to regenerate the documentation site.


```
git push origin gh-pages
```

> It will take a minute or two for the documentation site to refresh.


