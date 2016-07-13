# 
# Very simple string parser application to search for strings within and html page
#
# A simple use is to determine if a HREF link is bad.
#
# Chris Bogdon
# cbogdon@cisco.com
#


import sys

print("\n\n\nString Parser")
print("-------------")

if sys.version_info < (3, 0):
    print("Must use python 3.0 or greater\n")
    exit()

if len(sys.argv) < 2:
    print("Not enough paramters passed to the application! \n")
    print(sys.argv[0] + " {search_string} {filename}\n")
    exit()

print("Search String: " + sys.argv[1])
print("Parsing file: " + sys.argv[2])

# Open the file that is parsed to the application

f = open(sys.argv[2])

filetext = f.read()

# Determine the search string that we want to look for
# ENHANCEMENT: Make this passable via the command line
#
searchstring = sys.argv[1]
count = 0

print("\n\nSearching the file for all occurences of: %s\n\n" % searchstring)

print('{0:40} {1}'.format('Link Title on Page', 'URL'))
print('{0:40} {1}'.format('=======================================', '=========================================='))

# For each line in the file, let's start parsing and searching
for item in filetext.split("\n"):

    # If the searchstring is found, then let's try to parse out the fields
    if searchstring in item:
        # First save the original line
        line = item.strip()

        # Parse thru the line to determine the appropriate href location
        loc = line.find("href=")
        loc = loc + 6
        substring = line[loc:]
        endloc = substring.find("\"")

        # Parse through to determine the name
        start_bracket_loc = substring.find(">") + 1
        end_bracket_loc = substring.find("<")

        link_name = substring[start_bracket_loc:end_bracket_loc]

        # Print the resulting line
        #		print link_name + ":  " + substring[:endloc]
        print('{0:40} {1}'.format(link_name, substring[:endloc]))
        count = count + 1

print("\n\n")
print("Total number of occurences of count: %d" % count)
print("\n\n")
