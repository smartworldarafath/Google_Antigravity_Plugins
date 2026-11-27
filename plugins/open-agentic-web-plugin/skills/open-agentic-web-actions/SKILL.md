---
name: open-agentic-web-actions
description: Design, implement, and secure grounded website actions and cross-origin action bridges for autonomous agents using the open-agentic-web package. Covers defineAction, JSON Schema validation, irreversible action confirmation modals, WebCrypto ECDSA receipt signing, and MCP/OpenAI/A2A export adapters.
---

# Open Agentic Web Site Actions & Security Skill

This skill guides agents in creating safe, schema-validated website actions that personal AI agents can invoke without leaking private user data to third-party intermediaries.

## Defining a Grounded Site Action

Use `defineAction` from `open-agentic-web/actions`:

```javascript
import { defineAction } from "open-agentic-web/actions";

export const reserveRoomAction = defineAction({
  name: "website_reserve_room",
  description: "Reserve a boutique hotel room at HarborView Hotel.",
  effect: "irreversible", // "read" | "irreversible" | "undoable"
  availability: "bridge", // "bridge" | "local-only"
  callerOrigins: ["*"],   // Allowed orchestrator origins
  inputSchema: {
    type: "object",
    properties: {
      room_tier: { type: "string", enum: ["standard", "deluxe_bayview", "penthouse"] },
      nights: { type: "integer", minimum: 1, maximum: 14 },
      party_size: { type: "integer", minimum: 1, maximum: 6 }
    },
    required: ["room_tier", "nights"]
  },
  execute: async (args, context) => {
    // Grounded DOM or in-memory execution
    return { confirmation: "HV-8842", total: 378 };
  },
  undo: async (result, context) => {
    // Optional rollback handler for undoable actions
  }
});
```

## Security & Safety Guardrails

### 1. Human-in-the-Loop Confirmation
- Any action with `effect: "irreversible"` (financial transactions, bookings, cancellations) **must** invoke the user confirmation dialog before execution.
- Use `createConsentDialog` or supply an `onConfirm` callback to `setupActionBridge`.

### 2. Zero-Leakage Privacy Invariant
- Traveler preferences and payment credentials must reside strictly in client browser memory (RAM / local DOM).
- Static web servers receive **0 bytes** of customer profile data.

### 3. Cryptographic Action Receipts (ECDSA P-256)
- High-value operations must sign receipts using standard WebCrypto ECDSA P-256 keys:
```javascript
import { signActionReceipt, verifyActionReceipt, generateReceiptKeyPair } from "open-agentic-web/actions";

const { publicKeyJwk, privateKeyJwk } = await generateReceiptKeyPair();
const receipt = await signActionReceipt({ bookingId: "CG-9921", amount: 68 }, privateKeyJwk, { provider: "CityGlide Fleet" });
const verification = await verifyActionReceipt(receipt, publicKeyJwk);
// verification.valid === true
```

### 4. Universal Tool Adapters
Export registered actions to multiple agent protocols with zero boilerplate:
- **MCP (Model Context Protocol)**: `registry.toMCPTools()`
- **OpenAI Tool Calling**: `registry.toOpenAITools()`
- **Browser Native WebMCP**: `await registry.registerWebMCP()`
- **Agent-to-Agent (A2A)**: `toA2AAgentCard(manifest, registry)`
