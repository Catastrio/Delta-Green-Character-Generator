import random
import ezsheets
import time

ss = ezsheets.Spreadsheet('')
sheet = ss[0]
 
statList = ['STR', 'CON', 'DEX', 'INT', 'POW', 'CHA']
 
statDict = {
            'STR': 'C8',
            'CON': 'C9',
            'DEX': 'C10',
            'INT': 'C11',
            'POW': 'C12',
            'CHA': 'C13'
            }


skillPackages = {
        'Artist': ['Alertness', 'Craft (Choose One)', 'Disguise',
                   'Persuade', 'Art (Choose One)', 'Art (Choose Another)',
                   'Art (Choose one more)', 'HUMINT'],
        'Actor': ['Alertness', 'Craft (Choose One)', 'Disguise',
                   'Persuade', 'Art (Choose One)', 'Art (Choose Another)',
                   'Art (Choose one more)', 'HUMINT'],
        'Musician': ['Alertness', 'Craft (Choose One)', 'Disguise',
                   'Persuade', 'Art (Choose One)', 'Art (Choose Another)',
                   'Art (Choose one more)', 'HUMINT'],
        'Athlete': ['Alertness', 'Athletics', 'Dodge', 'First Aid',
                    'HUMINT', 'Persuade', 'Swim', 'Unarmed Combat'],
        'Author': ['Anthropology', 'Art (Choose One)', 'Bureaucracy', 'History',
                   'Law', 'Occult', 'Persuade', 'HUMINT'],
        'Editor': ['Anthropology', 'Art (Choose One)', 'Bureaucracy', 'History',
                   'Law', 'Occult', 'Persuade', 'HUMINT'],
        'Journalist': ['Anthropology', 'Art (Choose One)', 'Bureaucracy', 'History',
                   'Law', 'Occult', 'Persuade', 'HUMINT'],
        '"Black Bag" Training': ['Alertness', 'Craft (Choose One)', 'Craft (Electrician)',
                                 'Craft (Locksmithing)', 'Criminology', 'Disguise',
                                 'Search', 'Stealth'],
        'Blue-Collar Worker': ['Alertness', 'Craft (choose one)', 'Craft (choose another)',
                               'Drive', 'First Aid', 'Heavy Machinery', 'Navigate', 'Search'],
        'Bureaucrat': ['Accounting', 'Bureaucracy', 'Computer Science',
                       'Criminology', 'HUMINT', 'Law', 'Persuade', 'Personal Specialty'],
        'Clergy': ['Foreign Languages (choose three)', 'History',
                       'HUMINT', 'Occult', 'Persuade', 'Psychotherapy'],
        'Combat Veteran': ['Alertness', 'Dodge', 'Firearms', 'First Aid',
                           'Heavy Weapons', 'Melee Weapons', 'Stealth', 'Unarmed Combat.'],
        'Computer Enthusiast': ['Computer Science', 'Craft (Microelectronics)', 'Science (Mathematics)',
                                'SIGINT', 'Personal Specialty'],
        'Hacker': ['Computer Science', 'Craft (Microelectronics)', 'Science (Mathematics)',
                                'SIGINT', 'Personal Specialty'],
        'Counselor': ['Bureaucracy', 'First Aid', 'Foreign Language (choose one)',
                      'HUMINT', 'Law', 'Persuade', 'Psychotherapy', 'Search'],
        'Criminalist': ['Accounting', 'Bureaucracy', 'Computer Science',
                        'Criminology', 'Forensics', 'Law', 'Pharmacy', 'Search'],
        'Firefighter': ['Alertness', 'Demolitions', 'Drive', 'First Aid',
                        'Forensics', 'Heavy Machinery', 'Navigate', 'Search.'],
        'Gangster': ['Alertness', 'Criminology', 'Dodge', 'Drive', 'Persuade', 'Stealth',
                     'Athletics', 'Foreign Language', 'Firearms', 'HUMINT',
                     'Melee Weapons', 'Pharmacy', 'Unarmed Combat'],
        'Deep Cover': ['Alertness', 'Criminology', 'Dodge', 'Drive', 'Persuade', 'Stealth',
                     'Athletics', 'Foreign Language', 'Firearms', 'HUMINT',
                     'Melee Weapons', 'Pharmacy', 'Unarmed Combat'],
        'Interrogator': ['Criminology', 'Foreign Language (choose one)',
                         'Foreign Language (choose another)','HUMINT',
                         'Law', 'Persuade', 'Pharmacy', 'Search'],
        'Liberal Arts Degree': ['Anthropology or Archeology', 'Art (choose one)', 'Foreign Language (choose one)',
                        'History', 'Persuade', 'Personal Specialty'],
        'Military officer': ['Bureaucracy', 'Firearms', 'History', 'Military Science (choose one)',
                             'Navigate', 'Persuade', 'Unarmed Combat', 'Artillery',
                             'Heavy Machinery', 'Heavy Weapons', 'HUMINT', 'Pilot (choose one)', 'SIGINT'],
        'MBA': ['Accounting', 'Bureaucracy', 'HUMINT', 'Law', 'Persuade', 'Personal Specialty'],
        'Nurse': ['Alertness', 'First Aid', 'Medicine', 'Persuade', 'Pharmacy',
                  'Psychotherapy', 'Science (Biology)', 'Search.'],
        'Paramedic': ['Alertness', 'First Aid', 'Medicine', 'Persuade', 'Pharmacy',
                  'Psychotherapy', 'Science (Biology)', 'Search.'],
        'Pre-Med': ['Alertness', 'First Aid', 'Medicine', 'Persuade', 'Pharmacy',
                  'Psychotherapy', 'Science (Biology)', 'Search.'],
        'Occult Investigator': ['Anthropology', 'Archeology', 'Computer Science', 'Criminology',
                                'History', 'Occult', 'Persuade', 'Search'],
        'Conspiracy Theorist': ['Anthropology', 'Archeology', 'Computer Science', 'Criminology',
                                'History', 'Occult', 'Persuade', 'Search'],
        'Outdoorsman': ['Alertness', 'Athletics', 'Firearms',
                        'Navigate', 'Ride', 'Search', 'Stealth', 'Survival.'],
        'Photographer': ['Alertness', 'Art (Photography)', 'Computer Science', 'Persuade',
                         'Search', 'Stealth', 'Personal Specialty'],
        'Pilot': ['Alertness', 'Craft (Mechanic)', 'First Aid', 'Foreign Language (choose one)', 'Navigate',
                   'Pilot (choose one)', 'Survival', 'Swim'],
        'Sailor': ['Alertness', 'Craft (Mechanic)', 'First Aid', 'Foreign Language (choose one)', 'Navigate',
                   'Pilot (choose one)', 'Survival', 'Swim'],
        'Police Officer': ['Alertness', 'Criminology', 'Drive', 'Firearms',
                           'HUMINT', 'Law', 'Melee Weapons', 'Unarmed Combat'],
        'Science Grad Student': ['Bureaucracy', 'Computer Use', 'Craft (choose one)', 'Foreign Language (choose one)', 'Science (choose one)',
                                 'Science (choose another)', 'Science (choose another)', 'Accounting', 'Forensics', 'Law', 'Pharmacy'],
        'Social Worker': ['Bureaucracy', 'Criminology', 'Forensics', 'Foreign Language (choose one)',
                                    'HUMINT', 'Law', 'Persuade', 'Search'],
        'Criminal Justice Degree': ['Bureaucracy', 'Criminology', 'Forensics', 'Foreign Language (choose one)',
                                    'HUMINT', 'Law', 'Persuade', 'Search'],
        'Soldier': ['Alertness', 'Artillery', 'Athletics', 'Drive', 'Firearms',
                   'Heavy Weapons', 'Military Science (Land)', 'Unarmed Combat'],
        'Marine': ['Alertness', 'Artillery', 'Athletics', 'Drive', 'Firearms',
                   'Heavy Weapons', 'Military Science (Land)', 'Unarmed Combat'],
        'Translator': ['Anthropology', 'Foreign Language (choose one)', 'Foreign Language (choose another)', 'Foreign Language (choose another)',
                       'History', 'HUMINT', 'Persuade', 'Personal Specialty'],
        'Urban explorer': ['Alertness', 'Athletics', 'Craft (choose one)', 'Law',
                           'Navigate', 'Persuade', 'Search', 'Stealth']
    }

