import argparse
import re

def StripFileExtension(fileName):
    return fileName.split(".h")[0]

def ClassNameToSymbol(className):
    camelCaseList = re.findall('[a-zA-Z][^A-Z]*', className)
    result = ""
    for word in camelCaseList:
        result += word.upper() +"_"
    result += "H"
    return result

def GenerateOpenIFDef(className):
    symbolName = ClassNameToSymbol(className)
    ifDefString = "#ifndef " + symbolName + "\n"
    defineString = "#define " + symbolName + "\n"
    return ifDefString + defineString + "\n"

def GenerateCloseIFDef(className):
    return "#endif // " + ClassNameToSymbol(className)

def GenerateInheritance(className, interfaceEnabled):
    if interfaceEnabled:
        return " : public I" + className
    return ""

def GenerateOpenClassCode(className, interfaceEnabled=False):
    return "class " + className + GenerateInheritance(className, interfaceEnabled) + "\n{\n"

def GenerateCloseClassCode():
    return "\n};\n\n"


def WriteHeader(className):
    with open(className + ".h", "w") as outputFile:
        outputFile.write(GenerateOpenIFDef(className))
        outputFile.write(GenerateOpenClassCode(className))
        outputFile.write(GenerateCloseClassCode())
        outputFile.write(GenerateCloseIFDef(className))

