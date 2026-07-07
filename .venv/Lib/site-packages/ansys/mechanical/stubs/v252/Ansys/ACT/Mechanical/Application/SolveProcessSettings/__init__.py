"""SolveProcessSettings module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ILinuxSettings(object):

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        
            Gets or sets whether or not manual linux settings are enable for the configuration.
            
        """
        return None

    @property
    def UserName(self) -> typing.Optional[str]:
        """
        
            Gets or sets the user name field for the manual linux settings.
            
        """
        return None

    @property
    def WorkingFolder(self) -> typing.Optional[str]:
        """
        
            Gets or sets the working folder field for the manual linxus settings.
            
        """
        return None


class IQueueSettings(object):

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets or sets the name of the current queue for the configuration.
            
        """
        return None

    @property
    def JobName(self) -> typing.Optional[str]:
        """
        
            Gets or sets the Job Name field for the queue settings.
            
        """
        return None

    @property
    def License(self) -> typing.Optional[str]:
        """
        
            Gets or sets the License field for the queue settings.
            
        """
        return None

    @property
    def DCSUrl(self) -> typing.Optional[str]:
        """
        DCSUrl property.
        """
        return None

    @property
    def SolutionExecutionTarget(self) -> typing.Optional[str]:
        """
        SolutionExecutionTarget property.
        """
        return None

    @property
    def DCSUsername(self) -> typing.Optional[str]:
        """
        DCSUsername property.
        """
        return None

    @property
    def DCSPassword(self) -> typing.Optional[str]:
        """
        DCSPassword property.
        """
        return None


class ISolveConfiguration(object):

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets or sets the name of the SolveConfiguraiton Object
            
        """
        return None

    @property
    def Default(self) -> typing.Optional[bool]:
        """
        
            Gets whether or not this SolveConfiguration is the default configuration.
            
        """
        return None

    @property
    def Settings(self) -> typing.Optional[Ansys.ACT.Mechanical.Application.SolveProcessSettings.IQueueSettings]:
        """
        
            Gets the QueueSettings object for the configuration.
            
        """
        return None

    @property
    def SolveProcessSettings(self) -> typing.Optional[Ansys.ACT.Mechanical.Application.SolveProcessSettings.ISolveProcessSettings]:
        """
        
            Gets the SolveProcessSettings for the current object.
            
        """
        return None

    def SetAsDefault(self) -> None:
        """
        
            Sets 'this' to be the default configuration to solve with.
            
        """
        pass


