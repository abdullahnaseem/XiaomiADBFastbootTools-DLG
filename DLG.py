import os


def clear():
    os.system('cls')
    print("")
    print("")
    print("-------------------------------------------------")
    print("Debloat List Generator for XiaomiADBFastbootTools")
    print("-------------------------------------------------")
    print("github./abdullahnaseem/XiaomiADBFastbootTools-DLG")
    print("-------------------------------------------------")
    print("")


def getpackagename(line):
    start = line.rfind("/") + len("/")
    end = line.find(".apk")
    packagename = line[start:end]
    # print("Package Name : {}".format(packagename))
    return packagename


def getpackage(line):
    package = line.split("=")[1]
    # print("Package : {}".format(package))
    return package


def checkfile(file):
    try:
        with open(file):
            return True
    except IOError:
        # print("File not accessible")
        return False


def cpl(file):
    with open(appsindex) as fp:

        line = fp.readline()
        line = line.replace('\n', '').replace('\r', '')

        packagename = getpackagename(line)
        package = getpackage(line)
        packagedict = {package: packagename}

        open(packagelist, 'w').close()

        while line:
            with open(packagelist, 'a') as templist:
                templist.write("{}:{}\n".format(package, packagename))
                # print('{}:{}'.format(package, packagename))

            line = fp.readline()
            line = line.replace('\n', '').replace('\r', '')

            if not line:
                return packagedict
                # break
            else:
                packagename = getpackagename(line)
                package = getpackage(line)
                packagedict[package] = packagename


def csl(file):
    with open(customindex) as fp:

        line = fp.readline()
        line = line.replace('\n', '').replace('\r', '')

        if line.startswith('com'):
            package = line  # com.miui.app
            packagename = False
            #print('{}:{}'.format(package, packagename))
        else:
            package = False
            packagename = line  # miui-app
            #print('{}:{}'.format(package, packagename))

        open(customlist, 'w').close()

        while line:
            with open(customlist, 'a') as custlist:
                if package:
                    if package in packagedict:
                        # print('Found Package')
                        packagename = packagedict.get(package)
                        custlist.write("{}:{}\n".format(package, packagename))
                        # custlist.write("{}\n".format(package))
                elif packagename:
                    for pkg, pkgn in packagedict.items():
                        if packagename == pkgn:
                            # print('Found Package Name')
                            package = pkg
                            custlist.write("{}:{}\n".format(package, packagename))
                            # custlist.write("{}\n".format(package))

            line = fp.readline()
            line = line.replace('\n', '').replace('\r', '')

            if not line:
                break
            else:
                if line.startswith('com'):
                    package = line  # com.miui.app
                    packagename = False
                    #print('{}:{}'.format(package, packagename))
                else:
                    package = False
                    packagename = line  # miui-app
                    #print('{}:{}'.format(package, packagename))


def cdl(file):
    with open(debloatindex) as fp:

        line = fp.readline()
        line = line.replace('\n', '').replace('\r', '')

        package = line

        open(debloatlist, 'w').close()

        while line:
            with open(debloatlist, 'a') as deblist:
                if package in packagedict:
                    packagename = packagedict.get(package)
                    deblist.write("{}:{}\n".format(package, packagename))

            line = fp.readline()
            line = line.replace('\n', '').replace('\r', '')

            if not line:
                break
            else:
                package = line


print("")
print("")
print("-------------------------------------------------")
print("Debloat List Generator for XiaomiADBFastbootTools")
print("-------------------------------------------------")
print("github./abdullahnaseem/XiaomiADBFastbootTools-DLG")
print("-------------------------------------------------")
print("")
print("")

# implement app.yml from documents

appsindex = 'apps.txt'
packagelist = 'package-list.txt'

debloatindex = 'debloat.txt'
debloatlist = 'debloat-list.txt'

customindex = 'custom.txt'
customlist = 'custom-list.txt'

packagedict = {}


print("Checking Files...")
input("Press Enter to continue...")
clear()


if checkfile(appsindex) is True:
    print('')
    print('--------------')
    print('App List Found')
    print('--------------')
    print('')
    print('Creating Package-List Now')
    input("Press Enter to continue...")
    packagedict = cpl(appsindex)
    if bool(packagedict):
        print("Successfully Created Package-List")
        print("{} created from {}".format(packagelist, appsindex))
    else: 
        print("There was an Error")
        print('The Program will now Exit')
        input("Press Enter to continue...")
        print('')
        exit()
else:
    print('')
    print('------------------')
    print('App List Not Found')
    print('------------------')
    print('')
    print('Please Create an App List')
    print('The Program will now Exit')
    input("Press Enter to continue...")
    # print('Connect Your Device and Run the Batch File')
    print('')
    exit()


if checkfile(customindex) is True:
    print('')
    print('-----------------')
    print('Custom List Found')
    print('-----------------')
    print('')
    print('Creating Custom-List Now')
    input("Press Enter to continue...")
    csl(customindex)
    print("Successfully Created Custom-List")
    print("{} created from {}".format(customlist, customindex))
    print('')
    input("Press Enter to continue...")
    clear()
    exit()


if checkfile(debloatindex) is True:
    print('')
    print('------------------')
    print('Debloat List Found')
    print('------------------')
    print('')
    print('Creating Debloat-List Now')
    input("Press Enter to continue...")
    cdl(debloatindex)
    print("Successfully Created Debloat-List")
    print("{} created from {}".format(debloatlist, debloatindex))
else:
    print('')
    print('----------------------')
    print('Debloat List Not Found')
    print('----------------------')
    print('')
    print('Please Get a Debloat List')
    print('The Program will now Exit')
    input("Press Enter to continue...")
    # print('Fetching Debloat List')
    print('')
    exit()


print('')
input("Press Enter to continue...")
clear()
