# Semmy Gold Calculator

Native Android app (Kotlin + Jetpack Compose). Offline calculator for Exness Standard Cent XAUUSDc.

## Trading assumptions
- Balance input: USC; 100 USC = 1 USD.
- Risk: fixed 10% of balance.
- Risk/reward: 1:3.
- Custom calculator unit: 1 entered unit = $0.10 gold-price movement. 30 custom units = $3.00. Exness published XAUUSD pip size is $0.01, so convert the chart/broker stop distance before entering it.
- One cent lot is modeled as 1 troy ounce, subject to verifying the contract specifications shown in the user's own Exness account.

## Build APK with GitHub Actions
The workflow `.github/workflows/build-apk.yml` runs unit tests and builds a debug APK on every push to `main`, and can be started manually from Actions. Download the `semmy-gold-calculator-debug-apk` artifact from a successful workflow run; extract it to obtain `app-debug.apk`.

This is a debug APK for personal testing, not a Play Store release. Validate calculations and contract settings with a demo account before live trading.
