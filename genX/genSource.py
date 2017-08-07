import argparse
import genHeader


#TODO might be cleaner to make these classes? wouldn't have to pass className around.

def AddBraces(signature):
    return signature + "\n{\n}\n\n"

def AddOverride(signature):
    return signature.split("= 0")[0] + "override;\n\n"

def IsFunctionPrototype(line):
    return "(" in line and line.endswith(";\n") and "default" not in line and "delete" not in line and "/" not in line and line.lstrip()[0] != "*"

def ParsePrototypeLine(prototypeList):
    functionFound = False
    function = returnType = qualifiers = ""
    
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
    className = ""
    prototypeList = []
    for line in headerFile:
        if line.startswith("class"):
            className = line.split()[1]
        if IsFunctionPrototype(line): 
            prototypeList.append(line)
    return(prototypeList, className)


def GenerateOutputFileName(header, interfaceEnabled):
    if interfaceEnabled:
        return header[1:]
    else:
        return header.split(".h")[0] + ".cpp"

def ParseHeader(header):
    with open(header, "r") as headerFile:
         return ParseFile(headerFile)

def WriteInterfaceFile(header, filename, functionList, className):
    with open(filename, "w") as outfile:
        outfile.write(genHeader.GenerateOpenIFDef(className))
        outfile.write("#include \"" + header + "\"\n\n")
        outfile.write(genHeader.GenerateOpenClassCode(className, True))
        for func in functionList:
            outfile.write(AddOverride(func))

        outfile.write(genHeader.GenerateCloseClassCode())
        outfile.write(genHeader.GenerateCloseIFDef(className))

def WriteSourceFile(header, filename, functionList, className):
    with open(filename, "w") as outfile:
        outfile.write("#include \"" + header + "\"\n\n")
        for func in functionList:
            outfile.write(AddBraces(GenerateSignature(className, func)))

def WriteSource(header, interfaceEnabled=False):
    functionList, className = ParseHeader(header)
    filename = GenerateOutputFileName(header, interfaceEnabled) 

    if interfaceEnabled:
        WriteInterfaceFile(header, filename, functionList, className[1:])
    else:
        WriteSourceFile(header, filename, functionList, className)

def ParseCmdArguments():
    parser = argparse.ArgumentParser(description="Configure C++ Source Generator")
    parser.add_argument('fileName', type=str, help="File name to generate source for. If there is no extension provided it is assumed we want a header file called <fileName>.h")
    parser.add_argument('type', type=str, default="header", help="What type of source to generate. Options are header, source, or interface")
    args = parser.parse_args()
    return args.fileName, args.type


def main():

    filename, fileType = ParseCmdArguments()

    if fileType == "header":
        genHeader.WriteHeader(genHeader.StripFileExtension(filename))
    elif fileType == "source":
        WriteSource(filename)
    elif fileType == "interface":
        WriteSource(filename, True)
    else:
        print("Invalid file type provided. Valid types are header, source, and interface")


if __name__ == "__main__":
    main()
