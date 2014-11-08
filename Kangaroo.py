class Kangaroo( object ):

    def __init__( self ):
        self.pouch_contents = []

    def __str__( self ):
        contents = ""
        for i in self.pouch_contents:
            contents+= str(i) + " "
        return contents

    def put_in_pouch(self, contents):
        self.pouch_contents.append(contents)

roo = Kangaroo()
roo.put_in_pouch("roo")
kanga = Kangaroo()
kanga.put_in_pouch("kanga")
kanga.put_in_pouch(roo)
print kanga
