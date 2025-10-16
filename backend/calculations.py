"""
Financial Analytics Calculation Engine
========================================

Calculates 21 financial coefficients divided into 3 groups:
1. Profitability (6 metrics)
2. Working Capital (6 metrics)
3. Capital Efficiency (9 metrics)

Author: CashFlow Story Team
License: MIT
"""

import pandas as pd
from typing import Dict, Optional


def calculate_analytics(
    financial_data: Dict[str, float],
    previous_period: Optional[Dict[str, float]] = None
) -> Dict[str, float]:
    """
    Calculate 21 financial metrics for a single period.
    
    Args:
        financial_data: Current period financial data
        previous_period: Previous period data for growth calculations (optional)
    
    Returns:
        Dictionary with 21 calculated metrics
        
    Example:
        >>> data = {
        ...     'revenue': 1000000,
        ...     'cost_of_goods': 600000,
        ...     'overheads': 200000,
        ...     'cash': 100000,
        ...     'accounts_receivable': 150000,
        ...     'inventory': 200000,
        ...     'fixed_assets': 500000,
        ...     'current_liabilities': 100000,
        ...     'noncurrent_liabilities': 200000,
        ...     'accounts_payable': 75000
        ... }
        >>> analytics = calculate_analytics(data)
        >>> print(f"Gross Margin: {analytics['gross_margin_percent']:.2f}%")
    """
    
    analytics = {}
    
    # === EXTRACT VALUES WITH DEFAULTS ===
    
    # P&L Items
    revenue = financial_data.get('revenue', 0)
    cogs = financial_data.get('cost_of_goods', 0)
    overheads = financial_data.get('overheads', 0)
    depreciation = financial_data.get('depreciation', 0)
    interest = financial_data.get('interest_paid', 0)
    tax = financial_data.get('tax_paid', 0)
    
    # Balance Sheet - Assets
    cash = financial_data.get('cash', 0)
    receivables = financial_data.get('accounts_receivable', 0)
    inventory = financial_data.get('inventory', 0)
    fixed_assets = financial_data.get('fixed_assets', 0)
    
    # Balance Sheet - Liabilities
    current_liabilities = financial_data.get('current_liabilities', 0)
    noncurrent_liabilities = financial_data.get('noncurrent_liabilities', 0)
    payables = financial_data.get('accounts_payable', 0)
    
    # === GROUP 1: PROFITABILITY (6 metrics) ===
    
    # 1. Revenue Growth %
    # Measures year-over-year revenue growth
    if previous_period and previous_period.get('revenue', 0) > 0:
        prev_revenue = previous_period['revenue']
        analytics['revenue_growth_percent'] = round(
            ((revenue - prev_revenue) / prev_revenue) * 100, 2
        )
    else:
        analytics['revenue_growth_percent'] = 0.0
    
    # 2. Gross Margin %
    # Shows profit after direct costs (COGS)
    gross_margin = revenue - cogs
    analytics['gross_margin_percent'] = round(
        (gross_margin / revenue * 100) if revenue > 0 else 0, 2
    )
    
    # 3. Operating Profit %
    # Profit after all operating expenses
    operating_profit = gross_margin - overheads
    analytics['operating_profit_percent'] = round(
        (operating_profit / revenue * 100) if revenue > 0 else 0, 2
    )
    
    # Calculate EBITDA first (needed for multiple metrics)
    ebitda = operating_profit + depreciation
    
    # 4. Net Profit %
    # Bottom line profit after all expenses and taxes
    net_profit_before_tax = operating_profit - interest
    net_profit = net_profit_before_tax - tax
    analytics['net_profit_percent'] = round(
        (net_profit / revenue * 100) if revenue > 0 else 0, 2
    )
    
    # 5. EBITDA %
    # Earnings before interest, tax, depreciation, amortization
    analytics['ebitda_percent'] = round(
        (ebitda / revenue * 100) if revenue > 0 else 0, 2
    )
    
    # 6. Interest Coverage
    # Ability to pay interest from operating profit
    analytics['interest_coverage'] = round(
        (operating_profit / interest) if interest > 0 else 0, 2
    )
    
    # === GROUP 2: WORKING CAPITAL (6 metrics) ===
    
    # 7. Accounts Receivable Days
    # How long it takes to collect payment from customers
    analytics['accounts_receivable_days'] = round(
        (receivables / revenue * 365) if revenue > 0 else 0, 2
    )
    
    # 8. Inventory Days
    # How long inventory sits before being sold
    analytics['inventory_days'] = round(
        (inventory / cogs * 365) if cogs > 0 else 0, 2
    )
    
    # 9. Accounts Payable Days
    # How long before paying suppliers
    analytics['accounts_payable_days'] = round(
        (payables / cogs * 365) if cogs > 0 else 0, 2
    )
    
    # 10. Working Capital Cycle (Days)
    # Cash conversion cycle: AR Days + Inv Days - AP Days
    analytics['working_capital_days'] = round(
        analytics['accounts_receivable_days'] +
        analytics['inventory_days'] -
        analytics['accounts_payable_days'],
        2
    )
    
    # Calculate current assets and working capital
    current_assets = cash + receivables + inventory
    working_capital = current_assets - current_liabilities
    
    # 11. Working Capital per 100 Revenue
    # Working capital as percentage of revenue
    analytics['working_capital_per_100'] = round(
        (working_capital / revenue * 100) if revenue > 0 else 0, 2
    )
    
    # 12. Current Ratio
    # Liquidity ratio: can company pay short-term debts?
    analytics['current_ratio'] = round(
        (current_assets / current_liabilities) if current_liabilities > 0 else 0, 2
    )
    
    # === GROUP 3: CAPITAL EFFICIENCY (9 metrics) ===
    
    # Calculate total figures
    total_assets = current_assets + fixed_assets
    total_liabilities = current_liabilities + noncurrent_liabilities
    equity = total_assets - total_liabilities
    
    # 13. Return on Capital %
    # Profit generated from working capital + fixed assets
    total_capital = working_capital + fixed_assets
    analytics['return_on_capital'] = round(
        (operating_profit / total_capital * 100) if total_capital > 0 else 0, 2
    )
    
    # 14. Asset Turnover
    # How efficiently assets generate revenue
    analytics['asset_turnover'] = round(
        (revenue / total_assets) if total_assets > 0 else 0, 2
    )
    
    # 15. Return on Equity (ROE) %
    # Profit generated for shareholders
    analytics['return_on_equity'] = round(
        (net_profit / equity * 100) if equity > 0 else 0, 2
    )
    
    # 16. Return on Assets (ROA) %
    # How well company uses assets to generate profit
    analytics['return_on_assets'] = round(
        (net_profit / total_assets * 100) if total_assets > 0 else 0, 2
    )
    
    # 17. Fixed Assets Turnover
    # Revenue generated per dollar of fixed assets
    analytics['fixed_assets_turnover'] = round(
        (revenue / fixed_assets) if fixed_assets > 0 else 0, 2
    )
    
    # 18. Debt to Equity
    # Financial leverage ratio
    analytics['debt_to_equity'] = round(
        (total_liabilities / equity) if equity > 0 else 0, 2
    )
    
    # 19. Debt to Capital
    # Proportion of debt in capital structure
    total_capital_debt = equity + total_liabilities
    analytics['debt_to_capital'] = round(
        (total_liabilities / total_capital_debt) if total_capital_debt > 0 else 0, 2
    )
    
    # 20. Equity Ratio %
    # Proportion of assets financed by equity
    analytics['equity_ratio'] = round(
        (equity / total_assets * 100) if total_assets > 0 else 0, 2
    )
    
    # 21. Operating Cash Flow
    # Approximation: Net Profit + Depreciation
    analytics['operating_cash_flow'] = round(net_profit + depreciation, 2)
    
    return analytics