bondsDict = {
    'Bond 1': 'F9',
    'Bond 2': 'F10',
    'Bond 3': 'F11',
    'Bond 4': 'F12',
    'Bond 5': 'F13',
    'Bond 6': 'F114'
    }

bondsScoreDict = {
    'Score 1': 'H9',
    'Score 2': 'H10',
    'Score 3': 'H11',
    'Score 4': 'H12',
    'Score 5': 'H13',
    'Score 6': 'H114'
    }
 
skillDict = {
            'Accounting': 'C23',
            'Alertness': 'C24',
            'Anthropology': 'C25',
            'Archeology': 'C26',
            'Art': 'C27',
            'Artillery': 'C29',
            'Athletics': 'C30',
            'Bureaucracy': 'C31',
            'Computer Science': 'C32',
            'Craft': 'C33',
            'Criminology': 'C35',
            'Demolitions': 'C36',
            'Disguise': 'C37',
            'Dodge': 'C38',
            'Drive': 'C39',
            'Firearms': 'C40',
            'First Aid': 'E23',
            'Forensics': 'E24',
            'Heavy Machinery': 'E25',
            'Heavy Weapons': 'E26',
            'History': 'E27',
            'HUMINT': 'E28',
            'Law': 'E29',
            'Medicine': 'E30',
            'Melee Weapons': 'E31',
            'Military Science': 'E32',
            'Navigate': 'E34',
            'Occult': 'E35',
            'Persuade': 'E36',
            'Pharmacy': 'E37',
            'Pilot': 'E38',
            'Psychotherapy': 'E40',
            'Ride': 'G23',
            'Science': 'G24',
            'Search': 'G26',
            'SIGINT': 'G27',
            'Stealth': 'G28',
            'Surgery': 'G29',
            'Survival': 'G30',
            'Swim': 'G31',
            'Unarmed Combat': 'G32',
            'Unnatural': 'G33',
            'Other Skill 1': 'G35',
            'Other Skill 2': 'G36',
            'Other Skill 3': 'G37',
            'Other Skill 4': 'G38',
            'Other Skill 5': 'G39',
            'Other Skill 6': 'G40'
             }
 
defaultSkills = {
            'Accounting': '10',
            'Alertness': '20',
            'Anthropology': '0',
            'Archeology': '0',
            'Art': '0',
            'Artillery': '0',
            'Athletics': '30',
            'Bureaucracy': '10',
            'Computer Science': '0',
            'Craft': '0',
            'Criminology': '10',
            'Demolitions': '0',
            'Disguise': '10',
            'Dodge': '30',
            'Drive': '20',
            'Firearms': '20',
            'First Aid': '10',
            'Forensics': '0',
            'Heavy Machinery': '10',
            'Heavy Weapons': '0',
            'History': '10',
            'HUMINT': '10',
            'Law': '0',
            'Medicine': '0',
            'Melee Weapons': '30',
            'Military Science': '0',
            'Navigate': '10',
            'Occult': '10',
            'Persuade': '20',
            'Pharmacy': '0',
            'Pilot': '0',
            'Psychotherapy': '0',
            'Ride': '10',
            'Science': '0',
            'Search': '20',
            'SIGINT': '0',
            'Stealth': '10',
            'Surgery': '0',
            'Survival': '10',
            'Swim': '20',
            'Unarmed Combat': '40',
            'Unnatural': '0',
            'Other Skill 1': '0',
            'Other Skill 2': '0',
            'Other Skill 3': '0',
            'Other Skill 4': '0',
            'Other Skill 5': '0',
            'Other Skill 6': '0'
             }

anthropologistHistorianSkills = {
    'choices': [{
        'Archeology': '50',
        'Anthropology': '50'
        }], 
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '40'
        },
    'profSkills': {
        'Bureaucracy': '40',
        'History': '60',
        'Occult': '40',
        'Persuade': '40'
        },
    'chooseSkills': {
        'Anthropology': '40',
        'Archeology': '40',
        'HUMINT': '50',
        'Navigate': '50',
        'Ride': '50',
        'Search': '60',
        'Survival': '50'
        }       
}

computerScienceSkills = {
    'choices': [
        ], 
    'languages': {
        },
    'profSkills': {
        'Computer Science': '60',
        'Craft (Electrician)': '60',
        'Craft (Mechanic)': '40',
        'Craft (Microelectronics)': '40',
        'Science (Mathematics)': '40',
        'SIGINT': '40'
        },
    'chooseSkills': {
        'Accounting': '50',
        'Bureaucracy': '50',
        'Craft': '40',
        'Foreign Language': '40',
        'Heavy Machinery': '50',
        'Law': '40',
        'Science': '40'
        }       
}

federalAgentSkills = {
    'choices': [
        ], 
    'languages': {
        },
    'profSkills': {
        'Alertness': '50',
        'Bureaucracy': '40',
        'Criminology': '50',
        'Drive': '50',
        'Firearms': '50',
        'Forensics': '30',
        'HUMINT': '60',
        'Law': '30',
        'Persuade': '50',
        'Search': '50',
        'Unarmed Combat': '60'
        },
    'chooseSkills': {
        'Accounting': '60',
        'Computer Science': '50',
        'Foreign Language': '50',
        'Heavy Weapons': '50',
        'Pharmacy': '50'
        }       
}

criminalSkills = {
    'choices': [
        ], 
    'languages': {
        },
    'profSkills': {
        'Alertness': '50',
        'Criminology': '60',
        'Dodge': '40',
        'Drive': '50',
        'Firearms': '40',
        'Law': '40',
        'Melee Weapons': '40',
        'Persuade': '50',
        'Stealth': '50',
        'Unarmed Combat': '50'
        },
    'chooseSkills': {
        'Craft (Locksmithing)': '40',
        'Demolitions': '40',
        'Disguise': '50',
        'Foreign Language (Choose One)': '40',
        'Forensics': '40',
        'HUMINT': '50',
        'Navigate': '50',
        'Occult': '50',
        'Pharmacy': '40'
        }       
}

physicianSkills = {
    'choices': [
        ], 
    'languages': {
        },
    'profSkills': {
        'Bureaucracy': '50',
        'First Aid': '60',
        'Medicine': '60',
        'Persuade': '40',
        'Pharmacy': '50',
        'Science (Biology)': '60',
        'Search': '40'
        },
    'chooseSkills': {
        'Forensics': '50',
        'Psychotherapy': '60',
        'Science (Choose One)': '50',
        'Surgery': '50'
        }       
}

scientistSkills = {
    'choices': [
        ], 
    'languages': {
        },
    'profSkills': {
        'Bureaucracy': '40',
        'Computer Science': '40',
        'Science (choose one)': '60',
        'Science (choose another)': '50',
        'Science (choose one more)': '50',
        },
    'chooseSkills': {
        'Accounting': '60',
        'Craft (choose one)': '40',
        'Foreign Language (choose one)': '40',
        'Forensics': '40',
        'Law': '40',
        'Pharmacy': '40'
        }       
}

specialOperatorSkills = {
    'choices': [
        ], 
    'languages': {
        },
    'profSkills': {
        'Alertness': '60',
        'Athletics': '60',
        'Demolitions': '40',
        'Firearms': '60',
        'Heavy Weapons': '50',
        'Melee Weapons': '50',
        'Military Science (Land)': '60',
        'Navigate': '50',
        'Stealth': '50',
        'Survival': '50',
        'Swim': '50',
        'Unarmed Combat': '60',
        },
    'chooseSkills': {
        }       
}

firefighterSkills = {
    'choices': [
        ], 
    'languages': {
        },
    'profSkills': {
        'Alertness': '50',
        'Athletics': '60',
        'Craft (Electrician)': '40',
        'Craft (Mechanic)': '40',
        'Demolitions': '50',
        'Drive': '50',
        'First Aid': '50',
        'Forensics': '40',
        'Heavy Machinery': '50',
        'Navigate': '50',
        'Search': '40',
        },
    'chooseSkills': {
        }       
}

foreignServiceOfficerSkills = {
    'choices': [
        ], 
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '50',
        'Foreign Language (choose one more)': '40',
        },
    'profSkills': {
        'Accounting': '50',
        'Anthropology': '40',
        'Bureaucracy': '60',
        'History': '40',
        'HUMINT': '50',
        'Law': '40',
        'Persuade': '50',
        },
    'chooseSkills': {
        }       
}

