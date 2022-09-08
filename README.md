# cookiecutter-sc3-quark 

A cookiecutter to generate an sc3 quark package.

## Usage 

Set up a package in the current directory. 

```
$ cookiecutter https://github.com/bsnacks000/cookiecutter-sc3-quark.git 
```

You can put this wherever you have `sclang` look for quarks and it should be installable with:

```
sc3> Quarks.install("yourquark");
```