# === PANDAS VERSION FOR BATCH PROCESSING ===

def calculate_analytics_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate analytics for multiple periods at once using Pandas vectorization.
    
    This is much faster than looping through periods individually.
    Useful for historical analysis of 10+ periods.
    
    Args:
        df: DataFrame with columns matching FinancialData model
            Must include 'period' column for sorting
    
    Returns:
        DataFrame with all original columns plus 21 calculated metrics
        
    Example:
        >>> data = pd.DataFrame([
        ...     {'period': '2023-Q1', 'revenue': 1000000, 'cost_of_goods': 600000, ...},
        ...     {'period': '2023-Q2', 'revenue': 1200000, 'cost_of_goods': 700000, ...},
        ... ])
        >>> results = calculate_analytics_df(data)
        >>> print(results[['period', 'gross_margin_percent', 'roe']])
    """
    
    # Sort by period to ensure chronological order
    df = df.sort_values('period').copy()
    
    # === GROUP 1: PROFITABILITY ===
    
    # 1. Revenue Growth %
    df['revenue_growth_percent'] = df['revenue'].pct_change() * 100
    
    # 2-3. Margins
    df['gross_margin'] = df['revenue'] - df['cost_of_goods']
    df['gross_margin_percent'] = (df['gross_margin'] / df['revenue']) * 100
    
    df['operating_profit'] = df['gross_margin'] - df['overheads']
    df['operating_profit_percent'] = (df['operating_profit'] / df['revenue']) * 100
    
    # 4-5. EBITDA and Net Profit
    df['ebitda'] = df['operating_profit'] + df['depreciation']
    df['ebitda_percent'] = (df['ebitda'] / df['revenue']) * 100
    
    df['net_profit'] = df['operating_profit'] - df['interest_paid'] - df['tax_paid']
    df['net_profit_percent'] = (df['net_profit'] / df['revenue']) * 100
    
    # 6. Interest Coverage
    df['interest_coverage'] = df['operating_profit'] / df['interest_paid']
    df['interest_coverage'] = df['interest_coverage'].replace([float('inf'), -float('inf')], 0)
    
    # === GROUP 2: WORKING CAPITAL ===
    
    # 7-9. Days metrics
    df['accounts_receivable_days'] = (df['accounts_receivable'] / df['revenue']) * 365
    df['inventory_days'] = (df['inventory'] / df['cost_of_goods']) * 365
    df['accounts_payable_days'] = (df['accounts_payable'] / df['cost_of_goods']) * 365
    
    # 10. Working Capital Cycle
    df['working_capital_days'] = (
        df['accounts_receivable_days'] + 
        df['inventory_days'] - 
        df['accounts_payable_days']
    )
    
    # 11-12. Working Capital metrics
    df['current_assets'] = df['cash'] + df['accounts_receivable'] + df['inventory']
    df['working_capital'] = df['current_assets'] - df['current_liabilities']
    df['working_capital_per_100'] = (df['working_capital'] / df['revenue']) * 100
    df['current_ratio'] = df['current_assets'] / df['current_liabilities']
    
    # === GROUP 3: CAPITAL EFFICIENCY ===
    
    # Calculate base figures
    df['total_assets'] = df['current_assets'] + df['fixed_assets']
    df['total_liabilities'] = df['current_liabilities'] + df['noncurrent_liabilities']
    df['equity'] = df['total_assets'] - df['total_liabilities']
    
    # 13. Return on Capital
    df['total_capital'] = df['working_capital'] + df['fixed_assets']
    df['return_on_capital'] = (df['operating_profit'] / df['total_capital']) * 100
    
    # 14. Asset Turnover
    df['asset_turnover'] = df['revenue'] / df['total_assets']
    
    # 15-16. ROE and ROA
    df['return_on_equity'] = (df['net_profit'] / df['equity']) * 100
    df['return_on_assets'] = (df['net_profit'] / df['total_assets']) * 100
    
    # 17. Fixed Assets Turnover
    df['fixed_assets_turnover'] = df['revenue'] / df['fixed_assets']
    
    # 18-20. Debt ratios
    df['debt_to_equity'] = df['total_liabilities'] / df['equity']
    df['total_capital_debt'] = df['equity'] + df['total_liabilities']
    df['debt_to_capital'] = df['total_liabilities'] / df['total_capital_debt']
    df['equity_ratio'] = (df['equity'] / df['total_assets']) * 100
    
    # 21. Operating Cash Flow
    df['operating_cash_flow'] = df['net_profit'] + df['depreciation']
    
    # Replace inf/-inf with 0 (from division by zero)
    df = df.replace([float('inf'), -float('inf')], 0)
    
    # Round all calculated columns to 2 decimals
    calculated_columns = [
        'revenue_growth_percent', 'gross_margin_percent', 'operating_profit_percent',
        'net_profit_percent', 'ebitda_percent', 'interest_coverage',
        'accounts_receivable_days', 'inventory_days', 'accounts_payable_days',
        'working_capital_days', 'working_capital_per_100', 'current_ratio',
        'return_on_capital', 'asset_turnover', 'return_on_equity',
        'return_on_assets', 'fixed_assets_turnover', 'debt_to_equity',
        'debt_to_capital', 'equity_ratio', 'operating_cash_flow'
    ]
    
    for col in calculated_columns:
        if col in df.columns:
            df[col] = df[col].round(2)
    
    return df


# === UTILITY FUNCTIONS ===

def get_metric_explanation(metric_name: str) -> str:
    """
    Get human-readable explanation of a financial metric.
    
    Args:
        metric_name: Name of the metric (e.g., 'gross_margin_percent')
    
    Returns:
        Explanation string
    """
    explanations = {
        'revenue_growth_percent': 'Year-over-year revenue growth rate',
        'gross_margin_percent': 'Profit after direct costs (COGS)',
        'operating_profit_percent': 'Profit after all operating expenses',
        'net_profit_percent': 'Bottom line profit after all expenses',
        'ebitda_percent': 'Earnings before interest, tax, depreciation, amortization',
        'interest_coverage': 'Ability to pay interest from operating profit',
        'accounts_receivable_days': 'Average days to collect payment from customers',
        'inventory_days': 'Average days inventory sits before being sold',
        'accounts_payable_days': 'Average days before paying suppliers',
        'working_capital_days': 'Cash conversion cycle length',
        'working_capital_per_100': 'Working capital as percentage of revenue',
        'current_ratio': 'Ability to pay short-term debts',
        'return_on_capital': 'Profit generated from working capital + fixed assets',
        'asset_turnover': 'Revenue efficiency per dollar of assets',
        'return_on_equity': 'Profit generated for shareholders',
        'return_on_assets': 'Profit efficiency per dollar of assets',
        'fixed_assets_turnover': 'Revenue per dollar of fixed assets',
        'debt_to_equity': 'Financial leverage ratio',
        'debt_to_capital': 'Proportion of debt in capital structure',
        'equity_ratio': 'Proportion of assets financed by equity',
        'operating_cash_flow': 'Approximated cash from operations'
    }
    
    return explanations.get(metric_name, 'No explanation available')


def validate_financial_data(data: Dict[str, float]) -> tuple[bool, str]:
    """
    Validate financial data before calculation.
    
    Args:
        data: Financial data dictionary
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check required fields
    required_fields = ['revenue']
    for field in required_fields:
        if field not in data or data[field] is None:
            return False, f"Missing required field: {field}"
    
    # Check for negative values where they shouldn't be
    non_negative_fields = ['revenue', 'cash', 'accounts_receivable', 
                          'inventory', 'fixed_assets']
    for field in non_negative_fields:
        if field in data and data[field] < 0:
            return False, f"{field} cannot be negative"
    
    return True, ""
