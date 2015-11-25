#!/usr/bin/env python
DUT="./ueb02"
suite = [
	Test(
		name = "Ausgabe Usage",
		description = "Usage korrekt ausgegeben",
		command = "$DUT -h",
		stdout = StringifiedFile("test/usage.txt"),
		returnCode = 0
	),
	Test(
		name = "01 - Addition und transposition",
		description = "",
		command = "$DUT -f test/matrix1.mat -a test/matrix2.mat -t",
		stdout = StringifiedFile("test/ergebnis01.txt"),
		returnCode = 0
	),
	Test(
		name = "02 - Matrix lesen",
		description = "",
		command = "$DUT -f test/matrix1.mat",
		stdout = StringifiedFile("test/matrix1_exspected.mat"),
		returnCode = 0
	),
	Test(
		name = "03 - Matrix lesen",
		description = "",
		command = "$DUT -f test/matrix2.mat",
		stdout = StringifiedFile("test/matrix2.mat"),
		returnCode = 0
	),
	Test(
		name = "04 - INVALID Matrix lesen",
		description = "ein Nenner zu wenig hinten dran",
		command = "$DUT -f test/matrix3.mat",
		stdout = StringifiedFile("test/usage.txt"),
		returnCode = 9
	),
	Test(
		name = "05 - INVALID Matrix lesen",
		description = "ein Element zu wenig hinten dran",
		command = "$DUT -f test/matrix4.mat",
		stdout = StringifiedFile("test/usage.txt"),
		returnCode = 9
	),
	Test(
		name = "06 - Matrix lesen",
		description = "Leerzeichen zwischen Elementen",
		command = "$DUT -f test/matrix5.mat",
		stdout = StringifiedFile("test/matrix5.mat"),
		returnCode = 0
	),	
	Test(
		name = "07 - Matrix lesen",
		description = "Leerzeichen zwischen Zeile und Spalte",
		command = "$DUT -f test/matrix6.mat",
		stdout = StringifiedFile("test/matrix6.mat"),
		returnCode = 0
	),	
	Test(
		name = "08 - INVALID Matrix lesen",
		description = "Keine Zeile",
		command = "$DUT -f test/matrix7.mat",
		stdout = StringifiedFile("test/usage.txt"),
		returnCode = 4
	),	
	Test(
		name = "09 - INVALID Matrix lesen",
		description = "Keine Spalte",
		command = "$DUT -f test/matrix8.mat",
		stdout = StringifiedFile("test/usage.txt"),
		returnCode = 5
	),
	Test(
		name = "10 - INVALID Matrix lesen",
		description = "zu gross",
		command = "$DUT -f test/matrix9.mat",
		stdout = StringifiedFile("test/usage.txt"),
		returnCode = 5
	),								
	Test(
		name = "Matrix Addition",
		description = "Addition (2x3)",
		command = "$DUT -f test/MATRIX_ADD1_1.mat -a test/MATRIX_ADD1_2.mat",
		stdout = StringifiedFile("test/MATRIX_ADD1_3.mat"),
		returnCode = 0
	),		
		Test(
		name = "Matrix SkalarMultiplikation",
		description = "SkalarMult (2x3) * 3",
		command = "$DUT -f test/MATRIX_SCA1_1.mat -s test/MATRIX_SCA1_2.mat",
		stdout = StringifiedFile("test/MATRIX_SCA1_3.mat"),
		returnCode = 0
	),		
	Test(
		name = "Matrix Multiplikation",
		description = "Multiplikation (2x3) * (3x2) = (2x2)",
		command = "$DUT -f test/MATRIX_MUL1_1.mat -m test/MATRIX_MUL1_2.mat",
		stdout = StringifiedFile("test/MATRIX_MUL1_3.mat"),
		returnCode = 0
	),	
	Test(
		name = "Matrix Determinante",
		description = "(2x2) = 21",
		command = "$DUT -f test/MATRIX_DET1_1.mat -d",
		stdout = StringifiedFile("test/MATRIX_DET1_2.mat"),
		returnCode = 0
	),	
	Test(
		name = "Matrix Determinante",
		description = "(3x3) = 3",
		command = "$DUT -f test/MATRIX_DET2_1.mat -d",
		stdout = StringifiedFile("test/MATRIX_DET2_2.mat"),
		returnCode = 0
	),	
	Test(
		name = "Matrix Inverse",
		description = "Inverse (2x2)",
		command = "$DUT -f test/MATRIX_INV1_1.mat -i",
		stdout = StringifiedFile("test/MATRIX_INV1_2.mat"),
		returnCode = 0
	),	
	Test(
		name = "Matrix Transponieren",
		description = "Transponieren (2x3) -> (3x2)",
		command = "$DUT -f test/MATRIX_TRA1_1.mat -t",
		stdout = StringifiedFile("test/MATRIX_TRA1_2.mat"),
		returnCode = 0
	),	
	Test(
		name = "Kuerzen",
		description = "Kuerzen 8/4 -> 2/1",
		command = "$DUT -f test/MATRIX_KUR1_1.mat",
		stdout = StringifiedFile("test/MATRIX_KUR1_2.mat"),
		returnCode = 0
	),	
	Test(
		name = "Kuerzen",
		description = "Kuerzen 4/8 -> 1/2",
		command = "$DUT -f test/MATRIX_KUR2_1.mat",
		stdout = StringifiedFile("test/MATRIX_KUR2_2.mat"),
		returnCode = 0
	),
	Test(
		name = "Negative nur im Zaehler",
		description = "2/-1 -> -2/1",
		command = "$DUT -f test/MATRIX_NEG1_1.mat",
		stdout = StringifiedFile("test/MATRIX_NEG1_2.mat"),
		returnCode = 0
	),
]