class ISolveProcessSettings(object):

    @property
    def DistributeSolution(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the boolean "Distribute Solution (if possible)" field.
            
        """
        return None

    @property
    def MaxNumberOfCores(self) -> typing.Optional[int]:
        """
        
            Gets or sets the "Maximum number of utilized cores" field.
            
        """
        return None

    @property
    def NumberOfGPUDevices(self) -> typing.Optional[int]:
        """
        
            Gets or sets the "Number of utilized GPU devices" field.
            
        """
        return None

    @property
    def AdditionalCommandLineArguments(self) -> typing.Optional[str]:
        """
        
            Gets or sets the "Additional Command Line Arguments" field.
            
        """
        return None

    @property
    def CustomExecutablePath(self) -> typing.Optional[str]:
        """
        
            Gets or sets the "Custom Executable Name (with path)" field.
            
        """
        return None

    @property
    def UserString(self) -> typing.Optional[str]:
        """
        
            Gets or sets the User String field.
            
        """
        return None

    @property
    def LicenseQueuing(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the "License Queuing: Wait for Available License" field.
            
        """
        return None

    @property
    def UseSharedLicense(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the "Use Shared License, if possible" field.
            
        """
        return None

    @property
    def SolveInSynchronousMode(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the "Solve in synchronous mode" field.
            
        """
        return None

    @property
    def ManualSolverMemorySettings(self) -> typing.Optional[Ansys.ACT.Mechanical.Application.SolveProcessSettings.ISolverMemorySettings]:
        """
        
            Gets the SolverMemorySettings object for the configuration.
            
        """
        return None

    @property
    def ManualLinuxSettings(self) -> typing.Optional[Ansys.ACT.Mechanical.Application.SolveProcessSettings.ILinuxSettings]:
        """
        
            Gets the LinuxSettings object for the configuration.
            
        """
        return None

    @property
    def GPUAccelerationDevice(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GPUAccelerationDevicesType]:
        """
        
            Gets or sets the "GPU Acceleration Device" field.
            
        """
        return None

    @property
    def HybridParallel(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the boolean "Hybrid Parallel (Mechanical APDL)" field.
            
        """
        return None

    @property
    def ThreadsPerProcess(self) -> typing.Optional[int]:
        """
        
            Gets or sets the "Threads per process" field.
            
        """
        return None

    @property
    def NumberOfProcesses(self) -> typing.Optional[int]:
        """
        
            Gets or sets the "Number of processes" field.
            
        """
        return None

    @property
    def DCSAutoDownloadResults(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the "DCS Auto Download Results" field.
            
        """
        return None


class ISolverMemorySettings(object):

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        
            Gets or sets whether or not manual memory settings are active in the current configuration.
            
        """
        return None

    @property
    def Workspace(self) -> typing.Optional[int]:
        """
        
            Gets or sets the workspace memory amount (megabytes).
            
        """
        return None

    @property
    def Database(self) -> typing.Optional[int]:
        """
        
            Gets or sets the database memory amount (MB).
            
        """
        return None


class SolveConfigurations(object):
    """
    
            The application's collection of solve configurations.
            
    """

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            The number of solve configurations in the collection.
            
        """
        return None

    def Add(self, item: Ansys.ACT.Mechanical.Application.SolveProcessSettings.SolveConfiguration) -> None:
        """
        
            Adds the given SolveConfiguration object to the collection.
            
        """
        pass

    def Remove(self, item: Ansys.ACT.Mechanical.Application.SolveProcessSettings.SolveConfiguration) -> bool:
        """
        
            Removes the given SolveConfiguration from the collection.
            
        """
        pass


class LinuxSettings(object):
    """
    
            The class representing the linux settings portion of the solve process settings.
            
    """

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        
             Whether the linux settings are active.
            
        """
        return None

    @property
    def UserName(self) -> typing.Optional[str]:
        """
        
            The user name.
            
        """
        return None

    @property
    def WorkingFolder(self) -> typing.Optional[str]:
        """
        
            The working folder.
            
        """
        return None


class QueueSettings(object):
    """
    
            The class representing queue settings.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            The name of the queue settings.
            
        """
        return None

    @property
    def JobName(self) -> typing.Optional[str]:
        """
        
            The job name of the queue settings.
            
        """
        return None

    @property
    def License(self) -> typing.Optional[str]:
        """
        
            The license of the queue settings.  The setter will throw an exception if the given license is not valid.
            
        """
        return None


class RSMQueue(object):
    """
    
            The class representing an RSM Queue.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            The name of the RSM Queue.
            
        """
        return None

    @property
    def HPCConfiguration(self) -> typing.Optional[str]:
        """
        
            The HPC configuration of the RSM Queue.
            
        """
        return None

    @property
    def HPCQueue(self) -> typing.Optional[str]:
        """
        
            The HPC Queue of the RSM Queue.
            
        """
        return None

    @property
    def HPCType(self) -> typing.Optional[str]:
        """
        
            The HPC type of the RSM Queue
            
        """
        return None


class SolveConfiguration(object):
    """
    
            The class representing a solve configuration.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            The name of the solve configuration.
            
        """
        return None

    @property
    def Default(self) -> typing.Optional[bool]:
        """
        
            Whether this solve configuration is the default.
            
        """
        return None

    @property
    def Settings(self) -> typing.Optional[Ansys.ACT.Mechanical.Application.SolveProcessSettings.QueueSettings]:
        """
        
            Returns the queue settings of this solve configuration.
            
        """
        return None

    @property
    def SolveProcessSettings(self) -> typing.Optional[Ansys.ACT.Mechanical.Application.SolveProcessSettings.SolveProcessSettings]:
        """
        
            Returns the solve process settings of this solve configuration.
            
        """
        return None

    def SetAsDefault(self) -> None:
        """
        
            Sets this solve configuration as the default.
            
        """
        pass


class SolverMemorySettings(object):
    """
    
            The class representing the solver memory settings portion of the solve process settings.
            
    """

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        
             Whether the solver memory settings are active.
            
        """
        return None

    @property
    def Workspace(self) -> typing.Optional[int]:
        """
        
             Workspace size.
            
        """
        return None

    @property
    def Database(self) -> typing.Optional[int]:
        """
        
             Database size.
            
        """
        return None


class SolveProcessSettings(object):
    """
    
            The class representing solve process settings.
            
    """

    @property
    def DistributeSolution(self) -> typing.Optional[bool]:
        """
        
            Whether to run the solution in distributed mode.
            
        """
        return None

    @property
    def MaxNumberOfCores(self) -> typing.Optional[int]:
        """
        
            The maximum number of cores the solver will use.
            
        """
        return None

    @property
    def NumberOfGPUDevices(self) -> typing.Optional[int]:
        """
        
            The number of GPU devices.
            
        """
        return None

    @property
    def AdditionalCommandLineArguments(self) -> typing.Optional[str]:
        """
        
            Any additional command line arguments to give to the solver.
            
        """
        return None

    @property
    def CustomExecutablePath(self) -> typing.Optional[str]:
        """
        
            The custom executable path for user programmable features in the solver.
            
        """
        return None

    @property
    def LicenseQueuing(self) -> typing.Optional[bool]:
        """
        
            Whether license queueing is active.
            
        """
        return None

    @property
    def UseSharedLicense(self) -> typing.Optional[bool]:
        """
        
            Whether the solver will use a shared license.
            
        """
        return None

    @property
    def SolveInSynchronousMode(self) -> typing.Optional[bool]:
        """
        
            Whether the solve will be in synchronous mode.
            
        """
        return None

    @property
    def ManualSolverMemorySettings(self) -> typing.Optional[Ansys.ACT.Mechanical.Application.SolveProcessSettings.SolverMemorySettings]:
        """
        
            Returns the manual solver memory settings.
            
        """
        return None

    @property
    def ManualLinuxSettings(self) -> typing.Optional[Ansys.ACT.Mechanical.Application.SolveProcessSettings.LinuxSettings]:
        """
        
            Returns the manual linux settings.
            
        """
        return None

    @property
    def GPUAccelerationDevice(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GPUAccelerationDevicesType]:
        """
        
            The GPU Acceleration device the solver will use.
            
        """
        return None

    @property
    def HybridParallel(self) -> typing.Optional[bool]:
        """
        
            Whether to run the solution in hybrid parallel.
            
        """
        return None

    @property
    def ThreadsPerProcess(self) -> typing.Optional[int]:
        """
        
            The threads per process the solver will use.
            
        """
        return None

    @property
    def NumberOfProcesses(self) -> typing.Optional[int]:
        """
        
            The number of processes the solver will use.
            
        """
        return None

    @property
    def DCSAutoDownloadResults(self) -> typing.Optional[bool]:
        """
        
            Whether results need to be automatically downloaded for DCS job after completion.
            
        """
        return None


