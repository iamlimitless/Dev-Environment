import argparse

#TODO extend this to generate a header file that overrides an interface

def AddBraces(signature):
    return signature + "\n{\n}\n\n"

def AddOverride(signature):
    return signature.split(";")[0] + " override;"

def IsFunctionPrototype(line):
    return "(" in line and line.endswith(";\n") and "default" not in line and "delete" not in line and "/" not in line and line.lstrip()[0] != "*"

def ParsePrototypeLine(prototypeList):
    functionFound = False
    returnType = ""
    function = ""
    qualifiers = ""
    
    for word in prototypeList:
        if "(" in word:
            function = word
            functionFound = True
            continue
        if functionFound:
            qualifiers += word + " "
        else:
            returnType += word + " "
    return returnType, function, qualifiers.split(";")[0]


def GenerateSignature(className, prototypeLine):
    returnType, function, qualifiers = ParsePrototypeLine(prototypeLine.split())
    return returnType + className + "::" + function + " " + qualifiers


def ParseFile(headerFile):
    #parses file for className and header list
    className = ""
    prototypeList = []
    for line in headerFile:
        if line.startswith("class"):
            className = line.split()[1]
        if IsFunctionPrototype(line): 
            prototypeList.append(line)
    return(prototypeList, className)


def WriteSource(header, interfaceEnabled):
    with open(header, "r") as headerFile:
        functionList, className = ParseFile(headerFile)

    sourceFile = header.split(".h")[0] + ".cpp"
    with open(sourceFile, "w") as sourceFile:
        sourceFile.write("#include \"" + header + "\"\n\n")
        for func in functionList:
            if interfaceEnabled:
                sourceFile.write(AddOverride(func))
            else:
                sourceFile.write(AddBraces(GenerateSignature(className, func)))

def main():
    parser = argparse.ArgumentParser(description="Configure C++ Source Generator")
    parser.add_argument('fileName', type=str, help="Header file for which to generate source for")
    parser.add_argument('interface', type=bool, default=false, help="Generate in interface mode")

    args = parser.parse_args()
    headerFile = args.fileName

    WriteSource(headerFile, args.interface)


if __name__ == "__main__":
    main()