intelligenceAnalystSkills = {
    'choices': [
        ], 
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '50',
        'Foreign Language (choose one more)': '40',
        },
    'profSkills': {
        'Anthropology': '40',
        'Bureaucracy': '50',
        'Computer Science': '40',
        'Criminology': '50',
        'History': '40',
        'HUMINT': '50',
        'SIGINT': '40',
        },
    'chooseSkills': {
        }       
}

lawyerBusinessExecutiveSkills = {
    'choices': [
        ], 
    'languages': {
        },
    'profSkills': {
        'Accounting': '40',
        'Bureaucracy': '50',
        'HUMINT': '50',
        'Persuade': '40',
        },
    'chooseSkills': {
        'Computer Science': '50',
        'Criminology': '60',
        'Foreign Language (choose one)': '50',
        'Law': '50',
        'Pharmacy': '50',
        }       
}

intelligenceCaseOfficerSkills = {
    'choices': [
        ], 
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '40',
        },
    'profSkills': {
        'Alertness': '50',
        'Bureaucracy': '40',
        'Criminology': '50',
        'Disguise': '50',
        'Drive': '40',
        'Firearms': '40',
        'HUMINT': '60',
        'Persuade': '60',
        'SIGINT': '40',
        'Stealth': '50',
        'Unarmed Combat': '50',
        },
    'chooseSkills': {
        }       
}

mediaSpecialistSkills = {
    'choices': [{
        'Art (Creative Writing)': '60',
        'Art (Journalism)': '60',
        'Art (Poetry)': '60',
        'Art (Scriptwriting)': '60',
        }],  
    'languages': {
        },
    'profSkills': {
        'History': '40',
        'HUMINT': '40',
        'Persuade': '50',
        },
    'chooseSkills': {
        'Anthropology': '40',
        'Archeology': '40',
        'Art (choose one)': '40',
        'Bureaucracy': '50',
        'Computer Science': '40',
        'Criminology': '50',
        'Foreign Language (choose one)': '40',
        'Law': '40',
        'Military Science (choose one)': '40',
        'Occult': '50',
        'Science (choose one)': '40',
        }       
}

nurseParamedicSkills = {
    'choices': [
        ],  
    'languages': {
        },
    'profSkills': {
        'Alertness': '40',
        'Bureaucracy': '40',
        'First Aid': '60',
        'HUMINT': '40',
        'Medicine': '40',
        'Persuade': '40',
        'Pharmacy': '40',
        'Science (Biology)': '40',
        },
    'chooseSkills': {
        'Drive': '60',
        'Forensics': '40',
        'Navigate': '50',
        'Psychotherapy': '50',
        'Search': '60',
        }       
}

pilotSailorSkills = {
    'choices': [
        ],  
    'languages': {
        },
    'profSkills': {
        'Alertness': '60',
        'Bureaucracy': '30',
        'Craft (Electrician)': '40',
        'Craft (Mechanic)': '40',
        'Navigate': '50',
        'Pilot (choose one)': '60',
        'Science (Meteorology)': '40',
        'Swim': '40',
        },
    'chooseSkills': {
        'Foreign Language (choose one)': '50',
        'Pilot (choose another one)': '50',
        'Heavy Weapons': '50',
        'Military Science (choose one)': '50',
        }      
}

policeOfficerSkills = {
    'choices': [
        ],  
    'languages': {
        },
    'profSkills': {
        'Alertness': '60',
        'Bureaucracy': '40',
        'Criminology': '40',
        'Drive': '50',
        'Firearms': '40',
        'First Aid': '30',
        'HUMINT': '50',
        'Law': '30',
        'Melee Weapons': '50',
        'Navigate': '40',
        'Persuade': '40',
        'Search': '40',
        'Unarmed Combat': '60',
        },
    'chooseSkills': {
        'Forensics': '50',
        'Heavy Machinery': '60',
        'Heavy Weapons': '50',
        'Ride': '60',
        }       
}

programManagerSkills = {
    'choices': [
        ], 
    'languages': {
        'Foreign Language (choose one)': '50'
        },
    'profSkills': {
        'Accounting': '60',
        'Bureaucracy': '60',
        'Computer Science': '50',
        'History': '40',
        'Law': '40',
        'Persuade': '50'
        },
    'chooseSkills': {
        'Anthropology': '30',
        'Art (choose one)': '30',
        'Craft (choose one)': '30',
        'Science (choose one)': '30'
        }       
}

soldierMarineSkills = {
    'choices': [
        ],  
    'languages': {
        },
    'profSkills': {
        'Alertness': '50',
        'Athletics': '50',
        'Bureaucracy': '30',
        'Drive': '40',
        'Firearms': '40',
        'First Aid': '40',
        'Military Science (Land)': '40',
        'Navigate': '40',
        'Persuade': '30',
        'Unarmed Combat': '50',
        },
    'chooseSkills': {
        'Artillery': '40',
        'Computer Science': '40',
        'Craft (choose one)': '40',
        'Demolitions': '40',
        'Foreign Language (choose one)': '40',
        'Heavy Machinery': '50',
        'Heavy Weapons': '40',
        'Search': '60',
        'SIGINT': '40',
        'Swim': '60',
        }       
}

anthroHisto = {'profSkill': anthropologistHistorianSkills,
               'numOfChoices': 2,
               'bonds': 4,
               'recStat': 'INT'
               }

compSciHack = {'profSkill': computerScienceSkills,
               'numOfChoices': 4,
               'bonds': 3,
               'recStat': 'INT'
               }

fedAgent = {'profSkill': federalAgentSkills,
            'numOfChoices': 1,
            'bonds': 3,
            'recStat': 'CON, POW, CHA'
            }

physician = {'profSkill': physicianSkills,
            'numOfChoices': 2,
            'bonds': 3,
            'recStat': 'INT, POW, CON'
            }

scientist = {'profSkill': scientistSkills,
            'numOfChoices': 3,
            'bonds': 4,
            'recStat': 'INT'
            }

specOp = {'profSkill': specialOperatorSkills,
            'numOfChoices': 0,
            'bonds': 2,
            'recStat': 'STR, CON, POW'
            }

criminal = {'profSkill': criminalSkills,
            'numOfChoices': 2,
            'bonds': 4,
            'recStat': 'STR, DEX'
            }

firefighter = {'profSkill': firefighterSkills,
            'numOfChoices': 0,
            'bonds': 3,
            'recStat': 'STR, DEX, CON'
            }

fso = {'profSkill': foreignServiceOfficerSkills,
            'numOfChoices': 0,
            'bonds': 3,
            'recStat': 'INT, CHA'
            }

intelAnal = {'profSkill': intelligenceAnalystSkills,
            'numOfChoices': 0,
            'bonds': 3,
            'recStat': 'INT'
            }

lawExec = {'profSkill': lawyerBusinessExecutiveSkills,
            'numOfChoices': 4,
            'bonds': 4,
            'recStat': 'INT, CHA'
            }

ico = {'profSkill': intelligenceCaseOfficerSkills,
            'numOfChoices': 0,
            'bonds': 2,
            'recStat': 'INT, POW, CHA'
            }

medSpec = {'profSkill': mediaSpecialistSkills,
            'numOfChoices': 5,
            'bonds': 4,
            'recStat': 'INT, CHA'
            }

nursePara = {'profSkill': nurseParamedicSkills,
            'numOfChoices': 2,
            'bonds': 4,
            'recStat': 'INT, POW, CHA'
            }

piloSail = {'profSkill': pilotSailorSkills,
            'numOfChoices': 2,
            'bonds': 3,
            'recStat': 'DEX, INT'
            }

police = {'profSkill': policeOfficerSkills,
            'numOfChoices': 1,
            'bonds': 3,
            'recStat': 'STR, CON, POW'
            }

progMana = {'profSkill': programManagerSkills,
            'numOfChoices': 1,
            'bonds': 4,
            'recStat': 'INT, CHA'
            }

soldier = {'profSkill': soldierMarineSkills,
            'numOfChoices': 3,
            'bonds': 4,
            'recStat': 'STR, CON'
            }

statArray = []

statPoints = 72

