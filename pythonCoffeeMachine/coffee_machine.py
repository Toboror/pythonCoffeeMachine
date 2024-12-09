import time
import random
import subprocess


class CoffeMachine:
    machineState = True

    # Standard message for if the coffee machine has enough resources to make the given coffee.
    enoughResources = 'I have enough resources, making you a coffee!'

    # Standard message for if the coffee machine does not have enough resources to make the given coffee.
    sorryNotEnough = 'Sorry, not enough '

    # Espresso stats
    espressoWaterCost = 250
    espressoCoffeeBeanCost = 16
    espressoPrice = 4

    # Latte stats
    latteWaterCost = 350
    latteMilkCost = 75
    latteCoffeeBeanCost = 20
    lattePrice = 7

    # Cappuccino stats
    cappuccinoWaterCost = 200
    cappuccinoMilkCost = 100
    cappuccinoCoffeBeanCost = 12
    cappuccinoPrice = 6

    # Machine maintenance
    machineCleaningNeed = 0
    machineBroken = 0

    # Coffee brewing speeds.
    def standardSpeed(self):
        str(time.sleep(1))
        print('[:----]')
        str(time.sleep(1))
        print('[::---]')
        str(time.sleep(1))
        print('[:::--]')
        str(time.sleep(1))
        print('[::::-]')
        str(time.sleep(1))
        print('[:::::]')
        str(time.sleep(1))
        print('Done!')
        str(time.sleep(1))

    # The coffee brewing speed after it has been upgraded.
    def upgradedSpeed(self):
        str(time.sleep(0.65))
        print('[:----]')
        str(time.sleep(0.65))
        print('[::---]')
        str(time.sleep(0.65))
        print('[:::--]')
        str(time.sleep(0.65))
        print('[::::-]')
        str(time.sleep(0.65))
        print('[:::::]')
        str(time.sleep(0.65))
        print('Done!')
        str(time.sleep(1))

    # Chance of machine breaking down. It has a 12.5% chance.
    breakChance = random.randint(1, 8)

    # Machine upgrades.
    betterFilter = 0
    fasterMaker = 0

    # Prompts the user on what to do next.
    def whatToDo(self):
        print('Write action (buy, take, remaining, maintenance, upgrade, money, exit)')

    def __init__(self, name, water, coffeeBeans, milk, money, cups):
        self.name = 'The coffee machine'
        self.water = 400  # Ml
        self.coffeeBeans = 120  # Grams
        self.milk = 540  # Ml
        self.money = 5500  # Dollar
        self.cups = 9  # Amount of disposable cups

    def userInput(self):
        _userInput = str(input())
        return _userInput

    def checkMissingIngredients(self):
        # Checks if enough water.
        if self.cappuccinoWaterCost > self.water or self.latteWaterCost > self.water \
                or self.espressoWaterCost > self.water:
            return ' water!'
        # Checks if enough coffe beans.
        elif self.cappuccinoCoffeBeanCost > self.coffeeBeans or \
                self.latteCoffeeBeanCost > self.coffeeBeans \
                or self.espressoCoffeeBeanCost > self.coffeeBeans:
            return ' coffe beans!'
        # Checks if enough milk.
        elif self.cappuccinoMilkCost > self.milk or self.latteMilkCost > self.milk:
            return ' milk!'
        # Checks if enough cups.
        if self.cups == 0:
            return 'Sorry, not enough cups!'

    def buyAutomatic(self):
        # Espresso.
        if self.water >= self.espressoWaterCost and \
                self.coffeeBeans >= self.espressoCoffeeBeanCost and self.machineCleaningNeed < 5:
            print(self.enoughResources)
            self.makingCoffee()
            self.coffeeBeans -= self.espressoCoffeeBeanCost
            self.water -= self.espressoWaterCost
            self.money += self.espressoPrice
            self.machineCleaningNeed += 1
        elif self.machineCleaningNeed > 5:
            print('Not able to make coffee. The machine needs cleaning.')
        else:
            print(self.sorryNotEnough + str(self.checkMissingIngredients()))

    def buy(self):
        print('What do you want to buy? '
              '| 1 - espresso - $' + str(self.espressoPrice),
              '| 2 - latte - $' + str(self.lattePrice),
              '| 3 - cappuccino - $' + str(self.cappuccinoPrice),
              '| back - to main menu:')
        _userInput = self.userInput()
        if _userInput == '1' or _userInput == '2' or _userInput == '3':
            self.cups -= 1
            # Espresso.
            if _userInput == '1':
                if self.water >= self.espressoWaterCost and \
                        self.coffeeBeans >= self.espressoCoffeeBeanCost and self.machineCleaningNeed < 5:
                    print(self.enoughResources)
                    self.makingCoffee()
                    self.coffeeBeans -= self.espressoCoffeeBeanCost
                    self.water -= self.espressoWaterCost
                    self.money += self.espressoPrice
                    self.machineCleaningNeed += 1
                elif self.machineCleaningNeed > 5:
                    print('Not able to make coffee. The machine needs cleaning.')
                else:
                    print(self.sorryNotEnough + str(self.checkMissingIngredients()))
            # Latte
            elif _userInput == '2':
                if self.water >= self.latteWaterCost and \
                        self.coffeeBeans >= self.latteCoffeeBeanCost \
                        and self.milk >= self.latteMilkCost and self.machineCleaningNeed < 5:
                    print(self.enoughResources)
                    self.makingCoffee()
                    self.coffeeBeans -= self.latteCoffeeBeanCost
                    self.water -= self.latteWaterCost
                    self.money += self.lattePrice
                    self.machineCleaningNeed += 1
                elif self.machineCleaningNeed > 5:
                    print('Not able to make coffee. The machine needs cleaning.')
                else:
                    print(self.sorryNotEnough + str(self.checkMissingIngredients()))
            # Cappuccino.
            elif _userInput == '3':
                if self.water >= self.cappuccinoWaterCost and \
                        self.coffeeBeans >= self.cappuccinoCoffeBeanCost \
                        and self.milk >= self.cappuccinoMilkCost and self.machineCleaningNeed < 5:
                    print(self.enoughResources)
                    self.makingCoffee()
                    self.coffeeBeans -= self.cappuccinoCoffeBeanCost
                    self.water -= self.cappuccinoWaterCost
                    self.money += self.cappuccinoPrice
                    self.machineCleaningNeed += 1
                elif self.machineCleaningNeed > 5:
                    print('Not able to make coffee. The machine needs cleaning.')
                else:
                    print(self.sorryNotEnough + str(self.checkMissingIngredients()))
            # Back to main menu.
            elif _userInput == 'back':
                self.whatToDo()

    # Maintenance on the coffe machine.
    def maintenance(self):
        print('What do you want to do? | 1 - fill | 2 - clean | 3 - repair | 4 - back')
        _userInput = self.userInput()
        if _userInput == '1':
            self.fill()
        elif _userInput == '2':
            self.clean()
        elif _userInput == '3':
            self.repair()
        elif _userInput == '4':
            print()

    # Cleans the coffee machine.
    def clean(self):
        print('Starting the cleaning process')
        self.standardSpeed()

        self.machineCleaningNeed = 0

    # Upgrades the coffe machine.
    def upgrade(self):
        print('What do you want to upgrade?'
              '\n1 - Better filter - cost $750, -15% machine breakdown base chance'
              '\n2 - Faster coffee maker - cost $1500, +35% coffee making speed'
              '\n3 - Back to main menu')
        _userInput = self.userInput()
        if _userInput == '1' and self.money >= 750 and self.betterFilter != 1:
            print('Starting the upgrade of a better filter')
            self.standardSpeed()

            self.money -= 750
            self.betterFilter += 1
            self.breakChance = random.randint(1, 20)
        elif _userInput == '1':
            if self.money < 750:
                print('Not enough money for the better filter')
            elif self.betterFilter == 1:
                print('You already have the better filter!')

        elif _userInput == '2':
            if self.money >= 1500 and self.fasterMaker != 1:
                print('Starting the upgrade of a faster coffee maker')
                self.money -= 1500
                self.fasterMaker += 1
                self.standardSpeed()
            elif self.money < 1500:
                print('Not enough money for the faster coffee maker!')
            elif self.fasterMaker == 1:
                print('You already have the faster coffee maker!')

    # Repairs the coffee machine.
    def repair(self):
        print('You start repairing the machine.')
        self.standardSpeed()

        self.machineBroken -= 1

    # Fills the coffee machine's resources
    def fill(self):
        print('Write how many ml of water you want to add:')
        _userInputWater = self.userInput()
        self.water += int(_userInputWater)
        print('Write how many ml of milk you want to add:')
        _userInputMilk = self.userInput()
        self.milk += int(_userInputMilk)
        print('Write how many grams of coffee beans you want to add:')
        _userInputCoffeeBeans = self.userInput()
        self.coffeeBeans += int(_userInputCoffeeBeans)
        print('Write how many disposable cups you want to add:')
        _userInputCups = self.userInput()
        self.cups += int(_userInputCups)

    # Takes out all the money in machine.
    def take(self):
        print('I gave you $' + str(self.money))
        self.money = 0

    # Displays remaining resources in the coffe machine.
    def resources(self):
        return ('{} has:'
                '\n{} ml of water'
                '\n{} ml of milk'
                '\n{} g of coffee beans'
                '\n{} disposable cups'.format(self.name, self.water, self.milk, self.coffeeBeans, self.cups))

    # Displays current amount of money
    def checkMoney(self):
        return print('$' + str(self.money))

    # Turns the machine 'off'
    def exit(self):
        self.machineState = False
        subprocess.run(["python", "main.py"])

    def makingCoffee(self):
        if self.betterFilter == 1:
            self.upgradedSpeed()
        else:
            self.standardSpeed()


CoffeMachine = CoffeMachine('The coffee machine', 400, 120, 540, 550, 9)


def runMachine():
    while CoffeMachine.machineState:

        CoffeMachine.whatToDo()

        userInput = CoffeMachine.userInput()

        # A 5% chance of the machine breaking down everything user tries to buy.
        if userInput == 'buy':
            if CoffeMachine.machineBroken == 1:
                print('The machine has broken down. It needs repair.')
            else:
                if CoffeMachine.breakChance == 1:
                    print('The machine has broken down. It needs repair.')
                    CoffeMachine.machineBroken += 1
                else:
                    CoffeMachine.buy()
        elif userInput == 'upgrade':
            CoffeMachine.upgrade()
        elif userInput == 'maintenance':
            CoffeMachine.maintenance()
        elif userInput == 'take':
            CoffeMachine.take()
        elif userInput == 'remaining':
            print(CoffeMachine.resources())
            print()
        elif userInput == 'money':
            CoffeMachine.checkMoney()
        elif userInput == 'exit':
            CoffeMachine.exit()


if __name__ == "__main__":
    runMachine()
