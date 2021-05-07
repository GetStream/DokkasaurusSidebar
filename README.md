# Dokkasaurus Sidebar

This script creates a `sidebars.js` file from the `.md` files generated from Dokkasaurus. The output contains a JSON mapping the file hierarchy of the documentation. Paste the `sidebars.js` file to a Docussaros project and it will generate the sidebar for your Dokka documentation.

**This mini CLI need to be used with Dokkasaurus pluggin.**

## Installing

Make sure your have python installed in your machine, clone this project, go the the directory of the project and run:

```
pip install .
```

## Running

### Single module projects

Add the Dokkasaurus plugin to your gradle files, and then run dokka:

```
./gradlew [yourProject]dokkaHtml
```

Then you need to generate your `sidebar.js` or generate your `_category_.json` files. This CLI support both ways, you just need to use the optional parameters the way suits your best.

Running `dokkasaurus --help` gives your the structure of this command:

```
Usage: dokkasaurus [OPTIONS] PATH ROOT_NAME

  This command traverses the dokka directory and look for .md files to map
  the hierarchy of files

Options:
  -p, --root-position INTEGER  [default: 1]
  -o, --output-path TEXT       [default: ./]
  --auto-generated
  --multi-module
  --filter-file TEXT
  --help
```

You need to include the path to the root directory of your docusaurus `.md` files and pass the name of the section that will be created for you. Also you have the options:

- **--auto-generated**: The diferentiate the way you create your sidebar. If you don't use this option, the CLI will create a json file containing the whole structure of your sidebar. If you use this option, the CLI will create the `_category_.json` for your sections.  

- **--root-position**: This option can only be used with **auto generated** option. This will set the position of your first "_category.json" file. Use this to position your root section.

- **--output-path**: Output path for your **sidebar.js** file. It can only be used for non auto generated sidebars.

- **--multi-module**: Wheater this is a multi module project or not. You can filter some of your modules using a filter file if you don't want to include all your modules.

- **--filter-file**: The file with a json array containing the modules that should be included.

Example of use:

```
dokkasaurus build/dokka/htmlMultiModule Dokka --root-position 5 --auto-generated --multi-module --filter-file dokkasaurus_filter.json
```

### Using inside CI
To use this command inside the CI, you can run the `ci.py` script to avoid installing `Click`. Follow the structure:

```
python ci.py \
[project_path] \
[root_sidebar_name] \
[position of root category] \
[output path] \
[is sidebar auto generated] \
[is multi module] \
[path for filter file]
```

example:

```
python ci.py \
/Users/leandroferreira/stream/stream-chat-android/build/dokka/htmlMultiModule \
Dokka \
 5 \
 ./ \
 True \
 True \
/Users/leandroferreira/stream/stream-chat-android/dokkasaurus_filter.json
```
