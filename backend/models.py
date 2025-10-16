"""
Pydantic models for Cash Flow Story API

Defines data structures for:
- Input financial data (P&L + Balance Sheet)
- Output analytics results
- Batch operations
- Error responses
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict
from datetime import datetime


class FinancialData(BaseModel):
    """
    Financial data model for a single period
    
    Includes both P&L (Profit & Loss) and Balance Sheet data.
    All monetary values should be in the same currency.
    
    Attributes:
        company_name: Name of the company
        period: Period identifier (e.g., "2024-Q4", "2024", "Dec 2024")
        
        # P&L Statement
        revenue: Total revenue/sales
        cost_of_goods: Direct costs (COGS)
        overheads: Operating expenses (SG&A)
        depreciation: Depreciation and amortization
        interest_paid: Interest expense
        tax_paid: Income tax
        
        # Balance Sheet - Assets
        cash: Cash and cash equivalents
        accounts_receivable: Trade receivables
        inventory: Inventory value
        fixed_assets: Property, plant, equipment (net)
        
        # Balance Sheet - Liabilities
        current_liabilities: Short-term liabilities
        noncurrent_liabilities: Long-term liabilities
        accounts_payable: Trade payables
    """
    
    # Metadata
    company_name: str = Field(..., min_length=1, description="Company name")
    period: str = Field(..., description="Period identifier")
    
    # P&L Statement
    revenue: float = Field(..., ge=0, description="Total revenue")
    cost_of_goods: float = Field(0, ge=0, description="Cost of goods sold")
    overheads: float = Field(0, ge=0, description="Operating expenses")
    depreciation: float = Field(0, ge=0, description="Depreciation & amortization")
    interest_paid: float = Field(0, ge=0, description="Interest expense")
    tax_paid: float = Field(0, ge=0, description="Income tax")
    
    # Balance Sheet - Assets
    cash: float = Field(0, ge=0, description="Cash and equivalents")
    accounts_receivable: float = Field(0, ge=0, description="Trade receivables")
    inventory: float = Field(0, ge=0, description="Inventory")
    fixed_assets: float = Field(0, ge=0, description="Fixed assets (net)")
    
    # Balance Sheet - Liabilities
    current_liabilities: float = Field(0, ge=0, description="Current liabilities")
    noncurrent_liabilities: float = Field(0, ge=0, description="Non-current liabilities")
    accounts_payable: float = Field(0, ge=0, description="Trade payables")
    
    @validator('revenue')
    def revenue_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Revenue must be greater than 0')
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "company_name": "Acme Corp",
                "period": "2024-Q4",
                "revenue": 1000000,
                "cost_of_goods": 600000,
                "overheads": 200000,
                "depreciation": 50000,
                "interest_paid": 10000,
                "tax_paid": 30000,
                "cash": 100000,
                "accounts_receivable": 150000,
                "inventory": 200000,
                "fixed_assets": 500000,
                "current_liabilities": 120000,
                "noncurrent_liabilities": 300000,
                "accounts_payable": 80000
            }
        }


class AnalyticsResponse(BaseModel):
    """
    Analytics calculation response
    
    Contains:
    - Original input data
    - Calculated 21 financial metrics
    - Optional previous period data
    - Calculation timestamp
    
    All percentage values are in % (not decimal).
    All ratio values are absolute numbers.
    All days values are in calendar days.
    """
    
    input_data: FinancialData = Field(..., description="Original input data")
    analytics: Dict[str, float] = Field(..., description="Calculated metrics")
    previous_period: Optional[FinancialData] = Field(None, description="Previous period data")
    calculated_at: datetime = Field(default_factory=datetime.now, description="Calculation timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "input_data": {
                    "company_name": "Acme Corp",
                    "period": "2024-Q4",
                    "revenue": 1000000
                },
                "analytics": {
                    "revenue_growth_percent": 15.5,
                    "gross_margin_percent": 40.0,
                    "net_profit_percent": 11.0,
                    "roe": 25.3,
                    "working_capital_days": 45
                }
            }
        }


class BatchCalculationRequest(BaseModel):
    """
    Batch calculation request model
    
    Used for calculating analytics for multiple periods at once.
    Periods should be sorted chronologically for growth calculations.
    """
    
    company_name: str = Field(..., description="Company name")
    periods: List[FinancialData] = Field(..., min_items=1, description="List of periods to calculate")
    
    @validator('periods')
    def validate_periods(cls, v):
        if len(v) < 1:
            raise ValueError('At least one period required')
        return v


class BatchAnalyticsResponse(BaseModel):
    """
    Batch analytics calculation response
    
    Contains calculated analytics for all requested periods.
    """
    
    company_name: str = Field(..., description="Company name")
    periods: List[AnalyticsResponse] = Field(..., description="Analytics for each period")
    total_periods: int = Field(default=0, description="Total number of periods")
    
    def __init__(self, **data):
        super().__init__(**data)
        if 'total_periods' not in data or data['total_periods'] == 0:
            data['total_periods'] = len(data.get('periods', []))
        self.total_periods = len(self.periods)


class ErrorResponse(BaseModel):
    """
    Error response model
    """
    
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
    timestamp: datetime = Field(default_factory=datetime.now, description="Error timestamp")
