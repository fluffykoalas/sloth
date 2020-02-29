# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------


class ZeroFloat(float):
    """
    Special float type which returns zero if the amount to be subtracted is zero
    """
    
    def __sub__(self, other):
        return float(self) - float(other) if other != 0 else 0
