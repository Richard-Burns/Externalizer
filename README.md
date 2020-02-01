# Externalizer
 Externalize TouchDesigner projects

## How to Use

Externalizer will make external any text DATs or COMPs named py_* or module_* For anything you don't want to externalize give another naming convention.

To save the entire project and externalize save module_utilities.tox in your project and hit CTRL + S to save everything.
By default externals are saved in lib/

If you're inside a module and only want to save that particular module and it's children then hit CTRL + ALT + , and it will only save the parent COMP and it's child modules / scripts.

If you ONLY want to save the top level of a module and not it's children then you can hit CTRL + ALT + . and it will save the parent COMP and scripts on the level below but go no further.