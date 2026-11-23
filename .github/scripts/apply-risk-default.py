from pathlib import Path

specs = Path("app/src/main/java/com/example/model/TradingCalculation.kt")
text = specs.read_text()
old = "const val RISK_PERCENT = 10.0 // 10%"
if old not in text:
    raise SystemExit("Expected risk default not found; refusing a blind edit.")
specs.write_text(text.replace(old, "const val RISK_PERCENT = 1.0 // 1% default; editable by user"))

vm = Path("app/src/main/java/com/example/viewmodel/GoldCalculatorViewModel.kt")
text = vm.read_text()
text = text.replace('riskPercentInput: String = "10"', 'riskPercentInput: String = "1"')
text = text.replace("calculatePosition(10000.0, 60.0, 10.0, 3.0)", "calculatePosition(10000.0, 60.0, 1.0, 3.0)")
vm.write_text(text)

tests = Path("app/src/test/java/com/example/TradingCalculationTest.kt")
text = tests.read_text()
text = text.replace("calculatePosition(balance, slPips)", "calculatePosition(balance, slPips, 10.0, 3.0)")
text = text.replace("calculatePosition(5000.0, 80.0)", "calculatePosition(5000.0, 80.0, 10.0, 3.0)")
text = text.replace("calculatePosition(50.0, 60.0)", "calculatePosition(50.0, 60.0, 10.0, 3.0)")
text = text.replace("calculatePosition(2000000.0, 30.0)", "calculatePosition(2000000.0, 30.0, 10.0, 3.0)")
tests.write_text(text)

Path("app/src/test/java/com/example/DefaultRiskTest.kt").write_text('''package com.example

import com.example.model.calculatePosition
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class DefaultRiskTest {
    @Test
    fun defaultRiskIsOnePercentAndKeepsRiskBelowBudget() {
        val result = calculatePosition(10000.0, 60.0)
        assertTrue(result.isValid)
        assertEquals(1.0, result.riskPercent, 0.001)
        assertEquals(100.0, result.riskAmountUsc, 0.001)
        assertEquals(0.16, result.recommendedLotSize, 0.001)
        assertEquals(96.0, result.potentialLossUsc, 0.001)
    }
}
''')

readme = Path("README.md")
text = readme.read_text()
text = text.replace("- Risk: fixed 10% of balance.", "- Risk: default 1% of balance; editable in the calculator.")
readme.write_text(text)
