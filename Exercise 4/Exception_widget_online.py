from http import HTTPStatus
import json
import datetime
import traceback


class WidgetException(Exception):
    'The base class for all our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Widget exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args, user_err_msg=None):
        if args:
            args = (self.internal_err_msg, ) + args
            super().__init__(*args)

        else:
            super().__init__(self.internal_err_msg)
        
        if user_err_msg is not None:
            self.user_err_msg = user_err_msg
    
    @property
    def traceback(self):
        return traceback.TracebackException.from_exception(self).format()

    def to_json(self):
        err_json = {
            'type': self.__class__.__name__,
            'http_status': self.http_status,
            'internal_err_msg': self.internal_err_msg,
            'user_err_msg': self.user_err_msg,
            'args': self.args[1:],
            'traceback': list(self.traceback)
        }

        return json.dumps(err_json)
    
    def log_exception(self):
        log = self.to_json()

        print(f'EXCEPTION: {datetime.datetime.utcnow().isoformat()}: {log}')


class SupplierException(WidgetException):
    'The subclass Suplier exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Supplier exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class NotManufacturedException(SupplierException):
    'The subclass Not Manufatured exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Not Manufactured exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

class ProductionDelayedException(SupplierException):
    'The subclass Production Delayed exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Production Delayed exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class ShippingDelayException(SupplierException):
    'The subclass Shipping Delay exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Shipping Delay exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class CheckOutException(WidgetException):
    'The subclass Checkout exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Checkout exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class InventoryTypeException(CheckOutException):
    'The subclass Inventory Type exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Inventory Type exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class OutStockException(InventoryTypeException):
    'The subclass Out of Stock exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Out of Stock exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class PricingException(CheckOutException):
    'The subclass Pricing exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Pricing exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class InvalidCoupon(PricingException):
    'The subclass Invalid Coupon Code exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Invalid Coupon Code exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.BAD_REQUEST


class StackCouponException(PricingException):
    'The subclass Cannot Stack Coupon exception from our custom exceptions we raise from our Widget application'

    internal_err_msg = 'Cannot Stack Coupon exception occurred.'
    user_err_msg = None
    http_status = HTTPStatus.BAD_REQUEST





try:
    raise StackCouponException(15, 20, user_err_msg='hola')
except WidgetException as ex:
    print(ex.__dict__)
    print(str(ex), repr(ex))
    
    print(ex.to_json())
    ex.log_exception()
