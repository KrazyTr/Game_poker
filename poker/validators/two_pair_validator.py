class TwoPairValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Two Pair"

    def is_valid(self):
        ranks_with_two_pair = self._ranks_with_count(2)
        return len(ranks_with_two_pair) >= 2
    
    def valid_cards(self):
        ranks_with_pair = self._ranks_with_count(2)
        cards = [card for card in self.cards if card.rank in ranks_with_pair.keys()]
        return cards
    
    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }
    
    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts