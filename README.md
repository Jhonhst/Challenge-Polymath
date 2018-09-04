# script for the challenge of Polymath Ventures made with python 3

#### The program consists of extracting a tree of categories from the api of eBay, saving them in a sql database, later, choosing a category can be rendered in an html file of that category.

## Documentation

#### To execute the script we use the following commands:

### --rebuild
#### Extract the categories from the eBay api, create a table in the database and save the extracted data there, if the database exists, it will be deleted to proceed to be created again.

### --render <category_id>
#### With this command the html file is rendered, In addition to the attribute --render you must also place the identification of the category you want to render.

### If the user wishes, he can execute the html file by dialing 1 followed by an enter, if you do not want it, you can just enter an enter to exit.

### for example:

```
$ python3 categories.py --rebuild
is to created successfully the base of data
$ python3 categories.py --render 14111
successfully rendered html file. You may now open 14111 in your browser
press 1 to execute in the browser or double enter to exit: (1: execute) (enter: exit)
$ python3 categories.py --render 0000000
No category with ID:0000000
$ python3 categories.py --probando
Error: invalid command
```

## The database:
### It is a simple scheme of a single table with 5 fields,"CategoryID", "CategoryName", "CategoryLevel", "BestOfferEnabled" y "ParentID de categoría". 