inventory = ['Glock 19 (Medium Pistol)', 'First Aid Kit', 'Self-Applying Tourniquet',
          'Hemostatic Gel', 'Clothes', 'Boxes of Ammunition', 'S&W Model 36 (Light Pistol)',
          'Extra Pistol Magazines', 'Flashlight', 'Folding Knife (Knife)', 'Basic Tools',
          'Doorstops', 'Chalk', 'Bottled Water', 'Energy Bars', 'Batteries', 'Sunscreen',
          'Antibacterial Gel', 'Dufflebag or Backpack']

listOfMotivations = ['Exploiting the unnatural', 'Recognition for achievements',
                     'Showing others how its done', 'Correcting past mistakes',
                     'Success despite obstacles', 'Proving my worth', 'Getting the job done',
                     'Living up to expectations', 'Doing a job no one else can do',
                     'Constant improvement', 'Conspiracy theorizing',
                     'Making sense of a past tragedy', 'The thrill of discovery',
                     'Exploration', 'Solving a particular mystery', 'Understanding the unnatural',
                     'Learning a groups secrets', 'Expanding human knowledge',
                     'Solving hard problems', 'Survival at all costs',
                     'Professionalism', 'Doing whats right', 'Following the law',
                     'Healing', 'Faith', 'Patriotism', 'Personal integrity', 'Atonement',
                     'Protect a bond', 'Protect my family', 'Protect my friends/colleagues',
                     'Protect an organization', 'Protect a community', 'Protect my country',
                     'Protect humanity', 'Protect innocents',
                     'Figuring out what people want to hear', 'Telling lies from the turth',
                     'Communication', 'Diplomacy', 'Family obligations',
                     'Knowing what makes people tick', 'We can fix this',
                     'Never letting a particular bond down', 'New romance',
                     'Recruiting new agents and friendlies', 'Investigating...',
                     'Revenge against...', 'Staying one step ahead of...', 'Stopping...',
                     'A beloved pet', 'Favorite academic pursuit', 'Favorite art form',
                     'Favorite hobby', 'Favorite bad habit', 'Finding true meaning',
                     'Home', 'Sports', 'Intimacy', 'Anything for a sense of control']

listOfBonds = ['Spouse', 'Ex-Spouse', 'Son', 'Daughter',
               'Parent', 'Grandparent', 'Best Friend',
               'Coworker', 'Partner', 'Psychologist',
               'Therapist', 'Spouse & Children', 'Parents',
               'Siblings', 'Colleagues in an intense job',
               'Church', 'Support Group', 'Survivors of a shared trauma',
               'Brother', 'Sister']

listOfEmployers = ['Federal Bureau of Investigation', 'Drug Enforcement Administration',
                   'Immigration & Customs Enforcement', 'U.S. Marshal',
                   'U.S. Army', 'U.S. Airforce', 'U.S. Navy', 'U.S. Marines',
                   'U.S. Special Operations Command', 'Central Intelligence Agency',
                   'Department of State', 'Centre for Disease Control', 'None']

listOfProfessions = ['Anthropologist', 'Historian', 'Computer Scientist',
                     'Engineer', 'Federal Agent', 'Physician',
                     'Scientist', 'Special Operator', 'Criminal',
                     'Firefighter', 'Foreign Service Officer',
                     'Intelligence Analyst', 'Lawyer', 'Business Executive',
                     'Intelligence Case Officer', 'Media Specialist', 'Nurse',
                     'Paramedic', 'Police Officer', 'Pilot', 'Sailor',
                     'Program Manager', 'Soldier', 'Marine']

listOfDisorders = ['Amnesia', 'Depersonalization Disorder', 'Depression',
                   'Dissociative Identity Disorder', 'Fugues', 'Megalomania',
                   'Paranoia', 'Sleep Disorder']


