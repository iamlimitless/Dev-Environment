#include <iostream>
#include <dirent.h>

static const char* c_devPciPath = "/sys/bus/pci/devices";

//padding:bus:dev.func
void PrintPciSlotBusFunc(struct dirent* dir)
{
    std::string dirName = dir->d_name;
    size_t busStart = dirName.find(':');

    size_t busFinish = dirName.find(':', busStart+1);
    size_t funcStart = dirName.find('.', busFinish+1);

    if(busStart != std::string::npos && busFinish != std::string::npos && funcStart != std::string::npos)
    {
        std::string bus = dirName.substr(busStart+1, busFinish-(busStart+1));
        std::string slot = dirName.substr(busFinish+1, funcStart-(busFinish+1));
        std::string func = dirName.substr(funcStart+1);
        std::cout << "Bus " << bus << ", Slot/device " << slot << ", func " << func << '\n';
    }

}

int main()
{
    DIR *dirp = opendir(c_devPciPath);
    struct dirent *directory;
    
    if (dirp != nullptr)
    {
        while ((directory = readdir(dirp)) != NULL)
        {
            PrintPciSlotBusFunc(directory);
        }
        
        closedir(dirp);
    }
    return(0);
}
