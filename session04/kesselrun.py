
START = "Kessel"
BOAT = "Millenium Falcon"
FINISH = "Si'Klaata Cluster"

FISSILE_MATS = "perfectly safe fissile material"
LEAKY_NEUTRAL_DAMPER = "sealed neutral damper"
PLASTIPHAGE_GOOP_EVERYWHERE_DAMMIT = "plastiphages (extreme biohazard!)"

class KesselRun:

    def __init__(self):
        self._parsecs = 4   # So mean!
        self._boat = START
        self._cargo = { FISSILE_MATS: START, LEAKY_NEUTRAL_DAMPER: START, PLASTIPHAGE_GOOP_EVERYWHERE_DAMMIT: START }

    def Status(self):
        print( "Looking good - no Imps in sight!")

    def Parsecs(self):
        return self._parsecs

    def IsComplete(self):
        if self._parsecs >= 12:
            return False
        for v in self._cargo.values():
            if v != FINISH:
                return False
        return self._boat == FINISH

    def LoadRadioactiveHazard(self):
        self.LoadCargo(FISSILE_MATS)
    
    def LoadExplosiveTriggers(self):
        self.LoadCargo(LEAKY_NEUTRAL_DAMPER)

    def LoadBiohazard(self):
        self.LoadCargo(PLASTIPHAGE_GOOP_EVERYWHERE_DAMMIT)
        
    def LoadCargo(self, item):
        if self._cargo[item] == self._boat:
            self._cargo[item] = BOAT
        else:
            raise Exception(f"Crew cannot locate {item}! You disband pronto, before the Syndicate catches up with you!")

    def Unload(self):
        n = 0
        for (k, v) in self._cargo.items():
            if v == BOAT:
                n += 1
                self._cargo[k] = self._boat
        if n == 0:
            raise Exception("You hunt high and low but the cargo is gone! You are the laughing stock of the Edge! Don't expect another job this side of the Maw :(")

    def ToFarSide(self):
        self._parsecs += 1
        self._checkParsecs()
        self._checkLoading()
        self._boat = FINISH
        self._checkCargo()

    def ReturnTrip(self):
        self._parsecs += 1
        self._checkParsecs()
        self._checkLoading()
        self._boat = START

    def _checkParsecs(self):
        if self._parsecs >= 12:
            raise Exception("Tsk! Even rounding down, you're no Hans Solo .... wait until he hears about this! You'll never live it down!")

    def _checkLoading(self):
        if len([ k for (k, v) in self._cargo.items() if v == BOAT ]) > 1:
            raise Exception("Danger! Insufficient fuel for this cargo run! Unable to make stable orbit. WE ARE LOST IN SPACE!")

    def _checkCargo(self):
        if self._boat != START:
            self._checkKesselSituation()
        elif self._boat != FINISH():
            self._checkSiKlaataSituation() 

    def _checkKesselSituation(self):
        includes = set()
        for (k, v) in self._cargo.items():
            if v == START:
                includes.add(k)
        self._checkCargoSafety(includes)

    def _checkSiKlaataSituation(self):
        for (k, v) in self._cargo.items():
            if v == FINISH:
                includes.add(k)
        self._checkCargoSafety(includes)        

    def _checkCargoSafety(self, includes):
        if FISSILE_MATS in includes and LEAKY_NEUTRAL_DAMPER in includes:
            raise Exception(f"A gigantic explosion engulfs the warehouse you left the {FISSILE_MATS} ... maybe the sealing on the {LEAKY_NEUTRAL_DAMPER} ...")
        if PLASTIPHAGE_GOOP_EVERYWHERE_DAMMIT in includes and LEAKY_NEUTRAL_DAMPER in includes:
            raise Exception(f"What is this goo ... uh oh, I guess the {PLASTIPHAGE_GOOP_EVERYWHERE_DAMMIT} has found the {LEAKY_NEUTRAL_DAMPER}. Errr ... help?!")

if __name__ == "__main__":
    print("Create an instance of KesselRun and complete it in under 12 parsecs!")
    p = KesselRun()
    p.LoadExplosiveTriggers()
    p.ToFarSide()
    p.Unload()
    p.ReturnTrip()
    p.LoadRadioactiveHazard()
    p.ToFarSide()
    p.Unload()
    p.LoadExplosiveTriggers()
    p.ReturnTrip()
    p.Unload()
    p.LoadBiohazard()
    p.ToFarSide()
    p.Unload()
    p.ReturnTrip()
    p.LoadExplosiveTriggers()
    p.ToFarSide()
    p.Unload()
    print( f"Complete = {p.IsComplete()}" )