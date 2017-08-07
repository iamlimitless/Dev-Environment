import argparse
import genHeader

#TODO refactor and clean up. See if we can merge/ combine code between files for genSource and genHeader 

def AddBraces(signature):
    return signature + "\n{\n}\n\n"

def AddOverride(signature):
    return signature.split("= 0")[0] + "override;\n\n"

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


def GenerateOutputFileName(header, interfaceEnabled):
    if interfaceEnabled:
        return header[1:]
    else:
        return header.split(".h")[0] + ".cpp"

def WriteSource(header, interfaceEnabled):
    with open(header, "r") as headerFile:
        functionList, className = ParseFile(headerFile)

    filename = GenerateOutputFileName(header, interfaceEnabled) 
    
    with open(filename, "w") as outfile:
        if interfaceEnabled:
            className = genHeader.StripFileExtension(filename)
            outfile.write(genHeader.GenerateOpenIFDef(className))
            outfile.write("#include \"" + header + "\"\n\n")
            outfile.write(genHeader.GenerateClassCode(className).split("}")[0] + "\n")
        else:
            outfile.write("#include \"" + header + "\"\n\n")

        for func in functionList:
            if interfaceEnabled:
                outfile.write(AddOverride(func))
            else:
                outfile.write(AddBraces(GenerateSignature(className, func)))

        if interfaceEnabled:
            outfile.write("};\n\n")
            outfile.write(genHeader.GenerateCloseIFDef(genHeader.StripFileExtension(filename)))

def main():
    parser = argparse.ArgumentParser(description="Configure C++ Source Generator")
    parser.add_argument('fileName', type=str, help="Header file for which to generate source for")
    parser.add_argument('interface', type=bool, default=False, help="Generate in interface mode")

    args = parser.parse_args()
    headerFile = args.fileName

    WriteSource(headerFile, args.interface)


if __name__ == "__main__":
    main()