def mergeDictsReplace(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict2[key] = int(dict1[key])# + int(dict2[key])
            del dict1[key]
    dict2.update(dict1)
    return dict2


def mergeDicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict2[key] = int(dict2[key]) + int(dict1[key])
            del dict1[key]
    dict2.update(dict1)
    return dict2

def spendBonusPoints(listOfSkills):
    startingPoints = 160
    spentPoints = 20
    currentPoints = startingPoints
    i = 1
    skillsDict = {}
    for item in listOfSkills:
        if item not in skillDict.keys():
            skillsDict[item] = 0

    printFromList(listOfSkills)
    print("\nPlease select a skill to put " + str(spentPoints) + " points into.")
    while currentPoints > 0:
        print("You have " + str(currentPoints) + " remaining.")
        choice = input()
        try:
            choice = int(choice)
        except:
            ("Please input at number.")
            continue

        choice = choice - 1
        
        if choice < len(listOfSkills):
            chosenSkill = listOfSkills[choice]
        else:
            print("Please input a smaller number.")
            continue
        
        if chosenSkill in skillsDict.keys():
            specialSkill = skillsDict[chosenSkill] + spentPoints
            if specialSkill <= 80:
                skillsDict.update({chosenSkill: int(skillsDict[chosenSkill]) + spentPoints})
                print("\nYour " + chosenSkill + " stat is: " + str(skillsDict[chosenSkill]))
                currentPoints = currentPoints - spentPoints
                continue
            if skillsDict[chosenSkill] > 80:
                print("Please choose a different skill. Can't exceed 80% right now.")
                continue
        
        statValue = int(sheet.get(skillDict[chosenSkill]).replace('%', ''))
        statValue = statValue + spentPoints

        if statValue <= 80:
            sheet[skillDict[chosenSkill]] = str(statValue) + "%"
            print("\nYour " + chosenSkill + " stat is: " + str(statValue))
            currentPoints = currentPoints - spentPoints
            continue
        if statValue > 80:
            print("\nPlease choose a different skill. Can't exceed 80% right now.")
            continue

    removalList = []
    for key in skillsDict.keys():
        if skillsDict[key] == 0:
            removalList.append(key)

    for item in removalList:
        skillsDict.pop(item)
   
    return skillsDict

        
def printFromList(inputList):
    i = 1
    for item in inputList:
        print(str(i) + ". " + item)
        i += 1
    

def printBonusSkills(skillPackages):
    i = 1
    for key in skillPackages.keys():
        print(str(i) + ". " + key + ': \n' + ', '.join([str(elem) for elem in skillPackages[key]]) + '\n')
        i += 1

def printSkills(chosenSkills):
    i = 1
    for skill in chosenSkills:
        print(str(i) + ". " + skill)
        i += 1
    

def setBonusSkills(skillPackages):
    print("\nSelect a bonus skill package to put points into\n")
    printBonusSkills(skillPackages)
    print("Please select a skill package by number:")
    while True:
        choice = input()
        try:
            choice = int(choice)
        except:
            print("Please enter a number")
            continue
        try:
            choice -= 1
            userChoice = list(skillPackages.keys())[choice]
        except:
            print("Please use a different number")
            continue
        break

    return list(skillPackages.keys())[choice]

def getPackageSkills(skillPackages, choice):
    print("You've chosen: " + choice)
    return skillPackages[choice]
 
def randomStat():
    Stat = sum(sorted([random.randint(1,6) for x in range(4)])[1:])
    return Stat
 
def setSkillValue(skillDict, choice, amount):
    iterator = 4
    skills = list(skillDict.keys())
    while iterator > 0:
        print("Please select a skill:")
        choice = input()
        try:
            choice = int(choice)
        except:
            print("Enter a number.")
            continue

        if choice < len(skills):
            choice = choice - 1
            yourChoice = skills[int(choice) - 1]
            chosenSkill = skills[choice]
            chosenStat = skillDict[chosenSkill]
            stat = int(sheet.get(chosenStat).replace('%', ''))
            stat = stat + amount
            sheet[chosenStat] = str(stat) + "%"
            iterator -= 1
            continue
        else:
            print("Please try again!")
            continue
 
def setStatArray():
    statArray = []
    for loops in range(6):
        stat = randomStat()
        statArray.append(stat)
        statArray.sort(reverse = True)
    return statArray
 
def compareDicts(skillDict, profDict):
    listOfSkills = []
    for key in skillDict.keys():
        
        if key not in profDict.keys():
            listOfSkills.append(key)
 
        setSheetValue(skillDict, key, str(profDict[key]) + "%")
        
 
def setSheetValue(dictName, dictKey, sheetValue):
    sheet[dictName[dictKey]] = sheetValue

def setSheetName(cellKey, value):
    sheet[cellKey] = value
 
def setSkills(skillDict, profDict):
    iterator = 1
    cellIterator = 35
    for key in profDict.keys():
        if key in skillDict:
            setSheetValue(skillDict, key, str(profDict[key]) + '%')
        if key not in skillDict:
            value = key
            key = 'Other Skill ' + str(iterator)
            cellKey = "F" + str(cellIterator)
            iterator += 1
            cellIterator += 1
            setSheetName(cellKey, value)
            setSheetValue(skillDict, key, str(profDict[value]) + '%')
            
    cellIterator += 1
    
 
def setSpentPoints(amount):
    global statPoints
    statPoints -= amount
 
def updateStatList(choice):
    if choice in statList:
        statList.remove(choice)
 
def setStatValue(statName, amount):
    if statName in statList:
        sheet[statDict[statName]] = amount
    if statName not in statList:
        choice = input("Please choose from: " + str(statList) + "!\n")
        setStatValue(choice, amount)

def setSheetStatValue(statArray):
    while True:
        choice = input("\nWhere would you like to place: " + str(statArray[0]) + "?\n")
        try:
            choice = int(choice)
        except:
            print("Please input a number.")
            continue
        statIndex = choice - 1
        try:
            statChoice = statList[statIndex]
            print(statChoice)
        except IndexError:
            print("\nYour number isn't on the list. Try again")
            continue

        sheet[statDict[statChoice]] = statArray[0]
        updateStatList(statChoice)
        break
    
    
        
##def resetStats(statArray):
##     while len(statArray) > 0:
##            for stat in statList:
##                setSheetStatValue(statArray)
##                updateStatList(stat)
##                statArray.pop(0)
            
def setStatDistribution(statArray):
    while len(statArray) > 0:
            print("\nPlease choose from the following:")
            i = 1
            for item in statList:
                print(str(i) + ". " + item)
                i += 1
            setSheetStatValue(statArray)
            statArray.pop(0)
 
def handleRandomStats():
    statArray = setStatArray()
    print('Your stats are: ' + str(statArray) + " which totals " + str(sum(statArray)))
    print('Are you satisfied? Y to continue, N to reroll\n')
    while True:
        choice = input()
        if choice.lower() == "y":
            setStatDistribution(statArray)
            break
        if choice.lower() == "n":
            handleRandomStats()
##        else:
##            print("Please select Y or N")
##            continue
            
    return statArray
            
def printListedProfessions():
    i = 0
    while i < len(listOfProfessions):
        print(str(i + 1) + ". " + listOfProfessions[i])
        i += 1

def affirm():
    print("\nAre you sure? Y/N")
    choice = input()
    if choice.lower() == "y":
        return True
    elif choice.lower() == "n":
        return False
    else:
        print("Please input Y or N")

def printProfessionInfo(profSkill, numOfChoices, bonds, recStat):
    iterator = 1
    print("\nYour professional skills:")
    for key in profSkill["profSkills"]:
        print(str(iterator) + ". " + key + ": " + profSkill["profSkills"][key] + "%")
        iterator += 1
    print("\nYou'll be able to choose " + str(numOfChoices) + " skills from:")
    iterator = 1
    for key in profSkill["chooseSkills"]:
        print(str(iterator) + ". " + key + ": " + profSkill["chooseSkills"][key] + "%")
        iterator += 1
    print("\nYou'll have " + str(bonds) + " bonds")
    print("\nThis profession's recommended stats are: " + recStat)
    

def confirmSelection(userChoice):
    if userChoice == "Anthropologist" or userChoice == "Historian":
        print('''\nDescription:\nYou study humanity. You’re concerned with the
patterns that emerge over time, across land masses,
cultures, and language groups. You might be a number-
cruncher, a field worker trudging through the jungle,
a consultant in a war zone, or a think-tank analyst
sifting myth from history in studies of the Tcho-Tcho
peoples.''')
        printProfessionInfo(**anthroHisto)
        if affirm():
            return setProfessionSkills(**anthroHisto)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))
        
    if userChoice == "Computer Scientist" or userChoice == "Engineer":
        print('''Computers and machinery are the backbone of
modern industry. You are a craftsman with data or
machinery, possibly for the government and most
definitely for profit. However you use your skills,
the overlap between information technology and
awareness of the unnatural could make this the most
dangerous job on the planet.''')
        printProfessionInfo(**compSciHack)
        if affirm():
            return setProfessionSkills(**compSciHack)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Federal Agent":
        print('''Many Delta Green Agents are federal law enforcement
officers, mostly from the FBI. Delta Green decided
long ago that federal agents have the optimum balance
of skills and mental stability needed to confront
the unnatural.''')
        printProfessionInfo(**fedAgent)
        if affirm():
            return setProfessionSkills(**fedAgent)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Physician":
        print('''Doctors are often the first to uncover signs of an unnatural
incursion, and the most valuable investigators
of its disastrous effects on humanity.''')
        printProfessionInfo(**physician)
        if affirm():
            return setProfessionSkills(**physician)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Scientist":
        print('''You expand human knowledge in a field such as
biology, physics, or chemistry. When certain forms of
knowledge cause insanity and death, it’s easy to conclude
that some hypotheses should not be tested.''')
        printProfessionInfo(**scientist)
        if affirm():
            return setProfessionSkills(**scientist)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Special Operator":
        print('''As part of a force like the U.S. Army Rangers, you
volunteered for a more difficult path than other soldiers.
You’ve spent years in the most grueling training
on the planet, and now serve on the most dangerous
missions around.''')
        printProfessionInfo(**specOp)
        if affirm():
            return setProfessionSkills(**specOp)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Criminal":
        print('''So much is illegal that there are broad economies of crime.
This profile fits a hardened militant or a traditional “black
collar” criminal: pimp, burglar, extortionist, or thug. If you
want a white-collar criminal, choose Computer Scientist or
Business Executive and make very risky decisions.''')
        printProfessionInfo(**criminal)
        if affirm():
            return setProfessionSkills(**criminal)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Firefighter":
        print('''Your job oscillates between the tedium of maintaining your
gear, exhilaration when the alarm finally comes, and the
work of investigating a scene after the smoke has cleared. If
you’re involved with Delta Green, you clearly stumbled into
something worse than a house fire.''')
        printProfessionInfo(**firefighter)
        if affirm():
            return setProfessionSkills(**firefighter)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Foreign Service Officer":
        print('''You travel to strange lands, meet interesting people, and
try to get along with them. Odds are you work for the State
Department, though USAID, the Commercial Service and
the Foreign Agriculture Service also have FSOs. Either way,
you’ve had every opportunity to learn exotic and deadly
things; the kinds of things that qualify you for Delta Green
clearance.''')
        printProfessionInfo(**fso)
        if affirm():
            return setProfessionSkills(**fso)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Intelligence Analyst":
        print('''In the FBI, NSA and CIA, there are those who gather
information and those who decide what it means. You
take information from disparate sources—newspapers,
websites, informants, ELINT, and the assets developed by
Case Officers—and figure out what it means. In short,
your job is the piecing together of unrelated knowledge, a
dangerous endeavor in the world of Delta Green.''')
        printProfessionInfo(**intelAnal)
        if affirm():
            return setProfessionSkills(**intelAnal)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Lawyer" or userChoice == "Business Executive":
        print('''Your tools are a computer and smartphone. You might
be moving millions of dollars, or bits of data, or both.
Or you might be a prosecutor, a defense attorney, or
judge.''')
        printProfessionInfo(**lawExec)
        if affirm():
            return setProfessionSkills(**lawExec)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Intelligence Case Officer":
        print('''You recruit people to spy on their own countries for your
agency, probably the CIA. Your job is to develop foreign
intelligence sources (‘assets’), communicate with them,
and keep them under control, productive, and alive. It’s
a hard business because you must view everyone as a
potential threat, liar, or tool to further your agenda. If your
name came to the attention of Delta Green, congratulations;
you are now someone else’s asset.''')
        printProfessionInfo(**ico)
        if affirm():
            return setProfessionSkills(**ico)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Media Specialist":
        print('''You might be an author, an editor, a researcher for a
company or any branch of the government, a blogger,
a TV reporter, or a scholar of rare texts. With the
unnatural, you’ve uncovered the stor y of a lifetime.''')
        printProfessionInfo(**medSpec)
        if affirm():
            return setProfessionSkills(**medSpec)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Nurse" or userChoice == "Paramedic":
        print('''Medical professionals are on the front line when awful
things happen. Is that what brought you to the group’s
attention?''')
        printProfessionInfo(**nursePara)
        if affirm():
            return setProfessionSkills(**nursePara)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Pilot" or userChoice == "Sailor":
        print('''Air or sea, commercial or military, your duty is to keep your
passengers alive and craft intact. This can lead to hard
choices when your passengers put the vehicle in danger. Or
are you a drone operator, flying a Predator from a thousand
miles away? Either way, what op brought you to the attention
of Delta Green?''')
        printProfessionInfo(**piloSail)
        if affirm():
            return setProfessionSkills(**piloSail)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Police Officer":
        print('''You serve and protect. Police officers walk the beat in uniform.
Deputy sheriffs answer to an elected law enforcer and
have jurisdiction over an entire county. Detectives come in
after the fact and put the pieces together.''')
        printProfessionInfo(**police)
        if affirm():
            return setProfessionSkills(**police)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))

    if userChoice == "Program Manager":
        print('''You run an organization. Someone has to secure funding, move
resources, and make connections—and that’s you. You control
a budget and are responsible for how your program is maintained
and where the money goes. Organizations discover the
most startling things in their pursuit of profit or the public good.''')
        printProfessionInfo(**progMana)
        if affirm():
            return setProfessionSkills(**progMana)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))
        
    if userChoice == "Soldier" or userChoice == "Marine":
        print('''Governments will always need boots on the ground and
steady hands holding rifles. When war begins, civilization
gets out of the way. With the social contract void, unnatural
things creep in at the edges. There’s a reason Delta Green
began in the military.''')
        printProfessionInfo(**soldier)
        if affirm():
            return setProfessionSkills(**soldier)
        else:
            return confirmSelection(getProfessionSelection(listOfProfessions))   
        
       
