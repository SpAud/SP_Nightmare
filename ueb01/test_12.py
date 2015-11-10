#!/usr/bin/env python
DUT="./ueb01"

suite = [	
	Test(
	name = "Ausgabe Usage",
	description = "Usage korrekt ausgegeben",
	command = "$DUT -h",
	stdout = StringifiedFile("test/Usage.txt"),
	returnCode = 0
	),
	
	Test(
	name = "INVALID - Wrong Usage call",
	description = "Falsche Eingabe",
	command = "$DUT -h2",
	stderr = StringifiedFile("test/ERR_SYNTAX.txt"),
	returnCode = lambda x: x!=0
	),
	
	Test(
	name = "Use map with (+2) on the list [1,2,3]",
	description = "Adds 2 to every element of the list",
	command = "$DUT 1 2 3 -M 2 -a",
	stdout = "3 4 5",
	returnCode = 0
	),
	
	Test(
	name = "Use map with (+2) on the list [-1,-2,-3]",
	description = "Adds 2 to every element of the list",
	command = "$DUT -1 -2 -3 -M 2 -a",
	stdout = "1 0 -1",
	returnCode = 0
	),	
	
	Test(
	name = "Use map with (-2) on the list [1,2,3]",
	description = "Subtract 2 from every element of the list",
	command = "$DUT 1 2 3 -M 2 -s",
	stdout = "-1 0 1",
	returnCode = 0
	),
	
	Test(
	name = "Use map with (*2) on the list [1,2,3]",
	description = "Multiply 2 to every element of the list",
	command = "$DUT 1 2 3 -M 2 -m",
	stdout = "2 4 6",
	returnCode = 0
	),
	
	Test(
	name = "Use map with (/2) on the list [1,2,3]",
	description = "Divide every element of the list with 2",
	command = "$DUT 1 2 3 -M 2 -d",
	stdout = "0 1 1",
	returnCode = 0
	),	
	
	Test(
	name = "Use Reduce on list [1,2,3] with Add",
	description = "Reduces list to Integer by Adding",
	command = "$DUT 1 2 3 -R -a",
	stdout = "6",
	returnCode = 0
	),
	
	Test(
	name = "Use Reduce on list [1,2,3] with Mult",
	description = "Reduces list to Integer by multiply",
	command = "$DUT 1 2 3 -R -m",
	stdout = "6",
	returnCode = 0
	),	

	Test(
	name = "INVALID - Use Reduce on list [1,2,3] with Subtraction",
	description = "Reduces list to Integer by subtract",
	command = "$DUT 1 2 3 -R -s",
	stderr = StringifiedFile("test/ERR_INVALID_OPERATION.txt"),
	returnCode = lambda x: x!=0
	),
	
	Test(
	name = "INVALID - Use Reduce on list [1,2,3] with Divide",
	description = "Reduces list to Integer by divide",
	command = "$DUT 1 2 3 -R -d",
	stderr = StringifiedFile("test/ERR_INVALID_OPERATION.txt"),
	returnCode = lambda x: x!=0
	),
	
	Test(
	name = "INVALID - Call of -xo",
	description = "Invalid Call",
	command = "$DUT 1 2 3 -xo 1 -R -a",
	stderr = StringifiedFile("test/ERR_SYNTAX.txt"),
	returnCode = lambda x: x!=0
	),	
	
		
	Test(
	name = "Call of mutiple filters",
	description = "-x 1 -o",
	command = "$DUT 1 2 3 4 5 6 -x 1 -o -R -a",
	stdout = "21",
	returnCode = 0
	),	
	
	Test(
	name = "Take mutiples of Integer into account",
	description = "Shows only Mutiples of 3",
	command ="$DUT 1 2 3 -x 3 -M 0 -a ",
	stdout = "3",
	returnCode = 0
	),
	
	Test(
	name = "Take even values into account",
	description = "Shows only 2",
	command ="$DUT 1 2 3 -e -M 0 -a ",
	stdout = "2",
	returnCode = 0
	),
	
	Test(
	name = "Take odd values into account",
	description = "Shows 1, 3",
	command ="$DUT 1 2 3 -o -M 0 -a ",
	stdout = "1 3",
	returnCode = 0
	),	
	
	Test(
	name = "REVERT - Take mutiples of Integer into account",
	description = "Shows only Mutiples of 3",
	command ="$DUT -x 3 1 2 3 -M 0 -a ",
	stdout = "3",
	returnCode = 0
	),
	
	Test(
	name = "REVERT - Take even values into account",
	description = "Shows only 2",
	command ="$DUT -e 1 2 3 -M 0 -a ",
	stdout = "2",
	returnCode = 0
	),
	
	Test(
	name = "REVERT - Take odd values into account",
	description = "Shows 1, 3",
	command ="$DUT -o 1 2 3 -M 0 -a ",
	stdout = "1 3",
	returnCode = 0
	),			
]
