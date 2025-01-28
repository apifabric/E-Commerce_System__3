import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not -7734070350272732800 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer1 = Customer(id=1, name="Alice", credit_limit=Decimal('5000.00'), balance=Decimal('0.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7734070350272732800)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 9099654295009757538 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer2 = Customer(id=2, name="Bob", credit_limit=Decimal('3000.00'), balance=Decimal('0.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(9099654295009757538)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3107466695854775971 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer3 = Customer(id=3, name="Carol", credit_limit=Decimal('4000.00'), balance=Decimal('0.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3107466695854775971)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4109270164458645017 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer4 = Customer(id=4, name="David", credit_limit=Decimal('3500.00'), balance=Decimal('0.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4109270164458645017)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2087686345799579687 in succeeded_hashes:  # avoid duplicate inserts
            instance = order1 = Order(id=1, customer_id=1, date_shipped=None, amount_total=Decimal('0.00'), notes="Express delivery requested")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2087686345799579687)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7253570041907178775 in succeeded_hashes:  # avoid duplicate inserts
            instance = order2 = Order(id=2, customer_id=2, date_shipped=None, amount_total=Decimal('0.00'), notes="Gift package")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7253570041907178775)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1185107446286668051 in succeeded_hashes:  # avoid duplicate inserts
            instance = order3 = Order(id=3, customer_id=3, date_shipped=None, amount_total=Decimal('0.00'), notes="Ship to work address")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1185107446286668051)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5585103274285043597 in succeeded_hashes:  # avoid duplicate inserts
            instance = order4 = Order(id=4, customer_id=4, date_shipped=None, amount_total=Decimal('0.00'), notes="Call before delivery")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5585103274285043597)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1721233750170039187 in succeeded_hashes:  # avoid duplicate inserts
            instance = item1 = Item(id=1, order_id=1, product_id=1, quantity=Decimal('2.00'), unit_price=Decimal('20.00'), amount=Decimal('40.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1721233750170039187)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -9076378671977899551 in succeeded_hashes:  # avoid duplicate inserts
            instance = item2 = Item(id=2, order_id=2, product_id=2, quantity=Decimal('1.00'), unit_price=Decimal('15.00'), amount=Decimal('15.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-9076378671977899551)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 653287181209551224 in succeeded_hashes:  # avoid duplicate inserts
            instance = item3 = Item(id=3, order_id=3, product_id=3, quantity=Decimal('3.00'), unit_price=Decimal('10.00'), amount=Decimal('30.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(653287181209551224)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2126196613467518851 in succeeded_hashes:  # avoid duplicate inserts
            instance = item4 = Item(id=4, order_id=4, product_id=4, quantity=Decimal('4.00'), unit_price=Decimal('5.00'), amount=Decimal('20.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2126196613467518851)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4875494214984151404 in succeeded_hashes:  # avoid duplicate inserts
            instance = product1 = Product(id=1, name="Widget", price=Decimal('20.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4875494214984151404)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8121954202362332297 in succeeded_hashes:  # avoid duplicate inserts
            instance = product2 = Product(id=2, name="Gadget", price=Decimal('15.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8121954202362332297)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6523238597754660591 in succeeded_hashes:  # avoid duplicate inserts
            instance = product3 = Product(id=3, name="Doohickey", price=Decimal('10.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6523238597754660591)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6629712005322140727 in succeeded_hashes:  # avoid duplicate inserts
            instance = product4 = Product(id=4, name="Thingamajig", price=Decimal('5.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6629712005322140727)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8996722427261110073 in succeeded_hashes:  # avoid duplicate inserts
            instance = address1 = Address(id=1, customer_id=1, street="123 Main St", city="Anytown", postal_code="12345")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8996722427261110073)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3781906704958688052 in succeeded_hashes:  # avoid duplicate inserts
            instance = address2 = Address(id=2, customer_id=2, street="456 Side St", city="Othertown", postal_code="67890")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3781906704958688052)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2554616032890882946 in succeeded_hashes:  # avoid duplicate inserts
            instance = address3 = Address(id=3, customer_id=3, street="789 Back St", city="Thistown", postal_code="54321")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2554616032890882946)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 271469973897981998 in succeeded_hashes:  # avoid duplicate inserts
            instance = address4 = Address(id=4, customer_id=4, street="101 Front St", city="Newtown", postal_code="98765")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(271469973897981998)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1237054248352642565 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment1 = Payment(id=1, customer_id=1, order_id=1, amount=Decimal('40.00'), date_of_payment=date(2023, 10, 13))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1237054248352642565)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8702983801110592431 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment2 = Payment(id=2, customer_id=2, order_id=2, amount=Decimal('15.00'), date_of_payment=date(2023, 10, 14))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8702983801110592431)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 9171263220848631470 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment3 = Payment(id=3, customer_id=3, order_id=3, amount=Decimal('30.00'), date_of_payment=date(2023, 10, 15))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(9171263220848631470)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -828585912175690537 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment4 = Payment(id=4, customer_id=4, order_id=4, amount=Decimal('20.00'), date_of_payment=date(2023, 10, 16))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-828585912175690537)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5233674517445644829 in succeeded_hashes:  # avoid duplicate inserts
            instance = carrier1 = Carrier(id=1, name="FastShip", tracking_code="FS123")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5233674517445644829)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6994674178336918865 in succeeded_hashes:  # avoid duplicate inserts
            instance = carrier2 = Carrier(id=2, name="QuickDelivery", tracking_code="QD456")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6994674178336918865)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8314190598078867743 in succeeded_hashes:  # avoid duplicate inserts
            instance = carrier3 = Carrier(id=3, name="ShipNow", tracking_code="SN789")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8314190598078867743)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1513392388561306909 in succeeded_hashes:  # avoid duplicate inserts
            instance = carrier4 = Carrier(id=4, name="DeliverIt", tracking_code="DI101")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1513392388561306909)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2438214558896834545 in succeeded_hashes:  # avoid duplicate inserts
            instance = order_status1 = OrderStatus(id=1, description="Pending")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2438214558896834545)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5447352930570535297 in succeeded_hashes:  # avoid duplicate inserts
            instance = order_status2 = OrderStatus(id=2, description="Shipped")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5447352930570535297)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7899135538450741434 in succeeded_hashes:  # avoid duplicate inserts
            instance = order_status3 = OrderStatus(id=3, description="Delivered")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7899135538450741434)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2495870404675756530 in succeeded_hashes:  # avoid duplicate inserts
            instance = order_status4 = OrderStatus(id=4, description="Cancelled")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2495870404675756530)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6057614739892918476 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer_note1 = CustomerNote(id=1, customer_id=1, note="VIP customer")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6057614739892918476)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8940720413488683505 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer_note2 = CustomerNote(id=2, customer_id=2, note="Frequent complaints")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8940720413488683505)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6192454515127832609 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer_note3 = CustomerNote(id=3, customer_id=3, note="Early adopter")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6192454515127832609)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6397030860405953436 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer_note4 = CustomerNote(id=4, customer_id=4, note="No returns")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6397030860405953436)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 638871347130157855 in succeeded_hashes:  # avoid duplicate inserts
            instance = shipment1 = Shipment(id=1, order_id=1, carrier_id=1, ship_date=date(2023, 9, 30))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(638871347130157855)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6133174849063927754 in succeeded_hashes:  # avoid duplicate inserts
            instance = shipment2 = Shipment(id=2, order_id=2, carrier_id=2, ship_date=date(2023, 9, 27))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6133174849063927754)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3519750964645494194 in succeeded_hashes:  # avoid duplicate inserts
            instance = shipment3 = Shipment(id=3, order_id=3, carrier_id=3, ship_date=date(2023, 10, 2))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3519750964645494194)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5423678862195051666 in succeeded_hashes:  # avoid duplicate inserts
            instance = shipment4 = Shipment(id=4, order_id=4, carrier_id=4, ship_date=date(2023, 10, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5423678862195051666)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3284653749407852877 in succeeded_hashes:  # avoid duplicate inserts
            instance = warehouse1 = Warehouse(id=1, location="North Facility")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3284653749407852877)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8580630118719728438 in succeeded_hashes:  # avoid duplicate inserts
            instance = warehouse2 = Warehouse(id=2, location="South Facility")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8580630118719728438)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3848128759221882331 in succeeded_hashes:  # avoid duplicate inserts
            instance = warehouse3 = Warehouse(id=3, location="East Facility")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3848128759221882331)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7817677332610194176 in succeeded_hashes:  # avoid duplicate inserts
            instance = warehouse4 = Warehouse(id=4, location="West Facility")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7817677332610194176)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6730026516445166771 in succeeded_hashes:  # avoid duplicate inserts
            instance = inventory1 = Inventory(id=1, product_id=1, warehouse_id=1, quantity=Decimal('100.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6730026516445166771)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2466001594695313297 in succeeded_hashes:  # avoid duplicate inserts
            instance = inventory2 = Inventory(id=2, product_id=2, warehouse_id=2, quantity=Decimal('150.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2466001594695313297)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5546268399021111334 in succeeded_hashes:  # avoid duplicate inserts
            instance = inventory3 = Inventory(id=3, product_id=3, warehouse_id=3, quantity=Decimal('200.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5546268399021111334)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1595152209177270105 in succeeded_hashes:  # avoid duplicate inserts
            instance = inventory4 = Inventory(id=4, product_id=4, warehouse_id=4, quantity=Decimal('250.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1595152209177270105)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