def getProfessionSelection(profList):
    printListedProfessions()
    print("\nPlease select a profession by number:")
    while True:
        choice = input()
        try:
            choice = int(choice)
        except:
            print("Please enter a number")
            continue
        try:
            choice -= 1
            userChoice = profList[choice]
        except:
            print("Please use a different number")
            continue
        break

    print("\nYou have chosen: " + userChoice)
    return userChoice
 
def setProfessionStats(profChoice):
    print("You have chosen: " + profChoice)

def setProfessionSkills(profSkill, numOfChoices, bonds, recStat):
    dictOfSkillAssigns = {}
    skillsList = []
    iterator = 1
    
    for choices in profSkill.get('choices'):
        listOfChoices = list(choices.keys())
        
        for item in listOfChoices:
            print(str(iterator) + ". " + item)
            iterator += 1
        while True:
            choice = input()
            try:
                choice = int(choice)
            except:
                print("Please input a number.")
                continue
            try:
                choice -= 1
                userChoice = listOfChoices[choice]
            except:
                print("Please try a different number.")
                continue
            
            if choice < len(listOfChoices):
                print("You've chosen " + userChoice + ": " + choices[userChoice])
                dictOfSkillAssigns.update({userChoice: choices[userChoice]})
                break
            else:
                print('Please enter the correct skill name.')

    iterator = 1
                
    for language in list(profSkill['languages'].items()):
        print('Please choose ' + language[0])
        choice = input()
        print("You've chosen " + choice + " " + language[1])
        dictOfSkillAssigns.update({"Foreign Language (" + choice + ")": language[1]})

    for skill in profSkill['profSkills'].items():
        dictOfSkillAssigns.update({skill[0]: skill[1]})

    if numOfChoices > 0:
        print("Please choose " + str(numOfChoices) + " skills from this list that you don't already have: ")
        for skill in profSkill['chooseSkills'].items():
            skillsList.append(skill[0])
            print(str(iterator) + ". " + skill[0] + ": " + skill[1])
            iterator += 1
        
    while numOfChoices > 0:
        choice = input()
        try:
            choice = int(choice)
        except:
            print("Please input a number.")
            continue
        try:
            choice -= 1
            userChoice = skillsList[choice]
        except:
            print("Please try a different number.")
            continue
        
        if choice < len(skillsList):
            dictOfSkillAssigns.update({userChoice: profSkill['chooseSkills'][userChoice]})
            numOfChoices -= 1
            if numOfChoices == 0:
                break
            print("You chose " + userChoice + " please select " + str(numOfChoices) + " more.")
            
        else:
            print("Please enter the correct skill number.")
            
    print("\nUpdating values on character sheet, please wait...")
    return dictOfSkillAssigns

def resetSkills():
    print("Resetting stats...")
    sheet['C8'] = "12"
    sheet['C9'] = "12"
    sheet['C10'] = "12"
    sheet['C11'] = "12"
    sheet['C12'] = "12"
    sheet['C13'] = "12"

    print("Resetting skills...")
    setSkills(skillDict, defaultSkills)
    skillReset = 6
    cellIterator = 35
    iterator = 1
    while skillReset > 0:
        key = 'Other Skill ' + str(iterator)
        cellKey = "F" + str(cellIterator)
        iterator += 1
        cellIterator += 1
        skillReset -= 1
        setSheetName(cellKey, key)
        setSheetValue(skillDict, key, defaultSkills[key] + '%')
    skillReset = 5
    cellIterator = 9

    print("Resetting bonds...")
    while skillReset > 0:
        key = ''
        cellKey = "F" + str(cellIterator)
        iterator += 1
        cellIterator += 1
        skillReset -= 1
        setSheetName(cellKey, key)
    skillReset = 5
    cellIterator = 9
    while skillReset > 0:
        key = ''
        cellKey = "H" + str(cellIterator)
        iterator += 1
        cellIterator += 1
        skillReset -= 1
        setSheetName(cellKey, key)

    print("Resetting name, age, profession, etc..")
    sheet['E1'] = "John Doe"
    sheet['B3'] = ''
    sheet['C4'] = 'None'
    sheet['C5'] = ''
    sheet['G5'] = ''
    sheet['H5'] = ''
    sheet['J40'] = ''
    sheet['D3'] = ' '
    sheet['D18'] = ' '
    sheet['D19'] = ' '
    sheet['J3'] = 'None'
    sheet['J4'] = 'None'
    sheet['J5'] = 'None'

    print("Resetting motivations...")
    keyIterator = 16
    i = 6
    while i > 0:
        key = ("E" + str(keyIterator))
        sheet[key] = ' '
        keyIterator += 1
        i -= 1

    print("Resetting inventory...")
    keyIterator = 28
    indexIterator = 0

    while indexIterator < 11:
        key = "J" + str(keyIterator)
        item = ' '
        keyIterator += 1
        indexIterator += 1
        sheet[key] = item
    keyIterator = 28
    while indexIterator < 22:
        key = "M" + str(keyIterator)
        item = ' '
        keyIterator += 1
        indexIterator += 1
        sheet[key] = item
        
    
        
    
        
        
def pointBuy(points):
    spentPoints = getSpentPoints(points)
    chosenStat = getChosenStat(spentPoints)
    setStatValue(chosenStat, spentPoints)
    updateStatList(chosenStat)
    setSpentPoints(int(spentPoints))
    return int(spentPoints)

def handlePointBuy(statPoints):
    currentPoints = statPoints
    while currentPoints > 0:
        points = pointBuy(currentPoints)
        currentPoints -= points

def getSpentPoints(points):
    print("You have " + str(points) + " points. How many would you like to spend?\n")
    while True:
        spentPoints = input()
        try:
            spentPoints = int(spentPoints)
        except ValueError:
            print("Please input a number")
            continue

        if spentPoints > 0 and (points - spentPoints) >= 0:
            return spentPoints
            continue
        else:
            print("Please try again")

