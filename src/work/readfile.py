f = open('/Users/yupeng/Desktop/install3', 'r')
text = f.readlines()
list = [];
dependencelist = [];
for i in text:
    strlist = i.split('-')
    jar = strlist[-1]
    version = jar.split('.')
    version.pop()
    strlist.pop()
    componet = '-'.join(strlist)
    ver = '.'.join(version)
    str = 'mvn install:install-file -DgroupId=com.appengine -DartifactId=' + componet + ' -Dversion=' + ver + ' -Dpackaging=jar -Dfile=' + i
    list.append(str);
    dependence = '<dependency><groupId>com.appengine</groupId><artifactId>' + componet + '</artifactId><version>' + ver + '</version></dependency>\n'
    dependencelist.append(dependence)

with open('/Users/yupeng/Desktop/install2', 'w') as install:
    for p in list:
        install.write(p)
with open('/Users/yupeng/Desktop/dependence2', 'w') as depend:
    for q in dependencelist:
        depend.write(q)
