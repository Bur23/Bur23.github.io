#! /usr/bin/python3
print("Content-Type: text/html\n\n")

# Base HTML template from which every page is made
page = '''

<!DOCTYPE html>
<html>
    <head>
        _HEAD_
        <title>
            _title_
        </title>
    </head>
    <body>
        _navbar_
        _BODY_
    </body>
</html>
'''

#This list of types is used for the navbar and type page creation
types = ["Normal","Fire","Water","Grass","Electric","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Steel","Fairy"]

#Define global variables and page elements
comment = "\n<!--_ctext_-->\n"
tab = "    "
header = "<h1>_header_</h1>"
paragraph = "\n" + 2 *tab + "<p>_ptext_</p>"

#This function is called during creation of every page and creates the navbar
def createNavbar():
    navBar ='''
        <nav>
            <ul>
                <li><a href="makePokedex.py">Home</a></li>
                <li><a href="#item">Types</a>
                    <ul class="dropdown">
                        _types_
                    </ul>
                </li>
                <li><a href="pokedex.html">All Pokemon</a></li>
                <li><a href="top10.html">Top 10</a></li>
            </ul>
        </nav>'''
    allTypes = ""
    for type in types:
        li = '<li><a href="'+type+'.html"><div class="droptext">'+type+'</div></a></li>\n'
        allTypes += li + 6*tab
    allTypes = allTypes[:len(allTypes)-25]
    navBar = navBar.replace("_types_",allTypes)
    navBar = comment.replace("_ctext_","Start of navbar") + navBar
    return navBar

#Define elements of every page
css = '<link href="style.css" rel="stylesheet">'
page = page.replace("_HEAD_",css)
page = page.replace("_navbar_", createNavbar())

# Open the CSV file and turn it into a list of lists called pokeLst
with open("pokemon.csv","r") as text:
    read = text.read()    
lst = read.split("\n")
pokeLst = []
for l in lst:
    newL = l.split(",")
    pokeLst.append(newL)
pokeLst[0].insert(0, "Front")
pokeLst[0].insert(1,"Back")

# Creates a table of Pokemon. Used for every page with a table.
def makeHTMLTable(data):
    table = '''
        <table>
        _tbod_
        </table>'''
    tdata = "<td>_tdata_</td>"
    thead = "<th>_thead_</th>"
    tbod = tab + "<tr>"
    for item in data[0]:
        tbod += "\n" + 4*tab + thead.replace("_thead_",item)
    tbod += "\n" + tab*3 + "</tr>\n"
    for i in range(1,len(data)):
        image1 = '<img src="img/front/' + str(data[i][0]) + '.png">'
        image2 = '<img src="img/back/' + str(data[i][0]) + '.png">'
        tbod += 3*tab + "<tr>\n" + 4 *tab + tdata.replace("_tdata_",image1) + "\n" + 4 *tab + tdata.replace("_tdata_",image2)
        for item in data[i]:
            tbod += "\n" + 4*tab + tdata.replace("_tdata_",item)
        tbod += "\n" + 3*tab + "</tr>\n"
    tbod = tbod[:len(tbod)-1]
    table = table.replace("_tbod_",tbod)
    table = comment.replace("_ctext_","Start of table") + "\n" + table
    return table

# Create the home page. This page is printed rather than created as a separate page.

homeLst = []
homeLst.append(pokeLst[0])
for lst in pokeLst:
    if lst[1] == "Gloom":
        homeLst.append(lst)
        
homeHead = header.replace("_header_","Nora's Pokemon Website")
homeParagraph = paragraph.replace("_ptext_","Hi! This is my Pokemon website. I'm not a super big Pokemon fan, but I do like them. My favorite Pokemon is Gloom, and its stats are shown at the bottom. I hope you enjoy looking through my website!")
homeImg = '<img src="pokemon.jpg" width=250>'
homePage = page.replace("_BODY_",homeHead+homeImg+homeParagraph+makeHTMLTable(homeLst))
homePage = homePage.replace("_title_","Nora's Pokemon Website")
print(homePage)
    
#Create the All Pokemon page
html_file = open("pokedex.html","w")
pokeParagraph = paragraph.replace("_ptext_","As I said on my home page, I like pokemon, but I don't have a very strong opinion on them. My mom works on Pokemon books for her job, so she knows almost all of the Pokemon and their types, and sometimes we have random Pokemon stuff lying around in our house. I've also played Pokemon games before, like Pokemon Go, and my younger brother went through a Pokemon phase.")
pokeHeader = header.replace("_header_","Pokedex")
pokedexPage = page.replace("_BODY_",pokeHeader + pokeParagraph + makeHTMLTable(pokeLst))
pokedexPage = pokedexPage.replace("_title_","Pokedex")

print(pokedexPage, file=html_file)
html_file.close()

# Create the Top 10 page
html_file = open("top10.html","w")

favorites = [25,44,51,39,131,143,102,54,8,94]
favLst = []
favLst.append(pokeLst[0])
for item in favorites:
    favLst.append(pokeLst[item])

favHeader = header.replace("_header_","Top 10")
favParagraph = paragraph.replace("_ptext_", "These are my top 10 favorite Pokemon (not in order). There are a bunch of different reasons I like these Pokemon, but mainly they're the ones that I think are the most cute. For some of them, I also like their names or what they represent, such as Exeggcute and Psyduck.")
favPage = page.replace("_BODY_",favHeader + favParagraph + makeHTMLTable(favLst))
favPage = favPage.replace("_title_","Top 10")
print(favPage, file=html_file)

html_file.close()

# Create a page for each type
for type in types:
    filename = type + ".html"
    html_file = open(filename,"w")
    typeLst = []
    typeLst.append(pokeLst[0])
    for lst in pokeLst:
        if lst[2] == type or lst[3] == type:
            typeLst.append(lst)

    typeHeader = header.replace("_header_",type)
    typePage = page.replace("_BODY_",typeHeader + makeHTMLTable(typeLst))
    typePage = typePage.replace("_title_",type)

    print(typePage, file=html_file)
    html_file.close()