import random

class LoremGenerator():
	def __init__(self):

		self.USER = 1
		self.GROUP = 2
		self.PROJECT = 3
	
		self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.numbers = "1234567890"
		self.words = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split(" ")
		self.first_names = "james robert john michael david william richard joseph thomas charles christopher daniel matthew anthony mark donald steven paul andrew joshua kenneth kevin brian george timothy ronald edward jason jeffrey ryan jacob gary nicholas eric jonathan stephen larry justin scott brandon benjamin samuel gregory alexander frank patrick raymond jack dennis jerry tyler aaron jose adam nathan henry douglas zachary peter kyle ethan walter noah jeremy christian keith roger terry gerald harold sean austin carl arthur lawrence dylan jesse jordan bryan billy joe bruce gabriel logan albert willie alan juan wayne elijah randy roy vincent ralph eugene russell bobby mason philip louis mary patricia jennifer linda elizabeth barbara susan jessica sarah karen lisa nancy betty margaret sandra ashley kimberly emily donna michelle carol amanda dorothy melissa deborah stephanie rebecca sharon laura cynthia kathleen amy angela shirley anna brenda pamela emma nicole helen samantha katherine christine debra rachel carolyn janet catherine maria heather diane ruth julie olivia joyce virginia victoria kelly lauren christina joan evelyn judith megan andrea cheryl hannah jacqueline martha gloria teresa ann sara madison frances kathryn janice jean abigail alice julia judy sophia grace denise amber doris marilyn danielle beverly isabella theresa diana natalie brittany charlotte marie kayla alexis lori".split(" ")
		self.surnames = "williams brown jones garcia miller davis rodriguez martinez hernandez lopez gonzalez wilson anderson thomas taylor moore jackson martin lee perez thompson white harris sanchez clark ramirez lewis robinson walker young allen king wright scott torres nguyen hill flores green adams nelson baker hall rivera camobell mitchell carter roberts gomez philips evans turner diaz parker cruz edwards collins reyes stewart morris morales cook rogers gutierrez ortiz morgan coiper peterson bailey reed kelly howard ramos kim cox ward richardson watson brooks chavez wood james bennet gray mendoza ruiz hughes price alvarez castillo sanders patel myerslong ross foster jimenes".split(" ")
		self.animals = "alpaca anaconda ant antelope baboon badger bat dragon beaver bee bison bobcat cat chipmunk crab dog duck eel flamingo frog goat gorilla hawk hummingbird impala monkey zebra mule owl panda parrot pig rabbit rat seal sheep skunk sloth snail tiger wombat".split(" ")
		self.cities = "tokyo delhi shanghai cairo mumbai beijing dhaka osaka karachi chongqing istanbul kolkata manila lagos tianjin kinshasa guangzhou moscow shenzhen lahore bangalore paris bogota jakarta chennai lima bangkok seoul nagoya hyderabad london tehran chicago chengdu nanjing wuhan luanda".split(" ")
		
		self.elements = "﻿Hydrogen Helium Lithium Beryllium Boron Carbon Nitrogen Oxygen Fluorine Neon Sodium Magnesium Aluminium Silicon Phosphorus Sulfur Chlorine Argon Potassium Calcium Scandium Titanium Vanadium Chromium Manganese Iron Cobalt Nickel Copper Zinc Gallium Germanium Arsenic Selenium Bromine Krypton Rubidium Strontium Yttrium Zirconium Niobium Molybdenum Technetium Ruthenium Rhodium Palladium Silver Cadmium Indium Tin Antimony Tellurium Iodine Xenon Caesium Barium Lanthanum Cerium Praseodymium Neodymium Promethium Samarium Europium Gadolinium Terbium Dysprosium Holmium Erbium Thulium Ytterbium Lutetium Hafnium Tantalum Tungsten Rhenium Osmium Iridium Platinum Gold Mercury Thallium Lead Bismuth Polonium Astatine Radon Francium Radium Actinium Thorium Protactinium Uranium Neptunium Plutonium Americium Curium Berkelium Californium Einsteinium Fermium Mendelevium Nobelium Lawrencium Rutherfordium Dubnium Seaborgium Bohrium Hassium Meitnerium Darmstadtium Roentgenium Copernicium Nihonium Flerovium Moscovium Livermorium Tennessine Oganesson".split(" ")
		
		self.nato_alphabet = "﻿Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu Zero One Two Three Four Five Six Seven Eight Nine".split(" ")
		
		self.org_prefix = "﻿Nexus Cryogenics Alpha Delsoft Hornet Foxfire Lyle Millennium Argon Nova Mayflower Durton Cobra Venus Hunley Maryland Princeton Andromeda".split(" ")
		self.org_suffix = "﻿Limited Systems LLC Cybernetics Group Corporation International Electronics Security Inc Incorporated Ltd Networks Global Dynamics Bionics &Sons Logistics".split(" ")
		
		self.sections = "art code qa audio design ui marketing it hr accounting production logistics engineering support finance payroll executives".split(" ")
		self.sub_sections = "characters environment outsource vfx lighting tech server tools render modelling animation writing management portfolio".split(" ")


	def generateList(self, number, what):
		names = []
		duplicates = 0
		while len(names) < number:
			if what == self.USER:
				new_name = self.generateUserName()
			elif what == self.GROUP:
				new_name = self.generateGroupName()
			elif what == self.PROJECT:
				new_name = self.generateProjectName()
			else:
				print("Unknown name to generate")
				break
			if not new_name in names:
				names.append(new_name)
			else:
				duplicates = duplicates + 1
			if duplicates > 100:
				print("Too many duplicates (100). No more names added.")
				break
		return names
	
	def generateProjectName(self):	
		prefix = random.choice(["A", "B", "C","C", "D"])
		if prefix == "A":
			return "Gen" + " " + random.choice(self.letters) + str(random.randint(1,10000))
		elif prefix == "B":
			return "Project " + str(random.randint(1,100000))
			
		elif prefix == "C":
			return random.choice(self.words).capitalize() + " " + random.choice(self.org_prefix).capitalize() + " " + random.choice(self.org_suffix).capitalize()
		else:
			return random.choice(self.words).capitalize() + " " + random.choice(self.words).capitalize() + " " + random.choice(self.letters).capitalize() + str(random.randint(1,100))
		
	def generateUserName(self):
		return random.choice(self.first_names).capitalize() + " " + random.choice(self.surnames).capitalize()
		
	def generateGroupName(self):
		prefix = random.choice(["Site", "Team", "Group", "Test", "Section"])
		if prefix == "Site":
			return random.choice(self.cities).capitalize() + " " + random.choice(self.letters).capitalize() + random.choice(self.numbers)
		elif prefix == "Team":
			return random.choice(self.elements).capitalize() + " " + random.choice(self.animals).capitalize() + "s"
		elif prefix == "Group":
			return random.choice(self.nato_alphabet).capitalize() + " " + random.choice(self.letters).capitalize() + random.choice(self.numbers)
		elif prefix == "Section":
			return random.choice(self.sections).capitalize() + " " + random.choice(self.sub_sections).capitalize()
		else:
			return random.choice(self.elements).capitalize() + " " + random.choice(self.nato_alphabet).capitalize()
