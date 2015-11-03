__author__ = 'sanymathew'
import operator

f = open('emacs.log','r')
count = 0;
maxNumberOfRevisions = 0;
maxFileName = ""
listLines = []
authorSet = set()
maxAuthorSize = 0
maxAuthorFileName = ""
authorCount = dict()
fileName = ""
mostCommits = 0
for line in f:
    if (line.__contains__("===")):
        count = count + 1

        authorLen = len(authorSet)
        if (authorLen > maxAuthorSize):
            maxAuthorSize = authorLen
            maxAuthorFileName = fileName

        if len(authorCount) > 0:
            mostCommits = max(authorCount.iteritems(), key = operator.itemgetter(1))[0]
        print fileName, mostCommits, ":", authorCount.get(mostCommits)
        authorSet = set()
        authorCount = dict()
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
        if lines.__contains__("author:"):
            authorindex = lines.find("author:")
            authorname = lines[authorindex+7:lines.find(";",authorindex)]
            authorSet.add(authorname)
            if(authorCount.has_key(authorname)):
                newCount = authorCount.get(authorname)+1
                authorCount.__setitem__(authorname,newCount)
            else:
                authorCount.__setitem__(authorname,1)


    listLines = []

print "Number of Files: ", count
print "Most Number of Revisions:",maxNumberOfRevisions
print "File Name:",maxFileName
print "Max Author File: ", maxAuthorFileName, "NumberOfAuthors: ",maxAuthorSize










