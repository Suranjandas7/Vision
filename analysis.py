#Project Vision
#Analysis module

#This class will create a virtual poker table which will contain all the infor
#mation about their stack, poker hands and decisions. The anaysis for the decis
#ions happens in the analysis function which is called from outside sourcers wit
#h data and it returns the specific analysis.
class table:

    def __init__(self, table_type, ul, ll):
        self.stake = [ul, ll]
        self.table_type = table_type
        if table_type == '6max':
            self.table_template = {
                "B":'',
                "sb":'',
                "bb":'',
                "utg":'',
                "1":'',
                "co":'',
            }
            self.pf_container = {
                'B':[],
                'sb':[],
                'bb':[],
                '1':[],
                'utg':[],
                'co':[],
            }
        if table_type == '9max':
            self.table_template = {
                "B":'',
                "sb":'',
                "bb":'',
                "utg":'',
                "1":'',
                "2":'',
                "3":'',
                "hj":'',
                "co":'',
            }
        self.pre_flop_hands = {}
        self.stack_sizes = {}
        self.hole_cards = []

        if self.table_type == '6max':
            self.s_o_e = ["sb", "bb", "1", "utg", "co", "B"]
            self.pf_s_o_e = ["utg", "1", "co", "B", "sb", "bb"]
        if self.table_type == '9max':
            self.s_o_e = ["sb", "bb", "utg", "1", "2", "3", "hj", "co", "B"]
            self.pf_s_o_e = ["utg", "1", "2", "3", "hj", "co", "B", "sb", "bb"]

    def input_names(self):
        #storing the names and tying them to positions
        for key in self.table_template:
            print ('Enter label for ' + key)
            label = input('')
            print ('Enter stack size for : ' + key)
            stack = input('')
            self.table_template[key] = str(label)
            self.stack_sizes[key] = str(stack)
        for element in self.s_o_e:
            print ('Enter hand for : ' + self.table_template[element])
            hand = input('')
            self.pre_flop_hands[element] = hand

    def input_river(self):
        print ('RIVER')
        self.r_container = {}
        for pos, data in self.t_container.items():
            if data[len(data)-1] == 'Fold':
                pass
            else:
                self.r_container[pos] = data

        Possible_moves = {'1':'Fold', '2':'Raise',
                        '3':'Bet', '4':'All_in',
                        '5':'Check','6':'Won'}

        FlagFlag = False

        while(FlagFlag == False):
            for element in self.s_o_e:
                try:
                    value_check = len(self.r_container[element]) - 1
                    if self.r_container[element][value_check] == 'Fold':
                        pass
                    else:
                        print ('Enter turn for', element)
                        print (Possible_moves)
                        choice = str(input(':'))
                        if choice == '1' or choice == '5' or choice == '6':
                            move = Possible_moves[choice]
                            self.r_container[element].append(move)
                        else:
                            amount = input('Amount : ')
                            self.r_container[element][2] = float(self.stack_sizes[element]) - float(amount)
                            move = Possible_moves[choice]
                            self.r_container[element].append(move+';'+str(amount))
                except KeyError:
                    pass
            end_flag = input('EndCycle')
            if str(end_flag) == "yes":
                FlagFlag = True

        river = input("Enter river card : ")
        self.hole_cards.append(river)

    def input_turn(self):
        print ('TURN')
        self.t_container = {}
        for pos, data in self.pf_container.items():
            if data[len(data)-1] == 'Fold':
                pass
            else:
                self.t_container[pos] = [data[0], data[1], data[2], data[3]]

        Possible_moves = {'1':'Fold', '2':'Raise',
                        '3':'Bet', '4':'All_in',
                        '5':'Check','6':'Won'}

        FlagFlag = False

        while(FlagFlag == False):
            for element in self.s_o_e:
                try:
                    value_check = len(self.t_container[element]) - 1
                    if self.t_container[element][value_check] == 'Fold':
                        pass
                    else:
                        print ('Enter turn for', element)
                        print (Possible_moves)
                        choice = str(input(':'))
                        if choice == '1' or choice == '5' or choice == '6':
                            move = Possible_moves[choice]
                            self.t_container[element].append(move)
                        else:
                            amount = input('Amount : ')
                            self.t_container[element][2] = float(self.stack_sizes[element]) - float(amount)
                            move = Possible_moves[choice]
                            self.t_container[element].append(move+';'+str(amount))
                except KeyError:
                    pass
            end_flag = input('EndCycle')
            if str(end_flag) == "yes":
                FlagFlag = True
        turn = input("Enter turn card : ")
        self.hole_cards.append(turn)

        continue_counter = 0
        for keys, values in self.pf_container.items():
            if values[len(values)-1] == 'Fold':
                pass
            else:
                continue_counter = continue_counter + 1
        if continue_counter == 1:
            exit()
        else:
            self.input_river()

    #Pre-flop
    def input_preflop(self):
        print ('PREFLOP')
        for pos, name in self.table_template.items():
            for con_pos in self.pf_container:
                if pos is con_pos:
                    self.pf_container[con_pos].append(name)
                    self.pf_container[con_pos].append(
                        self.stack_sizes[con_pos]
                    )
                    self.pf_container[con_pos].append(
                        self.stack_sizes[con_pos]
                    )
                    self.pf_container[con_pos].append(
                        self.pre_flop_hands[con_pos]
                    )

        #pf_container = 'position' : ['name', stack size[start],
        #stack size[end], hand, move1, move2, move3, moven]

        Possible_moves = {'1':'Fold', '2':'Raise',
                        '3':'Bet', '4':'All_in',
                        '5':'Check','6':'Won'}

        self.pf_container['sb'][2] = float(self.stack_sizes['sb']) - float(self.stake[0])
        self.pf_container['bb'][2] = float(self.stack_sizes['bb']) - float(self.stake[1])

        FlagFlag = False

        while(FlagFlag == False):
            for element in self.pf_s_o_e:
                value_check = len(self.pf_container[element]) - 1
                if self.pf_container[element][value_check] == 'Fold':
                    pass
                else:
                    print ('Enter turn for', element)
                    print (Possible_moves)
                    choice = str(input(':'))
                    if choice == '1' or choice == '5' or choice == '6':
                        move = Possible_moves[choice]
                        self.pf_container[element].append(move)
                    else:
                        amount = input('Amount : ')
                        self.pf_container[element][2] = float(self.stack_sizes[element]) - float(amount)
                        move = Possible_moves[choice]
                        self.pf_container[element].append(move+';'+str(amount))
            end_flag = input('EndCycle')
            if str(end_flag) == "yes":
                FlagFlag = True
        for x in range(0, 3):
            hole_card = input("Enter hole cards: ")
            self.hole_cards.append(hole_card)

        continue_counter = 0
        for keys, values in self.pf_container.items():
            if values[len(values)-1] == 'Fold':
                pass
            else:
                continue_counter = continue_counter + 1
        if continue_counter == 1:
            exit()
        else:
            self.input_turn()

    def testing(self, key):
        if key == 'fn':
            list_of_names = [
                ['Jugnu1', 100],
                ['Jugnu2', 200],
                ['Jugnu3', 300],
                ['Jugnu4', 400],
                ['Jugnu5', 500],
                ['Jugnu6', 600],
                ['Jugnu7', 700],
                ['Jugnu8', 800],
                ['Jugnu9', 900],
            ]
            counter = 1
            for label, name in self.table_template.items():
                self.table_template[label] = list_of_names[counter][0]
                self.stack_sizes[label] = list_of_names[counter][1]
                counter += 1

            counter2 = 1
            for name in self.table_template:
                self.pre_flop_hands[name] = "H" + str(counter)
                counter += 1

        if key == 'showtt':
            print (self.table_template)
        if key == 'soe':
            print (self.s_o_e)
        if key == 'show_pre_flop':
            print (self.pre_flop_hands)

        if key == 'show_pf_dets':
            #considering info is filled
            print ('PreFlop Details')
            print (self.pf_container)

            print ('Pos - Name - StackStart - StackEnd - Hand')
            def print_details(pos):
                print (pos, self.pf_container[pos][0], self.pf_container[pos][1],
                self.pf_container[pos][2], self.pf_container[pos][3],
                self.pf_container[pos][4])
            for element in self.s_o_e:
                print_details(element)

            no_of_moves = 0
            for keys, values in self.pf_container.items():
                if len(values) > no_of_moves:
                    no_of_moves = len(values)
            no_of_moves = no_of_moves - 2
            print ('No of Moves Total in this round : ', str(no_of_moves))
