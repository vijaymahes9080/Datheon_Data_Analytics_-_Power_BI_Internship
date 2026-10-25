#!/usr/bin/env python3
"""
Light-Theme Vector Graphics & LinkedIn Showcase Generator
Outputs:
  - docs/images/hero_banner.svg
  - docs/images/methodology_risk.svg
  - docs/images/star_schema_model.svg
  - docs/images/executive_kpis.svg
  - docs/images/linkedin_project_showcase.svg
"""

import os
import sys

def create_hero_banner():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="1200" height="380">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E40AF"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-10%" width="110%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="380" fill="url(#heroBg)" rx="16" stroke="#E2E8F0" stroke-width="2"/>
  
  <!-- Subtle Grid Accent -->
  <g stroke="#E2E8F0" stroke-width="0.75" opacity="0.6">
    <line x1="0" y1="80" x2="1200" y2="80"/>
    <line x1="0" y1="160" x2="1200" y2="160"/>
    <line x1="0" y1="240" x2="1200" y2="240"/>
    <line x1="0" y1="320" x2="1200" y2="320"/>
    <line x1="300" y1="0" x2="300" y2="380"/>
    <line x1="600" y1="0" x2="600" y2="380"/>
    <line x1="900" y1="0" x2="900" y2="380"/>
  </g>

  <!-- Top Pill Badge -->
  <rect x="50" y="32" width="310" height="30" rx="15" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
  <circle cx="68" cy="47" r="5" fill="#2563EB"/>
  <text x="82" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" letter-spacing="0.8">ENTERPRISE DECISION INTELLIGENCE</text>

  <!-- Main Headline -->
  <text x="50" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="34" font-weight="800" fill="#0F172A">
    RISK Decision Intelligence Platform
  </text>
  <text x="50" y="138" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="500" fill="#475569">
    Autonomous Problem Solving: Retail Diagnostics • Star Schema Power BI • Churn ML • Financial Simulation
  </text>

  <!-- Feature Pills -->
  <g transform="translate(50, 160)">
    <rect x="0" y="0" width="170" height="28" rx="14" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.2"/>
    <text x="14" y="18" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#166534">✓ 4 Analytical Engines</text>

    <rect x="180" y="0" width="190" height="28" rx="14" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.2"/>
    <text x="194" y="18" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#92400E">★ Star Schema &amp; DAX</text>

    <rect x="380" y="0" width="190" height="28" rx="14" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.2"/>
    <text x="394" y="18" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#3730A3">● Predictive Retention</text>

    <rect x="580" y="0" width="200" height="28" rx="14" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.2"/>
    <text x="594" y="18" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#6B21A8">◆ Scenario Simulation</text>
  </g>

  <!-- Metric Ribbon Cards -->
  <g transform="translate(50, 215)">
    <!-- Card 1 -->
    <rect x="0" y="0" width="255" height="120" rx="12" fill="url(#cardGrad)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect x="0" y="0" width="255" height="4" rx="2" fill="#2563EB"/>
    <text x="20" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#64748B" letter-spacing="0.5">ANALYZED REVENUE</text>
    <text x="20" y="70" font-family="system-ui, -apple-system, sans-serif" font-size="30" font-weight="800" fill="#0F172A">$2,297,201</text>
    <text x="20" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#059669">9,994 Orders • 0 Loss Ingestion</text>

    <!-- Card 2 -->
    <rect x="280" y="0" width="255" height="120" rx="12" fill="url(#cardGrad)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect x="280" y="0" width="255" height="4" rx="2" fill="#DC2626"/>
    <text x="300" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#64748B" letter-spacing="0.5">DISCOUNT DESTRUCTION</text>
    <text x="300" y="70" font-family="system-ui, -apple-system, sans-serif" font-size="30" font-weight="800" fill="#DC2626">-$135,376</text>
    <text x="300" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#B91C1C">On discounts &gt; 20% (-37% margin)</text>

    <!-- Card 3 -->
    <rect x="560" y="0" width="255" height="120" rx="12" fill="url(#cardGrad)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect x="560" y="0" width="255" height="4" rx="2" fill="#D97706"/>
    <text x="580" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#64748B" letter-spacing="0.5">TOXIC TRIAD CHURN</text>
    <text x="580" y="70" font-family="system-ui, -apple-system, sans-serif" font-size="30" font-weight="800" fill="#D97706">60.37%</text>
    <text x="580" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#92400E">Month-to-Month + Fiber + E-Check</text>

    <!-- Card 4 -->
    <rect x="840" y="0" width="260" height="120" rx="12" fill="url(#cardGrad)" stroke="#E2E8F0" stroke-width="1.5" filter="url(#cardShadow)"/>
    <rect x="840" y="0" width="260" height="4" rx="2" fill="#059669"/>
    <text x="860" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#64748B" letter-spacing="0.5">EBITDA RESTORATION</text>
    <text x="860" y="70" font-family="system-ui, -apple-system, sans-serif" font-size="30" font-weight="800" fill="#059669">+$920,525</text>
    <text x="860" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#047857">10% discount policy adjustment</text>
  </g>
</svg>'''
    return svg


def create_methodology_risk():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <filter id="dropShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <rect width="1200" height="420" fill="url(#bgGrad)" rx="16" stroke="#E2E8F0" stroke-width="2"/>

  <!-- Section Header -->
  <text x="50" y="45" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#2563EB" letter-spacing="1">PROPRIETARY METHODOLOGY</text>
  <text x="50" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="26" font-weight="800" fill="#0F172A">The 4-Stage RISK Analytical Framework</text>
  <text x="50" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="500" fill="#64748B">A disciplined engineering approach ensuring absolute reproducibility, schema integrity, and commercial impact.</text>

  <!-- 4 Framework Cards -->
  <g transform="translate(50, 130)">
    <!-- Stage R -->
    <g transform="translate(0, 0)">
      <rect width="255" height="250" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#dropShadow)"/>
      <rect width="255" height="6" rx="3" fill="#2563EB"/>
      <circle cx="36" cy="40" r="18" fill="#EFF6FF"/>
      <text x="31" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#2563EB">R</text>
      <text x="65" y="45" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A">Reconnaissance</text>
      
      <text x="20" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#2563EB">Auditing &amp; Requirements</text>
      
      <text x="20" y="110" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Schema &amp; Type Auditing</text>
      <text x="20" y="135" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Missingness Profiling</text>
      <text x="20" y="160" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Boundary Value Checks</text>
      <text x="20" y="185" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Zero-Loss Ingestion Pipeline</text>
      <text x="20" y="220" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E40AF">Output: Data Quality Ledger</text>
    </g>

    <!-- Stage I -->
    <g transform="translate(285, 0)">
      <rect width="255" height="250" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#dropShadow)"/>
      <rect width="255" height="6" rx="3" fill="#D97706"/>
      <circle cx="36" cy="40" r="18" fill="#FFFBEB"/>
      <text x="33" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#D97706">I</text>
      <text x="65" y="45" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A">Intelligence</text>
      
      <text x="20" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#D97706">Extraction &amp; Deep Investigation</text>
      
      <text x="20" y="110" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Multi-Dimensional Slicing</text>
      <text x="20" y="135" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Discount Hazard Modeling</text>
      <text x="20" y="160" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Tenure Cohort Decay</text>
      <text x="20" y="185" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Root Cause Diagnostic Isolation</text>
      <text x="20" y="220" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#B45309">Output: 17 Diagnostic Charts</text>
    </g>

    <!-- Stage S -->
    <g transform="translate(570, 0)">
      <rect width="255" height="250" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#dropShadow)"/>
      <rect width="255" height="6" rx="3" fill="#059669"/>
      <circle cx="36" cy="40" r="18" fill="#F0FDF4"/>
      <text x="31" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#059669">S</text>
      <text x="65" y="45" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A">Solution</text>
      
      <text x="20" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#059669">Development &amp; Simulation</text>
      
      <text x="20" y="110" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Star Schema Architecture</text>
      <text x="20" y="135" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Calibrated Retention ML</text>
      <text x="20" y="160" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• What-If Sensitivity Simulator</text>
      <text x="20" y="185" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Production DAX Formulas</text>
      <text x="20" y="220" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#047857">Output: Star Tables &amp; Models</text>
    </g>

    <!-- Stage K -->
    <g transform="translate(855, 0)">
      <rect width="245" height="250" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#dropShadow)"/>
      <rect width="245" height="6" rx="3" fill="#7C3AED"/>
      <circle cx="36" cy="40" r="18" fill="#FAF5FF"/>
      <text x="31" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#7C3AED">K</text>
      <text x="65" y="45" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A">KPI Verification</text>
      
      <text x="20" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#7C3AED">Knowledge &amp; Executive Delivery</text>
      
      <text x="20" y="110" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• 21 Automated Pytest Suites</text>
      <text x="20" y="135" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• $0.00 DAX Reconciliation</text>
      <text x="20" y="160" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Executive Strategic Reports</text>
      <text x="20" y="185" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">• Interactive HTML Portal</text>
      <text x="20" y="220" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#6D28D9">Output: 5 Executive Memorandums</text>
    </g>
  </g>
</svg>'''
    return svg


def create_star_schema_model():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 640" width="1200" height="640">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <filter id="shadowBox" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <rect width="1200" height="640" fill="url(#bgGrad2)" rx="16" stroke="#E2E8F0" stroke-width="2"/>

  <!-- Header -->
  <text x="50" y="45" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#2563EB" letter-spacing="1">POWER BI RELATIONAL ARCHITECTURE</text>
  <text x="50" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="26" font-weight="800" fill="#0F172A">Enterprise Star Schema &amp; Dimensional Model</text>
  <text x="50" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="500" fill="#64748B">Central FactSales table surrounded by 4 conforming dimensions with 1-to-many single-directional relationships.</text>

  <!-- Connective Lines -->
  <g stroke="#94A3B8" stroke-width="2" stroke-dasharray="4,4">
    <line x1="260" y1="210" x2="440" y2="280"/>
    <line x1="260" y1="470" x2="440" y2="400"/>
    <line x1="940" y1="210" x2="760" y2="280"/>
    <line x1="940" y1="470" x2="760" y2="400"/>
  </g>

  <!-- Central Fact Table -->
  <g transform="translate(440, 160)" filter="url(#shadowBox)">
    <rect width="320" height="420" rx="12" fill="#FFFFFF" stroke="#2563EB" stroke-width="2"/>
    <rect width="320" height="45" rx="12" fill="#2563EB"/>
    <rect y="35" width="320" height="10" fill="#2563EB"/>
    <text x="20" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" fill="#FFFFFF">FactSales</text>
    <text x="210" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#BFDBFE">9,994 Rows</text>
    
    <!-- Fields -->
    <g transform="translate(20, 65)" font-family="system-ui, -apple-system, sans-serif" font-size="13">
      <text y="15" font-weight="700" fill="#1E40AF">🔑 Row ID [PK]</text>
      <text y="40" font-weight="500" fill="#475569">Order ID</text>
      <text y="65" font-weight="700" fill="#059669">🔗 Order Date [FK -&gt; DimDate]</text>
      <text y="90" font-weight="500" fill="#475569">Ship Date &amp; Ship Mode</text>
      <text y="115" font-weight="700" fill="#059669">🔗 Customer ID [FK -&gt; DimCustomer]</text>
      <text y="140" font-weight="700" fill="#059669">🔗 Postal Code [FK -&gt; DimGeography]</text>
      <text y="165" font-weight="700" fill="#059669">🔗 Product ID [FK -&gt; DimProduct]</text>
      <line x1="0" y1="180" x2="280" y2="180" stroke="#E2E8F0" stroke-width="1"/>
      <text y="205" font-weight="700" fill="#0F172A">📊 Sales ($2,297,200.86)</text>
      <text y="230" font-weight="700" fill="#0F172A">📊 Quantity (37,873 units)</text>
      <text y="255" font-weight="700" fill="#DC2626">📊 Discount (0% - 80%)</text>
      <text y="280" font-weight="700" fill="#059669">📊 Profit ($286,397.02)</text>
      <text y="305" font-weight="500" fill="#475569">Profit Margin % (12.47%)</text>
      <text y="330" font-weight="500" fill="#475569">Is Profitable Flag</text>
    </g>
  </g>

  <!-- Dimension 1: DimProduct (Top Left) -->
  <g transform="translate(50, 140)" filter="url(#shadowBox)">
    <rect width="230" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="230" height="35" rx="10" fill="#0F172A"/>
    <rect y="25" width="230" height="10" fill="#0F172A"/>
    <text x="15" y="23" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">DimProduct (1,862 SKUs)</text>
    
    <g transform="translate(15, 55)" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#334155">
      <text y="15" font-weight="700" fill="#2563EB">🔑 Product ID [PK]</text>
      <text y="40">Category (Technology, Furn...)</text>
      <text y="65">Sub-Category (Phones, Chairs...)</text>
      <text y="90">Product Name</text>
      <text y="115" font-weight="600" fill="#059669">Cardinality: 1 to Many [1:*]</text>
    </g>
  </g>

  <!-- Dimension 2: DimCustomer (Bottom Left) -->
  <g transform="translate(50, 390)" filter="url(#shadowBox)">
    <rect width="230" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="230" height="35" rx="10" fill="#0F172A"/>
    <rect y="25" width="230" height="10" fill="#0F172A"/>
    <text x="15" y="23" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">DimCustomer (793 Users)</text>
    
    <g transform="translate(15, 55)" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#334155">
      <text y="15" font-weight="700" fill="#2563EB">🔑 Customer ID [PK]</text>
      <text y="40">Customer Name</text>
      <text y="65">Segment (Consumer, Corp...)</text>
      <text y="90">Total Historical Orders</text>
      <text y="115" font-weight="600" fill="#059669">Cardinality: 1 to Many [1:*]</text>
    </g>
  </g>

  <!-- Dimension 3: DimGeography (Top Right) -->
  <g transform="translate(920, 140)" filter="url(#shadowBox)">
    <rect width="230" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="230" height="35" rx="10" fill="#0F172A"/>
    <rect y="25" width="230" height="10" fill="#0F172A"/>
    <text x="15" y="23" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">DimGeography (631 Areas)</text>
    
    <g transform="translate(15, 55)" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#334155">
      <text y="15" font-weight="700" fill="#2563EB">🔑 Postal Code [PK]</text>
      <text y="40">City &amp; State</text>
      <text y="65">Region (West, East, Central, S)</text>
      <text y="90">Country (United States)</text>
      <text y="115" font-weight="600" fill="#059669">Cardinality: 1 to Many [1:*]</text>
    </g>
  </g>

  <!-- Dimension 4: DimDate (Bottom Right) -->
  <g transform="translate(920, 390)" filter="url(#shadowBox)">
    <rect width="230" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="230" height="35" rx="10" fill="#0F172A"/>
    <rect y="25" width="230" height="10" fill="#0F172A"/>
    <text x="15" y="23" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">DimDate (1,464 Days)</text>
    
    <g transform="translate(15, 55)" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#334155">
      <text y="15" font-weight="700" fill="#2563EB">🔑 Date [PK]</text>
      <text y="40">Year, Quarter, Month</text>
      <text y="65">Fiscal Quarter &amp; Month-Year</text>
      <text y="90">Day of Week &amp; IsWeekend</text>
      <text y="115" font-weight="600" fill="#059669">Cardinality: 1 to Many [1:*]</text>
    </g>
  </g>
</svg>'''
    return svg


def create_executive_kpis():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 620" width="1200" height="620">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
    <filter id="bentoShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <rect width="1200" height="620" fill="url(#bgGrad3)" rx="16" stroke="#E2E8F0" stroke-width="2"/>

  <!-- Header -->
  <text x="50" y="45" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#2563EB" letter-spacing="1">EXECUTIVE DECISION REGISTER</text>
  <text x="50" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="26" font-weight="800" fill="#0F172A">Quantified Findings Across the 4 Business Pillars</text>
  <text x="50" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="500" fill="#64748B">Real diagnostic results extracted from validated datasets and reconciled analytics engines.</text>

  <!-- Bento Grid Container -->
  <g transform="translate(50, 130)">
    <!-- Pillar 1: Retail Sales Discovery -->
    <g transform="translate(0, 0)" filter="url(#bentoShadow)">
      <rect width="535" height="210" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect width="535" height="4" rx="2" fill="#2563EB"/>
      <text x="24" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A">1. Retail Sales &amp; Margin Diagnostics</text>
      
      <!-- Metrics row -->
      <g transform="translate(24, 55)">
        <text y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">TOTAL REVENUE</text>
        <text y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#0F172A">$2,297,201</text>
        <text y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#059669">Net Margin: 12.47%</text>

        <text x="180" y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">DISCOUNT HAZARD</text>
        <text x="180" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#DC2626">-$135,376</text>
        <text x="180" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#B91C1C">Loss on Disc &gt; 20%</text>

        <text x="360" y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">TOP ENGINE</text>
        <text x="360" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#2563EB">50.79%</text>
        <text x="360" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#1E40AF">Technology Profit</text>
      </g>
      
      <line x1="24" y1="140" x2="510" y2="140" stroke="#F1F5F9" stroke-width="1.5"/>
      <text x="24" y="165" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">
        • Tables subcategory loses -$17,725.48 across 319 transactions due to runaway 30%+ promotions.
      </text>
      <text x="24" y="188" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">
        • West Region leads corporate EBITDA with $108,418.45 in profit (14.93% margin).
      </text>
    </g>

    <!-- Pillar 2: Customer Churn Intelligence -->
    <g transform="translate(565, 0)" filter="url(#bentoShadow)">
      <rect width="535" height="210" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect width="535" height="4" rx="2" fill="#D97706"/>
      <text x="24" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A">2. Customer Churn &amp; Retention ML</text>
      
      <!-- Metrics row -->
      <g transform="translate(24, 55)">
        <text y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">OVERALL CHURN</text>
        <text y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#0F172A">26.54%</text>
        <text y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#D97706">1,869 / 7,043 subs</text>

        <text x="180" y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">YEAR 1 CHURN</text>
        <text x="180" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#DC2626">47.44%</text>
        <text x="180" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#B91C1C">0-12 month tenure hazard</text>

        <text x="360" y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">MODEL ROC-AUC</text>
        <text x="360" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#059669">0.8418</text>
        <text x="360" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#047857">Calibrated Classifier</text>
      </g>

      <line x1="24" y1="140" x2="510" y2="140" stroke="#F1F5F9" stroke-width="1.5"/>
      <text x="24" y="165" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">
        • "Toxic Triad" (Month-to-month + Fiber optic + E-check) produces a staggering 60.37% churn.
      </text>
      <text x="24" y="188" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">
        • Two-year contract commitments slash subscriber churn risk down to just 2.83%.
      </text>
    </g>

    <!-- Pillar 3: Financial Scenario Simulation -->
    <g transform="translate(0, 235)" filter="url(#bentoShadow)">
      <rect width="535" height="210" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect width="535" height="4" rx="2" fill="#059669"/>
      <text x="24" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A">3. Financial Performance &amp; Simulation</text>
      
      <!-- Metrics row -->
      <g transform="translate(24, 55)">
        <text y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">GROSS PROFIT</text>
        <text y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#0F172A">$16.89M</text>
        <text y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#059669">Margin: 13.20%</text>

        <text x="180" y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">ENTERPRISE DEFICIT</text>
        <text x="180" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#DC2626">-$614.5K</text>
        <text x="180" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#B91C1C">Loss on $19.61M sales</text>

        <text x="360" y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">DISCOUNT SENSITIVITY</text>
        <text x="360" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#059669">+$920.5K</text>
        <text x="360" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#047857">10% Discount Cut Lever</text>
      </g>

      <line x1="24" y1="140" x2="510" y2="140" stroke="#F1F5F9" stroke-width="1.5"/>
      <text x="24" y="165" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">
        • Channel Partners segment yields premium 73.13% profit margin with minimal discount exposure.
      </text>
      <text x="24" y="188" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">
        • Multi-variate what-if sensitivity matrix models elasticity across price, volume, and inflation.
      </text>
    </g>

    <!-- Pillar 4: Engineering & Quality Verification -->
    <g transform="translate(565, 235)" filter="url(#bentoShadow)">
      <rect width="535" height="210" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect width="535" height="4" rx="2" fill="#7C3AED"/>
      <text x="24" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A">4. Enterprise Rigor &amp; Verification</text>
      
      <!-- Metrics row -->
      <g transform="translate(24, 55)">
        <text y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">PYTEST COVERAGE</text>
        <text y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#059669">21 / 21</text>
        <text y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#047857">100% Tests Passing</text>

        <text x="180" y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">DAX RECONCILIATION</text>
        <text x="180" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#2563EB">$0.00</text>
        <text x="180" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#1E40AF">Penny-perfect parity</text>

        <text x="360" y="15" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B">COMMITS ON MAIN</text>
        <text x="360" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#7C3AED">30 Commits</text>
        <text x="360" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#6D28D9">Discrete Staged History</text>
      </g>

      <line x1="24" y1="140" x2="510" y2="140" stroke="#F1F5F9" stroke-width="1.5"/>
      <text x="24" y="165" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">
        • Zero orphan surrogate keys across 9,994 orders, 1,862 products, and 793 customers.
      </text>
      <text x="24" y="188" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#475569">
        • Production HTML dashboard portal providing instantaneous executive drilldown.
      </text>
    </g>
  </g>
</svg>'''
    return svg


def create_linkedin_project_showcase():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1500" width="1200" height="1500">
  <defs>
    <linearGradient id="linkedInBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="40%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="50%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <filter id="liShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Canvas Base -->
  <rect width="1200" height="1500" fill="url(#linkedInBg)" rx="20" stroke="#CBD5E1" stroke-width="2"/>

  <!-- Top Accent Bar -->
  <rect width="1200" height="10" rx="5" fill="url(#headerGrad)"/>

  <!-- Header Section -->
  <g transform="translate(60, 45)">
    <!-- Subtitle Pill -->
    <rect x="0" y="0" width="370" height="32" rx="16" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <circle cx="16" cy="16" r="5" fill="#2563EB"/>
    <text x="30" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" letter-spacing="0.8">DATA ANALYTICS &amp; DECISION INTELLIGENCE</text>
    
    <!-- Title -->
    <text x="0" y="75" font-family="system-ui, -apple-system, sans-serif" font-size="38" font-weight="800" fill="#0F172A">
      RISK Decision Intelligence Platform
    </text>
    
    <!-- Tagline -->
    <text x="0" y="112" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="500" fill="#475569">
      Turning Raw Data into Boardroom Strategy Across Retail, Churn ML, Finance &amp; Power BI
    </text>

    <!-- Author & Portfolio Tag -->
    <text x="0" y="142" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#2563EB">
      Portfolio Showcase &amp; Internship Project • Authored by Vijay Maheswari
    </text>
  </g>

  <!-- Top KPI Highlight Ribbon (4 Cards) -->
  <g transform="translate(60, 215)">
    <!-- Card 1 -->
    <rect x="0" y="0" width="250" height="115" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#liShadow)"/>
    <rect x="0" y="0" width="250" height="4" rx="2" fill="#2563EB"/>
    <text x="20" y="30" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#64748B" letter-spacing="0.5">RETAIL REVENUE</text>
    <text x="20" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="800" fill="#0F172A">$2.30M</text>
    <text x="20" y="95" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#059669">9,994 Orders • 12.47% Margin</text>

    <!-- Card 2 -->
    <rect x="275" y="0" width="250" height="115" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#liShadow)"/>
    <rect x="275" y="0" width="250" height="4" rx="2" fill="#DC2626"/>
    <text x="295" y="30" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#64748B" letter-spacing="0.5">DISCOUNT DRAIN</text>
    <text x="295" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="800" fill="#DC2626">-$135.4K</text>
    <text x="295" y="95" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#B91C1C">Destroyed on Disct &gt; 20%</text>

    <!-- Card 3 -->
    <rect x="550" y="0" width="250" height="115" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#liShadow)"/>
    <rect x="550" y="0" width="250" height="4" rx="2" fill="#D97706"/>
    <text x="570" y="30" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#64748B" letter-spacing="0.5">TOXIC TRIAD CHURN</text>
    <text x="570" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="800" fill="#D97706">60.37%</text>
    <text x="570" y="95" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#92400E">M2M + Fiber + E-Check</text>

    <!-- Card 4 -->
    <rect x="825" y="0" width="255" height="115" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#liShadow)"/>
    <rect x="825" y="0" width="255" height="4" rx="2" fill="#059669"/>
    <text x="845" y="30" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#64748B" letter-spacing="0.5">EBITDA LEVER</text>
    <text x="845" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="800" fill="#059669">+$920.5K</text>
    <text x="845" y="95" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#047857">10% Discount Policy Adjustment</text>
  </g>

  <!-- 4 Core Project Pillars Section -->
  <g transform="translate(60, 360)">
    <text x="0" y="20" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#0F172A">
      4 Pillars of the Decision Intelligence Solution
    </text>

    <!-- Pillar 1 Card -->
    <g transform="translate(0, 35)" filter="url(#liShadow)">
      <rect width="525" height="215" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect width="525" height="4" rx="2" fill="#2563EB"/>
      <text x="24" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" fill="#0F172A">
        Pillar 1: Retail Sales Discovery Engine
      </text>
      <text x="24" y="55" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#2563EB">
        Superstore Diagnostic Analysis • Discount Elasticity
      </text>
      <text x="24" y="85" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Unmasked severe margin erosion: Discounts above 20%
      </text>
      <text x="34" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#DC2626">
        yield an aggregate -$135,376.06 loss (-37.32% margin).
      </text>
      <text x="24" y="132" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Identified Tables subcategory as a chronic deficit driver
      </text>
      <text x="34" y="152" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#DC2626">
        losing -$17,725.48 across 319 transactions.
      </text>
      <text x="24" y="179" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Technology powers 50.79% of corporate profits ($145.4K).
      </text>
      <rect x="24" y="190" width="475" height="15" fill="#EFF6FF" rx="4"/>
      <text x="30" y="201" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#1D4ED8">
        ACTION: Enforce hard discount caps at 20% &amp; bundle table warranties.
      </text>
    </g>

    <!-- Pillar 2 Card -->
    <g transform="translate(555, 35)" filter="url(#liShadow)">
      <rect width="525" height="215" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect width="525" height="4" rx="2" fill="#D97706"/>
      <text x="24" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" fill="#0F172A">
        Pillar 2: Power BI Star Schema &amp; DAX Suite
      </text>
      <text x="24" y="55" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#D97706">
        Relational Data Architecture • $0.00 Measure Reconciliation
      </text>
      <text x="24" y="85" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Engineered Star Schema: FactSales (9,994 rows) connected
      </text>
      <text x="34" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        to DimProduct (1,862), DimCustomer (793), DimGeography (631).
      </text>
      <text x="24" y="132" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Complete continuous 1,464-day calendar dimension (DimDate)
      </text>
      <text x="34" y="152" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        enabling robust Time Intelligence (YoY Sales, Sales YTD).
      </text>
      <text x="24" y="179" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Every DAX measure cross-validated with Python ($0.00 variance).
      </text>
      <rect x="24" y="190" width="475" height="15" fill="#FFFBEB" rx="4"/>
      <text x="30" y="201" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#92400E">
        ACTION: Zero orphan keys; delivers sub-second executive dashboard queries.
      </text>
    </g>

    <!-- Pillar 3 Card -->
    <g transform="translate(0, 275)" filter="url(#liShadow)">
      <rect width="525" height="215" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect width="525" height="4" rx="2" fill="#DC2626"/>
      <text x="24" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" fill="#0F172A">
        Pillar 3: Customer Churn &amp; Retention ML
      </text>
      <text x="24" y="55" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#DC2626">
        Tenure Cohort Hazard • Calibrated Predictive Models
      </text>
      <text x="24" y="85" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Early-stage tenure risk: 47.44% churn rate in months 0–12
      </text>
      <text x="34" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        dropping sharply to 6.61% for subscribers past 5 years.
      </text>
      <text x="24" y="132" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Uncovered the "Toxic Triad": Month-to-Month + Fiber Optic
      </text>
      <text x="34" y="152" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#DC2626">
        + Electronic Check triggers a severe 60.37% churn rate.
      </text>
      <text x="24" y="179" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Calibrated Machine Learning achieves 0.8418 ROC-AUC score.
      </text>
      <rect x="24" y="190" width="475" height="15" fill="#FEF2F2" rx="4"/>
      <text x="30" y="201" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B">
        ACTION: Deploy 90-day onboarding concierge &amp; $10 autopay switch credit.
      </text>
    </g>

    <!-- Pillar 4 Card -->
    <g transform="translate(555, 275)" filter="url(#liShadow)">
      <rect width="525" height="215" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect width="525" height="4" rx="2" fill="#059669"/>
      <text x="24" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" fill="#0F172A">
        Pillar 4: Financial Performance &amp; Simulation
      </text>
      <text x="24" y="55" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#059669">
        Segment Economics • What-If Sensitivity Engine
      </text>
      <text x="24" y="85" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Corporate financial diagnosis: Enterprise operates at a net
      </text>
      <text x="34" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#DC2626">
        loss of -$614,531.20 despite generating $19.61M in gross sales.
      </text>
      <text x="24" y="132" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Channel Partners segment yields an elite 73.13% profit margin.
      </text>
      <text x="24" y="159" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="#475569">
        • Built interactive What-If Engine: 10% discount cut restores
      </text>
      <text x="34" y="179" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#059669">
        +$920,524.82 directly to EBITDA (+5.45% margin increase).
      </text>
      <rect x="24" y="190" width="475" height="15" fill="#F0FDF4" rx="4"/>
      <text x="30" y="201" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#166534">
        ACTION: Overhaul Enterprise tier discount structures &amp; incentivize partners.
      </text>
    </g>
  </g>

  <!-- The RISK Methodology Strip -->
  <g transform="translate(60, 905)">
    <rect width="1080" height="155" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#liShadow)"/>
    <text x="25" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" fill="#0F172A">
      The RISK Analytical Framework
    </text>
    <text x="25" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="500" fill="#64748B">
      Rigorous 4-stage engineering lifecycle applied consistently across all datasets and models
    </text>

    <!-- 4 Step Boxes -->
    <g transform="translate(25, 70)">
      <!-- Step R -->
      <rect x="0" y="0" width="240" height="65" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
      <text x="15" y="26" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#1D4ED8">R — Reconnaissance</text>
      <text x="15" y="48" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="500" fill="#475569">Schema audit, missingness, assertions</text>

      <!-- Step I -->
      <rect x="260" y="0" width="240" height="65" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1"/>
      <text x="275" y="26" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#B45309">I — Intelligence</text>
      <text x="275" y="48" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="500" fill="#475569">Diagnostics, cohorts, root causes</text>

      <!-- Step S -->
      <rect x="520" y="0" width="240" height="65" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
      <text x="535" y="26" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#15803D">S — Solution</text>
      <text x="535" y="48" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="500" fill="#475569">Star schema, ML models, simulator</text>

      <!-- Step K -->
      <rect x="780" y="0" width="245" height="65" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1"/>
      <text x="795" y="26" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#7E22CE">K — KPI Verification</text>
      <text x="795" y="48" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="500" fill="#475569">Pytest suite, DAX parity, memos</text>
    </g>
  </g>

  <!-- Technical Rigor & Verification Badges -->
  <g transform="translate(60, 1090)">
    <text x="0" y="20" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="800" fill="#0F172A">
      Verified Engineering Standards &amp; Deliverables
    </text>

    <!-- 3 Stat Blocks -->
    <g transform="translate(0, 35)">
      <rect x="0" y="0" width="340" height="90" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#liShadow)"/>
      <text x="20" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#64748B">AUTOMATED TESTING</text>
      <text x="20" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#059669">21 / 21 Tests Passing</text>
      <text x="20" y="78" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="500" fill="#475569">Schema, assertions, calculation parity</text>

      <rect x="370" y="0" width="340" height="90" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#liShadow)"/>
      <text x="390" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#64748B">PUBLICATION FIGURES</text>
      <text x="390" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#2563EB">17 Diagnostic Visuals</text>
      <text x="390" y="78" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="500" fill="#475569">Clean seaborn / matplotlib figures</text>

      <rect x="740" y="0" width="340" height="90" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#liShadow)"/>
      <text x="760" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#64748B">INTERACTIVE PORTAL</text>
      <text x="760" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#7C3AED">Executive Dashboard</text>
      <text x="760" y="78" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="500" fill="#475569">Complete HTML/CSS decision web app</text>
    </g>
  </g>

  <!-- Technology Stack & Bottom Bar -->
  <g transform="translate(60, 1250)">
    <rect width="1080" height="175" rx="12" fill="#0F172A"/>
    
    <text x="35" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#94A3B8" letter-spacing="1">
      ENTERPRISE TECHNOLOGY STACK
    </text>
    
    <!-- Tech Badges -->
    <g transform="translate(35, 60)">
      <rect x="0" y="0" width="95" height="32" rx="6" fill="#1E293B"/>
      <text x="16" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#60A5FA">Python</text>

      <rect x="110" y="0" width="95" height="32" rx="6" fill="#1E293B"/>
      <text x="126" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#F472B6">Pandas</text>

      <rect x="220" y="0" width="125" height="32" rx="6" fill="#1E293B"/>
      <text x="233" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#FB923C">Scikit-Learn</text>

      <rect x="360" y="0" width="115" height="32" rx="6" fill="#1E293B"/>
      <text x="375" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#FACC15">Power BI</text>

      <rect x="490" y="0" width="125" height="32" rx="6" fill="#1E293B"/>
      <text x="502" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#38BDF8">DAX Engine</text>

      <rect x="630" y="0" width="90" height="32" rx="6" fill="#1E293B"/>
      <text x="646" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#4ADE80">Pytest</text>

      <rect x="735" y="0" width="130" height="32" rx="6" fill="#1E293B"/>
      <text x="747" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#C084FC">Jupyter Lab</text>

      <rect x="880" y="0" width="130" height="32" rx="6" fill="#1E293B"/>
      <text x="895" y="21" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#A78BFA">Git Versioning</text>
    </g>

    <!-- Connect / Hire Callout -->
    <line x1="35" y1="112" x2="1045" y2="112" stroke="#334155" stroke-width="1"/>
    <text x="35" y="142" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#FFFFFF">
      Looking for a Data Analytics &amp; Decision Intelligence Engineer? Let's connect on LinkedIn!
    </text>
    <text x="770" y="142" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#60A5FA">
      github.com/vijaymahes9080
    </text>
  </g>
</svg>'''
    return svg


def main():
    os.makedirs("docs/images", exist_ok=True)
    
    files = {
        "docs/images/hero_banner.svg": create_hero_banner(),
        "docs/images/methodology_risk.svg": create_methodology_risk(),
        "docs/images/star_schema_model.svg": create_star_schema_model(),
        "docs/images/executive_kpis.svg": create_executive_kpis(),
        "docs/images/linkedin_project_showcase.svg": create_linkedin_project_showcase(),
    }
    
    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {path} ({len(content)} bytes)")

if __name__ == "__main__":
    main()
