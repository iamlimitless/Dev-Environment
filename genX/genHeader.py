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

def GenerateClassCode(className):
    return "class " + className + "\n{\n};\n\n"

def WriteHeader(className):
    with open(className + ".h", "w") as outputFile:
        outputFile.write(GenerateOpenIFDef(className))
        outputFile.write(GenerateClassCode(className))
        outputFile.write(GenerateCloseIFDef(className))

def main():
    parser = argparse.ArgumentParser(description="Configure C++ Header Generator")
    parser.add_argument('className', type=str, help="class name for which to generate header files")

    args = parser.parse_args()
    className = StripFileExtension(args.className)

    WriteHeader(className)


if __name__ == "__main__":
    main()
