#Project Vision
#To handle storage of data in a format machine and human readable

#Input = [
#   0. 'pf',
#   1. '1',
#   2. [0, ['JamesBhunt', 'B'] OR [1,['JamesBhunt', 'B'],{'xyz':'sb', 'xyz':'bb', 'xtz':'utg'}],
#   3. {'B':'500', 'sb': '400', 'bb':'500', 'utg':'50'}
#]

class container:
    def __init__(self, info):
        stage_codes = {
            'pf':'Pre-Flop',
            'f':'Flop',
            't':'Turn',
            'r':'River',
        }

        current_stage = stage_codes[info[0]] + str(info[1])

        p_names_mod = info[2] #if player names are requred or not
        if p_names_mod[0] is 0:
            self.table = {
                'B':[''],
                'sb':[''],
                'bb':[''],
                'utg':[''],
                '1':[''],
                'co':[''],
            }
            self.table[p_names_mod[1][1]][0] = p_names_mod[1][0]

            for key in self.table:
                if self.table[key][0] is p_names_mod[1][0]:
                    pass
                else:
                    self.table[key][0] = str(key)
        stack_sizes = info[3]
        for key in stack_sizes:
            self.table[key].append(stack_sizes[key])

class tests():
    def main(self):
        info = ['pf', '1', [0, ['JamesBhunt', 'B']], {'B':'500', 'sb':'400', 'bb':'300'}]
        c = container(info)
        assertion = False

        for key in c.table:
            if key == c.table[key][0] or c.table[key][0] is 'JamesBhunt':
                pass
            else:
                return assertion

        print ('NamesFormatting : OKAY')

        for key in c.table:
            try:
                if info[3][key] == c.table[key][1]:
                    pass
                else:
                    return assertion
            except KeyError:
                pass

        print ('StacksRecognized : OKAY')

        assertion = True
        return assertion
