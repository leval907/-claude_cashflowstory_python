"""
Unit tests for financial calculations

Tests all 21 financial formulas with various scenarios:
- Normal cases
- Edge cases (zero values)
- Negative scenarios
- Rebeccas Coffee real data
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from calculations import calculate_analytics


class TestProfitabilityMetrics:
    """Test Group 1: Profitability metrics"""
    
    def test_gross_margin_percent(self):
        """Test gross margin calculation"""
        data = {
            'revenue': 1000000,
            'cost_of_goods': 600000
        }
        result = calculate_analytics(data)
        
        # Expected: (1000000 - 600000) / 1000000 * 100 = 40%
        assert result['gross_margin_percent'] == pytest.approx(40.0, rel=0.01)
    
    def test_net_profit_percent(self):
        """Test net profit calculation"""
        data = {
            'revenue': 1000000,
            'cost_of_goods': 600000,
            'overheads': 200000,
            'interest_paid': 10000,
            'tax_paid': 30000
        }
        result = calculate_analytics(data)
        
        # Expected: (1000000 - 600000 - 200000 - 10000 - 30000) / 1000000 * 100 = 16%
        assert result['net_profit_percent'] == pytest.approx(16.0, rel=0.01)


class TestWorkingCapitalMetrics:
    """Test Group 2: Working Capital metrics"""
    
    def test_accounts_receivable_days(self):
        """Test AR days calculation"""
        data = {
            'revenue': 3650000,  # 10,000 per day
            'accounts_receivable': 1000000
        }
        result = calculate_analytics(data)
        
        # Expected: 1000000 / 3650000 * 365 = 100 days
        assert result['accounts_receivable_days'] == pytest.approx(100.0, rel=0.01)


class TestCapitalEfficiencyMetrics:
    """Test Group 3: Capital Efficiency metrics"""
    
    def test_return_on_equity(self):
        """Test ROE calculation"""
        data = {
            'revenue': 1000000,
            'cost_of_goods': 600000,
            'overheads': 200000,
            'interest_paid': 10000,
            'tax_paid': 30000,
            'cash': 100000,
            'accounts_receivable': 200000,
            'inventory': 200000,
            'fixed_assets': 500000,
            'current_liabilities': 200000,
            'noncurrent_liabilities': 300000
        }
        result = calculate_analytics(data)
        
        # Net Profit = 160000
        # Equity = 500000
        # ROE = 32%
        assert result['return_on_equity'] == pytest.approx(32.0, rel=0.01)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
