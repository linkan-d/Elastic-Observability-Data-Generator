# 🎬 Demo Preparation Guide

## Overview

This guide helps you prepare and deliver effective Elastic Observability demos using realistic scenarios.

---

## 📋 Before the Demo

### 1. Environment Setup (15 minutes before)

```bash
# Start the generator
python app_advanced.py

# Pre-generate data
# Go to http://localhost:8080
# Select industry + scenario
# Run for 10 minutes minimum
```

**Why pre-generate?**
- Elasticsearch needs 2-3 minutes to index data
- Service Map aggregations take time to build
- You want rich data to explore during the demo

### 2. Prepare Kibana

**Open these tabs in advance:**
1. Observability → APM → Service Map
2. Observability → APM → Services
3. Observability → APM → Traces
4. Observability → Logs → Stream
5. Observability → Uptime

**Set time range:** "Last 15 minutes" (or match your generation duration)

### 3. Know Your Story

When you select a scenario in the UI, you'll now see a **Demo Script panel** with:
- 📖 The scenario story
- 💬 Talking points
- 📊 Expected metrics
- 🔍 What to show in Kibana
- 🎬 Suggested demo flow

---

## 🎯 Demo Flow Template

### Act 1: Set the Scene (2 minutes)

**Goal:** Establish context

**Script:**
> "Today I'm going to show you how Elastic Observability helps you understand what's happening in your [INDUSTRY] platform. Let me set the scene..."

**Then read the scenario story** (shown in the demo script panel)

**Example for Black Friday:**
> "It's Black Friday and your e-commerce platform is experiencing unprecedented traffic. The search and recommendation services are showing increased latency. Let's see how Elastic Observability helps us understand and respond to this situation."

### Act 2: Show the Impact (3 minutes)

**Navigate to:** Observability → APM → Service Map

**Talking Points:**
- "Here's our Service Map - a real-time view of all our microservices"
- "Notice these services [point to affected ones] - they're showing degradation"
- "The red/yellow indicators show where we have problems"
- "You can see the dependencies between services"

**Click on an affected service:**
- "This service normally runs at 100ms, but now it's at [X]ms"
- "Error rate has spiked from 2% to [X]%"
- "This is directly impacting user experience"

### Act 3: Investigate (5 minutes)

**Navigate to:** APM → Traces

**Talking Points:**
- "Let's look at some actual requests to understand what's happening"
- "Here's a slow transaction - let's click into it"
- **Show waterfall:**
  - "This visualization shows the entire request flow"
  - "Each bar is a different service call"
  - "You can see exactly where time is being spent"
  - "Notice this [point to slow span] - this is our bottleneck"

**Navigate to:** Logs

- "Now let's correlate this with application logs"
- Filter by the affected service
- Filter by ERROR level
- "See these errors? They're happening at the same time as our performance degradation"
- "This is the smoking gun"

### Act 4: Show the Solution (2 minutes)

**Explain how you'd resolve it:**

**For Traffic Spike:**
> "With this insight, we can:
> 1. Scale up the affected services
> 2. Add caching to reduce database load
> 3. Set up alerts so we catch this earlier next time"

**For Database Issues:**
> "We can see:
> 1. Which queries are slow
> 2. Which services are holding connections
> 3. We need to increase the connection pool size"

### Act 5: Close with Value (1 minute)

**Key Messages:**
- "Without Elastic Observability, this would take hours to debug"
- "We found the root cause in minutes with distributed tracing"
- "The Service Map gives us instant situational awareness"
- "Logs and traces correlated together tell the complete story"

---

## 🎪 Scenario-Specific Demo Scripts

### 🛒 E-Commerce: Black Friday Traffic Spike

**Duration:** 15 minutes of generation
**Best for:** Retail, e-commerce, high-traffic platforms

**The Story:**
> "It's Black Friday - the biggest shopping day of the year. Traffic has increased 10x from our normal baseline. The search and recommendation engines are struggling under load. We need to identify bottlenecks before checkout starts failing completely."

**What to Show:**
1. **Service Map:** Point out search-service and recommendation-engine in red/yellow
2. **Services View:** Show latency increase from 100ms → 300ms
3. **Traces:** Click into a slow search request, show 5-second waterfall
4. **Logs:** Filter for "search-service" + ERROR, show timeout messages
5. **Dashboard:** Create a quick visualization of error rate over time

**Key Metrics:**
- Error Rate: 5% (up from 2%)
- Latency: 3x normal
- Throughput: 10x normal volume

**Talking Points:**
- "Notice the correlation between traffic volume and error rate"
- "The search service is the bottleneck - it's calling recommendation engine"
- "Distributed tracing shows the exact dependency chain"
- "We can see this is a capacity issue, not a bug"

**Resolution:**
- Horizontal scaling of search and recommendation services
- Add caching layer for popular searches
- Implement circuit breakers to prevent cascade failures

---

### 🏦 Banking: Database Connection Pool Exhaustion

**Duration:** 25 minutes of generation
**Best for:** Banking, finance, transaction-heavy systems

