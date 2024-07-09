from io import StringIO

struct_name = "vac_winapi"
member_size = 4


import_list = """
LoadLibraryExA
GetProcAddress
NtOpenProcess
FreeLibrary
GetVolumeInformationW
GetFileInformationByHandleEx
QueryFullProcessImageNameW
GetLastError
OpenProcess
CryptMsgGetParam
OpenSCManagerA
GetTokenInformation
CertCloseStore
WideCharToMultiByte
GetModuleHandleExA
SetFilePointerEx
FindFirstVolumeW
Module32FirstW
CryptMsgClose
GetFileVersionInfoSizeA
GetCurrentProcess
GetModuleInformation
VerQueryValueA
FlushInstructionCache
Sleep
ResumeThread
WinVerifyTrust
GetModuleFileNameExA
GetCurrentThread
GetProcessId
GetFileInformationByHandle
GetVolumePathNamesForVolumeNameW
SetupDiGetClassDevsA
CreateToolhelp32Snapshot
ConvertSidToStringSidA
WriteFile
NtWow64QueryVirtualMemory64
GetModuleBaseNameA
RegEnumKeyExA
CertGetNameStringW
GetSystemDirectoryW
GetProcessImageFileNameA
QueryServiceConfigA
GetUserNameExW
IsBadReadPtr
CryptQueryObject
GetFileVersionInfoSizeW
CloseServiceHandle
RegQueryValueExA
NtQuerySystemInformation
GetVolumeInformationByHandleW
EncodePointer
OpenThread
GetFileVersionInfoA
QueryServiceConfigW
NtMapViewOfSection
ReadFile
GetProcessTimes
CertFindCertificateInStore
EnumServicesStatusA
VerQueryValueW
GetComputerNameExW
GetMappedFileNameW
VirtualQueryEx
GetThreadId
GetProcessHeap
GetModuleBaseNameW
GetModuleFileNameExW
CloseHandle
NtQueryInformationThread
OpenProcessToken
MultiByteToWideChar
VirtualFreeEx
Module32NextW
OpenServiceA
OpenServiceW
EnumServicesStatusW
GetFileSizeEx
LookupPrivilegeValueA
GetThreadContext
GetWindowsDirectoryW
HeapAlloc
Heap32First
UnmapViewOfFile
RegCloseKey
GetUdp6Table
EnumProcessModules
MapViewOfFile
NtDuplicateObject
Thread32Next
CreateFileW
StackWalk64
HeapFree
NtWow64ReadVirtualMemory64
GetProcessImageFileNameW
NtOpenSection
CreateFileMappingW
QueryDosDeviceA
GetVersionExW
SwitchToThread
WriteProcessMemory
LocalAlloc
EnumProcesses
GetFileVersionInfoW
NtQueryObject
NtWow64QueryInformationProcess64
QueryDosDeviceW
WinVerifyTrustEx
GetCurrentProcessId
GetTcp6Table
SetThreadAffinityMask
VirtualAlloc
VirtualQuery
SetFilePointer
Process32FirstW
CreateRemoteThread
NtQueryVirtualMemory
SuspendThread
CryptDecodeObject
NtQueryInformationProcess
LoadLibraryA
SetupDiGetDeviceRegistryPropertyA
FindVolumeClose
NtReadVirtualMemory
IsWow64Process
GetModuleHandleA
GetDriveTypeW
RegQueryInfoKeyA
AdjustTokenPrivileges
Thread32First
GetVersionExA
FindNextVolumeW
GetCurrentThreadId
NtQueryDirectoryObject
RtlGetCompressionWorkSpaceSize
GetSystemDirectoryA
SetupDiDestroyDeviceInfoList
GetUserProfileDirectoryA
GetTickCount
ReadProcessMemory
VirtualFree
CryptHashCertificate
VirtualAllocEx
NtClose
Process32NextW
CertFreeCertificateContext
NtOpenDirectoryObject
GetSystemTimeAsFileTime
OutputDebugStringA
GetUserProfileDirectoryW
AddVectoredExceptionHandler
GetSystemInfo
GetModuleFileNameA
WaitForSingleObject
SymFunctionTableAccess64
SetupDiEnumDeviceInfo
SetLastError
GetUdpTable
LocalFree
RegOpenKeyExA
NtQuerySection
SymGetModuleBase64
GetFileSize
RtlDecompressBufferEx
VirtualProtect
GetLogicalDriveStringsA
OpenFileById
GetLogicalDriveStringsW
CreateFileA
GetTcpTable
GetWindowsDirectoryA
GetMappedFileNameA
NtQuerySystemInformation
GetVersion
GetNativeSystemInfo
Wow64EnableWow64FsRedirection
"""

def add_member(struct_id, member_name):
   idc.add_struc_member(struct_id, member_name.rstrip(), -1, idc.FF_DWORD, -1, member_size)

import_buffer = StringIO(import_list)

struct_id = idc.add_struc(-1, struct_name, 0)

for line in import_buffer:
  add_member(struct_id, line)
  
number_of_items = len(import_list.splitlines())

print(f"added all members ({number_of_items}) to struct {struct_name}")