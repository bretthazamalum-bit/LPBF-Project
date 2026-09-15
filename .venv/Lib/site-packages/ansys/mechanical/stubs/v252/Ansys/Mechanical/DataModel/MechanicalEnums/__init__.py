"""MechanicalEnums module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.Table as Table
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.SMARTCrackGrowth as SMARTCrackGrowth
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.Common as Common
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.Materials as Materials
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData as ExternalData
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.CompositeFailure as CompositeFailure
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.FluidPenetrationPressure as FluidPenetrationPressure
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.CondensedParts as CondensedParts
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.MeshWorkflow as MeshWorkflow
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.Charts as Charts
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.SolutionCombination as SolutionCombination
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.Substructure as Substructure
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.BoundaryConditions as BoundaryConditions
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.MorphControl as MorphControl
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.Graphics as Graphics
import ansys.mechanical.stubs.v252.Ansys.Mechanical.DataModel.MechanicalEnums.CrackInitiation as CrackInitiation


class MultizoneMappedMeshType(Enum):
    """
    To select Multizone Mesh Type.
    """

    AllQuad = 0
    QuadTri = 1
    AllTri = 2

