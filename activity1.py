__author__ = 'sanymathew'


f = open('emacs.log','r')
count = 0;
maxNumberOfRevisions = 0;
maxFileName = ""
listLines = []
authorSet = set()
maxAuthorSize = 0
maxAuthorFileName = ""
for line in f:
    if (line.__contains__("===")):
        count = count + 1

        authorLen = len(authorSet)
        if (authorLen > maxAuthorSize):
            maxAuthorSize = authorLen
            maxAuthorFileName = fileName
        authorSet = set()
        #continue;
    else:
        if line != '':
            listLines.append(line.rstrip())
            continue

    for lines in listLines:
        if lines.__contains__("Working file"):
            fileName = lines.split(":")[1]
        if lines.__contains__("total revisions"):
            a = lines.split("\t")
            #print a
            b = a[1].split(":")
            countRev = int(b[1])
            #print countRev,maxNumberOfRevisions
            if countRev > maxNumberOfRevisions:
                maxNumberOfRevisions = countRev
                maxFileName = fileName
        if lines.__contains__("author"):
            authorindex = lines.find("author")
            authorname = lines[authorindex+7:lines.find(";",authorindex)]
            authorSet.add(authorname)


    listLines = []

print "Number of Files: ", count
print "Most Number of Revisions:",maxNumberOfRevisions
print "File Name:",maxFileName
print "Max Author File: ", maxAuthorFileName, "NumberOfAuthors: ",maxAuthorSize









