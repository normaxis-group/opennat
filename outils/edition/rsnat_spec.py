# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""La spécification du RSNat est dans le moteur (`opennat/rsnat_spec.py`) : une seule définition sert au schéma XSD,
au schéma JSON, au dictionnaire de la partie 7 et à la sortie du moteur."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from opennat.rsnat_spec import *  # noqa: E402,F401,F403
from opennat.rsnat_spec import E, F, ENUMS, RACINE  # noqa: E402,F401
