def mechanicalInfoFun(material):
	global odb
	try:
		test = odb.materials[material].elastic.dependencies
		print "Elastic:"
		print "    Dependencies: " + str(odb.materials[material].elastic.dependencies)
		print "    Moduli: " + str(odb.materials[material].elastic.moduli)
		print "    No Compression: " + str(odb.materials[material].elastic.noCompression)
		print "    No Tension: " + str(odb.materials[material].elastic.noTension)
		print "    Temperature Dependency: " + str(odb.materials[material].elastic.temperatureDependency)
		print "    Type: " + str(odb.materials[material].elastic.type)
		print "    Table: " + str(odb.materials[material].elastic.table)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].plastic.dataType
		print "Plastic:"
		print "    Data Type: " + str(odb.materials[material].plastic.dataType)
		print "    Dependencies: " + str(odb.materials[material].plastic.dependencies)
		print "    Hardening: " + str(odb.materials[material].plastic.hardening)
		print "    Num Backstresses: " + str(odb.materials[material].plastic.numBackstresses)
		print "    Rate: " + str(odb.materials[material].plastic.rate)
		print "    Strain Range Dependency: " + str(odb.materials[material].plastic.strainRangeDependency)
		print "    Table: " + str(odb.materials[material].plastic.table)
		print "    Temperature Dependency: " + str(odb.materials[material].plastic.temperatureDependency)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].porousMetalPlasticity.dependencies
		print"Porous Metal Plasticity:"
		print "    Dependencies: " + str(odb.materials[material].porousMetalPlasticity.dependencies)
		print "    Relative Density: " + str(odb.materials[material].porousMetalPlasticity.relativeDensity)
		print "    Table: " + str(odb.materials[material].porousMetalPlasticity.table)
		print "    Temperature Dependency: " + str(odb.materials[material].porousMetalPlasticity.temperatureDependency)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].ductileDamageInitiation.alpha
		print"Ductile Damage Initiation:"
		print "    Alpha: " + str(odb.materials[material].ductileDamageInitiation.alpha)
		try:
			test = odb.materials[material].ductileDamageInitiation.damageEvolution.degradation
			print "    Damage Evolution:"
			print "        Degradation: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.degradation)
			print "        Dependencies: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.dependencies)
			print "        Mixed Mode Behavior: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.mixedModeBehavior)
			print "        Mode Mix Ratio: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.modeMixRatio)
			print "        Power: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.power)
			print "        Softening: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.softening)
			print "        Table: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.table)
			print "        Temperature Dependency: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.temperatureDependency)
			print "        Type: " + str(odb.materials[material].ductileDamageInitiation.damageEvolution.type)
		except AttributeError:
			strangeVariable = 0
		print "    Definition: " + str(odb.materials[material].ductileDamageInitiation.definition)
		print "    Dependencies: " + str(odb.materials[material].ductileDamageInitiation.dependencies)
		print "    Direction: " + str(odb.materials[material].ductileDamageInitiation.direction)
		print "    Feq: " + str(odb.materials[material].ductileDamageInitiation.feq)
		print "    Fnn: " + str(odb.materials[material].ductileDamageInitiation.fnn)
		print "    Fnt: " + str(odb.materials[material].ductileDamageInitiation.fnt)
		print "    Frequency: " + str(odb.materials[material].ductileDamageInitiation.frequency)
		print "    Ks: " + str(odb.materials[material].ductileDamageInitiation.ks)
		print "    Number Imperfections: " + str(odb.materials[material].ductileDamageInitiation.numberImperfections)
		print "    Omega: " + str(odb.materials[material].ductileDamageInitiation.omega)
		print "    Table: " + str(odb.materials[material].ductileDamageInitiation.table)
		print "    Temperature Dependency: " + str(odb.materials[material].ductileDamageInitiation.temperatureDependency)
		print "    Tolerance: " + str(odb.materials[material].ductileDamageInitiation.tolerance)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].maxsDamageInitiation.alpha
		print"Maxs Damage Initiation:"
		print "    Alpha: " + str(odb.materials[material].maxsDamageInitiation.alpha)
		try:
			test = odb.materials[material].maxsDamageInitiation.damageEvolution.degradation
			print "    Damage Evolution:"
			print "        Degradation: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.degradation)
			print "        Dependencies: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.dependencies)
			print "        Mixed Mode Behavior: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.mixedModeBehavior)
			print "        Mode Mix Ratio: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.modeMixRatio)
			print "        Power: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.power)
			print "        Softening: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.softening)
			print "        Table: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.table)
			print "        Temperature Dependency: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.temperatureDependency)
			print "        Type: " + str(odb.materials[material].maxsDamageInitiation.damageEvolution.type)
		except AttributeError:
			strangeVariable = 0
		print "    Definition: " + str(odb.materials[material].maxsDamageInitiation.definition)
		print "    Dependencies: " + str(odb.materials[material].maxsDamageInitiation.dependencies)
		print "    Direction: " + str(odb.materials[material].maxsDamageInitiation.direction)
		print "    Feq: " + str(odb.materials[material].maxsDamageInitiation.feq)
		print "    Fnn: " + str(odb.materials[material].maxsDamageInitiation.fnn)
		print "    Fnt: " + str(odb.materials[material].maxsDamageInitiation.fnt)
		print "    Frequency: " + str(odb.materials[material].maxsDamageInitiation.frequency)
		print "    Ks: " + str(odb.materials[material].maxsDamageInitiation.ks)
		print "    Number Imperfections: " + str(odb.materials[material].maxsDamageInitiation.numberImperfections)
		print "    Omega: " + str(odb.materials[material].maxsDamageInitiation.omega)
		print "    Table: " + str(odb.materials[material].maxsDamageInitiation.table)
		print "    Temperature Dependency: " + str(odb.materials[material].maxsDamageInitiation.temperatureDependency)
		print "    Tolerance: " + str(odb.materials[material].maxsDamageInitiation.tolerance)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].maxpsDamageInitiation.alpha
		print"Maxps Damage Initiation:"
		print "    Alpha: " + str(odb.materials[material].maxpsDamageInitiation.alpha)
		try:
			test = odb.materials[material].maxpsDamageInitiation.damageEvolution.degradation
			print "    Damage Evolution:"
			print "        Degradation: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.degradation)
			print "        Dependencies: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.dependencies)
			print "        Mixed Mode Behavior: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.mixedModeBehavior)
			print "        Mode Mix Ratio: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.modeMixRatio)
			print "        Power: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.power)
			print "        Softening: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.softening)
			print "        Table: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.table)
			print "        Temperature Dependency: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.temperatureDependency)
			print "        Type: " + str(odb.materials[material].maxpsDamageInitiation.damageEvolution.type)
		except AttributeError:
			strangeVariable = 0
		print "    Definition: " + str(odb.materials[material].maxpsDamageInitiation.definition)
		print "    Dependencies: " + str(odb.materials[material].maxpsDamageInitiation.dependencies)
		print "    Direction: " + str(odb.materials[material].maxpsDamageInitiation.direction)
		print "    Feq: " + str(odb.materials[material].maxpsDamageInitiation.feq)
		print "    Fnn: " + str(odb.materials[material].maxpsDamageInitiation.fnn)
		print "    Fnt: " + str(odb.materials[material].maxpsDamageInitiation.fnt)
		print "    Frequency: " + str(odb.materials[material].maxpsDamageInitiation.frequency)
		print "    Ks: " + str(odb.materials[material].maxpsDamageInitiation.ks)
		print "    Number Imperfections: " + str(odb.materials[material].maxpsDamageInitiation.numberImperfections)
		print "    Omega: " + str(odb.materials[material].maxpsDamageInitiation.omega)
		print "    Table: " + str(odb.materials[material].maxpsDamageInitiation.table)
		print "    Temperature Dependency: " + str(odb.materials[material].maxpsDamageInitiation.temperatureDependency)
		print "    Tolerance: " + str(odb.materials[material].maxpsDamageInitiation.tolerance)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].johnsonCookDamageInitiation.alpha
		print"Johnson Cook DamageInitiation:"
		print "    Alpha: " + str(odb.materials[material].johnsonCookDamageInitiation.alpha)
		try:
			test = odb.materials[material].johnsonCookDamageInitiation.damageEvolution.degradation
			print "    Damage Evolution:"
			print "        Degradation: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.degradation)
			print "        Dependencies: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.dependencies)
			print "        Mixed Mode Behavior: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.mixedModeBehavior)
			print "        Mode Mix Ratio: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.modeMixRatio)
			print "        Power: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.power)
			print "        Softening: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.softening)
			print "        Table: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.table)
			print "        Temperature Dependency: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.temperatureDependency)
			print "        Type: " + str(odb.materials[material].johnsonCookDamageInitiation.damageEvolution.type)
		except AttributeError:
			strangeVariable = 0
		print "    Definition: " + str(odb.materials[material].johnsonCookDamageInitiation.definition)
		print "    Dependencies: " + str(odb.materials[material].johnsonCookDamageInitiation.dependencies)
		print "    Direction: " + str(odb.materials[material].johnsonCookDamageInitiation.direction)
		print "    Feq: " + str(odb.materials[material].johnsonCookDamageInitiation.feq)
		print "    Fnn: " + str(odb.materials[material].johnsonCookDamageInitiation.fnn)
		print "    Fnt: " + str(odb.materials[material].johnsonCookDamageInitiation.fnt)
		print "    Frequency: " + str(odb.materials[material].johnsonCookDamageInitiation.frequency)
		print "    Ks: " + str(odb.materials[material].johnsonCookDamageInitiation.ks)
		print "    Number Imperfections: " + str(odb.materials[material].johnsonCookDamageInitiation.numberImperfections)
		print "    Omega: " + str(odb.materials[material].johnsonCookDamageInitiation.omega)
		print "    Table: " + str(odb.materials[material].johnsonCookDamageInitiation.table)
		print "    Temperature Dependency: " + str(odb.materials[material].johnsonCookDamageInitiation.temperatureDependency)
		print "    Tolerance: " + str(odb.materials[material].johnsonCookDamageInitiation.tolerance)
	except AttributeError:
		strangeVariable = 0

	try:
		test = odb.materials[material].eos.dependencies
		print"Eos:"
		print "    Dependencies: " + str(odb.materials[material].eos.dependencies)
		print "    Detonation Energy: " + str(odb.materials[material].eos.detonationEnergy)
		try:
			test = odb.materials[material].eos.detonationPoint.table
			print "    Detonation Point: "
			print "    	Table: " + str(odb.materials[material].eos.detonationPoint.table)
		except AttributeError:
			strangeVariable = 0
		print "    Gas Specific Table: " + str(odb.materials[material].eos.gasSpecificTable)
		print "    Gas Table: " + str(odb.materials[material].eos.gasTable)
		print "    Reaction Table: " + str(odb.materials[material].eos.reactionTable)
		print "    Solid Table: " + str(odb.materials[material].eos.solidTable)
		print "    Table: " + str(odb.materials[material].eos.table)
		print "    Temperature Dependency: " + str(odb.materials[material].eos.temperatureDependency)
		print "    Type: " + str(odb.materials[material].eos.type)
	except AttributeError:
		strangeVariable = 0

