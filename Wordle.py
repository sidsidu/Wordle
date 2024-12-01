import random
class TextColors:
    red = "\u001b[0;31m"
    green = "\u001b[0;32m"
    yellow = "\u001b[0;33m"
    end = "\u001b[0m"
wordlist = [
    "ABACK", "ABASE", "ABATE", "ABBey", "ABIDE", "ABOUT", "ABOVE", "ABYSS", "ACORN", "ACRID", "ACTOR", "ACUTE", 
    "ADAGE", "ADAPT", "ADMIT", "ADOBE", "ADOPT", "ADORE", "ADULT", "AFTER", "AGAIN", "AGAPE", "AGATE", "AGENT", 
    "AGILE", "AGING", "AGLOW", "AGONY", "AGREE", "AHEAD", "AISLE", "ALBUM", "ALIEN", "ALIKE", "ALIVE", "ALLOW", 
    "ALOFT", "ALONE", "ALOOF", "ALOUD", "ALPHA", "ALTAR", "ALTER", "AMASS", "AMBER", "AMISS", "AMPLE", "ANGEL", 
    "ANGER", "ANGRY", "ANGST", "ANODE", "ANTIC", "ANVIL", "AORTA", "APART", "APHID", "APPLE", "APPLY", "APRON", 
    "APTLY", "ARBOR", "ARDOR", "ARGUE", "AROMA", "ASCOT", "ASIDE", "ASKEW", "ASSET", "ATOLL", "ATONE", "AUDIO", 
    "AUDIT", "AVAIL", "AVERT", "AWAIT", "AWAKE", "AWASH", "AWFUL", "AXIOM", "AZURE", "BACON", "BADGE", "BADLY", 
    "BAGEL", "BAKER", "BALSA", "BANAL", "BARGE", "BASIC", "BASIN", "BATHE", "BATON", "BATTY", "BAWDY", "BAYOU", 
    "BEACH", "BEADY", "BEAST", "BEAUT", "BEEFY", "BEGET", "BEGIN", "BEING", "BELCH", "BELIE", "BELLY", "BELOW", 
    "BENCH", "BERET", "BERTH", "BESET", "BEVEL", "BINGE", "BIOME", "BIRCH", "BIRTH", "BLACK", "BLAME", "BLAND", 
    "BLARE", "BLAZE", "BLEAK", "BLEED", "BLEEP", "BLIMP", "BLOCK", "BLOKE", "BLOND", "BLOWN", "BLUFF", "BLURB", 
    "BLURT", "BLUSH", "BOOBY", "BOOST", "BOOZE", "BOOZY", "BORAX", "BOSSY", "BOUGH", "BRACE", "BRAID", "BRAIN", 
    "BRAKE", "BRASH", "BRASS", "BRAVE", "BRAVO", "BREAD", "BREAK", "BREED", "BRIAR", "BRIBE", "BRIDE", "BRIEF", 
    "BRINE", "BRING", "BRINK", "BRINY", "BRISK", "BROAD", "BROKE", "BROOK", "BROOM", "BROTH", "BRUSH", "BRUTE", 
    "BUDDY", "BUGGY", "BUGLE", "BUILD", "BUILT", "BULKY", "BULLY", "BUNCH", "BURLY", "CABLE", "CACAO", "CACHE", 
    "CADET", "CAMEL", "CAMEO", "CANDY", "CANNY", "CANOE", "CANON", "CAPER", "CARAT", "CARGO", "CAROL", "CARRY", 
    "CARVE", "CATCH", "CATER", "CAULK", "CAUSE", "CEDAR", "CHAFE", "CHAIN", "CHALK", "CHAMP", "CHANT", "CHAOS", 
    "CHARD", "CHARM", "CHART", "CHEAT", "CHEEK", "CHEER", "CHEST", "CHIEF", "CHILD", "CHILL", "CHIME", "CHOIR", 
    "CHOKE", "CHORD", "CHUNK", "CHUTE", "CIDER", "CIGAR", "CINCH", "CIRCA", "CIVIC", "CLASS", "CLEAN", "CLEAR", 
    "CLEFT", "CLERK", "CLICK", "CLIMB", "CLING", "CLOCK", "CLONE", "CLOSE", "CLOTH", "CLOUD", "CLOWN", "CLUCK", 
    "COACH", "COAST", "COCOA", "COLON", "COMET", "COMMA", "CONDO", "CONIC", "CORER", "CORNY", "COULD", "COUNT", 
    "COURT", "COVER", "COVET", "COWER", "COYLY", "CRAFT", "CRAMP", "CRANE", "CRANK", "CRASS", "CRATE", "CRAVE", 
    "CRAZE", "CRAZY", "CREAK", "CREDO", "CREPT", "CRIME", "CRIMP", "CROAK", "CRONE", "CROSS", "CROWD", "CROWN", 
    "CRUMB", "CRUSH", "CRUST", "CUMIN", "CURLY", "CYNIC", "DADDY", "DAISY", "DANCE", "DANDY", "DEATH", "DEBIT", 
    "DEBUG", "DEBUT", "DECAL", "DECAY", "DECOY", "DELAY", "DELTA", "DELVE", "DENIM", "DEPOT", "DEPTH", "DETER", 
    "DEVIL", "DIARY", "DICEY", "DIGIT", "DINER", "DINGO", "DISCO", "DITTO", "DODGE", "DOING", "DOLLY", "DONOR", 
    "DONUT", "DOUBT", "DOWRY", "DOZEN", "DRAIN", "DRAWN", "DREAM", "DRINK", "DRIVE", "DROLL", "DROOP", "DROVE", 
    "DUCHY", "DUTCH", "DUVET", "DWARF", "DWELL", "DWELT", "EARLY", "EARTH", "EASEL", "EBONY", "EDICT", "EGRET", 
    "EJECT", "ELDER", "ELOPE", "ELUDE", "EMAIL", "EMBER", "EMPTY", "ENACT", "ENEMA", "ENJOY", "ENNUI", "ENSUE", 
    "ENTER", "EPOCH", "EPOXY", "EQUAL", "EQUIP", "ERODE", "ERROR", "ERUPT", "ESSAY", "ETHER", "ETHIC", "ETHOS", 
    "EVADE", "EVENT", "EVERY", "EVOKE", "EXACT", "EXALT", "EXCEL", "EXERT", "EXIST", "EXPEL", "EXTRA", "EXULT", 
    "FACET", "FAINT", "FAITH", "FARCE", "FAULT", "FAVOR", "FEAST", "FEIGN", "FERAL", "FERRY", "FEWER", "FIBER", 
    "FIELD", "FIEND", "FIFTY", "FILET", "FINAL", "FINCH", "FINER", "FIRST", "FISHY", "FIXER", "FJORD", "FLAIL", 
    "FLAIR", "FLAKE", "FLAME", "FLANK", "FLARE", "FLASK", "FLESH", "FLICK", "FLING", "FLIRT", "FLOAT", "FLOCK", 
    "FLOOD", "FLOOR", "FLORA", "FLOSS", "FLOUR", "FLOUT", "FLOWN", "FLUFF", "FLUME", "FLUNK", "FLYER", "FOCAL", 
    "FOCUS", "FOGGY", "FOLLY", "FORAY", "FORCE", "FORGE", "FORGO", "FORTE", "FORTH", "FORTY", "FOUND", "FOYER", 
    "FRAIL", "FRAME", "FRANK", "FRESH", "FRIED", "FROCK", "FROND", "FRONT", "FROST", "FROTH", "FROWN", "FROZE", 
    "FULLY", "FUNGI", "FUNNY", "GAMER", "GAMMA", "GAMUT", "GAUDY", "GAUNT", "GAUZE", "GAWKY", "GECKO", "GENRE", 
    "GHOUL", "GIANT", "GIDDY", "GIRTH", "GIVEN", "GLASS", "GLAZE", "GLEAM", "GLEAN", "GLIDE", "GLOAT", "GLOBE",
    "GLOOM", "GLORY", "GLOVE", "GLYPH", "GNASH", "GOING", "GOLEM", "GONER", "GOOFY", "GOOSE", "GORGE", "GOUGE", 
    "GRACE", "GRADE", "GRAIL", "GRAND", "GRANT", "GRAPH", "GRASP", "GRATE", "GREAT", "GREEN", "GREET", "GRIEF", 
    "GRIME", "GRIMY", "GRIND", "GRIPE", "GROIN", "GROOM", "GROUP", "GROUT", "GROVE", "GROWL", "GRUEL", "GUANO", 
    "GUARD", "GUEST", "GUIDE", "GUILD", "GULLY", "GUMMY", "GUPPY", "GUSTY", "HAIRY", "HALVE", "HANDY", "HAPPY", 
    "HARSH", "HATCH", "HATER", "HAVOC", "HEADY", "HEARD", "HEART", "HEATH", "HEAVE", "HEAVY", "HEIST", "HELIX", 
    "HELLO", "HENCE", "HERON", "HINGE", "HITCH", "HOARD", "HOBBY", "HOMER", "HONEY", "HORDE", "HORSE", "HOTEL", 
    "HOUND", "HOUSE", "HOWDY", "HUMAN", "HUMID", "HUMOR", "HUMPH", "HUNCH", "HUNKY", "HURRY", "HUTCH", "HYPER", 
    "IGLOO", "IMAGE", "IMPEL", "INANE", "INDEX", "INEPT", "INERT", "INFER", "INLAY", "INNER", "INPUT", "INTER", 
    "INTRO", "IONIC", "IRATE", "IRONY", "ISLET", "ITCHY", "IVORY", "JAUNT", "JAZZY", "JELLY", "JERKY", "JIFFY", 
    "JOINT", "JOKER", "JOLLY", "JOUST", "JUDGE", "JUICE", "KARMA", "KAYAK", "KAZOO", "KEBAB", "KHAKI", "KIOSK", 
    "KNAVE", "KNEAD", "KNEEL", "KNELT", "KNOCK", "KNOLL", "KOALA", "LABEL", "LABOR", "LAGER", "LANKY", "LAPEL", 
    "LAPSE", "LARGE", "LARVA", "LASER", "LATTE", "LAYER", "LEAFY", "LEAKY", "LEAPT", "LEARN", "LEASH", "LEAVE", 
    "LEDGE", "LEECH", "LEERY", "LEGGY", "LEMON", "LIBEL", "LIGHT", "LILAC", "LIMIT", "LINEN", "LINER", "LINGO", 
    "LITHE", "LIVER", "LOCAL", "LOCUS", "LOFTY", "LOGIC", "LOOPY", "LOSER", "LOUSE", "LOVER", "LOWER", "LOWLY", 
    "LOYAL", "LUCID", "LUCKY", "LUNAR", "LUNCH", "LUNGE", "LUSTY", "LYING", "MACAW", "MADAM", "MAGIC", "MAGMA", 
    "MAIZE", "MAJOR", "MANIA", "MANGA", "MANLY", "MANOR", "MAPLE", "MARCH", "MARRY", "MARSH", "MASON", "MASSE", 
    "MATCH", "MATEY", "MAXIM", "MAYBE", "MAYOR", "MEALY", "MEANT", "MEDAL", "MEDIA", "MEDIC", "MELON", "MERCY", 
    "MERGE", "MERIT", "MERRY", "METAL", "METER", "METRO", "MICRO", "MIDGE", "MIDST", "MIMIC", "MINCE", "MINER", 
    "MINUS", "MODEL", "MODEM", "MOIST", "MOLAR", "MOMMY", "MONEY", "MONTH", "MOOSE", "MOSSY", "MOTOR", "MOTTO", 
    "MOULT", "MOUNT", "MOURN", "MOUSE", "MOVIE", "MUCKY", "MULCH", "MUMMY", "MURAL", "MUSHY", "MUSIC", "MUSTY", 
    "NAIVE", "NANNY", "NASTY", "NATAL", "NAVAL", "NEEDY", "NEIGH", "NERDY", "NEVER", "NICER", "NICHE", "NIGHT", 
    "NINJA", "NINTH", "NOBLE", "NOISE", "NORTH", "NYMPH", "OCCUR", "OCEAN", "OCTET", "OFFAL", "OFTEN", "OLDER", 
    "OLIVE", "ONION", "ONSET", "OPERA", "ORDER", "ORGAN", "OTHER", "OUGHT", "OUNCE", "OUTDO", "OUTER", "OVERT", 
    "OWNER", "OXIDE", "PAINT", "PANEL", "PANIC", "PAPAL", "PAPER", "PARER", "PARRY", "PARTY", "PASTA", "PATTY", 
    "PAUSE", "PEACE", "PEACH", "PEARL", "PENNE", "PERCH", "PERKY", "PESKY", "PHASE", "PHONE", "PHONY", "PHOTO", 
    "PIANO", "PICKY", "PIETY", "PILOT", "PINCH", "PINEY", "PINKY", "PINTO", "PIOUS", "PIPER", "PIQUE", "PITHY", 
    "PIXEL", "PIXIE", "PLACE", "PLAIT", "PLANK", "PLANT", "PLATE", "PLAZA", "PLEAT", "PLUCK", "PLUNK", "POINT", 
    "POISE", "POKER", "POLKA", "POLYP", "PORCH", "POUND", "POWER", "PRESS", "PRICE", "PRICK", "PRIDE", "PRIME", 
    "PRIMO", "PRIMP", "PRINT", "PRIOR", "PRIZE", "PROBE", "PRONE", "PRONG", "PROUD", "PROVE", "PROWL", "PROXY", 
    "PRUNE", "PSALM", "PULPY", "PURGE", "QUALM", "QUART", "QUEEN", "QUERY", "QUEST", "QUEUE", "QUICK", "QUIET", 
    "QUIRK", "QUITE", "QUOTE", "RADIO", "RAINY", "RAISE", "RAMEN", "RANCH", "RANGE", "RATIO", "RAYON", "REACT", 
    "READY", "REALM", "REBEL", "REBUS", "REBUT", "RECAP", "RECUR", "REFER", "REGAL", "RELIC", "RENEW", "REPAY", 
    "REPEL", "RERUN", "RESIN", "RETCH", "RETRO", "RETRY", "REVEL", "RHINO", "RHYME", "RIDER", "RIDGE", "RIGHT", 
    "RIPER", "RISEN", "RIVAL", "ROBIN", "ROBOT", "ROCKY", "RODEO", "ROGUE", "ROOMY", "ROUGE", "ROUND", "ROUSE", 
    "ROUTE", "ROVER", "ROYAL", "RUDDY", "RUDER", "RUPEE", "RUSTY", "SAINT", "SALAD", "SALLY", "SALSA", "SALTY", 
    "SANDY", "SASSY", "SAUCY", "SAUTE", "SAVOR", "SCALD", "SCALE", "SCANT", "SCARE", "SCARF", "SCENT", "SCOFF", 
    "SCOLD", "SCONE", "SCOPE", "SCORN", "SCOUR", "SCOUT", "SCRAM", "SCRAP", "SCRUB", "SEDAN", "SEEDY", "SENSE", 
    "SERUM", "SERVE", "SEVEN", "SEVER", "SHADE", "SHAFT", "SHAKE", "SHALL", "SHAME", "SHANK", "SHAPE", "SHARD", 
    "SHARP", "SHAVE", "SHAWL", "SHELL", "SHIFT", "SHINE", "SHIRE", "SHIRK", "SHORE", "SHORN", "SHOUT", "SHOWN", 
    "SHOWY", "SHRUB", "SHRUG", "SHYLY", "SIEGE", "SIGHT", "SINCE", "SISSY", "SIXTH", "SKATE", "SKIER", "SKIFF", 
    "SKILL", "SKIMP", "SKIRT", "SKUNK", "SLATE", "SLEEK", "SLEEP", "SLICE", "SLOPE", "SLOSH", "SLOTH", "SLUMP", 
    "SLUNG", "SMALL", "SMART", "SMASH", "SMEAR", "SMELT", "SMILE", "SMIRK", "SMITE", "SMITH", "SMOCK", "SMOKE", 
    "SNACK", "SNAFU", "SNAIL", "SNAKE", "SNAKY", "SNARE", "SNARL", "SNEAK", "SNOOP", "SNORT", "SNOUT", "SOGGY", 
    "SOLAR", "SOLID", "SOLVE", "SONIC", "SOUND", "SOWER", "SPACE", "SPADE", "SPEAK", "SPECK", "SPELL", "SPELT", 
    "SPEND", "SPENT", "SPICE", "SPICY", "SPIEL", "SPIKE", "SPILL", "SPINE", "SPIRE", "SPLAT", "SPOKE", "SPOON", 
    "SPOUT", "SPRAY", "SPURT", "SQUAD", "SQUAT", "STAFF", "STAGE", "STAID", "STAIN", "STAIR", "STAKE", "STALE", 
    "STALL", "STAND", "STARK", "START", "STASH", "STATE", "STEAD", "STEAM", "STEED", "STEEL", "STEIN", "STERN", 
    "STICK", "STIFF", "STILL", "STING", "STINK", "STINT", "STOCK", "STOIC", "STOLE", "STOMP", "STONE", "STONY", 
    "STOOL", "STORE", "STORM", "STORY", "STOUT", "STOVE", "STRAP", "STRAW", "STUDY", "STUNG", "STYLE", "SUGAR", 
    "SULKY", "SUPER", "SURER", "SURLY", "SUSHI", "SWEAT", "SWEEP", "SWEET", "SWELL", "SWILL", "SWINE", "SWIRL", 
    "SWISH", "SWOON", "SWUNG", "SYRUP", "TABLE", "TABOO", "TACIT", "TACKY", "TAKEN", "TALLY", "TALON", "TANGY", 
    "TAPER", "TAPIR", "TARDY", "TASTE", "TASTY", "TAUNT", "TAWNY", "TEACH", "TEARY", "TEASE", "TEMPO", "TENTH", 
    "TEPID", "TERSE", "THANK", "THEIR", "THEME", "THERE", "THESE", "THIEF", "THIGH", "THING", "THINK", "THIRD", 
    "THORN", "THOSE", "THREE", "THREW", "THROW", "THUMB", "THUMP", "THYME", "TIARA", "TIBIA", "TIDAL", "TIGER", 
    "TILDE", "TIPSY", "TITAN", "TITHE", "TITLE", "TODAY", "TONIC", "TOPAZ", "TOPIC", "TORCH", "TORSO", "TOTEM", 
    "TOUCH", "TOUGH", "TOWEL", "TOXIC", "TOXIN", "TRACE", "TRACT", "TRADE", "TRAIN", "TRAIT", "TRASH", "TRAWL", 
    "TREAT", "TREND", "TRIAD", "TRICE", "TRITE", "TROLL", "TROPE", "TROVE", "TRULY", "TRUSS", "TRUST", "TRUTH", 
    "TRYST", "TUTOR", "TUNIC", "TWANG", "TWEAK", "TWEED", "TWICE", "TWINE", "TWIRL", "ULCER", "ULTRA", "UNCLE", 
    "UNDER", "UNDUE", "UNFED", "UNFIT", "UNIFY", "UNITE", "UNLIT", "UNMET", "UNTIE", "UNTIL", "UNZIP", "UPSET", 
    "URBAN", "USAGE", "USHER", "USING", "USUAL", "USURP", "UTTER", "UVULA", "VAGUE", "VALET", "VALID", "VALUE", 
    "VAPID", "VAULT", "VENOM", "VERGE", "VERVE", "VIDEO", "VIGOR", "VINYL", "VIOLA", "VIRAL", "VISOR", "VITAL", 
    "VIVID", "VODKA", "VOICE", "VOILA", "VOTER", "VOUCH", "WACKY", "WAGON", "WALTZ", "WASTE", "WATCH", "WEARY", 
    "WEDGE", "WEIRD", "WHACK", "WHALE", "WHEEL", "WHELP", "WHERE", "WHICH", "WHIFF", "WHILE", "WHINE", "WHINY", 
    "WHIRL", "WHISK", "WHOOP", "WIDEN", "WINCE", "WINDY", "WOKEN", "WOMAN", "WOOER", "WORDY", "WORLD", "WORRY", 
    "WORSE", "WORST", "WOULD", "WOVEN", "WRATH", "WREAK", "WRIST", "WRITE", "WRONG", "WROTE", "WRUNG", "YACHT", 
    "YEARN", "YIELD", "YOUNG", "YOUTH", "ZEBRA", "ZESTY"
]
word = wordlist[random.randint(0,len(wordlist))-1]
word = word.upper()
#print(word) 
guesses =6
guessedWords = []
print(f"You have {guesses} guesses")
Won=False
aldready_guessed = 1
def inWord(guess,word):
    rword = []
    char = ''
    for i in range(5):
        if guess[i]==word[i]:
            color = TextColors.green 
        elif guess[i] in word:
            color = TextColors.yellow
        else:
            color = TextColors.red
        char =  color + guess[i] + TextColors.end
        rword.append(char)
    x= "  ".join(rword)
    print(x)
def blanks(guesses):
    for i in range(guesses):
        print("_  "*5,"\n")         
while guesses>0:
    guess = input("\nEnter a guess \n")
    guess = guess.upper()
    if len(guess) == 5:
        guessedWords.append(guess)
        for i in range(aldready_guessed):
            inWord(guessedWords[i],word)

        aldready_guessed+=1
        blanks(guesses-1)
        guesses-=1
        if guess == word:
                Won = True
                break
        print(f"\nYou have {guesses} guesses left")
    else:
        print("Enter a 5 letter word")
if Won:
    print("\nYOU WIN!! 🥳🥳🥳🥳")
else:
    print("\nYou lost the word was",word)
input("Press enter to exit")