You are building the frontend dashboard for a 24-hour hackathon project called "Kintsugi Monkey Banking".



Do not build backend code.

Backend is being built separately and exposes REST endpoints on:



http://localhost:4000



Project concept:

Kintsugi Monkey Banking is a chaos engineering dashboard for a simulated banking microservice system.

It intentionally breaks a banking service, collects logs/metrics, sends them to Gemini from the backend, and displays developer-facing repair recommendations as a Golden Trace.



Kintsugi philosophy:

The failure is not hidden. It becomes visible, stored, interpreted, and transformed into a learning trace.

In this project, every controlled service failure becomes a Golden Trace in the system's resilience memory.



Important:

\- Do not call Gemini from frontend.

\- Do not store API keys in frontend.

\- Frontend only calls backend.

\- Gemini response will come from POST /experiments/:id/analyze.

\- If Gemini is unavailable, backend fallback analyzer still returns the same shape.



Tech stack:

\- React + Vite

\- Plain CSS is acceptable

\- Tailwind is acceptable only if quick

\- No auth

\- No complex state management

\- Use fetch

\- Make it visually impressive and demo-friendly



Create frontend inside:

/frontend



Use environment variable:

VITE\_API\_BASE\_URL=http://localhost:4000



Required backend endpoints:



GET /health/services



Expected response:

{

&#x20; "services": \[

&#x20;   { "name": "account-service", "status": "UP or DOWN" },

&#x20;   { "name": "transaction-service", "status": "UP or DEGRADED or DOWN" },

&#x20;   { "name": "fraud-check-service", "status": "UP or DOWN" },

&#x20;   { "name": "notification-service", "status": "UP or DOWN" }

&#x20; ],

&#x20; "timestamp": "ISO\_DATE"

}



POST /banking/demo-transaction



Possible normal response:

{

&#x20; "transactionId": "txn\_1001",

&#x20; "status": "approved",

&#x20; "message": "Transaction approved after fraud check.",

&#x20; "fraudCheckStatus": "passed"

}



Possible degraded response:

{

&#x20; "transactionId": "txn\_1001",

&#x20; "status": "pending\_manual\_review",

&#x20; "message": "Fraud check service unavailable. Transaction moved to manual review queue.",

&#x20; "fraudCheckStatus": "unavailable",

&#x20; "degraded": true

}



POST /experiments/kill-fraud-check



POST /experiments/recover-fraud-check



GET /experiments



POST /experiments/:id/analyze



Expected analyze response:

{

&#x20; "id": "trace\_...",

&#x20; "experiment\_id": "exp\_...",

&#x20; "summary": "...",

&#x20; "suspected\_weak\_point": "...",

&#x20; "blast\_radius": "...",

&#x20; "risk\_level": "LOW | MEDIUM | HIGH",

&#x20; "safe\_degradation\_review": "...",

&#x20; "developer\_recommendations": \["...", "..."],

&#x20; "next\_experiments": \["...", "..."],

&#x20; "kintsugi\_lesson": "..."

}



GET /golden-traces



Build a single-page dashboard with these sections:



1\. Hero Section



Title:

Kintsugi Monkey Banking



Subtitle:

Safe chaos for resilient banking systems.



Slogan:

Break safely. Learn visibly. Repair stronger.



Short description:

Controlled chaos experiments that transform banking service failures into Golden Traces.



2\. Banking System Map



Show service cards:

\- account-service

\- transaction-service

\- fraud-check-service

\- notification-service



Show dependency line:

transaction-service -> fraud-check-service



Status visual rules:

\- UP: green

\- DEGRADED: amber/gold

\- DOWN: red



If fraud-check-service is DOWN, show a golden crack line between transaction-service and fraud-check-service.



If transaction-service is DEGRADED, show a strong banking-safe fallback badge:

"Pending Manual Review"



3\. Banking Demo Transaction Panel



Button:

Run Demo Transaction



It calls:

POST /banking/demo-transaction



Show response:

\- transactionId

\- status

\- message

\- fraudCheckStatus



If status is pending\_manual\_review, visually emphasize:

"Safe Degradation Activated"



4\. Chaos Controls



Buttons:

\- Refresh Health

\- Break fraud-check-service

\- Recover fraud-check-service

\- Analyze Last Experiment



Behavior:

\- Refresh Health calls GET /health/services

\- Break calls POST /experiments/kill-fraud-check

\- Recover calls POST /experiments/recover-fraud-check

\- Analyze calls POST /experiments/:id/analyze using latest experiment id



5\. Latest Experiment Panel



Show latest experiment:

\- id

\- domain

\- target\_service

\- affected\_service

\- fault\_type

\- status

\- started\_at

\- ended\_at

\- recovery\_time\_ms

\- safe\_degradation



If fields are missing, show "-".



6\. Metrics / Impact Panel



Show if available:

\- failed\_requests

\- degraded\_requests

\- fallback\_used

\- average\_latency\_ms

\- recovery\_time\_ms



If exact metrics are not available, show what backend returns.



7\. Golden Trace Panel



This is the most important section.



Show Gemini/fallback analysis response:



\- Summary

\- Suspected Weak Point

\- Blast Radius

\- Risk Level

\- Safe Degradation Review

\- Developer Recommendations

\- Next Experiments

\- Kintsugi Lesson



Risk Level styling:

\- LOW: green

\- MEDIUM: amber

\- HIGH: red



Developer Recommendations should be shown as a checklist.



Kintsugi Lesson should be shown as a special gold-highlighted card.



8\. Experiment History



List experiments from GET /experiments.



9\. Golden Trace History



List traces from GET /golden-traces.



Design direction:

\- Dark background

\- Gold accents

\- Banking-professional feel

\- Kintsugi-inspired crack motif

\- Clean cards

\- Strong visual clarity

\- Good for live demo and screenshots

\- Make system state understandable in 5 seconds



Polling:

\- Poll GET /health/services every 3 seconds.

\- Refresh experiments after chaos actions.

\- Refresh golden traces after analyze action.



Error handling:

\- Show a clean error banner if backend unavailable.

\- Do not crash.



Files to create:

\- package.json

\- index.html

\- src/main.jsx

\- src/App.jsx

\- src/App.css

\- README.md



README must include:

npm install

npm run dev



And:

VITE\_API\_BASE\_URL=http://localhost:4000



Important wording in UI:

Use:

\- Golden Trace

\- Gemini Analysis

\- Developer Recommendations

\- Safe Degradation

\- Fracture Memory

\- Resilience Memory

\- Kintsugi Lesson



Do not show:

\- "automatic fix applied"

\- "AI fixed the system"

\- "self-healing completed"



Because Gemini only recommends, it does not modify the system.



Deliverable:

Generate the full React dashboard.



After implementing:

\- list files

\- explain how to run

\- explain expected demo flow

