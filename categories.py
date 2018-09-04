# ! / usr / bin / env python
# - * - codificación: utf-8 - * -
import os
import sys
import requests
import sqlite3
import xml.etree.ElementTree as ET 

base_de_datos='base.db'

url = "https://api.sandbox.ebay.com/ws/api.dll"

# original token given as an example
#    <eBayAuthToken>AgAAAA**AQAAAA**aAAAAA**PlLuWA**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GlDpaDpAudj6x9nY+seQ**LyoEAA**AAMAAA**wSd/jBCbxJHbYuIfP4ESyC0mHG2Tn4O3v6rO2zmnoVSF614aVDFfLSCkJ5b9wg9nD7rkDzQayiqvwdWeoJkqEpNQx6wjbVQ1pjiIaWdrYRq+dXxxGHlyVd+LqL1oPp/T9PxgaVAuxFXlVMh6wSyoAMRySI6QUzalepa82jSQ/qDaurz40/EIhu6+sizj0mCgjcdamKhp1Jk3Hqmv8FXFnXouQ9Vr0Qt+D1POIFbfEg9ykH1/I2CYkZBMIG+k6Pf00/UujbQdne6HUAu6CSj9wGsqQSAEPIXXvEnVmtU+6U991ZUhPuA/DMFEfVlibvNLBA7Shslp2oTy2T0wlpJN+f/Jle3gurHLIPc6EkEmckEpmSpFEyuBKz+ix4Cf4wYbcUk/Gr3kGdSi20XQGu/ZnJ7Clz4vVak9iJjN99j8lwA2zKW+CBRuHBjZdaUiDctSaADHwfz/x+09bIU9icgpzuOuKooMM5STbt+yJlJZdE3SRZHwilC4dToTQeVhAXA4tFZcDrZFzBmJsoRsJYrCdkJBPeGBub+fqomQYyKt1J0LAQ5Y0FQxLHBIp0cRZTPAuL/MNxQ/UXcxQTXjoCSdZd7B55f0UapU3EsqetEFvIMPxCPJ63YahVprODDva9Kz/Htm3piKyWzuCXfeu3siJvHuOVyx7Q4wyHrIyiJDNz5b9ABAKKauxDP32uqD7jqDzsVLH11/imKLLdl0U5PN+FP30XAQGBAFkHf+pAvOFLrdDTSjT3oQhFRzRPzLWkFg</eBayAuthToken>
data = """<?xml version='1.0' encoding='utf-'?>
<GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
    <RequesterCredentials>
      <eBayAuthToken>AgAAAA**AQAAAA**aAAAAA**XnCJWw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4ajCpGApw6dj6x9nY+seQ**8bUEAA**AAMAAA**RqOlZ34WJJ3eVHw2FWkDRCMRHuEa1nfZLURCViu/R6FvFftocYX+Gt9V5H68/H466xu+neUkzG6s5Hw58GnRwPwhHNyfwTwGd54hBpiTJpop9uPC2+BC9m4MoaNeBcuiW2u0FI9vPJqL4YvTw/zIzSGeA7iWq/EJp/tP+J5coVlthnZY9zVq/K1AG4NoXx47Q1KnMNZPH/gmrRp47ZhberVsLDW56gDhLLbJdKPzNwa1/M3ZKDvk7Gg0K65XoE5LzTF04WZYjmP26HueJAf6gDVhbzLUB4vGRL9mTy/uHRb8YPuMVk8+Yc6hu8nmNtTS9CWbmVFhOsPU2orxe8hNqeUE6uRQTW0B9ObQTWG56dNMF4Bxtugux7gQpl/0v2zmKPavnew8HdQm4IKFlDDJ2ugg+i/1bdNVE/qnnv1Zdr/P0GKTvLC+ZxRzq7ZtM/mhYcbAoWiHSoL2DAsLSpoUyCiAhfWLLL8YmZ7KN4x7wmxnp14A5o5uQrJb8Z1R8GBCRVhl1pvxr7iEmg4kuff3d508GxisTqBWFHDUe8do5ZLhNjVZ5pQbys0Xc0QfJbbqLAp2cCdwAsXfKDW2w7QdaZTEnMt3zeogTmZlTzOisws5J2v2edLx8rBgtE66WWqXRplrqdynGZf34IYMEwVxgQIwtHqV1/bY7ODBmT20mf6XO5uKu5Xxbxl885jTI2qRlkmxHv8yDsS6pFAukKFy8Hn4NALXy7qJqe6B7C3LTQycowL+ciZA6jLhM5u16zmI</eBayAuthToken>
    </RequesterCredentials>
    <CategorySiteID>0</CategorySiteID>
    <DetailLevel>ReturnAll</DetailLevel>
</GetCategoriesRequest>"""

headers = {
'X-EBAY-API-CALL-NAME' : 'GetCategories',
'X-EBAY-API-APP-NAME' : 'EchoBay62-5538-466c-b43b-662768d6841',
'X-EBAY-API-CERT-NAME' : '00dd08ab-2082-4e3c-9518-5f4298f296db',
'X-EBAY-API-DEV-NAME' : '16a26b1b-26cf-442d-906d-597b60c41c19',
'X-EBAY-API-SITEID' : '0',
'X-EBAY-API-COMPATIBILITY-LEVEL': '861'
}

