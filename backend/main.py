"""
FastAPI Server for Cash Flow Story

Provides REST API endpoints for financial analytics calculations.

Endpoints:
    - POST /api/calculate - Calculate analytics for single period
    - POST /api/calculate/batch - Batch calculation for multiple periods
    - GET /api/demo/rebeccas - Get Rebeccas Coffee demo data
    - GET /health - Health check
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Dict
import uvicorn

from models import (
    FinancialData,
    AnalyticsResponse,
    BatchCalculationRequest,
    BatchAnalyticsResponse,
    ErrorResponse
)
from calculations import calculate_analytics
from demo_data import get_rebeccas_data


app = FastAPI(
    title="Cash Flow Story API",
    description="B2B Financial Analytics - Automatic calculation of 21+ financial coefficients",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # React dev server
        "http://localhost:3000",  # Alternative React port
        "https://cashflowstory.com",  # Production (update with your domain)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Root endpoint with API information"""
    return {
        "message": "Cash Flow Story API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint
    
    Returns:
        dict: Health status
    """
    return {
        "status": "ok",
        "service": "cash-flow-story-api"
    }


@app.post(
    "/api/calculate",
    response_model=AnalyticsResponse,
    responses={
        200: {"description": "Successfully calculated analytics"},
        422: {"description": "Validation error"},
        500: {"description": "Internal server error"}
    }
)
def calculate(
    data: FinancialData,
    previous_period: Optional[FinancialData] = None
):
    """
    Calculate 21 financial metrics for a single period
    
    Args:
        data: Current period financial data (P&L + Balance Sheet)
        previous_period: Optional previous period data for growth calculations
    
    Returns:
        AnalyticsResponse with calculated metrics
    
    Example:
        ```bash
        curl -X POST http://localhost:8000/api/calculate \\
          -H "Content-Type: application/json" \\
          -d '{
            "company_name": "Test Company",
            "period": "2024-Q4",
            "revenue": 1000000,
            "cost_of_goods": 600000,
            "overheads": 200000,
            "depreciation": 50000,
            "cash": 100000,
            "accounts_receivable": 150000,
            "inventory": 200000
          }'
        ```
    """
    try:
        # Convert Pydantic models to dicts
        financial_dict = data.model_dump()
        previous_dict = previous_period.model_dump() if previous_period else None
        
        # Calculate analytics
        analytics = calculate_analytics(financial_dict, previous_dict)
        
        return AnalyticsResponse(
            input_data=data,
            analytics=analytics,
            previous_period=previous_period
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Calculation error: {str(e)}"
        )


@app.post(
    "/api/calculate/batch",
    response_model=BatchAnalyticsResponse
)
def calculate_batch(request: BatchCalculationRequest):
    """
    Calculate analytics for multiple periods at once
    
    Useful for historical analysis and trend visualization.
    
    Args:
        request: Batch calculation request with list of periods
    
    Returns:
        BatchAnalyticsResponse with all calculated periods
    """
    try:
        results = []
        
        for i, period_data in enumerate(request.periods):
            # Get previous period if exists
            previous = request.periods[i-1] if i > 0 else None
            
            # Calculate
            financial_dict = period_data.model_dump()
            previous_dict = previous.model_dump() if previous else None
            analytics = calculate_analytics(financial_dict, previous_dict)
            
            results.append(
                AnalyticsResponse(
                    input_data=period_data,
                    analytics=analytics,
                    previous_period=previous
                )
            )
        
        return BatchAnalyticsResponse(
            company_name=request.company_name,
            periods=results
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Batch calculation error: {str(e)}"
        )


@app.get("/api/demo/rebeccas", response_model=BatchAnalyticsResponse)
def get_rebeccas_demo():
    """
    Get Rebeccas Coffee demo data with calculated analytics
    
    Returns complete historical data (2015-2018) with all metrics calculated.
    Useful for testing and demonstration purposes.
    
    Returns:
        BatchAnalyticsResponse with 4 years of Rebeccas Coffee data
    """
    try:
        demo_data = get_rebeccas_data()
        
        # Calculate for all periods
        results = []
        for i, period_data in enumerate(demo_data):
            previous = demo_data[i-1] if i > 0 else None
            
            financial_dict = period_data.model_dump()
            previous_dict = previous.model_dump() if previous else None
            analytics = calculate_analytics(financial_dict, previous_dict)
            
            results.append(
                AnalyticsResponse(
                    input_data=period_data,
                    analytics=analytics,
                    previous_period=previous
                )
            )
        
        return BatchAnalyticsResponse(
            company_name="Rebeccas Coffee",
            periods=results
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Demo data error: {str(e)}"
        )


if __name__ == "__main__":
    # Run the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload during development
        log_level="info"
    )
