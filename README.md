# ExtractTodoTags

## Description

The tool extracts TODO tags denoted by `# TODO` of Python files (`.py`) and stores found tags in an output file. The input directory to process and the output filename can be passed via command line arguments. In addition, you can specify a command to open the output file if desired. Provide `--help` for futher information about how to use the script.

## Dependencies

- Python 3.6 or later (using f-strings)
- [pandas](https://pandas.pydata.org/) (for data handling)
- [tabulate](https://pypi.org/project/tabulate/) (to parse nice tables)

## Why?

There are many great extensions to handle TODO tags for common editors like VS Code (e.g. [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)) or Sublime Text (e.g. [TodoReview](https://packagecontrol.io/packages/TodoReview)). However, I was looking for an easy way to handle and sort more detailed tags throughout a given project folder and save them in a file for later usage or as a reference. Detailed TODO tags look like this:

```
# TODO: Refactoring: ...
# TODO: Feature: ...
# TODO: Improvement: ...
```

All tags are sorted upon filename, additional tag (`Refactoring`, `Feature` ...) and the line number which `# TODO` was found in. Tag and tag description are separated by a single colon. You can provide any string as an additional tag, a complete TODO tag needs to be formatted in the following form:

```
# TODO: <additional tag>: <description>
```

## Remarks

Using `pandas` in this little tool is definitely over-engineering, but was obviously _the_ solution, since it is part of my default working environment.
