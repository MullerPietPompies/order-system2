import  pandas as pd
import numpy as np
import time 
import datetime as dt
import os

inventory = pd.DataFrame(columns=['Product', 'Amount'])
dfEggs = pd.DataFrame(columns=['Product', 'Amount'])
dfMeat = pd.DataFrame(columns=['Product', 'Amount'])
dfVeg_Starch = pd.DataFrame(columns=['Product', 'Amount'])
dfEierTye = pd.DataFrame(columns=['Eier Tipe', 'Tyd', 'Gas'])

'''Dear future me. I am very sorry for what you are about to have to use.'''

icreate_own = 0
ieggsbenedict = 0
icroissant = 0 
iomelette = 0
itoasted = 0
iburger = 0
iwrap = 0
    
    
'''Eggs'''
ifried_s = 0
ifried_m = 0
ifried_h = 0 
    
iboiled_s = 0
iboiled_m = 0
iboiled_h = 0
    
ipoached_s = 0
ipoached_m = 0
ipoached_h = 0

iscrambled = 0
    
'''Meat options'''
ibacon = 0
ipatty_mince = 0
isteak = 0
iboerewors = 0
ichick_liv = 0
ipork = 0
icheesegriller = 0
ichick_schn = 0
ichick_nugg = 0
ipulled_pork = 0
    
    
ichick_mayo = 0
    
    
'''Veggie Starch'''
ipap_relish = 0
ibeans = 0
ihashbrown = 0
imushroom = 0
ionion = 0
ionion_ring = 0
ichips = 0

'''Other'''
icheese = 0
itomato = 0
igreenpepper = 0

itoastbread_b = 0
itoastbread_w =0
ihamb_bun = 0
iwrap = 0
iengmuffin = 0


guest = ""
egg_type = ''


