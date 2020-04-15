from .abc import MoleculeABC
from ..algorithms.isomorphism import Isomorphism
from typing import Dict


class Molecule(Isomorphism, MoleculeABC):
    def __init__(self, atoms: Dict, bonds: Dict):
        super().__init__()
        if isinstance(atoms, dict) and isinstance(bonds, dict):
            self._atoms = atoms
            self._bonds = bonds
        else:
            print('Atoms and bonds must be dictionary')
            raise TypeError

    def add_atom(self, element: str, number: int):
        if number in self._atoms:
            print('Atom has already exist')
            raise IndexError
        else:
            self._atoms[number] = element

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom == end_atom:
            print('Atom cannot have a bond with itself')
            raise ValueError
        elif start_atom in self._bonds and end_atom in self._bonds[start_atom]:
            print('Bond has already exist')
            raise IndexError
        elif start_atom in self._bonds:
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[end_atom][start_atom] = bond_type
        else:
            self._bonds[start_atom] = {end_atom: bond_type}
            self._bonds[end_atom] = {start_atom: bond_type}


__all__ = ['Molecule']