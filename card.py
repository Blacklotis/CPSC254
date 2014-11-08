class Card( object ):

    def __init__( self, rank, suit ):

        self.rank= rank

        self.suit= suit

        self.points= rank

    def __str__( self ):

        return "%2d%s" % (self.rank, self.suit)

    def hard( self ):

        return self.points

    def soft( self ):

        return self.points

d = Card (4,"D")

print d
