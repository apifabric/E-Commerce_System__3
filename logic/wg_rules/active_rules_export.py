import logging
from logic_bank.logic_bank import DeclareRule, Rule, LogicBank
from database.models import *
from decimal import Decimal
from datetime import date, datetime

log = logging.getLogger(__name__)

def declare_logic():
    """
        declare_logic - declare rules
        this function is called from logic/declare_logic.py
    """
    log.info("declare_logic - active rules")
    
    # Exported Rules:
    # Check Customer Balance 
    # Ensure customer's balance is less than or equal to credit limit.
    Rule.constraint(validate=Customer, as_condition=lambda row: row.balance <= row.credit_limit, error_msg="Customer balance ({row.balance}) exceeds credit limit ({row.credit_limit})")
    
    # Customer Balance Calculation 
    # Customer balance is sum of Order's amount_total where date_shipped is null.
    Rule.sum(derive=Customer.balance, as_sum_of=Order.amount_total, where=lambda row: row.date_shipped is None)
    
    # Order Amount Calculation 
    # Order's amount_total is the sum of Item amount.
    Rule.sum(derive=Order.amount_total, as_sum_of=Item.amount)
    
    # Item Amount Calculation 
    # Item amount is quantity times unit price.
    Rule.formula(derive=Item.amount, as_expression=lambda row: row.quantity * row.unit_price)
    