def api_table():
    """
    In this function you will make the connection with the api of ebay para extract the files, 
    once you extracted the files proceeds to create the table with their fields,
    later we save the extracted data in variables and insert in the database through a cycle for
    """
    called = "{urn:ebay:apis:eBLBaseComponents}"
    response = requests.post(url, data=data, headers=headers)
    root_xml = ET.fromstring(response.text)
    category_array = root_xml.find(called + "CategoryArray")
    if(os.path.isfile(base_de_datos)):
        os.remove(base_de_datos)
    con= sqlite3.connect(base_de_datos)
    cursor = con.cursor()
    cursor.execute('CREATE TABLE records (CategoryID INT, CategoryName TEXT, CategoryLevel INT, BestOfferEnabled INT, CategoryParentID INT )')
    cursor.execute('CREATE INDEX CategoryIndex ON records (CategoryID)')
    for attract in category_array:
        ID = int(attract.find(called + "CategoryID").text)
        Name = attract.find(called + "CategoryName").text
        Level = int(attract.find(called + "CategoryLevel").text)
        if(attract.find(called + "BestOfferEnabled")):
            BOEnabledB = attract.find(called + "BestOfferEnabled").text
        else:
            BOEnabledB = False
        ParentID = int(attract.find(called + "CategoryParentID").text)
        if(BOEnabledB == 'true'):
            BOEnabled = 1
        else:
            BOEnabled = 0
        values = (ID, Name, Level, BOEnabled, ParentID)
        cursor.execute("INSERT INTO records(CategoryID, CategoryName, CategoryLevel, BestOfferEnabled, CategoryParentID) VALUES(?, ?, ?, ?, ?)", values)
    con.commit()
    con.close()
    print("is to created successfully the base of data")

def render_category(idcategory):
    """
    The id of the category was received as an argument to be identified in the html file and to 
    make the selection from the database. The header and footer of an html file will be created,
    the body of the html file will be made in the function buildBody () which we will call from 
    this function to make a union of the entire html file
    """
    ca_id = idcategory
    html_header = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>category:{ca_id}</title>
        <link rel="stylesheet" href="style.css">
      </head>
      <body>
        <img src="ebay_logo.png" class="img">
        <h1 >Category Tree for number: {ca_id}</h1>
        <div class='container'>
      """
    con= sqlite3.connect(base_de_datos)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM records WHERE CategoryID={a}".format(a=ca_id))
    category_item = cursor.fetchall()#no entendi
    con.close()
    if(len(category_item) == 0):
        print("the category with the id: " + str(ca_id) + " was not found")
        sys.exit()
    html_body = buildBody(category_item)
    html_close = """
    </div>
    </body>
    </html>
    """
    final_html = html_header + html_body + html_close
    global filename
    filename  = str(ca_id) + ".html"
    html_file = open(filename, "w")
    html_file.write(final_html)
    html_file.close()
    print("successfully rendered html file. You may now open " + filename + " in your browser" )

    e = input("Press 1 to run in the browser or double enter to exit: ")
    if e== '1':
        run()
    elif e == "":
        input()         
    else:
        print("wrong option")
    
def run():
    """
    This is so that the previously created html file is autoexected
    """
    os.system (filename)

def buildBody(items):
    """
    the articles of the row identified with the id already used in the function render_category ()
    are received as an argument. The body of the html file will be created, if the category of said
    id contains more levels these will also be created.
    """
    if(len(items) == 0):
        return ""
    html_body = "<ul>"
    for element in items:
        if(element[3] == 1):
            BestOfferEnabled = "true"
        else:
            BestOfferEnabled = "false"
        list_item = f"""
        <li><div class=list-item>
        <p> <span class="nane">{element[1]}</span> 
            <span class="id">Category ID:{element[0]}</span> /
            <span class="level">Category Level:{element[2]}</span> / 
            <span class="best">Best Offer Enabled:</span><span class="bool">{BestOfferEnabled}</span>
         </p>
        """
        con= sqlite3.connect(base_de_datos)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM records WHERE CategoryLevel={next_level} AND CategoryParentID={id}"\
        .format(id=element[0],next_level=element[2] + 1))
        category_item = cursor.fetchall()
        con.close()
        html_body += list_item + buildBody(category_item) + "</div></li>"
    html_body += "</ul>"
    return html_body


if(sys.argv[1]):
    if(sys.argv[1] == "--rebuild"):
        api_table()
    elif(sys.argv[1] == "--render"):
          if(os.path.isfile(base_de_datos)):
            if(sys.argv[2]):
                render_category(sys.argv[2])
            else:
                print("error: no categoryID entered")
          else:
            print("error: no database. Run '--rebuild' to continue")
    else:
        print("error: invalid argument")
else:
    print("error: no valid argument")      