def handleStandardArray():
    statArray = []
    print("\nPlease select from the following arrays:")
    print("1. Well Rounded: 13, 13, 12, 12, 11, 11")
    print("2. Focused: 15, 14, 12, 11, 10, 10")
    print("3. Highly Focused: 17, 14, 12, 10, 10, 9")
    print("This choice cannot be modified.")
    choice = input()
    if choice == "1":
        statArray = [13, 13, 12, 12, 11, 11]
    if choice == "2":
        statArray = [15, 14, 12, 11, 10, 10]
    if choice == "3":
        statArray = [17, 14, 12, 10, 10, 9]
    setStatDistribution(statArray)

def getChosenStat(points):
    print("What stat would you like to put " + str(points) + " into?\nPlease choose from " + str(statList) + "\n")
    chosenStat = input()
    return chosenStat

def handleDerivedStats():
    getStrCon = int(sheet['C8']) + int(sheet['C9'])
    dividedStrCon = float(getStrCon / 2)
    multipliedPow = int(sheet['C12'] * 5)
    getSanPow = int(multipliedPow - int(sheet['C12'])) 
    print("This is handled by the sheet but we will double check.")
    print("HP is equal to STR + CON (" + str(getStrCon) + ") divided by 2 (" + str(dividedStrCon) + ") rounded up (" + str(round(dividedStrCon)) + ") ")
    print("WP is equal to POW (" + str(sheet['C12']) + ") ")
    print("SAN is equal to POW x 5 (" + str(multipliedPow) + ") ")
    print("BP is equal to SAN - POW (" + str(getSanPow) + ") ")

def handleStatistics():
    options = [1, 2, 3, 4]
    while True:
        choice = input("Choose an option:\n1.Roll\n2.Point buy\n3.Array\n4.Reset Sheet\n")
        try:
            choice = int(choice)
        except:
            print("Please input a number.")
            continue

        if choice in options:
            if choice == 1:
                handleRandomStats()
                break
            if choice == 2:
                handlePointBuy(statPoints)
                break
            if choice == 3:
                handleStandardArray()
                break
            if choice == 4:
                resetSkills()
                quit()
                    
        if choice not in options:
            print("Please input a number on the list")
            
def printBonds(profName, profDict):
    print("\nAs a " + profName + " you have " + str(profDict['bonds']) + " bonds.")

def getBondsChoice(userChoice, profDict):
    printBonds(userChoice, profDict)
    
    print("\nWould you like to choose your bonds or create random bonds?")
    print("1. Random")
    print("2. Chosen")
    while True:
        choice = input()
        try:
            choice = int(choice)
        except:
            print("Please input 1 or 2.")
            continue
        
        if choice == 1:
            print("\nYou have chosen to have random bonds.")
            setBondsRandom(profDict['bonds'])
            break
        if choice == 2:
            print("\nYou have chosen to have chosen bonds.")
            setBondsChosen(profDict['bonds'])
            break

def getRandomBond():
    return random.choice(listOfBonds)

def setRandomMotivations():
    keyIterator = 16
    i = 5
    while i > 0:
        key = ("E" + str(keyIterator))
        sheet[key] = random.choice(listOfMotivations)
        keyIterator += 1
        i -= 1

def setBondsChosen(bonds):
    keyIterator = 1
    score = sheet.get('C13')
    while bonds > 0:
        print("\nYou have " + str(bonds) + " bonds remaining.")
        print("\nPlease enter a bond name or bond type:")
        choice = input()
        bondKey = ("Bond " + str(keyIterator))
        scoreKey = ("Score " + str(keyIterator))
        setSheetValue(bondsDict, bondKey, choice)
        setSheetValue(bondsScoreDict, scoreKey, score)
        keyIterator += 1
        bonds -= 1
            
def setBondsRandom(bonds):
    keyIterator = 1
    score = sheet.get('C13')
    while bonds > 0:
        bondKey = ("Bond " + str(keyIterator))
        scoreKey = ("Score " + str(keyIterator))
        setSheetValue(bondsDict, bondKey, getRandomBond())
        setSheetValue(bondsScoreDict, scoreKey, score)
        keyIterator += 1
        bonds -= 1

def handleBonds(userChoice):
    if userChoice == "Anthropologist" or userChoice == "Historian":
        getBondsChoice(userChoice, anthroHisto)
        
    if userChoice == "Computer Scientist" or userChoice == "Engineer":
        getBondsChoice(userChoice, compSciHack)
        
    if userChoice == "Federal Agent":
        getBondsChoice(userChoice, fedAgent)

    if userChoice == "Physician":
        getBondsChoice(userChoice, physician)

    if userChoice == "Scientist":
        getBondsChoice(userChoice, scientist)

    if userChoice == "Special Operator":
        getBondsChoice(userChoice, specOp)

    if userChoice == "Criminal":
        getBondsChoice(userChoice, criminal)

    if userChoice == "Firefighter":
        getBondsChoice(userChoice, firefighter)

    if userChoice == "Foreign Service Officer":
        getBondsChoice(userChoice, fso)

    if userChoice == "Intelligence Analyst":
        getBondsChoice(userChoice, intelAnal)

    if userChoice == "Lawyer" or userChoice == "Business Executive":
        getBondsChoice(userChoice, lawExec)

    if userChoice == "Intelligence Case Officer":
        getBondsChoice(userChoice, ico)

    if userChoice == "Media Specialist":
        getBondsChoice(userChoice, medSpec)

    if userChoice == "Nurse" or userChoice == "Paramedic":
        getBondsChoice(userChoice, nursePara)

    if userChoice == "Pilot" or userChoice == "Sailor":
        getBondsChoice(userChoice, piloSail)

    if userChoice == "Police Officer":
        getBondsChoice(userChoice, police)

    if userChoice == "Program Manager":
        getBondsChoice(userChoice, progMana)
        
    if userChoice == "Soldier" or userChoice == "Marine":
        getBondsChoice(userChoice, soldier)

def setEmployer():
    print("\nPlease select an employer from this list:")
    iterator = 1
    for item in listOfEmployers:
        print(str(iterator) + ". " + item)
        iterator += 1
    while True:
        choice = input()
        try:
            choice = int(choice)
        except:
            print("Enter a number!")
            continue
        choice = choice - 1
        if choice < len(listOfEmployers):
            sheet['C5'] = listOfEmployers[choice]
            break
        else:
            print("Your choice was not on the list!")
            continue

def handleLoadout():
    print("\nDo you want a default loadout? It includes:")
    iterator = 1
    for item in inventory:
        print(str(iterator) + ". " + item)
        iterator += 1
    print("\nPlease input Y/N:")
    choice = input()
    keyIterator = 28
    indexIterator = 0

    if choice.lower() == "y":
        while indexIterator < 11:
            key = "J" + str(keyIterator)
            item = inventory[indexIterator]
            keyIterator += 1
            indexIterator += 1
            sheet[key] = item
        keyIterator = 28
        while indexIterator < len(inventory):
            key = "M" + str(keyIterator)
            item = inventory[indexIterator]
            keyIterator += 1
            indexIterator += 1
            sheet[key] = item
            
        sheet['J3'] = "Medium Pistol"
        sheet['J4'] = "Light Pistol"
        sheet['J5'] = "Knife"

    if choice.lower() == "n":
        print("Congratulations, you have finished character creation!")


def setDOB():
    choice = input("\nHow old are you? Birthday will be randomly generated.\n")
    sheet['G5'] = choice
    birthday = str(random.randrange(1, 13)) + "/" + str(random.randrange(1, 31)) + "/" + str(2021 - int(choice))
    sheet['H5'] = birthday
    return birthday