def CountItems(raw_data):
    iJuice = 0
    iYoghurtPlain = 0
    iYoghurtFlav = 0
    iFruitSalad = 0
    indexnum = 0    

    
    '''Count Juice'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,6] == 'Yes;':
            iJuice = iJuice + 1
        else:
            pass
        
    # print('Juice ' + str(iJuice))
    indexnum+= 1
    inventory.loc[indexnum] = ['Juice',iJuice]
    
    
    
    '''Count Yoghurt'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,7] == 'Yes':
            if raw_data.iloc[i,8] == 'Fruit Flavoured':
                iYoghurtFlav = iYoghurtFlav + 1
            else:
                iYoghurtPlain = iYoghurtPlain + 1
        
        else:
            pass
    # print('Yoghurt Flavoured ' + str(iYoghurtFlav))
    # print('Yoghurt Plain ' + str(iYoghurtPlain))
    indexnum+= 1
    inventory.loc[indexnum] = ['Yoghurt Flavoured ',iYoghurtFlav]
    indexnum+= 1
    inventory.loc[indexnum] = ['Yoghurt Plain ', iYoghurtPlain]
    
    '''Count Fruit Salad'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,9] == 'Yes':
            iFruitSalad = iFruitSalad + 1
        else:
            pass
        
    # print('Fruit Salad ' + str(iFruitSalad))
    
    indexnum+= 1
    inventory.loc[indexnum] = ['Fruit Salad ',iFruitSalad]
    
    
    
'''Add Not Included'''
def NotIncluded(raw_data):
    

    print(' \nDo Not Include!!!')
    '''Display Not Included'''
    for i in range(0,raw_data.shape[0]):
        if type(raw_data.iloc[i,10]) != float:
            print(raw_data.iloc[i,0]+': ' + raw_data.iloc[i,10])
        else:
            pass 
        
'''Count Cereal'''
def Cereal(raw_data):
    icorn_flakes = 0
    ibran = 0
    imuesli_milk = 0
    imuesli_no_milk = 0
    ipronutro = 0
    ioats = 0
    indexnum = inventory.shape[0]
    
    '''Count Corn Flakes'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,11] == 'Corn Flakes with milk':
            icorn_flakes = icorn_flakes + 1
        else:
            pass
    # print('Corn Flakes ' + str(icorn_flakes))
    indexnum+= 1
    inventory.loc[indexnum] = ['Corn Flakes ',icorn_flakes]
    
    
    
    '''Count All Bran'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,11] == 'Bran Flakes with milk':
            ibran = ibran + 1
        else:
            pass
    # print('All Bran ' + str(ibran))
    indexnum+= 1
    inventory.loc[indexnum] = ['All Bran ',ibran]
    
    
    
    '''Count Muesli With milk'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,11] == 'Muesli with cold milk':
            imuesli_milk = imuesli_milk + 1
        else:
            pass
    # print('Muesli with milk ' + str(imuesli_milk))
    indexnum+= 1
    inventory.loc[indexnum] = ['Muesli with milk ' ,imuesli_milk]
    
    
    
    '''Count Muesli with yoghurt'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,11] == 'Muesli without milk - I will enjoy it with my yoghurt':
            imuesli_no_milk = imuesli_no_milk + 1
        else:
            pass
    # print('Muesli with Yoghurt ' + str(imuesli_no_milk))
    indexnum+= 1
    inventory.loc[indexnum] = ['Muesli with Yoghurt ' ,imuesli_no_milk]
    
    
    
    '''Count Pronutro'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,11] == 'Pronutro with milk':
            ipronutro = ipronutro + 1
        else:
            pass
    # print('Pronutro ' + str(ipronutro))
    
    indexnum+= 1
    inventory.loc[indexnum] = ['Pronutro ',ipronutro]
    
    
    
    '''Count Oats'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,11] == 'Oats with milk':
            ioats = ioats + 1
        else:
            pass
    # print('Oats ' + str(ioats))   
    
    indexnum+= 1
    inventory.loc[indexnum] = ['Oats ', ioats]
    
    
    
'''Bread'''
def CountBread(raw_data):
    it_brown = 0
    it_white = 0
    ip_brown = 0
    ip_white = 0
    indexnum = inventory.shape[0]
    
    '''Toasted brown'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,12] == 'Toasted brown':
            it_brown = it_brown + 1
        else:
            pass
    # print('Toasted Brown ' + str(it_brown))
    indexnum+= 1
    inventory.loc[indexnum] = ['Toasted Brown ',it_brown]
    
    '''Toasted White'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,12] == 'Toasted white':
            it_white = it_white + 1
        else:
            pass
    # print('Toasted White ' + str(it_white))
    indexnum+= 1
    inventory.loc[indexnum] = ['Toasted White ',it_white]
    
    
    '''Plain Brown'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.iloc[i,12] == 'Plain brown':
            ip_brown = ip_brown + 1
        else:
            pass
    # print('Plain Brown ' + str(ip_brown))
    indexnum+= 1
    inventory.loc[indexnum] = ['Plain Brown ',ip_brown]

    '''Plain White'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.loc[raw_data.index[i],'Bread'] == 'Plain white':
            ip_white = ip_white + 1
        else:
            pass
    # print('Plain White ' + str(ip_white))
    indexnum+= 1
    inventory.loc[indexnum] = ['Plain White ',ip_white]
    
    
'''Count Drinks'''

def CountDrinks(raw_data):
    ifilter_b = 0
    ifilter_w = 0 
    icuppuccino = 0
    icaflate = 0
    ihc = 0
    ifiveroses = 0
    irooibos = 0
    
    indexnum = inventory.shape[0]
    
    
    '''Filter black'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.loc[raw_data.index[i],'Can we add any of the following hot drinks to you order'] == 'Filter coffee - black':
            ifilter_b = ifilter_b + 1
        else:
            pass
    # print('Filter Coffee Black ' + str(ifilter_b))
    indexnum+= 1
    inventory.loc[indexnum] = ['Filter Coffee Black',ifilter_b]

    '''Filter White'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.loc[raw_data.index[i],'Can we add any of the following hot drinks to you order'] == 'Filter Coffee with milk':
            ifilter_w = ifilter_w + 1
        else:
            pass
    # print('Filter Coffee With Milk ' + str(ifilter_w))
    indexnum+= 1
    inventory.loc[indexnum] = ['Filter Coffee White',ifilter_w]
    
    '''Cuppuccino'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.loc[raw_data.index[i],'Can we add any of the following hot drinks to you order'] == 'Cappuccino':
            icuppuccino += 1
        else:
            pass
    # print('Cuppucino ' + str(icuppuccino))
    indexnum+= 1
    inventory.loc[indexnum] = ['Cuppucino',icuppuccino]

    '''Cafe late'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.loc[raw_data.index[i],'Can we add any of the following hot drinks to you order'] == 'Café Late':
            icaflate = icaflate + 1
        else:
            pass
    # print('Cafe Late ' + str(icaflate))
    indexnum+= 1
    inventory.loc[indexnum] = ['Cafe Late',icaflate]
    
    '''Hot Chocolate'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.loc[raw_data.index[i],'Can we add any of the following hot drinks to you order'] == 'Hot Chocolate':
            ihc += 1
        else:
            pass
    indexnum+= 1
    inventory.loc[indexnum] = ['Hot Chocolate',ihc]
    '''Five Roses'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.loc[raw_data.index[i],'Can we add any of the following hot drinks to you order'] == 'Five Roses tea':
            ifiveroses += 1
        else:
            pass
    indexnum+= 1
    inventory.loc[indexnum] = ['Five Roses',ifiveroses]
    
    '''Rooibos'''
    for i in range(0,raw_data.shape[0]):
        if raw_data.loc[raw_data.index[i],'Can we add any of the following hot drinks to you order'] == 'Rooibos Tea':
            irooibos += 1
        else:
            pass
    indexnum+= 1
    inventory.loc[indexnum] = ['Rooibos',irooibos]
    
    
'''Main Breakfast'''
def MainBreakfast(raw_data):
    '''Options'''
    


    
    
    for i in range(0,raw_data.shape[0]):
        
        time_of_order = raw_data.loc[raw_data.index[i], 'Time breakfast must be served']
        geust = raw_data.loc[raw_data.index[i], 'Name2']

        if raw_data.loc[raw_data.index[i],'Please choose one of the following'] == 'Create your own breakfast':
            icreate_own += 1
            print('\nCreate Own for : ' + raw_data.loc[raw_data.index[i],'Name2'] + ' at ' + raw_data.loc[raw_data.index[i],'Time breakfast must be served'])
            '''Fried eggs'''
            
            if raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Soft fried':
                print('Soft Fried')
                ifried_s += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] 


            elif raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Medium fried':
                print('Medium Fried')
                ifried_m += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']       

            elif raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Hard fried':
                print('Hard Fried')
                ifried_h += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']       
            else:
                pass
                
            '''Boiled Eggs'''
            if raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Soft boiled':
                print('Soft Boiled')
                iboiled_s += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']
            elif raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Medium boiled':
                print('Medium Boiled')
                iboiled_m += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']

            elif raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Hard boiled':
                print('Hard Boiled')
                iboiled_h += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']
            else:
                pass
            

            # dfEggs.loc[dfEggs.shape[0]+ 1] = 
            
            '''Poached Eggs'''
            if raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Soft Poached':
                print('Soft Poached')
                ipoached_s += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']

            elif raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Medium Poached':
                print('Medium Poached')
                ipoached_m += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']
            
            elif raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Hard Poached':
                print('Hard Poached')
                ipoached_h += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']
            else:
                pass
            
            '''Scrambled'''    
            
            if raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:'] == 'Scrambled':
                print('Scrambled')
                iscrambled += 2
                egg_type = raw_data.loc[raw_data.index[i],'Two eggs prepared the way you like it:']
            else:
                pass
            
            '''Meat Option 1'''
            if raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Bacon':
                print('Bacon')
                ibacon += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Beef Burger patty':
                print('Patty/Mince')
                ipatty_mince += 1
                
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Minute steak':
                print('Steak')
                isteak += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Savoury mince':
                print('Patty/Mince')
                ipatty_mince += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Boerewors':
                print('Boerewors')
                iboerewors += 1
                  
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Creamy chicken livers':
                print('Chicken livers')
                ichick_liv += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Pork Banger':
                print('Pork Banger')
                ipork += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Mini Cheese Griller':
                print('Cheese Griller')
                icheesegriller += 1
                
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Chicken schnitzel-patty':
                print('Chicken Schintzel')
                ichick_schn += 1
                
            elif raw_data.loc[raw_data.index[i],'Choose your first meat option'] == 'Chicken Nuggets':
                print('Chicken Nuggets')
                ichick_nugg += 1
            else:
                pass
            
            
            
            '''Meat Option 2'''
            if raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Bacon':
                print('Bacon')
                ibacon += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Beef Burger patty':
                print('Patty/Mince')
                ipatty_mince += 1
                
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Minute steak':
                print('Steak')
                isteak += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Savoury mince':
                print('Patty/Mince')
                ipatty_mince += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Boerewors':
                print('Boerewors')
                iboerewors += 1
                  
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Creamy chicken livers':
                print('Chicken livers')
                ichick_liv += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Pork Banger':
                print('Pork Banger')
                ipork += 1
            
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Mini Cheese Griller':
                print('Cheese Griller')
                icheesegriller += 1
                
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Chicken schnitzel-patty':
                print('Chicken Schintzel')
                ichick_schn += 1
                
            elif raw_data.loc[raw_data.index[i],'Choose your second meat option'] == 'Chicken Nuggets':
                print('Chicken Nuggets')
                ichick_nugg += 1
            else:
                pass 
            
            
            '''Veggie/Starch'''
            if raw_data.loc[raw_data.index[i],'Choose your vegetable/starch'] == 'Tomato relish with mieliepap':
                print('Pap en relish')
                ipap_relish += 1
                itomato += 1
                
            elif raw_data.loc[raw_data.index[i],'Choose your vegetable/starch'] == 'Baked beans':
                print('Baked beans')
                ibeans += 1
            elif raw_data.loc[raw_data.index[i],'Choose your vegetable/starch'] == 'Potato hash brown':
                print('Potato hash brown')
                ihashbrown += 1
            elif raw_data.loc[raw_data.index[i],'Choose your vegetable/starch'] == 'Mushrooms':
                print('Mushrooms')
                imushroom += 1
            elif raw_data.loc[raw_data.index[i],'Choose your vegetable/starch'] == 'Fried Onion':
                print('Fried Onion')
                ionion_ring += 1
            elif raw_data.loc[raw_data.index[i],'Choose your vegetable/starch'] == 'French Fries':
                print('Chips')
                ichips += 1
            else:
                pass
        
        '''Eggs Benedict'''
        if raw_data.loc[raw_data.index[i],'Please choose one of the following'] == 'Eggs Benedict':
            ieggsbenedict = 0
            iengmuffin += 1
            ibacon += 1
            print('\nEggs benedict for : ' + raw_data.loc[raw_data.index[i],'Name2'] + ' at ' + raw_data.loc[raw_data.index[i],'Time breakfast must be served'])
            if raw_data.loc[raw_data.index[i],'How must the eggs be poached for the Eggs Benedict?'] == 'Soft':
                print('Soft Eggs')
                ipoached_s += 2
                egg_type = 'Soft Poached'
            elif raw_data.loc[raw_data.index[i],'How must the eggs be poached for the Eggs Benedict?'] == 'Medium':
                print('Medium Eggs')
                ipoached_m += 2
                egg_type = 'Medium Poached'                
            elif raw_data.loc[raw_data.index[i],'How must the eggs be poached for the Eggs Benedict?'] == 'Hard':
                print('Hard Eggs')
                ipoached_h += 2
                egg_type = 'Hard Poached'                
                 
            else:
                pass
            
            if raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown'] == 'Chips':
                print('Chips')
                ichips += 1
            elif raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown'] == 'Hash Brown':
                print('Hash Brown')
                ihashbrown += 1
            else:
                pass
            
            
            '''Croissant '''
        if raw_data.loc[raw_data.index[i],'Please choose one of the following'] == 'Croissant filled with scrambled egg and bacon':
            print('\nCroissant for : ' + raw_data.loc[raw_data.index[i],'Name2'] + ' at ' + raw_data.loc[raw_data.index[i],'Time breakfast must be served'])
            ibacon += 1
            iscrambled += 2
            icheese += 1
            egg_type = "Scrambled"

            if raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown4'] == 'Chips':
                print('Chips')
                ichips += 1
            elif raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown4'] == 'Hash Browns':
                print('Hash Brown')
                ihashbrown += 1
            else:
                pass
            
            
        '''Omelette'''
        
        if raw_data.loc[raw_data.index[i],'Please choose one of the following'] == ' Omelette with cheese and your choice of two fillings':
            print('\nOmelette for : ' + raw_data.loc[raw_data.index[i],'Name2'] + ' at ' + raw_data.loc[raw_data.index[i],'Time breakfast must be served'])
            icheese += 1
            iscrambled += 3
            egg_type = "Scrambled Omelette"           
            
            if raw_data.loc[raw_data.index[i],'Omelette filling 1'] == 'Mushroom':
                print('Mushroom')
                imushroom +=1
            
            elif raw_data.loc[raw_data.index[i],'Omelette filling 1'] == 'Tomato': 
                print('Tomato')
                itomato +=1
            
            elif raw_data.loc[raw_data.index[i],'Omelette filling 1'] == 'Savoury mince': 
                print('Mince')
                ipatty_mince +=1
            
            elif raw_data.loc[raw_data.index[i],'Omelette filling 1'] == 'Bacon': 
                print('Bacon')
                ibacon +=1
                
            elif raw_data.loc[raw_data.index[i],'Omelette filling 1'] == 'Bacon': 
                print('Bacon')
                ibacon +=1
                
            elif raw_data.loc[raw_data.index[i],'Omelette filling 1'] == 'Steak strips': 
                print('Steak')
                isteak +=1
                
            elif raw_data.loc[raw_data.index[i],'Omelette filling 1'] == 'Grilled onion': 
                print('Onion')
                ionion +=1

            elif raw_data.loc[raw_data.index[i],'Omelette filling 1'] == 'Grilled green pepper': 
                print('Green Pepper')
                igreenpepper +=1
            else:
                pass
            
            
            
            if raw_data.loc[raw_data.index[i],'Omelette filling 2'] == 'Mushroom':
                print('Mushroom')
                imushroom +=1
            
            elif raw_data.loc[raw_data.index[i],'Omelette filling 2'] == 'Tomato': 
                print('Tomato')
                itomato +=1
            
            elif raw_data.loc[raw_data.index[i],'Omelette filling 2'] == 'Savoury mince': 
                print('Mince')
                ipatty_mince +=1
            
            elif raw_data.loc[raw_data.index[i],'Omelette filling 2'] == 'Bacon': 
                print('Bacon')
                ibacon +=1
                
            elif raw_data.loc[raw_data.index[i],'Omelette filling 2'] == 'Bacon': 
                print('Bacon')
                ibacon +=1
                
            elif raw_data.loc[raw_data.index[i],'Omelette filling 2'] == 'Steak strips': 
                print('Steak')
                isteak +=1
                
            elif raw_data.loc[raw_data.index[i],'Omelette filling 2'] == 'Grilled onion': 
                print('Onion')
                ionion +=1

            elif raw_data.loc[raw_data.index[i],'Omelette filling 2'] == 'Grilled green pepper': 
                print('Green Pepper')
                igreenpepper +=1
            else:
                pass
            
            if raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown2']  == 'Chips':
                print('Chips')
                ichips += 1
            elif raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown2'] == 'Hash Browns':
                print('Hash Brown')
                ihashbrown += 1
            else:
                pass
            
            
        '''Toasted Sandwich'''
        if raw_data.loc[raw_data.index[i],'Please choose one of the following'] == 'Toasted Sandwich ':
            print('\nToasted Sandwich for : ' + raw_data.loc[raw_data.index[i],'Name2'] + ' at ' + raw_data.loc[raw_data.index[i],'Time breakfast must be served'])
            
            if raw_data.loc[raw_data.index[i],'Bread for the sandwich'] == 'White bread':
                itoastbread_w += 3
            else:
                itoastbread_b += 3
                
            if raw_data.loc[raw_data.index[i],'Filling for the toasted sandwich'] == 'Cheese':
                print('Cheese')
                icheese += 1
            elif raw_data.loc[raw_data.index[i],'Filling for the toasted sandwich'] == 'Bacon and cheese':
                print('Bacon and cheese')
                ibacon += 1
                icheese += 1
            elif raw_data.loc[raw_data.index[i],'Filling for the toasted sandwich'] == 'Bacon, egg and cheese':
                print('Bacon, egg and cheese')
                ibacon += 1
                ifried_h += 2
                icheese += 1
                egg_type = "Fried Hard for sandwich"
            elif raw_data.loc[raw_data.index[i],'Filling for the toasted sandwich'] == 'Bacon, cheese and tomato': 
                print('Bacon, cheese and tomato')
                ibacon += 1
                icheese += 1
                itomato += 1
            elif raw_data.loc[raw_data.index[i],'Filling for the toasted sandwich'] == 'Chicken Mayonaise':
                print('Chicken Mayonaise')
                ichick_mayo += 1
            elif raw_data.loc[raw_data.index[i],'Filling for the toasted sandwich'] == 'Pulled pork and cheese':
                print('Pulled pork and cheese')
                ipulled_pork += 1
                icheese += 1
                
            if raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown3']  == 'Chips':
                print('Chips')
                ichips += 1
            elif raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown3'] == 'Hash Browns':
                print('Hash Brown')
                ihashbrown += 1
            else:
                pass
            
            
        '''Breakfast Burger'''    
        if raw_data.loc[raw_data.index[i],'Please choose one of the following'] == 'Breakfast burger ':
            print('\nBreakfast Bruger for : ' + raw_data.loc[raw_data.index[i],'Name2'] + ' at ' + raw_data.loc[raw_data.index[i],'Time breakfast must be served'])
            itomato += 1
            ionion_ring+=1
            ihamb_bun +=1
            iburger += 1
            
            if raw_data.loc[raw_data.index[i],'Breakfast burger option'] == 'Beef Patty':
                print('Beef')
                ipatty_mince += 1
            else:
                print('Chicken')
                ichick_schn += 1
            
            if raw_data.loc[raw_data.index[i],'How must the eggs be done for the breakfast burger?'] == 'Soft':
                print('Soft Egg')
                ifried_s += 1
                egg_type = "Soft Fried For Burger"
            elif raw_data.loc[raw_data.index[i],'How must the eggs be done for the breakfast burger?'] == 'Medium':
                print('Medium Egg')
                ifried_m += 1
                egg_type = "Medium Fried For Burger"
            elif raw_data.loc[raw_data.index[i],'How must the eggs be done for the breakfast burger?'] == 'Hard':
                print('Hard Egg')
                ifried_h += 1
                egg_type = "Hard Fried For Burger"
            else:
                pass
            
            if raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown4']  == 'Chips':
                print('Chips')
                ichips += 1
            elif raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown4'] == 'Hash Browns':
                print('Hash Brown')
                ihashbrown += 1
            else:
                pass
            
            
        '''Breakfast wrap'''           
        if raw_data.loc[raw_data.index[i],'Please choose one of the following'] == 'Breakfast wrap':
            print('\nBreakfast Wrap : ' + raw_data.loc[raw_data.index[i],'Name2'] + ' at ' + raw_data.loc[raw_data.index[i],'Time breakfast must be served'])
            iwrap += 1
            
            if raw_data.loc[raw_data.index[i],'Filling for the breakfast wrap'] == 'Scrambled egg, bacon and cheese':
                print('Scrambled egg, Bacon and Cheese')
                iscrambled += 2
                ibacon += 1
                icheese += 1
                egg_type = "Scrabled For Wrap"
            elif raw_data.loc[raw_data.index[i],'Filling for the breakfast wrap'] == 'Scrambled egg, tomato, bacon and cheese':
                print('Scrambled egg,Tomato, Bacon and Cheese')
                iscrambled += 2
                ibacon += 1
                icheese += 1
                itomato += 1
                egg_type = "Scrembled For Wrap"
            elif raw_data.loc[raw_data.index[i],'Filling for the breakfast wrap'] == 'Chicken mayonaise':
                print('Chicken Mayo')
                ichick_mayo += 1
            elif raw_data.loc[raw_data.index[i],'Filling for the breakfast wrap'] == 'Mince and cheese':
                print('Mince and cheese')
                ipatty_mince += 1
                icheese += 1
                
            elif raw_data.loc[raw_data.index[i],'Filling for the breakfast wrap'] == 'Steak, grilled onion and cheese': 
                print('Steak, grilled onion and cheese')
                isteak +=1
                ionion += 1
                icheese += 1
            elif raw_data.loc[raw_data.index[i],'Filling for the breakfast wrap'] == 'Marinated pulled pork and cheese':
                print('Marinated pulled pork and cheese')
                ipulled_pork += 1
                icheese += 1
                
            else:
                pass
            
            if raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown5']  == 'Chips':
                print('Chips')
                ichips += 1
            elif raw_data.loc[raw_data.index[i],'Choose Chips or Hash Brown5'] == 'Hash Browns':
                print('Hash Brown')
                ihashbrown += 1
            else:
                pass
            
            
        else:
            pass
        if egg_type != "":
            dfEierTye.loc[i] = [egg_type,time_of_order,geust]

    print('\nCreate Own Total: ' + str(icreate_own))
    

    indexnum = 0
    
    # print('\nEgg Totals')
    # print('Soft Fried: ' + str(ifried_s))
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Soft Fried',ifried_s]
    # print('Medium Fried: ' + str(ifried_m))
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Medium Fried',ifried_m]    
    # print('Hard Fried: ' + str(ifried_h))
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Hard Fried',ifried_h]
    
    

    # print('Soft Boiled: ' + str(iboiled_s))
    # print('Medium Boiled: ' + str(iboiled_m))
    # print('Hard Boiled: ' + str(iboiled_h))
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Soft Boiled'   , iboiled_s]
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Medium Boiled'  ,  iboiled_m]
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Hard Boiled' ,iboiled_h]

    indexnum+= 1
    dfEggs.loc[indexnum] = ['Soft Poaced' ,    ipoached_s]
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Medium Poaced' ,    ipoached_m]
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Hard Poaced' ,    ipoached_h]
    indexnum+= 1
    dfEggs.loc[indexnum] = ['Scrambled' ,    iscrambled] 


    indexnum = 0
    
    
    dfMeat.loc[indexnum] =['Bacon', ibacon]
    indexnum += 1
    dfMeat.loc[indexnum] =['Mince/Beef Patty', ipatty_mince]
    indexnum += 1
    dfMeat.loc[indexnum] =['Steak', isteak]
    indexnum += 1
    dfMeat.loc[indexnum] =['Boerewors', iboerewors]
    indexnum += 1
    dfMeat.loc[indexnum] =['Chicken Livers', ichick_liv]
    indexnum += 1
    dfMeat.loc[indexnum] =['Pork Banger', ipork]
    indexnum += 1
    dfMeat.loc[indexnum] =['Mini Cheese Griller', icheesegriller]
    indexnum += 1
    dfMeat.loc[indexnum] =['Chicken Schnitzel', ichick_schn]
    indexnum += 1
    dfMeat.loc[indexnum] =['Chicken Nuggets', ichick_nugg]
    indexnum += 1
    dfMeat.loc[indexnum] =['Pulled Pork', ipulled_pork]
    
    indexnum =0 
    
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Pap en Relish',ipap_relish]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Baked Beans', ibeans]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Hashbrown', ihashbrown]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Mushroom', imushroom]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Onions', ionion]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Onion Rings', ionion_ring]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Chips', ichips]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Tomato', itomato]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Green Pepper', igreenpepper]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Cheese', icheese]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Toasted Brown', itoastbread_b]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Toasted White', itoastbread_w]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Hamburger Bun', ihamb_bun]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Wrap', iwrap]
    dfVeg_Starch.loc[dfVeg_Starch.shape[0]+1] = ['Engish Muffin', iengmuffin]

    # print(f'{iburger} + {ipatty_mince} + {ichick_schn}')
    
    
   
def main(data):
    if os.path.exists('Out.xlsx'):
        os.remove('Out.xlsx')

    if data is not None:
    # print('Juice, Fruit and Yoghurt')
        CountItems(data)
    # print('\nCreal')
        Cereal(data)
        
        NotIncluded(data)
        CountBread(data)

        print('\nDrinks')
        CountDrinks(data)
        MainBreakfast(data)


        # dfEierTye['Tyd'] = pd.to_datetime(dfEierTye['Tyd'])
        # dfEierTye['Tyd'] = dfEierTye['Tyd'].apply(pd.Timestamp)
        # dfEierTye['Tyd'] = dfEierTye['Tyd'].dt.time 

        dfEierTye.sort_values(by=["Tyd"], inplace=True)
        
        with pd.ExcelWriter('Out.xlsx') as writer:
            inventory.to_excel(writer, sheet_name='Juice and Drinks', index=False)
            dfEggs.to_excel(writer, sheet_name='Eggs', index=False)
            dfMeat.to_excel(writer, sheet_name='Meat', index=False)
            dfVeg_Starch.to_excel(writer, sheet_name='Veg and Starch',index=False)
            dfEierTye.to_excel(writer, sheet_name="Eggs And time to be completed", index=False)

