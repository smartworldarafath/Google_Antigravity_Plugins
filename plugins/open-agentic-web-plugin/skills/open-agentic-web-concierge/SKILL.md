---
name: open-agentic-web-concierge
description: Orchestrate autonomous, federated cross-site travel, hotel booking, and mobility scheduling using the TripSteward multi-agent network. Use when coordinating room reservations, airport transfers, arrival delay buffer synchronization, or city experience passes.
---

# Open Agentic Web Federated Travel Concierge Skill

This skill teaches Antigravity (`agy`) agents how to orchestrate multi-site bookings and travel coordination across independent Open Agentic Web nodes with zero intermediary fees.

## Multi-Agent Network Topology

```
                  ┌────────────────────────────────────────┐
                  │         Chief Travel Concierge         │
                  │ (tripsteward_concierge.network.json)   │
                  └───────────────────┬────────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              ▼                       ▼                       ▼
    ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
    │ HarborView Hotel │    │ CityGlide Fleet  │    │ MetroPass Passes │
    │    (Port 8080)   │    │   (Port 8081)    │    │   (Port 8082)    │
    └──────────────────┘    └──────────────────┘    └──────────────────┘
```

## Step-by-Step Coordination Protocol

### Step 1: Ingest Traveler Preferences
- Call `get_trip_preferences` on TripSteward Hub to load travel dates, party size, budget limit, and flight number from browser memory.

### Step 2: Hotel Availability & Room Hold
- Search available room tiers and rates at HarborView Hotel.
- Call `reserve_hotel_room` with `room_tier` and `nights`. Enforce user confirmation for the hold.

### Step 3: Flight Delay Buffer & Chauffeur Scheduling
- For airport arrivals, call `quote_transfer_service` on CityGlide.
- CityGlide dynamically inspects flight status (e.g. flight arrival at 4:30 PM) and injects a 30-minute baggage delay buffer, automatically scheduling pickup at 5:00 PM.
- Call `schedule_airport_transfer` and obtain the signed ECDSA transfer receipt.

### Step 4: Curated City Activity Passes
- Search available activities in MetroPass via `search_experiences`.
- Call `book_experience_pass` to issue immediate, scannable QR ticket vouchers with direct supplier pricing (eliminating 15–30% aggregator commissions).

### Step 5: Seal Master Itinerary
- Call `compile_master_itinerary` to synthesize hotel, transfer, and experience bookings into a sealed, verifiable itinerary with total savings calculation.
