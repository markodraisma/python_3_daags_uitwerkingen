#!/usr/bin/env python3
class SortedDict(dict):
    """gedraagt zich als dict, maar met gesorteerde keys
    """
    def keys(self):
        """geef de keys in de dict als gesorteerde list terug
        """
        return sorted( super().keys() )

    def __iter__(self):
        """doorloop de dictionary in gesorteerde volgorde
        """
        return iter(self.keys())

    def __str__(self):
        """druk de dictionary gesorteerd af
        """
        return { a:self[a] for a in self.keys() }.__str__()

if __name__=='__main__':
    n = SortedDict({'allo': 3,'hallo': 2, 'nee': 9, 'hoi': 5})
    print(n)
    l = SortedDict()
    l["hoi"] = 5
    l["hallo"] = 2
    l["allo"] = 3
    l["nee"] = 9
    for k in l:
        print(k, l[k])
    print(l)
