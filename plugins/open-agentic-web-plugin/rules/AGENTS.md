# Open Agentic Web & TripSteward Agent Operating Rules

When this plugin is active, all Antigravity (`agy`) agents must adhere strictly to these architectural, security, and privacy rules:

## 1. Grounded Site Action Execution
- Personal agents act on behalf of the user by calling declared website tools (`website_*` or registered site actions) rather than hallucinating unstructured responses.
- All action arguments must strictly conform to their declared JSON Schema definitions (`type`, `properties`, `required`).

## 2. Zero-Leakage In-Browser Privacy
- Traveler preferences, itinerary constraints, and booking tokens reside **strictly in browser memory (RAM / client DOM)**.
- Static web hosting servers must receive **0 bytes** of customer profile data.

## 3. Human-in-the-Loop Confirmation for Irreversible Actions
- Any action tagged with `effect: "irreversible"` (e.g. room holds, transfer bookings, ticketing) **must** present a confirmation dialog to the user prior to execution.
- Never execute financial or binding reservations without explicit approval.

## 4. Cryptographic Action Receipts (ECDSA P-256)
- High-value operations must return signed action receipts using WebCrypto ECDSA P-256 keys.
- Always verify signature validity via `verifyActionReceipt` before committing an itinerary entry.

## 5. Declarative Multi-Agent Network Separation
- Keep declarative agent routing definitions strictly in `*.network.json`.
- Ground tools strictly in `site-actions.js` or via the `nsdeploy-actions-v1` bridge protocol.
- Remote node additions must trigger `onConsent` before fetching or executing external agent graphs.
