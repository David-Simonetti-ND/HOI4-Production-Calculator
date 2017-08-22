infantry_battalions = raw_input("Number of infantry battalions : ")
infantry_level = raw_input("Infantry Equipment Level (Basic, 1, 2, 3): ")
artillery_battalions = raw_input("Number of artillery batallions: ")
artillery_level = raw_input("Artillery Level (1, 2, 3): ")
light_tank_battalions = raw_input("Number of light tank batallions: ")
light_tank_level = raw_input("Light tank Level (1, 2, 3): ")
motorized_battalions = raw_input("Number of motorized divisions: ")
field_hospital = raw_input("Field Hospital(Y or N): ")
recon = raw_input("Recon Company (Y or N): ")
engineers = raw_input("Engineer Company (Y or N): ")
logistics = raw_input("Logistics Company (Y or N): ")
maintenence = raw_input("Maintenence Company (Y or N): ")
millitary_police = raw_input("Millitary Police (Y or N): ")
signal = raw_input("Signal Company (Y or N): ")
support_artillery = raw_input("Support Artillery (Y or N): ")

field_hospital_motorized = 0
field_hospital_support = 0
recon_infantry = 0
recon_support = 0
engineers_infantry = 0
engineers_support = 0
logistics_motorized = 0
logistics_support = 0
maintenence_support = 0
millitary_police_infantry = 0
millitary_police_support = 0
signal_support = 0
signal_motorized = 0
support_artillery_number = 0

if field_hospital == "Y":
    field_hospital_motorized = 20
    field_hospital_support = 30
if recon == "Y":
    recon_infantry = 40
    recon_support = 10
if engineers == "Y":
    engineers_support = 30
    engineers_infantry = 10
if logistics == "Y":
    logistics_motorized = 10
    logistics_support = 20
if maintenence == "Y":
    maintenence_support = 25
if millitary_police == "Y":
    millitary_police_support = 10
    millitary_police_infantry = 40
if signal == "Y":
    signal_support = 50
    signal_motorized = 10
support_support = field_hospital_support + recon_support + engineers_support + logistics_support + maintenence_support + millitary_police_support + signal_support
support_infantry = recon_infantry + engineers_infantry + millitary_police_infantry
support_motorized = field_hospital_motorized + logistics_motorized + signal_motorized


if (infantry_level) == "Basic":
    infantry_cost = 0.4
elif infantry_level == "1":
    infantry_cost = 0.5
elif infantry_level == "2":
    infantry_cost = 0.6
elif infantry_level == "3":
    infantry_cost = 0.7
else:
    infantry_cost = 0

infantry_production = int(infantry_battalions) * infantry_cost * 100 + 100 * int(motorized_battalions) * infantry_cost + support_infantry * infantry_cost

if artillery_level == "1":
    artillery_cost = 3.5
elif artillery_level == "2":
    artillery_cost = 4
elif artillery_level == "3":
    artillery_cost = 4.5
else:
    artillery_cost = 0

if support_artillery == "Y":
    support_artillery_number = 24

artillery_production = int(artillery_battalions) * artillery_cost * 36 + support_artillery_number * artillery_cost

if light_tank_level == "1":
    light_tank_cost = 8
elif light_tank_level == "2":
    light_tank_cost = 9
elif light_tank_level == "3":
    light_tank_cost = 10
else:
    light_tank_cost = 0


light_tank_production = int(light_tank_battalions) * light_tank_cost * 60

motorized_production = int(motorized_battalions) * 2.5 * 50 + support_motorized * 2.5

support_production = support_support * 4

total_production = infantry_production + artillery_production + light_tank_production + motorized_production + support_production
print "Infantry equipment percent:" + str(infantry_production / total_production * 100)
print "Artillery percent:" + str(artillery_production / total_production * 100)
print "Light tank percent:" + str(light_tank_production / total_production * 100)
print "Motorized percent:" + str(motorized_production / total_production * 100)
print "Support equipment percent: " + str(support_production / total_production * 100)

factory_number = raw_input("Number of factories: ")
print "Factories producing infantry equipment " + str(int(int(factory_number) * infantry_production / total_production))
print "Factories producing artillery " + str(int(int(factory_number) * artillery_production / total_production))
print "Factories producing light tanks " + str(int(int(factory_number) * light_tank_production / total_production))
print "Factories producing motorized " + str(int(int(factory_number) * motorized_production / total_production))
print "Factories producing support equipment " + str(int(int(factory_number) * support_production / total_production))

raw_input("Prompt : ")