**The Story:**
> "Our banking platform's database connection pool is exhausted. All connections are in use, causing timeouts and transaction failures. This is a critical issue affecting customer transactions."

**What to Show:**
1. **Service Map:** Multiple services showing errors (account, transaction, payment)
2. **Service Detail:** Show error rate jumping to 20%
3. **Traces:** Show failed transactions with "connection timeout" errors
4. **Logs:** Filter for "connection" + "timeout", show cascade of failures
5. **Transaction Duration:** Show spike from 200ms → 800ms

**Key Metrics:**
- Error Rate: 20% (critical!)
- Latency: 4x normal
- Affected: Account, Transaction, Payment services

**Talking Points:**
- "This is a cascade failure - one issue affecting multiple services"
- "Database connection pool exhaustion is a classic scaling problem"
- "Notice how errors propagate through the dependency chain"
- "Distributed tracing shows which service is holding connections longest"

**Resolution:**
- Increase database connection pool size
- Implement connection pooling best practices
- Add connection timeout monitoring
- Set up alerts for connection pool utilization

---

### 🎮 Gaming: DDoS Attack Pattern

**Duration:** 35 minutes of generation
**Best for:** Gaming, high-availability systems, security

**The Story:**
> "We're under DDoS attack. Game servers are receiving malicious traffic, overwhelming authentication and session management. Players can't log in or stay connected."

**What to Show:**
1. **Service Map:** Game-server, authentication-service, session-management all red
2. **Error Rate:** Spiked to 30%
3. **Traces:** Show failed authentication attempts
4. **Traffic Pattern:** Show abnormal request volume
5. **Logs:** Show repeated authentication failures from same IPs

**Key Metrics:**
- Error Rate: 30% (severe)
- Latency: 8x normal
- Traffic: Abnormal spike pattern

**Talking Points:**
- "Notice the traffic pattern - this isn't normal user behavior"
- "Authentication failures are correlated with the traffic spike"
- "The Service Map shows the blast radius of the attack"
- "We can identify which services are under attack vs. experiencing secondary effects"

**Resolution:**
- Enable rate limiting
- Block malicious IPs
- Scale authentication service
- Implement CAPTCHA for suspicious traffic

---

### 🏥 Healthcare: EHR System Slowdown

**Duration:** 35 minutes of generation
**Best for:** Healthcare, mission-critical systems

**The Story:**
> "Physicians are reporting slow access to patient records. The EHR system response time has degraded to 4.5x normal. This impacts patient care quality and wait times."

**What to Show:**
1. **Service Map:** EHR-service, patient-monitoring, prescription-service affected
2. **Latency:** 100ms → 450ms average
3. **Traces:** Show slow EHR queries taking 2-3 seconds
4. **Impact:** Show how it affects downstream services
5. **Logs:** Database slow query warnings

**Key Metrics:**
- Error Rate: 6%
- Latency: 4.5x normal
- Clinical Impact: High

**Talking Points:**
- "In healthcare, performance directly impacts patient care"
- "This 4.5x slowdown means physicians wait 4.5 times longer for records"
- "Distributed tracing shows the database is the bottleneck"
- "We can see which queries are slow and optimize them"

**Resolution:**
- Optimize slow database queries
- Add database read replicas
- Implement caching for frequently accessed records
- Set up SLA monitoring

---

### 📦 Logistics: Holiday Shipping Rush

**Duration:** 60 minutes of generation
**Best for:** Logistics, supply chain, seasonal businesses

**The Story:**
> "Holiday season is here. Order volumes are 15x normal and the system is struggling. Warehouse management, shipping, and tracking services are all degraded."

**What to Show:**
1. **Service Map:** Order-management, warehouse-management, shipping, tracking all affected
2. **Volume:** Show throughput increase
3. **Traces:** Show slow order processing chains
4. **Errors:** Package tracking update failures
5. **Business Impact:** Show how delays affect customer experience

**Key Metrics:**
- Error Rate: 6%
- Latency: 3.5x normal
- Volume: 15x baseline

**Talking Points:**
- "This is a capacity planning scenario"
- "Multiple services are at their scaling limits"
- "The Service Map shows the interdependencies clearly"
- "We need to scale the entire chain, not just one service"

**Resolution:**
- Horizontal scaling across the board
- Implement job queues for async processing
- Add circuit breakers between services
- Set up capacity alerts for next holiday season

---

## 💡 Pro Tips

### Before the Demo

1. **Practice your scenario** - Read through it 2-3 times
2. **Pre-position Kibana tabs** - Have everything ready
3. **Set time range correctly** - Match your data generation period
4. **Have a backup scenario** - In case something doesn't work

### During the Demo

1. **Start with the story** - People connect with narratives
2. **Show, don't tell** - Click around, explore the data
3. **Pause for questions** - Don't rush through
4. **Highlight the "aha" moments** - When you find the root cause
5. **Connect to business impact** - Revenue, customer experience, compliance

### After the Demo

1. **Offer to generate custom scenarios** - For their specific use cases
2. **Share this guide** - Help them prepare their own demos
3. **Follow up with questions**