def setBio(background, profession, veteranStatus):
    STR = int(sheet.get('C8'))
    CON = int(sheet.get('C9'))
    DEX = int(sheet.get('C10'))
    INT = int(sheet.get('C11'))
    POW = int(sheet.get('C12'))
    CHA = int(sheet.get('C13'))
    
    bio = "At a glance, people notice your "
    
    if STR < 4:
        bio = bio + "feeble and "
    if STR  < 8:
        bio = bio + "weak body."
    if STR >= 9 and STR <= 12:
        bio = bio + "completely forgettable, unremarkably-average build."
    if STR  > 12:
        bio = bio + "muscles are rippling"
    if STR > 17:
        bio = bio + " and huge."

    bio = bio + " Your physical health "

    if CON < 4:
        bio = bio + "leaves you bedridden and "
    if CON  < 8:
        bio = bio + "feels sickly."
    if CON >= 9 and CON <= 12:
        bio = bio + "meets the standards of an average adult. Heartbeat, breathing, most limbs, and all that."
    if CON  > 12:
        bio = bio + "is in perfect shape"
    if CON > 17:
        bio = bio + " and indefatigable."

    bio = bio + " Your coordination is "

    if DEX < 4:
        bio = bio + "barely mobile and "
    if DEX < 8:
        bio = bio + "clumsy."
    if DEX >= 9 and DEX <= 12:
        bio = bio + "on par with most folks your age. You probably shouldn't bend over too fast though."
    if DEX  > 12:
        bio = bio + "nimble"
    if DEX > 17:
        bio = bio + " and acrobatic."

    bio = bio + " Your mind's thoughts are "

    if INT < 4:
        bio = bio + "imbecilic and "
    if INT < 8:
        bio = bio + "slow."
    if INT >= 9 and INT <= 12:
        bio = bio + "the result of public schooling. Y'know, average. Take +10% on Firearms if it's American schooling."
    if INT > 12:
        bio = bio + "perceptive"
    if INT > 17:
        bio = bio + " and brilliant."

    bio = bio + " Your composure manifests as "

    if POW < 4:
        bio = bio + "spineless and "
    if POW < 8:
        bio = bio + "nervous."
    if POW >= 9 and POW <= 12:
        bio = bio + "tempered and quite normal. You're not a leader of men but you're not a bitch."
    if POW > 12:
        bio = bio + "strong-willed"
    if POW > 17:
        bio = bio + " and indomitable."

    bio = bio + " Your personality comes off as "

    if CHA < 4:
        bio = bio + "unbearable and "
    if CHA < 8:
        bio = bio + "awkward."
    if CHA >= 9 and CHA <= 12:
        bio = bio + "normal. You don't stand out but you're not boring."
    if CHA > 12:
        bio = bio + "charming"
    if CHA > 17:
        bio = bio + " and magnetic."

    bio = bio + " You spent some years working as a " + background + "."
    bio = bio + " After a while, you transitioned into becoming a " + profession + "."
    
    if veteranStatus == "None":
        bio = bio + " Some time recently, you were contacted to join Delta Green. You're not a damaged veteran but don't be fueled, time in the field is measured in trauma, not hours."
    if veteranStatus == "Extreme Violence":
        bio = bio + " You've experienced a lot of violence in the field. It doesn't phase you much. You're a bit abrasive now. Violence is always on the table when you're not bound by pesky morals."
    if veteranStatus == "Captivity or Imprisonment":
        bio = bio + " You've spent some time in a cell, alone with your thoughts. It's not so bad being confined. The narcissist in your head insists that you're the most interesting person to be around."
    if veteranStatus == "Hard Experience":
        bio = bio + " You've had a rough experience that changed you for the better. A small part of your soul was the price you paid. Not like you had anything better to spend it on."
    if veteranStatus == "Things Man Was Not Meant To Know":
        bio = bio + " You've experienced things that most normal people never do. You've seen the edges of reality. It could've been Eldritch, but it was probably LSD."

    print("\nYour bio is:\n" + bio)
    return bio
        
def handleFinalizing(background, profession, veteranStatus):
    sheet['C4'] = profession
    choice = input("\nWhat's your character's real name?\n")
    sheet['E1'] = choice
    choice = input("\nWhat is your character's alias or code name?\n")
    sheet['D3'] = choice
    choice = input("\nWhere did your character attend school?\n")
    sheet['B3'] = choice
    print("\nYou will be given a series of random motivations for inspiration.")
    setRandomMotivations()
    setEmployer()
    DOB = setDOB()
    print("\nYour date of birth is: " + DOB + " you may need to modify this a bit.\n")
    sheet['J40'] = setBio(background, profession, veteranStatus)

listOfVeterans = ['Extreme Violence', 'Captivity or Imprisonment',
                  'Hard Experience', 'Things Man Was Not Meant To Know']

def getVeteranType():
    print("What kind of trauma did you experience?:")
    iterator = 1
    for item in listOfVeterans:
        print(str(iterator) + ". " + item)
        iterator += 1
    while True:
        choice = input()
        try:
            choice = int(choice)
        except:
            print("Enter a number!")
            continue
        choice = choice - 1
        if choice < len(listOfVeterans):
            traumaChoice = listOfVeterans[choice]
            return traumaChoice
            break
        else:
            print("Your choice was not on the list!")
            continue
        

def handleVeteranType(choice):
    if choice == "Extreme Violence":
        print('''\nFor experiencing extreme violence:
Add +10% to your Agent’s Occult skill. Reduce SAN
by 5. Subtract 3 from your Agent’s CHA and each
Bond. Your Agent is Adapted to Violence.''')
        if affirm():
            occult = int(sheet['E35'].replace('%', ''))
            sheet['E35'] = str(occult + 10) + "%"
            sheet['D18'] = int(sheet.get('C18')) - 5
            sheet['C13'] = int(sheet.get('C13')) - 3
            return choice
        else:
            handleVeteranType(getVeteranType())

    if choice == "Captivity or Imprisonment":
        print('''\nAdd +10% to your Agent’s Occult skill. Reduce SAN
by 5. Subtract 3 from your Agent’s POW. Your Agent
is Adapted to Helplessness.''')
        if affirm():
            occult = int(sheet['E35'].replace('%', ''))
            sheet['E35'] = str(occult + 10) + "%"
            sheet['C12'] = int(sheet.get('C12')) - 3
            return choice
        else:
            handleVeteranType(getVeteranType())

    if choice == "Hard Experience":
        print('''\nAdd +10% to your Agent’s Occult and +10% to any
four skills other than Unnatural. This can bring skills
higher than 80%. Reduce your Agent’s SAN by 5.
Remove one Bond.''')
        if affirm():
            occult = int(sheet['E35'].replace('%', ''))
            sheet['E35'] = str(occult + 10) + "%"
            sheet['D18'] = int(sheet.get('C18')) - 5
            printSkills(defaultSkills.keys())
            setSkillValue(skillDict, choice, 10)
            return choice
        else:
            handleVeteranType(getVeteranType())

    if choice == "Things Man Was Not Meant To Know":
        print('''\nYour Agent gains 10% in the Unnatural skill and adds
+20% to Occult. Reduce your Agent’s SAN by his or
her POW. Your Agent gains a new disorder caused by
the Unnatural (see page 72). Reset your Agent’s Breaking
Point to his or her new SAN minus POW..''')
        if affirm():
            sheet['G33'] = "10%"
            occult = int(sheet['E35'].replace('%', ''))
            sheet['E35'] = str(occult + 20) + "%"
            sheet['D18'] = int(sheet.get('C18')) - int(sheet.get('C12'))
            sheet['D19'] = int(sheet.get('D18')) - int(sheet.get('C12'))
            setRandomDisorder()
            return choice
        else:
            handleVeteranType(getVeteranType())


def setRandomDisorder():
    sheet['E21'] = random.choice(listOfDisorders)

def getVeteranStatus():
    print("\nIs your character a damaged veteran? Y/N")
    while True:
        choice = input()
        if choice.lower() == "y":
            userChoice = getVeteranType()
            handleVeteranType(userChoice)
            return userChoice
            break
        if choice.lower() == "n":
            userChoice = "None"
            break
        else:
            print("Please select Y or N")
            continue


if __name__ == "__main__":
    print("\nStep 1: Determine Statistics")
    handleStatistics()
            
    print("\nStep 2: Calculate Derived Attributes")
    handleDerivedStats()

    print("\nStep 3: Select Profession & Skills")
    professionSelection = getProfessionSelection(listOfProfessions)
    profSkillsDict = confirmSelection(professionSelection)
    masterSkills = mergeDictsReplace(profSkillsDict, defaultSkills)
    setSkills(skillDict, masterSkills)
    backgroundSelection = setBonusSkills(skillPackages)
    bonusSkillsDict = spendBonusPoints(getPackageSkills(skillPackages, backgroundSelection))
    setSkills(skillDict, bonusSkillsDict)

    print("\nStep 4: Define Bonds")
    handleBonds(professionSelection)
                   
    print("\nStep 5: Finalizing Your Character")
    veteranStatus = getVeteranStatus()
    handleFinalizing(backgroundSelection, professionSelection, veteranStatus)
    handleLoadout()
