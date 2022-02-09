# m = TreeMaker()
# m.add( key: str, value: Any )
# m.start( key: str )
# m.end()
# m.make() -> Dict[str, Any]

from typing import Dict, Any

class TreeMaker:

    def __init__( self ):
        self._focus = {}
        self._dump = []

    def add( self, **kwargs ):
        self._focus.update( kwargs )

    def start( self, key: str ):
        new = {}
        self._focus[ key ] = new
        self._dump.append( self._focus )
        self._focus = new

    def end( self ):
        self._focus = self._dump.pop()

    def make( self ) -> Dict[str, Any]:
        result = self._focus
        self._focus = {}
        return result

if __name__ == "__main__":
    m = TreeMaker()
    m.add( name = 'Stephen' )
    m.add( age = 62 )
    m.start( 'activities' )
    m.start( 'coding' )
    m.add( duration = 45 )
    m.end()
    m.start( 'birdwatching' )
    m.add( duration = 40 )
    m.end()
    m.end()
    tree = m.make()
    print( tree )
    # {'name': 'Stephen', 'age': 62, 'activities': {'coding': {'duration': 45}, 'birdwatching': {'duration': 40}}}

