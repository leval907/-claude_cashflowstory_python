"""
Demo data: Rebeccas Coffee historical financials (2015-2018)

Based on real case study data from cashflowstory.com
Perfect for testing and demonstration purposes.
"""

from typing import List
from models import FinancialData


def get_rebeccas_data() -> List[FinancialData]:
    """
    Get Rebeccas Coffee historical data (2015-2018)
    
    Returns:
        List of FinancialData objects for 4 years
    
    Story:
        Rebeccas Coffee is a rapidly growing coffee shop chain.
        Key insights from the data:
        - Strong revenue growth (3.4M → 6.6M in 3 years)
        - Declining margins (overheads growing faster than revenue)
        - Working capital challenges (inventory and receivables growing)
        - High debt levels (2.1M non-current liabilities)
    """
    
    return [
        # 2015: Starting year
        FinancialData(
            company_name="Rebeccas Coffee",
            period="2015",
            
            # P&L
            revenue=3400000,
            cost_of_goods=2400000,
            overheads=600000,
            depreciation=100000,
            interest_paid=60000,
            tax_paid=60000,
            
            # Balance Sheet - Assets
            cash=150000,
            accounts_receivable=800000,
            inventory=900000,
            fixed_assets=1500000,
            
            # Balance Sheet - Liabilities
            current_liabilities=700000,
            noncurrent_liabilities=1500000,
            accounts_payable=400000
        ),
        
        # 2016: Growth phase
        FinancialData(
            company_name="Rebeccas Coffee",
            period="2016",
            
            # P&L
            revenue=4200000,
            cost_of_goods=2900000,
            overheads=750000,
            depreciation=120000,
            interest_paid=75000,
            tax_paid=85000,
            
            # Balance Sheet - Assets
            cash=180000,
            accounts_receivable=1100000,
            inventory=1200000,
            fixed_assets=1800000,
            
            # Balance Sheet - Liabilities
            current_liabilities=850000,
            noncurrent_liabilities=1700000,
            accounts_payable=550000
        ),
        
        # 2017: Rapid expansion
        FinancialData(
            company_name="Rebeccas Coffee",
            period="2017",
            
            # P&L
            revenue=5800000,
            cost_of_goods=4100000,
            overheads=950000,
            depreciation=150000,
            interest_paid=95000,
            tax_paid=120000,
            
            # Balance Sheet - Assets
            cash=190000,
            accounts_receivable=1400000,
            inventory=1600000,
            fixed_assets=2200000,
            
            # Balance Sheet - Liabilities
            current_liabilities=1000000,
            noncurrent_liabilities=1900000,
            accounts_payable=650000
        ),
        
        # 2018: Peak year (but challenges emerging)
        FinancialData(
            company_name="Rebeccas Coffee",
            period="2018",
            
            # P&L
            revenue=6600000,
            cost_of_goods=4700000,
            overheads=1100000,
            depreciation=180000,
            interest_paid=110000,
            tax_paid=140000,
            
            # Balance Sheet - Assets
            cash=200000,
            accounts_receivable=1500000,
            inventory=1800000,
            fixed_assets=2500000,
            
            # Balance Sheet - Liabilities
            current_liabilities=1200000,
            noncurrent_liabilities=2100000,
            accounts_payable=750000
        )
    ]


def get_rebeccas_summary() -> dict:
    """
    Get summary insights about Rebeccas Coffee
    
    Returns:
        Dictionary with key business insights
    """
    return {
        "company": "Rebeccas Coffee",
        "industry": "Food & Beverage - Coffee Shops",
        "years": "2015-2018",
        "revenue_cagr": "24.5%",
        
        "strengths": [
            "Strong revenue growth (94% over 3 years)",
            "Consistent positive cash flow",
            "Loyal customer base (high receivables)",
            "Asset-light model for coffee shops"
        ],
        
        "challenges": [
            "Declining gross margins (29.4% → 28.8%)",
            "Overheads growing faster than revenue",
            "Working capital cycle extending (inventory buildup)",
            "High debt to equity ratio (increasing leverage)",
            "Interest coverage declining"
        ],
        
        "key_metrics_2018": {
            "gross_margin": "28.8%",
            "operating_profit": "12.1%",
            "net_profit": "7.1%",
            "roe": "24.6%",
            "working_capital_days": "81 days",
            "debt_to_equity": "1.82"
        },
        
        "analyst_notes": [
            "Growth is impressive but profitability under pressure",
            "Need to control overhead growth",
            "Inventory management needs attention",
            "High leverage is a risk if growth slows",
            "Consider renegotiating supplier payment terms"
        ]
    }


# For quick testing
if __name__ == "__main__":
    data = get_rebeccas_data()
    print(f"Loaded {len(data)} periods for Rebeccas Coffee")
    
    for period in data:
        print(f"\n{period.period}:")
        print(f"  Revenue: ${period.revenue:,.0f}")
        print(f"  Gross Profit: ${period.revenue - period.cost_of_goods:,.0f}")
        print(f"  Net Assets: ${period.cash + period.accounts_receivable + period.inventory + period.fixed_assets - period.current_liabilities - period.noncurrent_liabilities:,.0f}")
    
    print("\n" + "="*50)
    print("SUMMARY INSIGHTS:")
    summary = get_rebeccas_summary()
    print(f"\nCompany: {summary['company']}")
    print(f"Revenue CAGR: {summary['revenue_cagr']}")
    print(f"\nKey Metrics (2018):")
    for key, value in summary['key_metrics_2018'].items():
        print(f"  {key}: {value}")
