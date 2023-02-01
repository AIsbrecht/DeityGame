from ai import HostileEnemy
import consumable
from fighter import Fighter
from inventory import Inventory
from equipment import Equipment
from level import Level
from entity import Actor, Item
import equippable
#From walkthrough
player = Actor(char="@", color=(255, 255, 255), name="Player", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=30, base_defense=1, base_power=2), inventory=Inventory(capacity=26), level=Level(level_up_base=200),)

orc = Actor(char="o", color=(63, 127, 63), name="Orc", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=10, base_defense=0, base_power=3), inventory=Inventory(capacity=0), level=Level(xp_given=10),)#weak mob
troll = Actor(char="T", color=(0, 127, 0), name="Troll", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=16, base_defense=1, base_power=4), inventory=Inventory(capacity=0), level=Level(xp_given=35),)#semi weak mob
#weak 10PP
gorgon = Actor(char="G", color=(0,0,255), name="Gorgon", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=7, base_defense=1, base_power=2), inventory=Inventory(capacity=0), level=Level(xp_given=10),)#weak mob?
sirens = Actor(char="S", color=(0,0,255), name="Sirens", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=9, base_defense=0, base_power=1), inventory=Inventory(capacity=0), level=Level(xp_given=5),)#weak mob?
harpie = Actor(char="P", color=(0,0,255), name="Harpie", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=5, base_defense=3, base_power=2), inventory=Inventory(capacity=0), level=Level(xp_given=10),)#weak mob?
mare = Actor(char="M", color=(0,0,255), name="Mare", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=6, base_defense=1, base_power=3), inventory=Inventory(capacity=0), level=Level(xp_given=10),)#weak mob?
stymphalian = Actor(char="t", color=(0,0,255), name="Stymphalian", equipment=Equipment(), ai_cls=HostileEnemy, fighter=Fighter(hp=5, base_defense=2, base_power=3), inventory=Inventory(capacity=0), level=Level(xp_given=10),)#weak?
python = Actor(char="p", color=(0,0,255), name="Python", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=2, base_defense=4, base_power=4), inventory=Inventory(capacity=0), level=Level(xp_given=10),)#weak?
basilisk = Actor(char="B", color=(0,0,255), name="Basilisk", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=5, base_defense=4, base_power=1), inventory=Inventory(capacity=0), level=Level(xp_given=5),)# weak?
#semi weak 18PP
cyclops = Actor(char="C", color=(50, 100, 50), name="Cyclops", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=12, base_defense=3, base_power=3), inventory=Inventory(capacity=0), level=Level(xp_given=20),)#semi weak mob
medusa = Actor(char="D", color=(124,252, 0), name="Medusa", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=8, base_defense=3, base_power=7), inventory=Inventory(capacity=0), level=Level(xp_given=25),)#semi weak mob?
dracaenae = Actor(char="E", color=(255, 255,255), name="Dracaenae", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=10, base_defense=3, base_power=5), inventory=Inventory(capacity=0), level=Level(xp_given=20),)#semi weak mob?
giant = Actor(char=":", color=(0,0,255), name="Giant", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=9, base_defense=5, base_power=4), inventory=Inventory(capacity=0), level=Level(xp_given=20),)#semi weak?
aeternae = Actor(char="A", color=(0,0,255), name="Aeternae", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=6, base_defense=7, base_power=5), inventory=Inventory(capacity=0), level=Level(xp_given=20),)#semi weak?
#semiboss 30PP
chimera = Actor(char="H", color=(237, 145, 33), name="Chimera", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=20, base_defense=5, base_power=5), inventory=Inventory(capacity=0), level=Level(xp_given=75),) #semiboss?
minotaur = Actor(char="M", color=(175,175,255), name="Minotaur", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=18, base_defense=5, base_power=7), inventory=Inventory(capacity=0), level=Level(xp_given=100),)#semiboss?
lamia = Actor(char="L", color=(0,0,255), name="Lamia", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=25, base_defense=0, base_power=5), inventory=Inventory(capacity=0), level=Level(xp_given=100),)#semiboss?
#boss 50PP
empusa = Actor(char="E", color=(0,0,0), name="Empusa", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=30, base_defense=10, base_power=10), inventory=Inventory(capacity=0), level=Level(xp_given=150),)#boss?
hydra = Actor(char="Y", color=(0,0,255), name="Hydra", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=20, base_defense=20, base_power=10), inventory=Inventory(capacity=0), level=Level(xp_given=200),)#boss?
cerberus = Actor(char="B", color=(0,0,255), name="Cerberus", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=20, base_defense=5, base_power=25), inventory=Inventory(capacity=0), level=Level(xp_given=200),)#boss?
scylla = Actor(char="*", color=(0,0,255), name="Scylla", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=17, base_defense=3, base_power=5), inventory=Inventory(capacity=0), level=Level(xp_given=100),)#boss? Together with bottom
charybdis = Actor(char="^", color=(0,0,255), name="Charybdis", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=10, base_defense=10, base_power=5), inventory=Inventory(capacity=0), level=Level(xp_given=100),)#boss?
#final floor 100PP
typhon = Actor(char="!", color=(255,255,255), name="Typhon", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=60, base_defense=10, base_power=30), inventory=Inventory(capacity=0), level=Level(xp_given=1000),)#final boss?
echidna = Actor(char="%", color=(255,255,255), name="Echidna", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=80, base_defense=15, base_power=5), inventory=Inventory(capacity=0), level=Level(xp_given=500),)#semi final boss?
#NPC
sphinx = Actor(char="@", color=(0,0,0), name="Sphinx", ai_cls=HostileEnemy, equipment=Equipment(), fighter=Fighter(hp=99999999, base_defense=1000, base_power=0), inventory=Inventory(capacity=0), level=Level(xp_given=0),)#NPC?

#healing potions
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)

stronger_health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Stronger Health Potion",
    consumable=consumable.HealingConsumable(amount=10),
)

extreme_health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Extreme Health Potion",
    consumable=consumable.HealingConsumable(amount=10),
)

full_health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Full Health Potion",
    consumable=consumable.HealingConsumable(amount= 30),
)

#scrolls

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

#weapons
dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

#armor

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)