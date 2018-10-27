list = odb.materials.keys()

for tmp in list:
	try:
		test = odb.materials[tmp].name
		print "Name: " + odb.materials[tmp].name
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].description
		print "Description: " + odb.materials[tmp].description
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].materialIdentifier
		print "Material Identifier: " + odb.materials[tmp].materialIdentifier
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].density.dependencies
		print "Density:"
		print "    Dependencies: " + str(odb.materials[tmp].density.dependencies)
		print "    Distribution Type: " + str(odb.materials[tmp].density.distributionType)
		print "    Field Name: " + odb.materials[tmp].density.fieldName
		print "    Temperature dependency: " + str(odb.materials[tmp].density.temperatureDependency)
		print "    Table: " + str(odb.materials[tmp].density.table)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].elastic.dependencies
		print "Elastic:"
		print "    Dependencies: " + str(odb.materials[tmp].elastic.dependencies)
		print "    Moduli: " + str(odb.materials[tmp].elastic.moduli)
		print "    No Compression: " + str(odb.materials[tmp].elastic.noCompression)
		print "    No Tension: " + str(odb.materials[tmp].elastic.noTension)
		print "    Temperature Dependency: " + str(odb.materials[tmp].elastic.temperatureDependency)
		print "    Type: " + str(odb.materials[tmp].elastic.type)
		print "    Table: " + str(odb.materials[tmp].elastic.table)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].plastic.dataType
		print "Plastic:"
		print "    Data Type: " + str(odb.materials[tmp].plastic.dataType)
		print "    Dependencies: " + str(odb.materials[tmp].plastic.dependencies)
		print "    Hardening: " + str(odb.materials[tmp].plastic.hardening)
		print "    Num Backstresses: " + str(odb.materials[tmp].plastic.numBackstresses)
		print "    Rate: " + str(odb.materials[tmp].plastic.rate)
		print "    Strain Range Dependency: " + str(odb.materials[tmp].plastic.strainRangeDependency)
		print "    Table: " + str(odb.materials[tmp].plastic.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].plastic.temperatureDependency)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].depvar.deleteVar
		print "Depvar:"
		print "    Delete Var: " + str(odb.materials[tmp].depvar.deleteVar)
		print "    N: " + str(odb.materials[tmp].depvar.n)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].userMaterial.mechanicalConstants
		print "User Material:"
		print "    Mechanical Constants: " + str(odb.materials[tmp].userMaterial.mechanicalConstants)
		print "    Thermal Constants: " + str(odb.materials[tmp].userMaterial.thermalConstants)
		print "    Type: " + str(odb.materials[tmp].userMaterial.type)
		print "    Unsymm: " + str(odb.materials[tmp].userMaterial.unsymm)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].conductivity.dependencies
		print "Conductivity:"
		print "    Dependencies: " + str(odb.materials[tmp].conductivity.dependencies)
		print "    Table: " + str(odb.materials[tmp].conductivity.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].conductivity.temperatureDependency)
		print "    Type: " + str(odb.materials[tmp].conductivity.type)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].inelasticHeatFraction.fraction
		print"Inelastic Heat Fraction:"
		print "    Fraction: " + str(odb.materials[tmp].inelasticHeatFraction.fraction)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].porousMetalPlasticity.dependencies
		print"Porous Metal Plasticity:"
		print "    Dependencies: " + str(odb.materials[tmp].porousMetalPlasticity.dependencies)
		print "    Relative Density: " + str(odb.materials[tmp].porousMetalPlasticity.relativeDensity)
		print "    Table: " + str(odb.materials[tmp].porousMetalPlasticity.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].porousMetalPlasticity.temperatureDependency)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].specificHeat.dependencies
		print"Specific Heat:"
		print "    Dependencies: " + str(odb.materials[tmp].specificHeat.dependencies)
		print "    Law: " + str(odb.materials[tmp].specificHeat.law)
		print "    Table: " + str(odb.materials[tmp].specificHeat.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].specificHeat.temperatureDependency)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].ductileDamageInitiation.alpha
		print"Ductile Damage Initiation:"
		print "    Alpha: " + str(odb.materials[tmp].ductileDamageInitiation.alpha)
		try:
			test = odb.materials[tmp].ductileDamageInitiation.damageEvolution.degradation
			print "    Damage Evolution:"
			print "        Degradation: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.degradation)
			print "        Dependencies: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.dependencies)
			print "        Mixed Mode Behavior: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.mixedModeBehavior)
			print "        Mode Mix Ratio: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.modeMixRatio)
			print "        Power: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.power)
			print "        Softening: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.softening)
			print "        Table: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.table)
			print "        Temperature Dependency: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.temperatureDependency)
			print "        Type: " + str(odb.materials[tmp].ductileDamageInitiation.damageEvolution.type)
		except AttributeError:
			strangeVariable = 0
		print "    Definition: " + str(odb.materials[tmp].ductileDamageInitiation.definition)
		print "    Dependencies: " + str(odb.materials[tmp].ductileDamageInitiation.dependencies)
		print "    Direction: " + str(odb.materials[tmp].ductileDamageInitiation.direction)
		print "    Feq: " + str(odb.materials[tmp].ductileDamageInitiation.feq)
		print "    Fnn: " + str(odb.materials[tmp].ductileDamageInitiation.fnn)
		print "    Fnt: " + str(odb.materials[tmp].ductileDamageInitiation.fnt)
		print "    Frequency: " + str(odb.materials[tmp].ductileDamageInitiation.frequency)
		print "    Ks: " + str(odb.materials[tmp].ductileDamageInitiation.ks)
		print "    Number Imperfections: " + str(odb.materials[tmp].ductileDamageInitiation.numberImperfections)
		print "    Omega: " + str(odb.materials[tmp].ductileDamageInitiation.omega)
		print "    Table: " + str(odb.materials[tmp].ductileDamageInitiation.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].ductileDamageInitiation.temperatureDependency)
		print "    Tolerance: " + str(odb.materials[tmp].ductileDamageInitiation.tolerance)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].maxsDamageInitiation.alpha
		print"Maxs Damage Initiation:"
		print "    Alpha: " + str(odb.materials[tmp].maxsDamageInitiation.alpha)
		try:
			test = odb.materials[tmp].maxsDamageInitiation.damageEvolution.degradation
			print "    Damage Evolution:"
			print "        Degradation: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.degradation)
			print "        Dependencies: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.dependencies)
			print "        Mixed Mode Behavior: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.mixedModeBehavior)
			print "        Mode Mix Ratio: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.modeMixRatio)
			print "        Power: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.power)
			print "        Softening: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.softening)
			print "        Table: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.table)
			print "        Temperature Dependency: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.temperatureDependency)
			print "        Type: " + str(odb.materials[tmp].maxsDamageInitiation.damageEvolution.type)
		except AttributeError:
			strangeVariable = 0
		print "    Definition: " + str(odb.materials[tmp].maxsDamageInitiation.definition)
		print "    Dependencies: " + str(odb.materials[tmp].maxsDamageInitiation.dependencies)
		print "    Direction: " + str(odb.materials[tmp].maxsDamageInitiation.direction)
		print "    Feq: " + str(odb.materials[tmp].maxsDamageInitiation.feq)
		print "    Fnn: " + str(odb.materials[tmp].maxsDamageInitiation.fnn)
		print "    Fnt: " + str(odb.materials[tmp].maxsDamageInitiation.fnt)
		print "    Frequency: " + str(odb.materials[tmp].maxsDamageInitiation.frequency)
		print "    Ks: " + str(odb.materials[tmp].maxsDamageInitiation.ks)
		print "    Number Imperfections: " + str(odb.materials[tmp].maxsDamageInitiation.numberImperfections)
		print "    Omega: " + str(odb.materials[tmp].maxsDamageInitiation.omega)
		print "    Table: " + str(odb.materials[tmp].maxsDamageInitiation.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].maxsDamageInitiation.temperatureDependency)
		print "    Tolerance: " + str(odb.materials[tmp].maxsDamageInitiation.tolerance)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].maxpsDamageInitiation.alpha
		print"Maxps Damage Initiation:"
		print "    Alpha: " + str(odb.materials[tmp].maxpsDamageInitiation.alpha)
		try:
			test = odb.materials[tmp].maxpsDamageInitiation.damageEvolution.degradation
			print "    Damage Evolution:"
			print "        Degradation: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.degradation)
			print "        Dependencies: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.dependencies)
			print "        Mixed Mode Behavior: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.mixedModeBehavior)
			print "        Mode Mix Ratio: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.modeMixRatio)
			print "        Power: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.power)
			print "        Softening: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.softening)
			print "        Table: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.table)
			print "        Temperature Dependency: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.temperatureDependency)
			print "        Type: " + str(odb.materials[tmp].maxpsDamageInitiation.damageEvolution.type)
		except AttributeError:
			strangeVariable = 0
		print "    Definition: " + str(odb.materials[tmp].maxpsDamageInitiation.definition)
		print "    Dependencies: " + str(odb.materials[tmp].maxpsDamageInitiation.dependencies)
		print "    Direction: " + str(odb.materials[tmp].maxpsDamageInitiation.direction)
		print "    Feq: " + str(odb.materials[tmp].maxpsDamageInitiation.feq)
		print "    Fnn: " + str(odb.materials[tmp].maxpsDamageInitiation.fnn)
		print "    Fnt: " + str(odb.materials[tmp].maxpsDamageInitiation.fnt)
		print "    Frequency: " + str(odb.materials[tmp].maxpsDamageInitiation.frequency)
		print "    Ks: " + str(odb.materials[tmp].maxpsDamageInitiation.ks)
		print "    Number Imperfections: " + str(odb.materials[tmp].maxpsDamageInitiation.numberImperfections)
		print "    Omega: " + str(odb.materials[tmp].maxpsDamageInitiation.omega)
		print "    Table: " + str(odb.materials[tmp].maxpsDamageInitiation.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].maxpsDamageInitiation.temperatureDependency)
		print "    Tolerance: " + str(odb.materials[tmp].maxpsDamageInitiation.tolerance)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].johnsonCookDamageInitiation.alpha
		print"Johnson Cook DamageInitiation:"
		print "    Alpha: " + str(odb.materials[tmp].johnsonCookDamageInitiation.alpha)
		try:
			test = odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.degradation
			print "    Damage Evolution:"
			print "        Degradation: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.degradation)
			print "        Dependencies: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.dependencies)
			print "        Mixed Mode Behavior: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.mixedModeBehavior)
			print "        Mode Mix Ratio: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.modeMixRatio)
			print "        Power: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.power)
			print "        Softening: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.softening)
			print "        Table: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.table)
			print "        Temperature Dependency: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.temperatureDependency)
			print "        Type: " + str(odb.materials[tmp].johnsonCookDamageInitiation.damageEvolution.type)
		except AttributeError:
			strangeVariable = 0
		print "    Definition: " + str(odb.materials[tmp].johnsonCookDamageInitiation.definition)
		print "    Dependencies: " + str(odb.materials[tmp].johnsonCookDamageInitiation.dependencies)
		print "    Direction: " + str(odb.materials[tmp].johnsonCookDamageInitiation.direction)
		print "    Feq: " + str(odb.materials[tmp].johnsonCookDamageInitiation.feq)
		print "    Fnn: " + str(odb.materials[tmp].johnsonCookDamageInitiation.fnn)
		print "    Fnt: " + str(odb.materials[tmp].johnsonCookDamageInitiation.fnt)
		print "    Frequency: " + str(odb.materials[tmp].johnsonCookDamageInitiation.frequency)
		print "    Ks: " + str(odb.materials[tmp].johnsonCookDamageInitiation.ks)
		print "    Number Imperfections: " + str(odb.materials[tmp].johnsonCookDamageInitiation.numberImperfections)
		print "    Omega: " + str(odb.materials[tmp].johnsonCookDamageInitiation.omega)
		print "    Table: " + str(odb.materials[tmp].johnsonCookDamageInitiation.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].johnsonCookDamageInitiation.temperatureDependency)
		print "    Tolerance: " + str(odb.materials[tmp].johnsonCookDamageInitiation.tolerance)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[tmp].eos.dependencies
		print"Eos:"
		print "    Dependencies: " + str(odb.materials[tmp].eos.dependencies)
		print "    Detonation Energy: " + str(odb.materials[tmp].eos.detonationEnergy)
		try:
			test = odb.materials[tmp].eos.detonationPoint.table
			print "    Detonation Point: "
			print "    	Table: " + str(odb.materials[tmp].eos.detonationPoint.table)
		except AttributeError:
			strangeVariable = 0
		print "    Gas Specific Table: " + str(odb.materials[tmp].eos.gasSpecificTable)
		print "    Gas Table: " + str(odb.materials[tmp].eos.gasTable)
		print "    Reaction Table: " + str(odb.materials[tmp].eos.reactionTable)
		print "    Solid Table: " + str(odb.materials[tmp].eos.solidTable)
		print "    Table: " + str(odb.materials[tmp].eos.table)
		print "    Temperature Dependency: " + str(odb.materials[tmp].eos.temperatureDependency)
		print "    Type: " + str(odb.materials[tmp].eos.type)
	except AttributeError:
		strangeVariable = 0



	print " "
	print " "
	print " "
	


















